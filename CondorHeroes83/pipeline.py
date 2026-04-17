#!/usr/bin/env python3
"""
Pipeline v5 for Legend of the Condor Heroes subtitle processing.
Usage: python3 pipeline.py <episode_number>

Whisper JSON preprocessing:
  1. Load chi_tra CSV as the alignment anchor (not eng — chi timings
     are closer to the actual Cantonese speech).
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

CSV yue input still supported as fallback.
"""

import sys, re, csv, io, json, os, glob

EP = int(sys.argv[1])
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
    Also strips opening/ending song segments and saves them separately.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    segments = data.get('segments', [])

    # ---- Strip credit songs ----
    OPENING_SIGS = ['人海之中', '找到了你', '一切變了有情', '從今心中就找到了美',
                    '人生匆匆', '萬水千山此生有人']
    ENDING_SIGS = ['若願將一世交換', '願將一世交換', '肯去承擔愛',
                   '寧可拋去生命', '癡心決不願改', '甘心去忍受', '濃情沒有東西能代']

    def has_sig(text, sigs):
        return any(s in text for s in sigs)

    ep_duration = max(s.get('end', 0) for s in segments) if segments else 0

    song_segments = {'opening': [], 'ending': []}
    dialogue_segments = []

    for seg in segments:
        text = seg.get('text', '').strip()
        start = seg.get('start', 0)
        is_song = False

        # Opening: first 120s with opening signatures
        if start < 120 and has_sig(text, OPENING_SIGS):
            song_segments['opening'].append(seg)
            is_song = True
        # Ending: last 120s with ending or opening-reprise signatures
        elif start > ep_duration - 120 and (has_sig(text, ENDING_SIGS) or has_sig(text, OPENING_SIGS)):
            song_segments['ending'].append(seg)
            is_song = True

        if not is_song:
            dialogue_segments.append(seg)

    stripped = len(segments) - len(dialogue_segments)
    if stripped:
        print(f"  Stripped {stripped} song segment(s): opening={len(song_segments['opening'])}, ending={len(song_segments['ending'])}")
        # Save song segments for reference
        song_out = f'{WORK}/ep{EP}_songs.json'
        with open(song_out, 'w', encoding='utf-8') as f:
            json.dump(song_segments, f, ensure_ascii=False, indent=2)

    segments = dialogue_segments
    # ---- End song stripping ----

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

yue_json_path = None
yue_is_whisper = False

# Check for pre-processed alignment first
yue_prealigned_path = os.path.join(WORK, f'ep{EP}-yue-aligned.json')

# Check for Whisper JSON
for pattern in [f'{EP}-yue.json', f'{EP}-yue-whisper.json', f'{EP}_yue.json',
                f'ep{EP}-yue.json', f'ep{EP}_yue.json']:
    candidate = os.path.join(UPLOADS, pattern)
    if os.path.exists(candidate):
        yue_json_path = candidate
        break
if not yue_json_path:
    matches = glob.glob(os.path.join(UPLOADS, f'*{EP}*yue*.json'))
    if not matches:
        matches = glob.glob(os.path.join(UPLOADS, f'*yue*.json'))
    if matches:
        yue_json_path = matches[0]

yue_csv_path = os.path.join(UPLOADS, f'{EP}-yue.csv')

# Load eng and chi
eng = parse_csv_subs(f'{UPLOADS}/{EP}-eng.csv')
chi = parse_csv_subs(f'{UPLOADS}/{EP}-chi_tra.csv')

# Load / preprocess yue
yue_aligned_data = None  # compact per-chi-sub alignment

if yue_json_path and os.path.exists(yue_json_path):
    print(f"Ep{EP}: Preprocessing Whisper JSON → chi_tra alignment")
    print(f"  Source: {yue_json_path}")
    yue_aligned_data = preprocess_whisper(yue_json_path, chi)
    yue_is_whisper = True

    # Save compact alignment
    with open(yue_prealigned_path, 'w', encoding='utf-8') as f:
        json.dump(yue_aligned_data, f, ensure_ascii=False, indent=1)
    print(f"  Saved: {yue_prealigned_path}")

    # Build yue list in CSV-compatible format for the alignment step
    # Index by chi sub index for lookup during eng alignment
    yue = []
    for ya in yue_aligned_data:
        ci = ya['chi_index']
        # Find corresponding chi sub for timing
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

    # Raw Whisper JSON is no longer needed
    del yue_aligned_data
    print(f"  Whisper JSON discarded from memory")

elif os.path.exists(yue_csv_path):
    yue = parse_csv_subs(yue_csv_path)
    print(f"Ep{EP}: yue loaded from CSV (fallback)")
else:
    yue = []
    print(f"Ep{EP}: WARNING — no yue track found")

print(f"Ep{EP}: eng={len(eng)}, chi={len(chi)}, yue={len(yue)}")

# ============================================================
# ALIGNMENT (eng as structural base, chi as authority)
# ============================================================

def best_overlap(target, candidates):
    best = None; best_o = 0
    for c in candidates:
        o = max(0, min(target['end_ms'], c['end_ms']) - max(target['start_ms'], c['start_ms']))
        if o > best_o: best_o = o; best = c
    if not best:
        best_d = float('inf')
        for c in candidates:
            d = min(abs(target['start_ms']-c['start_ms']), abs(target['end_ms']-c['end_ms']))
            if d < best_d and d < 2000: best_d = d; best = c
    return best

def find_yue_blocks(e_sub, yue_blocks):
    results = []
    for y in yue_blocks:
        o = max(0, min(e_sub['end_ms'], y['end_ms']) - max(e_sub['start_ms'], y['start_ms']))
        if o > 0: results.append(y)
    if not results:
        for y in yue_blocks:
            d = min(abs(e_sub['start_ms']-y['start_ms']), abs(e_sub['start_ms']-y['end_ms']),
                    abs(e_sub['end_ms']-y['start_ms']))
            if d < 2000: results.append(y); break
    return results

aligned = []
for e in eng:
    cm = best_overlap(e, chi)
    ym = find_yue_blocks(e, yue) if yue else []
    yue_end = max((y['end_ms'] for y in ym), default=0) if ym else 0

    # Build yue text — now compact (one chunk per chi sub, not a huge segment blob)
    if ym:
        # Deduplicate: if multiple yue entries matched, join unique texts
        seen = set()
        texts = []
        for y in ym:
            t = y['text']
            if t and t not in seen:
                texts.append(t)
                seen.add(t)
        yue_text = ' '.join(texts)
    else:
        yue_text = ''

    # Confidence and timing from yue
    yue_confidence = 'N/A'
    yue_avg_logprob = None
    yue_word_score = 0
    yue_word_start = 0
    yue_word_end = 0

    if yue_is_whisper and ym:
        best_seg = max(ym, key=lambda y: y.get('_avg_logprob', -999))
        yue_confidence = best_seg.get('_confidence', 'N/A')
        yue_avg_logprob = best_seg.get('_avg_logprob')
        yue_word_score = max(y.get('_avg_word_score', 0) for y in ym)
        # Timing from word boundaries
        starts = [y['_word_start_ms'] for y in ym if y.get('_word_start_ms', 0) > 0]
        ends = [y['_word_end_ms'] for y in ym if y.get('_word_end_ms', 0) > 0]
        if starts: yue_word_start = min(starts)
        if ends: yue_word_end = max(ends)

        if yue_confidence == 'LOW':
            yue_text = ''  # discard silently

    rec = {
        'index': e['index'],
        'start_ms': e['start_ms'],
        'end_ms': e['end_ms'],
        'eng': e['text'],
        'chi': cm['text'] if cm else '',
        'yue': yue_text,
        'yue_end_ms': yue_end,
        'yue_confidence': yue_confidence,
    }
    if yue_avg_logprob is not None:
        rec['yue_avg_logprob'] = round(yue_avg_logprob, 3)

    aligned.append(rec)

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
        # Find the chi sub this eng sub aligned to
        cm = best_overlap(a, chi)
        if not cm:
            continue
        ya = yue_compact_map.get(cm['index'])
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

with open(f'{WORK}/ep{EP}_aligned.json', 'w', encoding='utf-8') as f:
    json.dump(aligned, f, ensure_ascii=False, indent=1)

print(f"\n=== FULL DUMP Ep{EP} ({len(aligned)} subs) ===")
for a in aligned:
    e = a['eng'].replace('\n', ' // ')
    c = a['chi'].replace('\n', ' // ')
    y = a['yue'][:60] if a['yue'] else ''
    conf = a.get('yue_confidence', '')
    conf_tag = f' [{conf}]' if conf and conf != 'N/A' else ''
    adj = ' [T-ADJ]' if a.get('timing_adjusted') else ''
    print(f"{a['index']}|{e}|{c}|{y}{conf_tag}{adj}")

print(f"\n=== END DUMP ===")

# Confidence summary
if yue_is_whisper:
    print(f"\n=== YUE CONFIDENCE SUMMARY ===")
    counts = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0, 'N/A': 0}
    for a in aligned:
        counts[a.get('yue_confidence', 'N/A')] += 1
    for tier, n in counts.items():
        print(f"  {tier}: {n}")

print(f"\nEp{EP} pipeline complete. Next: auto_override_v2.py {EP}")
