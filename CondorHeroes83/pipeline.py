#!/usr/bin/env python3
"""
Pipeline v6 for Legend of the Condor Heroes subtitle processing.
Usage: python3 pipeline.py <episode_number>

Architecture: chi is the ENTRY SPINE.
  - Output entry count = chi entry count (not eng).
  - Eng content is reflowed onto chi entries (merge multi-eng-into-chi,
    split one-eng-across-multi-chi by proportion).
  - Yue (Whisper JSON) is preprocessed per chi sub.
  See PIPELINE.md Step 1 and STYLE.md §16 for the full spec.

Yue preprocessing (Whisper JSON):
  1. Load chi_tra CSV as the alignment anchor.
  2. Split coarse Whisper segments into per-chi-sub chunks using
     word-level timestamps: each word is assigned to the chi sub
     whose time range it best overlaps.
  3. Per chunk: concatenate word text, compute avg word score,
     inherit parent segment avg_logprob → derive confidence tier.
  4. Compute tight timing (first word start, last word end) per chunk
     for SRT timing adjustment.
  5. Output compact {EP}-yue-aligned.json (one entry per chi sub).
  6. Discard raw Whisper JSON from memory — only the compact
     alignment survives into the main pipeline.

Yue input: {N}-yue.json only (Whisper output). No CSV fallback.
"""

import sys, re, csv, io, json, os

UPLOADS = '/mnt/user-data/uploads'
WORK = '/home/claude'
OUTPUT = '/mnt/user-data/outputs'

# ============================================================
# CONFIDENCE THRESHOLDS
# ============================================================
HIGH_CONF   = -0.3
MEDIUM_CONF = -0.8
WORD_SCORE_THRESHOLD = 0.7

# ============================================================
# CSV PARSER
# ============================================================

def parse_timecode(tc_str):
    tc_str = tc_str.strip().strip('"')
    m = re.match(r'(\d+):(\d+):(\d+),(\d+)', tc_str)
    if not m: return 0
    return int(m.group(1))*3600000 + int(m.group(2))*60000 + int(m.group(3))*1000 + int(m.group(4))

def parse_csv_subs(filepath):
    subs = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read().replace('\r\n', '\n').replace('\r', '\n')
    reader = csv.DictReader(io.StringIO(content))
    for row in reader:
        subs.append({
            'index': int(row['Sequence']),
            'start_ms': parse_timecode(row['TimeIn']),
            'end_ms': parse_timecode(row['TimeOut']),
            'text': row['Text'].strip()
        })
    return subs

# ============================================================
# WHISPER PREPROCESSING — align words to chi_tra subs
# ============================================================

def preprocess_whisper(json_path, chi_subs):
    """
    Split Whisper segments into per-chi-sub chunks via word timestamps.
    Returns a list aligned to chi_subs (one entry per chi sub).
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    segments = data.get('segments', [])

    # Flatten all words with parent segment metadata
    all_words = []
    for seg in segments:
        avg_lp = seg.get('avg_logprob', -999)
        no_sp = seg.get('no_speech_prob', 0)
        for w in seg.get('words', []):
            all_words.append({
                'word':     w.get('word', ''),
                'start_ms': int(w.get('start', 0) * 1000),
                'end_ms':   int(w.get('end', 0) * 1000),
                'score':    w.get('score', 0),
                'seg_logprob': avg_lp,
                'seg_no_speech': no_sp,
            })

    # Also keep segment-level data for subs that have no word-level info
    seg_level = []
    for seg in segments:
        seg_level.append({
            'start_ms': int(seg.get('start', 0) * 1000),
            'end_ms':   int(seg.get('end', 0) * 1000),
            'text':     seg.get('text', '').strip(),
            'avg_logprob': seg.get('avg_logprob', -999),
        })

    print(f"  Whisper: {len(segments)} segments, {len(all_words)} words")

    # Assign each word to the chi sub it best overlaps with
    # Build a map: chi_index → list of words
    chi_words = {s['index']: [] for s in chi_subs}

    for w in all_words:
        best_sub = None
        best_overlap = 0
        for cs in chi_subs:
            overlap = max(0, min(w['end_ms'], cs['end_ms']) - max(w['start_ms'], cs['start_ms']))
            if overlap > best_overlap:
                best_overlap = overlap
                best_sub = cs['index']
        # Fallback: nearest chi sub by start time
        if best_sub is None:
            best_d = float('inf')
            for cs in chi_subs:
                d = abs(w['start_ms'] - cs['start_ms'])
                if d < best_d:
                    best_d = d
                    best_sub = cs['index']
        if best_sub is not None:
            chi_words[best_sub].append(w)

    # Build compact alignment: one entry per chi sub
    yue_aligned = []
    for cs in chi_subs:
        words = chi_words.get(cs['index'], [])
        if words:
            text = ''.join(w['word'] for w in words)
            avg_score = sum(w['score'] for w in words) / len(words)
            # Use the most common (mode) segment logprob among the words
            logprobs = [w['seg_logprob'] for w in words]
            avg_logprob = sum(logprobs) / len(logprobs)
            word_start = min(w['start_ms'] for w in words)
            word_end = max(w['end_ms'] for w in words)

            if avg_logprob >= HIGH_CONF:
                tier = 'HIGH'
            elif avg_logprob >= MEDIUM_CONF:
                tier = 'MEDIUM'
            else:
                tier = 'LOW'

            yue_aligned.append({
                'chi_index': cs['index'],
                'text': text.strip(),
                'confidence': tier,
                'avg_logprob': round(avg_logprob, 3),
                'avg_word_score': round(avg_score, 3),
                'word_start_ms': word_start,
                'word_end_ms': word_end,
                'word_count': len(words),
            })
        else:
            # No word-level match — try segment-level fallback
            best_seg = None
            best_o = 0
            for sl in seg_level:
                o = max(0, min(cs['end_ms'], sl['end_ms']) - max(cs['start_ms'], sl['start_ms']))
                if o > best_o:
                    best_o = o
                    best_seg = sl
            if best_seg and best_o > 0:
                lp = best_seg['avg_logprob']
                tier = 'HIGH' if lp >= HIGH_CONF else ('MEDIUM' if lp >= MEDIUM_CONF else 'LOW')
                yue_aligned.append({
                    'chi_index': cs['index'],
                    'text': best_seg['text'].strip(),
                    'confidence': tier,
                    'avg_logprob': round(lp, 3),
                    'avg_word_score': 0,
                    'word_start_ms': best_seg['start_ms'],
                    'word_end_ms': best_seg['end_ms'],
                    'word_count': 0,  # segment-level, no word granularity
                })
            else:
                yue_aligned.append({
                    'chi_index': cs['index'],
                    'text': '',
                    'confidence': 'N/A',
                })

    # Stats
    tiers = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0, 'N/A': 0}
    for ya in yue_aligned:
        tiers[ya.get('confidence', 'N/A')] += 1
    print(f"  Aligned to {len(chi_subs)} chi subs: HIGH={tiers['HIGH']}, MEDIUM={tiers['MEDIUM']}, LOW={tiers['LOW']}, N/A={tiers['N/A']}")

    # Words assigned stats
    assigned = sum(1 for ya in yue_aligned if ya.get('word_count', 0) > 0)
    print(f"  Word-level alignment: {assigned}/{len(chi_subs)} subs have word data")

    return yue_aligned

# ============================================================
# DETECT YUE FORMAT & LOAD
# ============================================================


def run(ep, *, uploads=UPLOADS, work=WORK, output=OUTPUT):
    """Run the pipeline for a given episode number. Paths default to production locations."""
    yue_json_path = None
    yue_is_whisper = False

    # Compact alignment output path (written during preprocessing)
    yue_prealigned_path = os.path.join(work, f'ep{ep}-yue-aligned.json')

    # Canonical input: {N}-yue.json only
    candidate = os.path.join(uploads, f'{ep}-yue.json')
    if os.path.exists(candidate):
        yue_json_path = candidate

    # Load eng and chi
    eng = parse_csv_subs(f'{uploads}/{ep}-eng.csv')
    chi = parse_csv_subs(f'{uploads}/{ep}-chi_tra.csv')

    # Load / preprocess yue (Whisper JSON only — CSV yue is no longer produced)
    yue_aligned_data = None  # compact per-chi-sub alignment

    if yue_json_path and os.path.exists(yue_json_path):
        print(f"Ep{ep}: Preprocessing Whisper JSON → chi_tra alignment")
        print(f"  Source: {yue_json_path}")
        yue_aligned_data = preprocess_whisper(yue_json_path, chi)
        yue_is_whisper = True

        # Save compact alignment
        with open(yue_prealigned_path, 'w', encoding='utf-8') as f:
            json.dump(yue_aligned_data, f, ensure_ascii=False, indent=1)
        print(f"  Saved: {yue_prealigned_path}")

        # Build yue list for the alignment step, keyed by chi sub index
        yue = []
        for ya in yue_aligned_data:
            ci = ya['chi_index']
            cs = next((c for c in chi if c['index'] == ci), None)
            if cs and ya.get('text'):
                yue.append({
                    'index': ci,
                    'start_ms': cs['start_ms'],
                    'end_ms': cs['end_ms'],
                    'text': ya['text'] if ya['confidence'] != 'LOW' else '',
                    '_confidence': ya['confidence'],
                    '_avg_logprob': ya.get('avg_logprob', -999),
                    '_avg_word_score': ya.get('avg_word_score', 0),
                    '_word_start_ms': ya.get('word_start_ms', 0),
                    '_word_end_ms': ya.get('word_end_ms', 0),
                })

        del yue_aligned_data
        print(f"  Whisper JSON discarded from memory")
    else:
        yue = []
        print(f"Ep{ep}: WARNING — no yue Whisper JSON found at expected path")

    print(f"Ep{ep}: eng={len(eng)}, chi={len(chi)}, yue={len(yue)}")

    # ============================================================
    # ALIGNMENT (chi as entry spine; eng reflowed onto chi)
    # ============================================================
    #
    # Previous behaviour: iterated over eng and attached chi/yue via timestamp
    # overlap. Output had one entry per eng sub with eng index/timing. This
    # produced "double-subs" when eng and chi authored the same spoken line at
    # offset timings — adjacent output entries ended up with near-duplicate
    # content. See PIPELINE.md Step 1 and STYLE.md §16.
    #
    # Current behaviour: chi is the entry spine. Output has one entry per chi
    # sub with chi index/timing. Eng content is reflowed onto chi entries:
    #   - Multiple eng overlap one chi → merge eng texts
    #   - One eng entry spans multiple chi → split eng text proportionally by
    #     chi window duration (heuristic; Step 4 human review adjusts)
    #   - Chi entry with no eng overlap → look within ±3 neighbours; else empty
    #
    # Yue is already chi-indexed from the Whisper preprocessing above.

    def overlap_ms(a, b):
        """Return timestamp-overlap in ms between two subs (with start_ms/end_ms)."""
        return max(0, min(a['end_ms'], b['end_ms']) - max(a['start_ms'], b['start_ms']))


    def find_overlapping_engs(chi_sub, eng_subs):
        """All eng subs that overlap this chi sub's window (ordered by index)."""
        hits = [e for e in eng_subs if overlap_ms(chi_sub, e) > 0]
        hits.sort(key=lambda e: e['index'])
        return hits


    def split_eng_proportionally(eng_text, eng_sub, chi_windows_for_this_eng):
        """
        One eng sub covers several chi windows — distribute eng_text across them
        proportionally to each chi window's duration within the eng window.
        Returns dict mapping chi_index → text chunk.

        Heuristic: split on sentence boundaries if the number matches, else on
        character-count proportion. Step 4 human review is the final arbiter;
        this keeps output structurally correct even if prose splits are imperfect.
        """
        eng_start = eng_sub['start_ms']
        eng_end = eng_sub['end_ms']
        eng_dur = max(1, eng_end - eng_start)

        # Order chi windows by their midpoint within the eng window
        ordered = sorted(chi_windows_for_this_eng, key=lambda c: c['start_ms'])

        # Try sentence-boundary split first if count matches
        sentences = re.split(r'(?<=[.!?])\s+', eng_text.strip())
        sentences = [s for s in sentences if s.strip()]
        if len(sentences) == len(ordered):
            return {c['index']: sentences[i] for i, c in enumerate(ordered)}

        # Newline split fallback (dialogue with em-dash lines)
        lines = [ln for ln in eng_text.split('\n') if ln.strip()]
        if len(lines) == len(ordered):
            return {c['index']: lines[i] for i, c in enumerate(ordered)}

        # Character-proportion fallback
        total_chars = len(eng_text)
        result = {}
        cursor = 0
        for i, c in enumerate(ordered):
            if i == len(ordered) - 1:
                # Last one gets the remainder (handles rounding)
                result[c['index']] = eng_text[cursor:].strip()
            else:
                # Share of eng_text proportional to chi window's share of eng window
                c_overlap = overlap_ms(c, eng_sub)
                share = c_overlap / eng_dur
                take = max(1, int(total_chars * share))
                # Prefer to break at a space near the target boundary
                end = min(cursor + take, total_chars)
                # Look for a space within ±10 chars of the target
                window = eng_text[max(cursor, end - 10):min(total_chars, end + 10)]
                if ' ' in window:
                    space_offset = window.rfind(' ')
                    end = max(cursor, end - 10) + space_offset
                result[c['index']] = eng_text[cursor:end].strip()
                cursor = end
        return result


    # Pass 1: for each eng sub, figure out which chi windows it overlaps.
    # Subs that fall entirely inside one chi window will be merged there.
    # Subs that span multiple chi windows will be split proportionally.
    eng_to_chis = {}  # eng_index → list of chi subs it overlaps
    for e in eng:
        overlapping = [c for c in chi if overlap_ms(e, c) > 0]
        eng_to_chis[e['index']] = overlapping

    # Pass 2: build per-chi eng content.
    # For each chi sub, collect contributions from any eng that overlaps it.
    chi_eng_contrib = {c['index']: [] for c in chi}  # chi_index → list of (eng_index, text)

    for e in eng:
        chi_hits = eng_to_chis[e['index']]
        if len(chi_hits) == 0:
            # Eng with no chi overlap — dropped (chi-spine means we don't emit
            # entries that aren't in chi). Worth noting for diagnostics.
            continue
        elif len(chi_hits) == 1:
            chi_eng_contrib[chi_hits[0]['index']].append((e['index'], e['text']))
        else:
            # One eng sub, multiple chi windows — split proportionally
            split = split_eng_proportionally(e['text'], e, chi_hits)
            for chi_idx, chunk in split.items():
                if chunk:
                    chi_eng_contrib[chi_idx].append((e['index'], chunk))

    # Pass 3: build the aligned list, one entry per chi sub.
    aligned = []
    orphan_chi_count = 0
    for c in chi:
        contribs = chi_eng_contrib[c['index']]

        # Merge eng contributions for this chi sub (if any)
        if contribs:
            # Order by eng index (preserves natural reading order)
            contribs.sort(key=lambda t: t[0])
            eng_text = '\n'.join(t for _, t in contribs if t.strip())
        else:
            # No direct overlap — try temporal-proximity fallback: look for an
            # eng sub that had no chi overlap at all (i.e. "dropped" in Pass 2)
            # and is within 2000ms of this chi window. Last-ditch rescue for
            # timing drift cases.
            eng_text = ''
            for e in eng:
                if eng_to_chis[e['index']]:  # eng sub already claimed by some chi
                    continue
                # Dropped eng sub — check temporal proximity to this chi
                if (overlap_ms(e, c) > 0
                        or abs(e['start_ms'] - c['start_ms']) < 2000
                        or abs(e['end_ms'] - c['end_ms']) < 2000):
                    eng_text = e['text']
                    break
            if not eng_text:
                orphan_chi_count += 1

        # Yue for this chi sub — look up by chi index (yue is chi-indexed from
        # Whisper preprocessing)
        y_matches = [y for y in yue if y['index'] == c['index']]
        yue_text = y_matches[0]['text'] if y_matches else ''
        yue_conf = 'N/A'
        yue_lp = None
        yue_word_score = 0
        yue_word_start = 0
        yue_word_end = 0

        if yue_is_whisper and y_matches:
            y = y_matches[0]
            yue_conf = y.get('_confidence', 'N/A')
            yue_lp = y.get('_avg_logprob')
            yue_word_score = y.get('_avg_word_score', 0)
            yue_word_start = y.get('_word_start_ms', 0)
            yue_word_end = y.get('_word_end_ms', 0)
            if yue_conf == 'LOW':
                yue_text = ''

        rec = {
            'index': c['index'],
            'start_ms': c['start_ms'],
            'end_ms': c['end_ms'],
            'eng': eng_text,
            'chi': c['text'],
            'yue': yue_text,
            'yue_end_ms': yue_word_end,
            'yue_confidence': yue_conf,
        }
        if yue_lp is not None:
            rec['yue_avg_logprob'] = round(yue_lp, 3)

        aligned.append(rec)

    # Diagnostics
    print(f"\n=== CHI-SPINE ALIGNMENT ===")
    print(f"  Output entries: {len(aligned)} (= chi count; eng had {len(eng)})")
    dropped_eng = sum(1 for e in eng if not eng_to_chis[e['index']])
    if dropped_eng:
        print(f"  ⚠ {dropped_eng} eng sub(s) had no chi overlap — content dropped (see Step 4 review)")
    if orphan_chi_count:
        print(f"  ⚠ {orphan_chi_count} chi sub(s) have no eng content — Step 3 will populate from chi")

    # ============================================================
    # TIMING ADJUSTMENT FROM WHISPER WORDS
    # ============================================================

    timing_adjustments = 0
    if yue_is_whisper:
        print(f"\n=== TIMING ADJUSTMENT PASS ===")
        # Re-read the compact alignment for word-level timing
        with open(yue_prealigned_path, 'r', encoding='utf-8') as f:
            yue_compact = json.load(f)
        # Build lookup: chi_index → compact entry
        yue_compact_map = {ya['chi_index']: ya for ya in yue_compact}

        for a in aligned:
            if a.get('yue_confidence') in ('LOW', 'N/A'):
                continue
            # Under chi-spine, a['index'] IS the chi index (one aligned entry per chi sub)
            ya = yue_compact_map.get(a['index'])
            if not ya or ya.get('word_count', 0) == 0:
                continue
            if ya.get('avg_word_score', 0) < WORD_SCORE_THRESHOLD:
                continue

            word_start = ya['word_start_ms']
            word_end = ya['word_end_ms']
            orig_start = a['start_ms']
            orig_end = a['end_ms']
            new_start = orig_start
            new_end = orig_end

            if abs(word_end - orig_end) > 100 and abs(word_end - orig_end) < 2000:
                new_end = word_end
            if word_start > orig_start + 100 and word_start < orig_start + 1500:
                new_start = word_start

            if new_start != orig_start or new_end != orig_end:
                a['start_ms_orig'] = orig_start
                a['end_ms_orig'] = orig_end
                a['start_ms'] = new_start
                a['end_ms'] = new_end
                a['timing_adjusted'] = True
                timing_adjustments += 1

        del yue_compact  # free memory

        print(f"  Adjusted {timing_adjustments}/{len(aligned)} sub timings")

        # Fix overlaps
        overlap_fixes = 0
        for i in range(len(aligned) - 1):
            if aligned[i]['end_ms'] > aligned[i+1]['start_ms']:
                aligned[i]['end_ms'] = aligned[i+1]['start_ms']
                overlap_fixes += 1
        if overlap_fixes:
            print(f"  Fixed {overlap_fixes} overlaps")

    # ============================================================
    # SAVE & DUMP
    # ============================================================

    with open(f'{work}/ep{ep}_aligned.json', 'w', encoding='utf-8') as f:
        json.dump(aligned, f, ensure_ascii=False, indent=1)

    # --- Dump goes to file, not stdout ---
    # Rationale: the full dump is the canonical Step 2 examination artifact.
    # In prior bundle versions (≤ v9) it was printed to stdout, which the
    # assistant would then re-read by echoing through `python3 -c` calls —
    # every round-trip cost context. Writing once to `ep{N}_dump.txt` lets
    # the assistant `view` selective line ranges without regenerating the
    # content. See PIPELINE.md Step 2.
    dump_path = f'{work}/ep{ep}_dump.txt'
    with open(dump_path, 'w', encoding='utf-8') as f:
        f.write(f"=== FULL DUMP Ep{ep} ({len(aligned)} subs) ===\n")
        f.write("FORMAT: index|conf|eng|chi|yue\n")
        f.write("  conf: HIGH/MEDIUM/LOW/N/A; [T-ADJ] = timing adjusted\n")
        f.write("  newlines in eng/chi are shown as ' // '\n")
        f.write("  yue is truncated to 200 chars per sub to keep the file compact\n")
        f.write("=" * 60 + "\n")
        for a in aligned:
            e = a['eng'].replace('\n', ' // ')
            c = a['chi'].replace('\n', ' // ')
            y = a['yue'][:200] if a['yue'] else ''
            conf = a.get('yue_confidence', 'N/A')
            adj = ' [T-ADJ]' if a.get('timing_adjusted') else ''
            f.write(f"{a['index']}|{conf}{adj}|E:{e}|C:{c}|Y:{y}\n")
        f.write("=== END DUMP ===\n")

    # --- Compact stdout summary ---
    print(f"\n=== Ep{ep} alignment complete ===")
    print(f"  Subs aligned: {len(aligned)}")
    print(f"  Dump written: {dump_path}")
    if yue_is_whisper:
        counts = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0, 'N/A': 0}
        for a in aligned:
            counts[a.get('yue_confidence', 'N/A')] += 1
        print(f"  Confidence: HIGH={counts['HIGH']} MEDIUM={counts['MEDIUM']} "
              f"LOW={counts['LOW']} N/A={counts['N/A']}")
        print(f"  Timing adjustments: {timing_adjustments}")
    print(f"\nNext: python3 auto_override_v2.py {ep}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pipeline.py <episode_number>")
        sys.exit(1)
    run(int(sys.argv[1]))


if __name__ == '__main__':
    main()
