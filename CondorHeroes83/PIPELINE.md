# Pipeline — Legend of the Condor Heroes 1983 TVB Subtitle Pipeline

Consolidated from: `LOCH1983-Handoff-Config-v3.md`, `ProcessSpecification-v2.md`, `EP28-HANDOFF-NOTES.md` (pipeline sections only).

> **Companion docs:**
> - `STYLE.md` — every style decision (variants, names, titles, idioms, yue register, formatting, anti-patterns)
> - `REFERENCE.md` — context-dependent judgment calls, error taxonomy, character framework
> - `SESSION-NOTES.md` — episode completion status, pending-episode previews, and a watch list of names/terms/oddities not yet promoted to the consolidated docs

---

## The Prime Directive

**Priority chain: yue (HIGH) > chi (semantic authority) > eng (draft).**

Yue (Cantonese) is the actual spoken dialogue of a Cantonese show. At HIGH Whisper confidence, yue overrides chi when it offers a more vivid, specific, or colloquial word — *provided the yue text is intelligible*. Whisper can be HIGH-confident on garbled output; when yue diverges from chi but reads as broken syntax or semantic nonsense, treat it as ASR noise and fall back to chi. Chi (Mandarin) is the semantic authority — a written translation that sometimes flattens the spoken register. English is an OCR'd fan-sub rough draft. For full treatment of the priority chain, the Yue-Authority Rule, and the intelligibility gate, see `STYLE.md` §2.

Every subtitle must be read against both chi and yue. The English track frequently:
- Fabricates content not in the Chinese (but check yue before deleting — yue may confirm the eng)
- Flattens nuance (好像 "seemed" → "became"; 奮不顧身 "risking one's life" → dropped)
- Drops address terms (仙姑, 前輩, 師父 → just "you" or nothing)
- Misses idioms (四字成語 present in chi but absent from English)
- Simplifies register (低聲下氣 "grovelling" → "begging") — yue often preserves the register chi flattened

**Examine EVERY sub.** Override if the content or register mismatches; otherwise default to the original English.

---

## Quality Control — MANDATORY

**One episode per request.** Batching is not a supported mode.

Before beginning work on any episode, the assistant reports the context state:
- Use the Step 0 context estimate together with the conservative sub-count defaults below to judge likely completion.
- Say explicitly: "My context estimate is ~ZZ%, and Episode N has XXX subs."
- If multiple episodes are requested in a single message, pick one and state the choice rather than asking.

**Thresholds are not fixed.** A session at ~70% baseline that has processed smaller episodes can often still handle another small one; a session at ~40% starting fresh with a 600-sub episode might still be tight. Judge from the delta data, not a hard percentage.

### Quality Outcomes (Diagnostic)

FULL is the target quality. PARTIAL and MECHANICAL-ONLY are named failure modes — they exist so a degraded delivery can be honestly labelled. Always aim for FULL; if the realistic outcome is PARTIAL or MECHANICAL-ONLY, say so in the Step 0 report so the user can decide how to proceed.

| Outcome | Description | When it happens |
|---------|-------------|-----------------|
| **FULL** (target) | Every sub examined against chi and yue; overrides written where content or register mismatches; OCR corrections via yue-as-witness, yue-authority overrides applied, idiom injection, characterisation preserved. | Step 4 examination loop completed for every sub. |
| **PARTIAL** (failure mode) | Step 3 preprocessing applied to all subs; Step 4 examination completed for roughly 20–60% of subs before aborting. Names/titles/idioms mechanically correct throughout; the unexamined subs retain whatever Step 3 produced, unchecked against chi and yue for meaning/register. | Step 4 had to abort partway — typically because context ran out mid-examination, or the assistant hit an output-length limit on a large override pass. Acknowledge the outcome honestly in delivery; flag which sub-range was examined and which wasn't. |
| **MECHANICAL-ONLY** (failure mode) | Step 3 preprocessing applied to all subs; Step 4 examination barely started (<20% of subs examined) or didn't run at all. Mechanical CJK substitutions and idiom injections are good, but meaning and register are not systematically checked. | Step 4 aborted very early, or the session delivered output after only running Steps 1–3. Acknowledge the outcome honestly in delivery. |

---

## Narration Discipline

Status output has a context cost. Long conversational summaries between tool calls — "Here's what I've done so far", "Summary of Step 4 work", "Candidates to promote", "Watch List additions" — consume roughly 15–25% of the session's budget during a FULL pass and largely repeat information the user already sees in tool output and the delivered SRTs. Keep conversational output minimal.

### Required output (keep)
- **Step 0 context baseline report.** Required before any tool call. Format per Step 0.
- **Step 8.5 SESSION-NOTES update and present.** Required after the three SRTs are presented. Format per Step 8.5.
- **Step 9 ending context report.** Required after the SESSION-NOTES `present_files`. Format per Step 9.
- **User-directed questions** when a genuine ambiguity requires a decision (rare in a FULL pass).
- **The final `present_files` call** with the three SRTs.

### Cut (don't produce)
- **Mid-turn "progress report" blocks** between script runs. The tool outputs already say "applied 420 overrides" or "✓ jyutping: clean" — don't restate.
- **"Let me now run X" / "Let me check Y" narration** before tool calls. Just run the tool.
- **End-of-turn recaps** that list what each step produced. The files produced are visible to the user; the TSV and overlay are in `/home/claude/` and reachable if needed.
- **Speculative interpretive commentary** on tool output ("Build guard caught...", "The lint warning is a false positive because..."). If the finding is actionable, act on it silently; if it's not, don't mention it.
- **"Candidates to promote" / "Watch List additions"** lists at the end of an episode. These belong in the `SESSION-NOTES.md` file that Step 8.5 writes and presents, not in chat. Make the edit, present the file, and stop — don't also list what you put in it.

### Exception — real issues
If something actually went wrong — a Step that couldn't complete, a source file that was malformed, a validation failure that required a non-trivial workaround — surface it in a short issues list at the end. One line per issue. Use plain phrasing, not section headers.

### Model for a Step 4 → present cycle

Good:
> *[runs pipeline.py, shared_extras.py, auto_override_v2.py silently]*
> *[reads dump in ranges, writes TSV silently]*
> *[runs apply_overrides, shared_extras, lint, build, cjk_fix_v2 silently]*
> *[runs validation silently]*
> *[calls present_files with the three SRTs]*
>
> Ep27 complete. 503 subs, 420 overrides applied. One issue: cjk_fix_v2's duplicate-gloss collapser has an 8-char-per-side minimum that missed "crafty — crafty"; post-cleaned.
>
> *[edits SESSION-NOTES.md: moves Ep27 to Completed table, adds 2 Watch List items, promotes 1 stable entry out]*
> *[calls present_files with the updated SESSION-NOTES.md]*
>
> [Step 9 context report]

Bad: narrating every step ("Let me now read STYLE.md...", "Step 3 complete — only 19 AUTO-KEEPs, which makes sense because..."), emitting progress-report blocks between script runs, and duplicating at end-of-turn the Watch-List / promotion lists that belong in SESSION-NOTES.md.

---

## Project Overview

Producing three SRT subtitle variants per episode from three source tracks (eng CSV, chi_tra CSV, yue Whisper JSON):

- `{N}-eng-hybrid-v{VERSION}.srt` — English prose with CJK for names/titles/idioms/places
- `{N}-eng-jyutping-v{VERSION}.srt` — Full Jyutping romanisation
- `{N}-eng-yale-v{VERSION}.srt` — Full Yale romanisation

`{VERSION}` is read from the `VERSION` file in the handoff bundle (see [Handoff Files Checklist](#handoff-files-checklist) below). Example with v9: `24-eng-hybrid-v9.srt`.

Source files:
- `/mnt/user-data/uploads/{N}-eng.csv`
- `/mnt/user-data/uploads/{N}-chi_tra.csv`
- `/mnt/user-data/uploads/{N}-yue.json` (Whisper output with word-level timing and `avg_logprob` confidence)

Output: `/mnt/user-data/outputs/`

PersonalNames lookup: `/home/claude/PersonalNamesUpdated.csv` (copy from uploads first).

---

## The Pipeline

### Step 0 — Estimate Starting Context

Before touching any files, report an estimated context use baseline. This feeds the Quality Control decision: the question isn't "is context above some threshold" but "will Step 4 have room to complete for this episode's sub count?"

The assistant can't read its own context percentage directly, but it can estimate from observable signals:
- Bytes of config/reference docs read (`PIPELINE.md`, `STYLE.md`, `REFERENCE.md`, `SESSION-NOTES.md`, `PersonalNamesUpdated.csv`)
- Bytes of any previously-loaded episode artifacts in this session (dumps, aligned JSON, override JSON)
- Number and size of prior tool-call outputs
- Conversation length

Report format:

```
Context baseline — Episode N
• Config/reference loaded: ~XX KB
• Prior episode artifacts in session: ~YY KB (or "none — fresh session")
• Estimated context use: ~ZZ%
• Episode size: XXX subs (from {N}-chi_tra.csv — chi is the entry spine)
• Expected delta for this episode: ~ΔΔ% (see "How to make the call" below)
• Projected quality at current context: FULL / borderline (may end PARTIAL) / likely MECHANICAL-ONLY
```

**How to make the call.** Conservative sub-count estimates: ~25% of context for a 400-sub episode during Step 4, ~40% for a 600-sub episode. If `baseline + expected delta` exceeds ~90%, project the outcome as borderline or likely-degraded. These estimates assume the file-based flow (reading `ep{N}_dump.txt` via `view` ranges rather than re-dumping via `python3 -c`) — reverting to stdout-and-echo patterns inflates usage significantly.

### Step 1 — Parse & Align

```bash
cp /mnt/user-data/uploads/PersonalNamesUpdated.csv /home/claude/
python3 pipeline.py <N>
```

Parses the three source tracks and aligns them onto a **chi-spine skeleton**: the output's entry count and timestamps are taken from chi, not eng. Outputs `ep{N}_aligned.json` plus a compact summary to stdout. The per-sub dump comes out of Step 3 (`auto_override_v2.py`), not this step — dump-writing colocates with flag-computation so `aligned.json` doesn't have to be re-read.

**Don't revert to stdout-dump-and-echo.** The dump is written once to disk and consumed via `view` line ranges in Step 2. Printing to stdout and round-tripping via `python3 -c` was the pre-v10 pattern and cost significant context; it caused real past sessions to run out of budget.

**Chi as entry spine:**
- Output entry count = chi entry count (not eng). See `STYLE.md` §16.
- For each chi entry, overlapping eng entries by timestamp window are reflowed onto the chi entry as the "draft content" field:
  - **Chi window spans multiple eng entries** → merge their content (joined with newlines, in eng-index order).
  - **One eng entry spans multiple chi entries** → split the eng text proportionally across the chi entries it covers. The split tries sentence boundaries first, then newlines, then character-proportion with space-snapping.
  - **Chi entry has no overlapping eng content** → look for a "dropped" eng entry (one that had no chi overlap) within 2000 ms and pull its text in. Otherwise leave eng empty; Step 3 and Step 4 will populate from chi.
- Yue words align to chi entries directly (chi timings are cleaner than eng).
- **Diagnostics printed at the end of alignment:** output-count vs chi-count, dropped-eng count (eng content that had no chi window and didn't get rescued), orphan-chi count (chi entries that ended up with empty eng).

**Why chi-spine:** eng and chi arrive with independently authored timings. Timestamp-overlap alignment using eng as the implicit skeleton produced "double-subs" — adjacent output entries with near-duplicate content when eng and chi both translated the same spoken line at offset times. Chi-spine makes structural duplication impossible: each spoken line has exactly one entry (chi's).

**Whisper JSON handling:**
- Reads yue from `{N}-yue.json` (Whisper output) only — no CSV fallback.
- Aligns yue words to chi_tra subs (chi-spine principle).
- Discards raw JSON from memory after extraction; keeps compact per-sub yue alignment only.

**Confidence tiers from `avg_logprob`:**
- **HIGH** (≥ −0.3) — yue is *candidate* authoritative over chi; flagged for manual review, where the reviewer applies the intelligibility gate (see `STYLE.md` §2) to decide whether yue actually overrides.
- **MEDIUM** (≥ −0.8) — chi remains authority; yue consulted for tone/register/nuance.
- **LOW** (< −0.8) — yue text discarded entirely; prefixed with `[DISCARDED]` in dump.

Each sub in the dump is annotated `[HIGH]` / `[MEDIUM]` / `[LOW]`, and `[T-ADJ]` marks subs whose start/end times were tightened to word boundaries (Whisper `score ≥ 0.7`). Per-sub confidence notes are written to `ep{N}_confidence.json` for the manual review pass.

### Step 2 — Read the Full Dump (MANDATORY)

Read EVERY line of `ep{N}_dump.txt`. Use `view` with line ranges — typically 100–200 subs per range — rather than `cat` or `python3 -c` round-trips.

**Dump format.** Each sub occupies 3–4 lines:

```
<idx>|<conf>|<flags>[ T-ADJ]
E <eng>
C <chi>
Y <yue>                      (omitted if empty; may be "[see N]" for dedup)
```

The `<flags>` column carries per-sub priority signals computed by `auto_override_v2.py`:

- `•` — AUTO-KEEP (passed all seven faithful_heuristic gates; likely quick-confirm)
- `!` — eng has fabrication-risk markers (long parenthetical, `", which"` clause)
- `i` — chi contains an idiom from the injection set
- `@` — chi has an address term (師父, 前輩, 老伯…) missing from the Step 3 output
- `o` — chi contains an OCR artifact (garbled quote marks, stray Latin letters amid CJK)
- `r` — **reflow risk**. Chi is thin (empty, ≤3 CJK chars) AND eng is substantive AND an adjacent sub has empty eng or chi. This is the signature of chi-spine alignment pulling eng content from a neighbouring beat into this sub's window. **When examining an `r`-flagged sub, do not call the eng fabrication without reading the adjacent subs first** — eng is probably legitimate dialogue that got reflowed here because its native window had no chi. Canonical case: Ep1 sub 18 (chi `上`, eng "What do you want?" — the victim's retort reflowed from the previous beat).
- `y` — **yue-solo**. Chi AND eng are both thin but yue is substantive at HIGH confidence. Either real dialogue lost from chi+eng (reflow stranded it, or the other two tracks skipped a beat) or Whisper ASR hallucination (invented plausible-sounding speech during music/silence/noise). Apply Rule C intelligibility gate + scene-context plausibility. If yue parses as real dialogue AND fits the scene, consider adding to hybrid; if yue is plausible-sounding but doesn't fit (theme-song lyrics during credits, crowd noise), treat as hallucination and ignore. **When in doubt, do not invent dialogue from yue alone.** Mutually exclusive with `r` (which takes priority when signatures overlap). HIGH-confidence-only by design — MEDIUM yue with richer content than chi+eng gets caught by normal Rule A register-examination in Step 4.

A blank flags column means "no priority signal" — scan quickly unless something else jumps out. Flags are priority signals, not gates: every sub must still be read, but time concentrates on non-blank flags.

**Scene markers.** Lines of the form `—— gap N.Ns ——` mark a timestamp gap > 5s between consecutive subs. These correlate with scene transitions and let the reviewer navigate by scene when re-reading a section (useful after a plot correction).

**Yue deduplication.** When a Whisper segment's yue text is identical across multiple consecutive chi subs (common — one 10-second yue span covers many short chi subs), the full text appears only at the sub with the strongest timing overlap. Other subs in the group show `Y [see N]`. If you need the yue context, scroll to sub N.

For each sub, compare the three columns:
- Column E (eng) — the rough draft
- Column C (chi) — the semantic authority
- Column Y (yue) — the actual spoken dialogue; at HIGH Whisper confidence, overrides chi on wording/register per the Yue-Authority Rule (`STYLE.md` §2)

Note as you go:
- **Fabrications** — eng says something neither chi nor yue supports → mark for deletion. If yue HIGH confirms eng and chi diverges, treat as OCR error in chi (see Ep28 Sub 22).
- **Meaning lost** — chi has nuance eng flattens → mark for rewriting
- **Yue-over-chi** — yue gives a more vivid/specific/colloquial word than chi and passes the intelligibility gate (coherent, parseable) → mark for yue-authority override
- **Garbled yue** — yue diverges from chi but reads as broken syntax or semantic nonsense → mark to ignore yue for this sub regardless of its confidence tier; trust chi
- **Address terms** — chi or yue has 仙姑 / 前輩 / 師父 / etc → must appear as CJK in hybrid
- **Idioms** — chi or yue has 四字成語 → must appear in hybrid
- **Register drift** — yue's emotional tone (blunt/warm/formal/colloquial) differs from the draft → mark for register fix even if chi meaning is preserved
- **OCR errors in chi** — yue is the witness (when yue is intelligible); fix the chi reading

### Step 3 — Apply Mechanical CJK Preprocessing

```bash
python3 shared_extras.py <N>
python3 auto_override_v2.py <N>
```

This is a **preprocessing pass**, not a translation attempt. It operates on the text's mechanical form — not its meaning — and its job is to get the tedious, error-prone substitutions right so Step 4 can focus on content and register. Specifically, it:

- Substitutes Pinyin → CJK (Guo Jing → 郭靖, Rong-er → 蓉兒)
- Substitutes English titles/places → CJK when chi has the CJK (White Camel Mountain → 白駝山, "teacher" → 師父 when 師父 is in chi)
- Injects address terms (仙姑, 前輩, 師父, etc.) where chi has them and eng dropped them
- Injects 四字成語 from chi that are missing in eng
- Fixes common OCR artifacts (`|` → `I`, etc.)

The output is saved to `ep{N}_h_all.json`. **This output is not a draft translation — it's the original English with mechanical substitutions applied.** It does NOT attempt to fix meaning, nuance, or register. That is Step 4's job.

Think of Step 3 as "setting up the hybrid's CJK scaffolding so the human isn't retyping 白駝山 or remembering to inject 奮不顧身 themselves."

**Baseline + overlay split.** `shared_extras.py` is a thin merger: it reads `extras_baseline.json` (ships with the bundle) and optionally `ep{N}_extras_add.json` (per-episode overlay — the reviewer writes this in Step 5), merges them, and writes `ep{N}_extra.json` for `build.py` to consume. A reviewer with nothing new to add can skip the overlay file; `shared_extras.py` still works. Overlay keys override baseline keys on collision.

**AUTO-KEEP heuristic.** `auto_override_v2.py` annotates each sub in `ep{N}_confidence.json` with an `auto_keep: true/false` flag. `auto_keep: true` means the sub passed all seven conservative gates (all tracks non-empty, yue HIGH/MEDIUM, no fabrication-risk markers, no idioms in chi, no missing address terms, ≤1.5× length ratio, ≥0.7 content-word overlap) — likely already faithful. AUTO-KEEP is a **priority signal, not a gate**: Step 4 still reads every sub, but concentrates examination time on the NEEDS REVIEW set (anything not flagged AUTO-KEEP). The heuristic is deliberately false-negative-biased: a false positive (flagging a subtly-flawed sub faithful) would silently degrade quality; a false negative just costs a quick-confirm examination.

### Step 4 — Examine Every Sub; Override When Warranted

Read `ep{N}_h_all.json` (populated with Step 3's CJK substitutions) alongside the chi track, the yue track, and `ep{N}_confidence.json`. Examine EVERY sub against the priority chain (**yue HIGH > chi > eng**) per `STYLE.md` §2 — which defines the Rule A register override, the Rule B semantic-disagreement default, and the Rule C intelligibility gate. If the Step 3 output already matches source content and register faithfully, default to it. Override only when content or register mismatches.

For every sub, walk this checklist:

1. Read chi for meaning, yue for register and (if HIGH) potential Rule A override. Compare against Step 3's output.
2. If eng says something neither chi nor yue supports → **DELETE** the fabrication. **But check reflow first** (the `r` flag in the Step 2 dump fires on this signature; see its explanation there). If chi is thin AND an adjacent sub has empty eng or chi, the eng content is probably reflow casualty, not invention — preserve it, merge with chi via em-dash dialogue-split (STYLE §13). If chi is substantive but eng still disagrees and yue confirms eng, treat as OCR error in chi (REFERENCE §8 Sub 22).
3. For `y`-flagged yue-solo subs, apply the procedure described with the flag in Step 2: Rule C intelligibility gate + scene-context plausibility. When in doubt, don't invent dialogue from yue alone.
4. If chi has nuance eng lacks → **REWRITE** to capture it.
5. If yue HIGH diverges from chi: pass through the intelligibility gate, then apply Rule A (synonyms, yue more vivid → rewrite to yue) or Rule B (different words → chi wins unless eng / prior-FULL-episode / visible chi OCR corroborates yue). See `STYLE.md` §2.
6. If yue's register is sharper/warmer/more colloquial than the draft → **REWRITE** to match yue's register (Rule A on a register-only difference).
7. If chi or yue has an address term Step 3 didn't catch → ensure it's **CJK in hybrid**.
8. If chi or yue has an idiom Step 3 didn't catch → ensure it's **in the hybrid sub**.
9. **Common-noun CJK sweep** — before finalising, check none of the following have been left as CJK in hybrid (see `STYLE.md` §7 "What does NOT get CJK" for the full list): generic wuxia vocabulary (武功/武林/江湖/內力/內功/輕功/功力), colloquial insult compounds (臭丫頭/死丫頭/死乞兒/臭乞兒/王八蛋/禁宮), Mandarin 叫化子 (use Cantonese 乞兒 or English "beggar"), descriptive common-noun metaphors (情蛇, 一流高手, X+高人/高手/蛇). Named techniques (九陰真經, 降龍十八掌, etc.) remain CJK. `lint_overrides.py`'s common-noun heuristic catches many automatically, but reviewer judgment is the final arbiter.
10. If none apply → **leave the sub alone**; the draft is faithful.
11. Collect corrections into `ep{N}_overrides.tsv` (format below) and apply with `apply_overrides.py`.

**Triage.** Subs with `auto_keep: true` in `ep{N}_confidence.json` should still be read, but quickly — the heuristic already checked fabrication risk, idiom injection, address-term drops, and length divergence. Concentrate examination time on `auto_keep: false`, where fabrications, meaning flattening, yue-authority overrides, register drift, and idiom injection cluster.

**Writing overrides.** Collect into `/home/claude/ep{N}_overrides.tsv`, one per line, tab-separated:

```
<index>\t<English text with \\n for embedded newlines>
```

Example:
```
22\tA useless man of sorts — 廢人 — cannot compare to 岳 將軍's spirit
47\t- 黃姑娘 will stay next door
296\t蓉兒\nNo need to say it — 梅超風 must be coming
```

Lines starting with `#` are comments. Apply the file with:

```bash
python3 apply_overrides.py <N>
```

This merges the TSV into `ep{N}_h_all.json`, replacing entries by index. Subs not listed keep whatever Step 3 wrote. **Don't revert to emitting overrides as a Python literal dict inside a patch script** — the pre-v10 pattern cost ~1.3× the context due to dict/quoting overhead.

Examining every sub is what makes FULL quality — not rewriting every sub. A faithful draft left untouched is a correct outcome.

**Exception — preserve Step 3 output when chi and yue are both empty/bare name.** For subs where chi is empty or just a bare name (opening-credits name cards, etc.) and yue offers no additional content, **keep the Step 3 output rather than rewriting.** Manually projecting a speaker from sparse sources caused a name-swap bug in prior sessions. If neither chi nor yue has content beyond a name, don't guess the speaker.

### Step 5 — Add Episode Extras

For any CJK that appears in the hybrid overrides but isn't already in `PersonalNamesUpdated.csv` or the shared baseline (`extras_baseline.json`), add entries to `ep{N}_extras_add.json` — the episode-specific **overlay**:

```json
{
  "jy": {
    "陸乘風": "Luk Sing-fung",
    "裘老前輩": "Elder Kau"
  },
  "yl": {
    "陸乘風": "Luhk Sihng-fung",
    "裘老前輩": "Elder Kauh"
  }
}
```

Then re-run `shared_extras.py <N>` to merge the overlay into `ep{N}_extra.json`.

**How to find what's missing.** After writing overrides in Step 4, scan `ep{N}_h_all.json` for CJK tokens not covered by the baseline. A quick Python one-liner works:

```python
import json, re
from collections import Counter
with open('/home/claude/ep{N}_h_all.json') as f: h = json.load(f)
runs = re.findall(r'[\u4e00-\u9fff]+', ' '.join(h.values()))
for tok, n in sorted(Counter(runs).items(), key=lambda x: -x[1])[:80]:
    print(f'{n:3d} {tok}')
```

Cross-reference against `extras_baseline.json` and `PersonalNamesUpdated.csv`; anything unmatched goes into the overlay.

**Promotion path.** If an overlay term proves stable across 2+ episodes (same CJK always rendered the same way), promote it into `extras_baseline.json` and drop it from the episode overlays. This is what the `extras_baseline.json` + overlay split exists to support.

### Step 5.5 — Pre-build Lint

```bash
python3 lint_overrides.py <N>
```

Runs two diagnostic checks on `ep{N}_h_all.json` and `ep{N}_extras_add.json`:

**Check 1 — concat-trap patterns.** Scans the hybrid for known CJK-leak concat patterns catalogued in `STYLE.md` §19 and the `SESSION-NOTES.md` Watch List. Catalogued patterns include `裘老前輩` / `裘前輩` (surname+title), `X大哥` (surname+Brother), `我爹` / `你爹` (possessive+kinship), `大金國` / `大宋` (dynasty prefix), `我<FullName>` (emphatic self-reference), `大師父`. Running this before `build.py` lets the reviewer register missing compounds in the overlay once rather than iterating after build.

**Check 2 — common-noun-rendering heuristic.** Scans overlay entries (`ep{N}_extras_add.json`) and flags any whose English rendering looks like a common noun (lowercase-starting, or article-plus-lowercase, or Capital-plus-lowercase-words). Enforces STYLE.md §7's exhaustive-lists rule: hybrid CJK is for names/titles/places/idioms/terms-of-art, not common nouns. Catches the Ep20-style "如意燈 kept as CJK when it should have been 'lucky lanterns' in English" failure.

Three action buckets: **(a)** genuine idiom/term-of-art → promote to STYLE.md §10; **(b)** common noun kept in CJK by mistake → drop from overlay, rewrite affected hybrid subs in English; **(c)** character voice / flavour phrase (臭要飯的) → judgment call; promote to STYLE.md only if recurring.

Both checks are non-fatal — the reviewer inspects each warning and decides. The lint exits 1 if either surfaces issues, 0 only if both are clean.

### Step 6 — Build 3 Variants

```bash
python3 build.py <N>
```

### Step 7 — CJK Fix Pass

```bash
python3 cjk_fix_v2.py <N>
```

Then apply targeted `sed` fixes for any remaining CJK in romanised files — see **Recurring CJK Fix Patterns** in `STYLE.md`.

### Step 8 — Banned-Term Sweep & Validate

- Grep romanised files for all **banned terms** (see `STYLE.md` §18).
- Grep hybrid file for **Pinyin leakage** (Guo Jing, Huang Rong, Rong-er, etc.).
- Grep hybrid file for **common-noun CJK** that should be English (`STYLE.md` §18): 武功 · 武林 · 江湖 · 內力 · 內功 · 輕功 · 功力 · 叫化子 · 臭丫頭 · 死丫頭 · 死乞兒 · 臭乞兒 · 王八蛋 · 禁宮. Any as CJK in hybrid is a build-time error — fix the hybrid sub and rebuild.
- Validate: zero CJK in romanised files; zero banned terms; zero overlapping timestamps; same subtitle count and indices as source `{N}-chi_tra.csv` (chi is the entry spine; see `STYLE.md` §16).
- `present_files` with all three SRTs.

### Step 8.5 — Update and Present SESSION-NOTES.md

After the three SRTs are presented, update `SESSION-NOTES.md` and present it so the user can drop it into the next session's handoff bundle. Without this step, session findings are lost between chats.

What to update, in order:

1. **Move the episode's status entry.** If the episode completed FULL under the current bundle version, move its row out of "Pending — Needs FULL Processing" into the "Completed (FULL)" table, **inserted at the position sorted by episode number ascending** (Ep4 goes between Ep3 and Ep5; the Bundle column is not the ordering key). Row schema: `| Episode | Bundle | Subs | Notes |`. If the outcome was PARTIAL or MECHANICAL-ONLY, leave the row in Pending and annotate honestly — don't promote a degraded delivery.

   **Row body format and size budget are specified in `SESSION-NOTES.md`'s own header** — read it before writing the row. Target ≤500 chars, hard cap ≤800 chars. Five elements in order: arc label (≤15 words), `First FULL firing for:` (flat comma-separated list), cross-episode precedents (omit if none), chi-OCR variants (omit if none), promotion flags (omit if none). Narrative plot detail does not belong in SESSION-NOTES — the SRTs carry the plot.

2. **Add new Watch List entries.** Anything without a settled rendering goes under a descriptive heading. Skip things already in `STYLE.md` §5 / §6 / §10 or `REFERENCE.md`. Recurring CJK leaks, name-variant OCR drift, cross-stage concat traps, and classical allusions are typical additions. If a concat-trap fix needed a post-build `sed` pass (rather than overlay registration), log the mechanism — that's what the "Cross-stage concat traps" section exists for.

3. **Promote stable items out of the Watch List.** Any entry that has fired in two-or-more episodes without contradicting renderings moves into the appropriate consolidated doc (name → `STYLE.md` §5; title → §6; idiom → §10; judgment call → `REFERENCE.md`; concat-trap → `cjk_fix_v2.py` or `extras_baseline.json`) and is deleted from `SESSION-NOTES.md`.

4. **Call `present_files` on the updated `SESSION-NOTES.md`.** Without a present_files call, the edit sits in `/home/claude/` where the user can't retrieve it.

What NOT to do:

- **Don't exceed the 800-char hard cap on row bodies.** Cut per-sub citations and who-said-what parentheticals first.
- Don't restate SESSION-NOTES edits in chat. One sentence is enough; often none is fine — the file speaks for itself.
- Don't add content-free edits (phrasing tweaks, reformatting). SESSION-NOTES is append-mostly with targeted promotions.
- Don't promote something after only one episode's evidence. The two-episode threshold exists because single-episode patterns often don't generalise.

### Step 9 — Report Ending Context

After `present_files` completes, report the ending context estimate in the same format as Step 0, plus the delta.

Report format:

```
Context ending — Episode N
• Baseline (Step 0): ~ZZ%
• Ending estimate: ~WW%
• Delta consumed by this episode: ~ΔΔ%
• Episode size processed: XXX subs
```

The delta is informational. Each session starts from the conservative defaults in Step 0.

---

## What "Examine Against Sources" Looks Like — Concrete Examples

See `REFERENCE.md` §8 **Error Taxonomy** for worked examples across all error categories: FABRICATION (Category 1, with the Ep28 Sub 22 yue-as-witness case study), CHI_MEANING_LOST (Category 2, with six examples showing meaning-flattening, address-term drops, and characterisation drops), YUE_AUTHORITY_REGISTER (Category 2b, with 古惑 / 淒涼 / 死乞兒 Rule A examples), NAME/TITLE LEAK (Category 3), and IDIOM MISSING (Category 4).

---

## Handoff Files Checklist

Upload ALL of these to start a new session — **15 bundle files + 3 per-episode inputs**:

### Config & reference (4 docs)
1. `PIPELINE.md` — this file
2. `STYLE.md` — style decisions (variants, names, titles, idioms, yue register, formatting, anti-patterns)
3. `REFERENCE.md` — context-dependent judgment calls, error taxonomy, Five Greats framework
4. `SESSION-NOTES.md` — episode completion status, pending-episode previews, watch list

### Version file (1)
5. `VERSION` — single line containing the handoff bundle version (e.g. `17`). `build.py` and `cjk_fix_v2.py` read this at runtime and stamp it into output SRT filenames (`{EP}-eng-{variant}-v{VERSION}.srt`). A bundle with missing or malformed VERSION fails loudly rather than shipping unstamped SRTs.

### Data files (2)
6. `PersonalNamesUpdated.csv` — name lookup (copy to `/home/claude/` first)
7. `extras_baseline.json` — shared romanisation baseline beyond personal names (titles, places, sects, idioms, kinship). Loaded by `shared_extras.py`; merged with any `ep{N}_extras_add.json` overlay to produce `ep{N}_extra.json`.

### Pipeline scripts (7)
8. `pipeline.py` — CSV/JSON parser and chi-spine alignment (importable module with `run()` and `main()`).
9. `auto_override_v2.py` — deep override with CJK injection, idiom handling, confidence-tier annotation, AUTO-KEEP flagging, and dump emission.
10. `shared_extras.py` — thin merger: baseline + optional `ep{N}_extras_add.json` overlay → `ep{N}_extra.json`.
11. `apply_overrides.py` — applies Step 4 reviewer overrides from `ep{N}_overrides.tsv` into `ep{N}_h_all.json`.
12. `lint_overrides.py` — pre-build lint for known CJK-leak concat patterns and common-noun renderings.
13. `build.py` — builder with all conversion tables. Expects `PersonalNamesUpdated.csv` at `/home/claude/PersonalNamesUpdated.csv`. Reads `VERSION` adjacent to itself.
14. `cjk_fix_v2.py` — comprehensive CJK cleanup for romanised files. Reads `VERSION` to locate the SRTs `build.py` wrote.

### Tests (1)
15. `test_pipeline.py` — unittest suite covering synthetic reflow cases and a 17-row Ep24 real-data slice. Run with `python3 -m unittest test_pipeline.py -v`. Not required for sub generation, but verifies `pipeline.py` still works correctly after any edits.

### Per-episode inputs (3)
16. `{N}-eng.csv`, `{N}-chi_tra.csv`, `{N}-yue.json`

---

## Quick-Start for New Chat

1. Upload the 15 bundle files + 3 per-episode sources above.
2. Say: *"Process episode N with full source-authority rewriting (FULL standard)"* — i.e. examine every sub against chi and yue per the priority chain in `STYLE.md` §2.
3. The assistant runs Steps 0 through 9 as specified in [The Pipeline](#the-pipeline) above. Step 0 context baseline is reported before any tool call; Steps 1–8 run silently between reports; Step 8.5 updates and presents `SESSION-NOTES.md`; Step 9 reports ending context.

**Hard rules:**
- **ONE EPISODE PER REQUEST for FULL quality.** If multiple episodes are uploaded, pick one and state the choice.
- **Follow [Narration Discipline](#narration-discipline).** Run tools silently between the Step 0 and Step 9 reports; surface only actual issues (one line each) and the final `present_files`. No mid-turn progress recaps, interpretive commentary on tool output, or end-of-episode "candidates to promote" summaries — those edits go in `SESSION-NOTES.md`.
- **Expect 3+ turns.** A FULL pass to completion often takes 3+ turns.
