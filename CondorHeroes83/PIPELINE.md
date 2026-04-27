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

- **FULL** (target) — Step 4 examination loop completed for every sub **and evidenced in `ep{N}_step4_log.txt`** (see Step 4 below). Overrides written where content or register mismatches; OCR corrections via yue-as-witness; yue-authority overrides applied with quoted yue phrase in the log; idiom injection with §10 gate criterion named; characterisation preserved.
- **PARTIAL** (failure mode) — Step 4 examined roughly 20–60% of subs before aborting (context ran out, or output-length limit on a large override pass). Names/titles/idioms mechanically correct throughout; unexamined subs retain whatever Step 3 produced. Acknowledge honestly in delivery; flag which sub-range was examined (the log makes this concrete — "log covers subs 1–220").
- **MECHANICAL-ONLY** (failure mode) — Step 4 barely started (<20%) or didn't run. Mechanical CJK substitutions and idiom injections are good, meaning and register not systematically checked. Acknowledge honestly.

### The forcing-function rule — writing is not examination

Step 4 has historically collapsed into Step 3 + fast rewriting: the assistant reads the dump quickly, writes a TSV of overrides, and calls it done. This satisfies the letter of "examine every sub" while skipping the per-sub yue/chi/eng comparison that Rules A/B/C demand. The pattern has recurred across sessions.

**The rule: no override is written until `ep{N}_step4_log.txt` for that sub's batch exists.** The log is the artifact that evidences examination. A sparse TSV with no log is indistinguishable from a fast-written TSV; a log with one line per HIGH-yue sub is visible work. Writing fluent overrides from plot knowledge rather than source comparison is the failure mode — the log is what makes that failure mode visible.

If context is tight enough that the log can't be written honestly, say so in Step 0 and deliver PARTIAL with the log as evidence of what was actually examined. **Do not skip the log to save tokens** — a PARTIAL with a log beats a nominal-FULL without one.

---

## Narration Discipline

Conversational summaries between tool calls consume ~15–25% of session budget and repeat tool output. Keep conversational output minimal.

### Required output (keep)
- **Step 0 context baseline report** before any tool call.
- **Step 4 log batches and pressure-test answers** as Step 4 proceeds. The log batches are tool calls, not chat narration — don't narrate each batch; the log file is the artifact. The three pressure-test answers at the end of Step 4 are chat text, concrete and concise (one to two lines per answer).
- **Step 8.5 SESSION-NOTES update and present** after the three SRTs.
- **Step 9 ending context report** after the SESSION-NOTES `present_files`.
- **User-directed questions** for genuine ambiguity (rare in FULL pass).
- **Final `present_files`** with the three SRTs.

### Cut (don't produce)
- Mid-turn progress-report blocks between script runs — tool output already says "applied 420 overrides" / "✓ jyutping: clean".
- "Let me now run X" narration before tool calls. Just run the tool.
- End-of-turn recaps of what each step produced — files are visible to the user.
- Speculative interpretive commentary on tool output. If finding is actionable, act silently; if not, don't mention.
- "Candidates to promote" / "Watch List additions" lists at end of episode — those belong in `SESSION-NOTES.md` written by Step 8.5.

### Exception — real issues
If something actually went wrong (Step couldn't complete, source file malformed, validation failure needing non-trivial workaround) — short issues list at end, one line per issue, plain phrasing.

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
- `r` — **reflow risk**. Chi thin (empty, ≤3 CJK chars) AND eng substantive AND adjacent sub has empty eng or chi — signature of chi-spine alignment pulling eng content from a neighbouring beat. **Do not call the eng fabrication without reading adjacent subs first.** Canonical case: Ep1 sub 18 (chi `上`, eng "What do you want?" — victim's retort reflowed from previous beat).
- `y` — **yue-solo**. Chi AND eng both thin but yue substantive at HIGH. Either real dialogue lost from chi+eng OR Whisper ASR hallucination (music/silence/noise). Apply Rule C intelligibility gate + scene-context plausibility. **When in doubt, do not invent dialogue from yue alone.** Mutually exclusive with `r` (which takes priority). HIGH-only by design — MEDIUM yue gets caught by normal Rule A examination in Step 4.

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

**Preprocessing pass, not translation** — operates on text's mechanical form to get substitutions right so Step 4 can focus on content and register. Substitutes Pinyin → CJK, English titles/places → CJK when chi has CJK (White Camel Mountain → 白駝山, "teacher" → 師父), injects address terms and 四字成語 from chi where eng dropped them, fixes common OCR artifacts. Output saved to `ep{N}_h_all.json` — original English with mechanical substitutions only. Meaning/nuance/register is Step 4's job.

**Baseline + overlay split.** `shared_extras.py` reads `extras_baseline.json` (bundled) + optional `ep{N}_extras_add.json` overlay (reviewer writes in Step 5), merges → `ep{N}_extra.json` for `build.py`. Overlay keys override baseline on collision.

**AUTO-KEEP heuristic.** `auto_override_v2.py` annotates each sub in `ep{N}_confidence.json` with `auto_keep: true/false`. True means the sub passed all seven conservative gates (all tracks non-empty, yue HIGH/MEDIUM, no fabrication-risk markers, no idioms in chi, no missing address terms, ≤1.5× length ratio, ≥0.7 content-word overlap). A **priority signal, not a gate** — Step 4 still reads every sub; concentrate time on NEEDS REVIEW. Deliberately false-negative-biased (false positive silently degrades quality; false negative just costs a quick-confirm).

### Step 4 — Examine Every Sub; Log First, Override Second

Step 4 has two outputs, produced in this order: (1) `ep{N}_step4_log.txt`, written in batches of ~50 subs as you work through the dump; (2) `ep{N}_overrides.tsv`, derived from the log. **The log is mandatory and is written before the TSV.** Writing the TSV first and back-filling the log defeats the purpose — the log exists to make examination visible, which only works if it records what you actually thought while examining.

Read `ep{N}_h_all.json` (populated with Step 3's CJK substitutions) alongside the chi track, the yue track, and `ep{N}_confidence.json`. Examine EVERY sub against the priority chain (**yue HIGH > chi > eng**) per `STYLE.md` §2.

#### The Step 4 log format

One line per sub. Every sub gets a line — not just the ones that will become overrides. The shape:

```
<idx> <conf> <flag> <decision> <reason>
```

- `<idx>` — sub number
- `<conf>` — HIGH / MEDIUM / LOW / N/A (from `ep{N}_confidence.json`)
- `<flag>` — the Step 2 dump flag column (`•!i@ory` or blank)
- `<decision>` — one of:
  - `KEEP` — Step 3 output is faithful, no override
  - `YUE-A` — Rule A fired (yue more vivid/colloquial synonym)
  - `YUE-B` — Rule B override (chi-OCR visible, eng corroborates yue, or prior FULL-ep precedent — must be one of these)
  - `CHI` — chi wins over yue (Rule B default, semantic disagreement with no independent corroboration)
  - `REFLOW` — `r`-flag case, content preserved from adjacent sub per §13 em-dash split
  - `IDIOM` — idiom injection from chi that Step 3 missed; name §10 criterion (1/2/3/4) or mark `plain-prose → English`
  - `ADDR` — address term (師父/前輩/老伯/etc) Step 3 dropped
  - `FAB` — eng fabrication removed, neither chi nor yue supports
  - `OCR` — chi-OCR canonicalisation (e.g. `老示童 → 老頑童`)
  - `FILL` — empty Step 3 output populated from chi
- `<reason>` — one short phrase. For YUE-A: **quote the yue phrase** that triggered the override (e.g. `yue 大蝦勢 vivid over chi 以大欺小`). For YUE-B: name the corroboration (eng/cross-ep/OCR). For IDIOM: name the §10 criterion or write `plain-prose → English`. For KEEP, a terse note is fine (`Step 3 faithful`, `bare name, no content to examine`).

AUTO-KEEP subs (`•` flag + `auto_keep: true` in confidence.json) can take the shortest form: `<idx> HIGH • KEEP auto-keep faithful`. The seven-gate heuristic has already done real checking; sanity check against yue and chibut to not spend too muhc time. NEEDS-REVIEW subs must state the Rule A/B/C call explicitly.

**Batch discipline.** Write the log in batches of ~50 subs, appending as you go. Do not write all 400 lines in one `create_file` call at the end — that lets the log be back-filled from the TSV, defeating the forcing function. The correct pattern is: read dump lines 1–200 → write log entries 1–50 → read 200–400 → write log entries 51–100 → and so on. Each batch is a real examination pass on a bounded range.

#### Worked log examples

```
1 HIGH    KEEP    Step 3 faithful
10 HIGH    OCR    chi 鞭兒 → 蓉兒 (OCR batch, REFERENCE §1)
15 HIGH    IDIOM  想逝者 lament (§10 crit 4; chi 誰訴 variant, not Ep28 最苦)
39 HIGH i  IDIOM  女大不中留 §10 crit 3 (Ep30+31 2-ep promotion)
169 MEDIUM YUE-A  yue 大蝦勢 Cantonese "bullying-posture" — chi 以大欺小 flat
182 MEDIUM  §7  武功 → "skill" (STYLE §18 ban)
280 HIGH •  KEEP   "be calm" — yue 稍安勿躁 plain-prose fail §10 gate
324 HIGH    IDIOM  雞鳴狗盜 §10 crit 2 (史記 allusion, Lord Mengchang)
374 MEDIUM  KEEP   藥哥 intimate-address; needs overlay (not §7 ban — kinship)
```

#### The per-sub checklist

For each sub, walk this checklist once; the log entry records the outcome:

1. Read chi for meaning, yue for register and (if HIGH) potential Rule A override. Compare against Step 3's output.
2. If eng says something neither chi nor yue supports → **FAB** (delete). **But check reflow first** (the `r` flag in the Step 2 dump fires on this signature; see its explanation there). If chi is thin AND an adjacent sub has empty eng or chi, the eng content is probably reflow casualty → **REFLOW**. If chi is substantive but eng still disagrees and yue confirms eng, **YUE-B** (OCR-in-chi case).
3. For `y`-flagged yue-solo subs, apply Rule C intelligibility gate + scene-context plausibility. When in doubt, don't invent dialogue from yue alone → **KEEP** with reason `yue-solo, garbled/implausible`.
4. If chi has nuance eng lacks → rewrite (log as `CHI` with one-word reason; the override will capture the nuance).
5. If yue HIGH diverges from chi: Rule C intelligibility first. Then Rule A (synonyms, yue more vivid → **YUE-A**, quote yue) or Rule B (different words → **CHI** by default unless corroboration → **YUE-B**).
6. If yue's register is sharper/warmer/more colloquial than the draft → **YUE-A** (register-only Rule A; quote yue).
7. If chi or yue has an address term Step 3 didn't catch → **ADDR**.
8. If chi or yue has an idiom Step 3 didn't catch → **IDIOM**; apply §10 admission gate in the log entry ("§10 crit N" or "plain-prose → English").
9. **Common-noun CJK sweep** — STYLE §7's "What does NOT get CJK" list (generic wuxia vocab, colloquial-insult compounds, Mandarin 叫化子, descriptive common-noun metaphors). Flag as `§7` in the log; render English. `lint_overrides.py`'s Check 2 catches many at Step 5.5; reviewer judgment is the final arbiter.
10. If none apply → **KEEP**; the draft is faithful.

#### The gate before writing the TSV

Before opening `ep{N}_overrides.tsv`, confirm these in-text:

- Every sub has a log entry (check: line count of `ep{N}_step4_log.txt` equals sub count).
- For every HIGH-yue sub that got YUE-A, the log quotes the yue phrase.
- For every IDIOM entry, the §10 gate decision is recorded (criterion number, or plain-prose fail).
- Count of each decision type. Typical healthy distribution for a FULL pass: 20–40% KEEP, 30–50% chi-content rewrites, 5–15% YUE-A, 1–5% IDIOM+ADDR+FAB+OCR+§7. A run with 0 KEEP or 0 YUE-A on a 200+ HIGH-yue episode is a red flag — you're likely not examining carefully.

Now write the TSV. Every TSV line derives from a log line with a non-KEEP decision. A TSV entry with no corresponding log decision is not allowed.

#### Writing overrides

Collect into `/home/claude/ep{N}_overrides.tsv`, one per line, tab-separated:

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

Examining every sub is what makes FULL quality — not rewriting every sub. A faithful draft left untouched is a correct outcome, and the log records it as **KEEP** with equal legitimacy to an override. The failure modes are: (a) rewrite-heavy sessions that over-edit faithful drafts, and (b) skim-sessions that nominally examine but don't produce the log evidence. The log addresses both — it forces examination to be real, and it records KEEP as real work.

**Exception — preserve Step 3 output when chi and yue are both empty/bare name.** For subs where chi is empty or just a bare name (opening-credits name cards, etc.) and yue offers no additional content, **keep the Step 3 output rather than rewriting.** Manually projecting a speaker from sparse sources caused a name-swap bug in prior sessions. Log as `KEEP bare name, no content`.

#### Pressure-test: the three questions

Before proceeding to Step 5, answer these in-text. If you can't answer concretely, Step 4 isn't done; go back to the log.

1. Cite three subs where Rule A fired (YUE-A in the log) — give the yue phrase, the chi phrase, and one-phrase reason yue was more vivid.
2. Cite three subs where you kept Step 3 verbatim (KEEP) — one sentence on why the draft was faithful.
3. For each CJK-kept idiom in the overrides, name the §10 admission-gate criterion (1/2/3/4) it passes. Any idiom for which you can't name a criterion should not be CJK — rewrite the hybrid entry to English.

Writing "done" to these three without specifics is the bluff the log-first discipline is designed to catch. If you find yourself hand-waving on them, the log wasn't written honestly — fix the log, then re-answer.

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

**Check 1 — concat-trap patterns.** Scans the hybrid for known CJK-leak concat patterns (surname+title, possessive+kinship, dynasty-prefix, emphatic-self-reference, etc — active catalogue in `lint_overrides.py RULES`). Running this before `build.py` lets the reviewer register missing compounds in the overlay once rather than iterating after build.

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

### Per-episode work artifacts (produced during processing, not uploaded)
- `ep{N}_step4_log.txt` — required for FULL. Evidences per-sub examination. Stays in `/home/claude/` during the session; not part of the handoff bundle. If a session ends mid-episode (PARTIAL), the log documents which sub-range was actually examined.

---

## Quick-Start for New Chat

1. Upload the handoff bundle — **4 reference docs + 1 VERSION file + 2 data files + 7 scripts + 1 test file = 15 files** (see [Handoff Files Checklist](#handoff-files-checklist) above) — plus the episode sources `{N}-eng.csv`, `{N}-chi_tra.csv`, `{N}-yue.json`.
2. Say: *"Process episode N with full source-authority rewriting (FULL standard)"* — i.e. examine every sub against chi and yue per the priority chain in `STYLE.md` §2.
3. The assistant MUST:
   - **Report Step 0 context baseline** before doing anything else
   - Copy `PersonalNamesUpdated.csv` to `/home/claude/`
   - Place/create all 7 scripts and `extras_baseline.json`
   - Run `pipeline.py` → `ep{N}_aligned.json` (structural alignment only; dump comes from Step 3)
   - Run `shared_extras.py` → `ep{N}_extra.json` (baseline only, initially)
   - Run `auto_override_v2.py` → `ep{N}_h_all.json` + `ep{N}_confidence.json` + `ep{N}_dump.txt` (with per-sub flags)
   - `view` the dump file in ranges; examine every sub; concentrate effort on subs whose flags column is non-blank
   - Collect corrections into `ep{N}_overrides.tsv`; run `apply_overrides.py <N>`
   - Write `ep{N}_extras_add.json` if new CJK terms introduced; re-run `shared_extras.py <N>` to merge
   - Run `lint_overrides.py <N>` — fix any concat-trap warnings by updating the overlay
   - Build, CJK-fix, validate (zero CJK in romanised, zero banned terms)
   - Present output files
   - **Update and present `SESSION-NOTES.md`** — move episode's row into Completed table (keep rows sorted by episode number ascending — see SESSION-NOTES.md sort rule; row body ≤500 chars target, ≤800 hard cap), add new Watch List items, promote stable items out (see Step 8.5)
   - **Report Step 9 ending context** (informational)
4. **ONE EPISODE PER REQUEST for FULL quality.** If there are multiple episodes uploaded, only process one then.
5. **Follow Narration Discipline.** Run tools silently between the Step 0 and Step 9 reports; surface only actual issues (one line each) and the final `present_files`. Do not produce mid-turn progress recaps, interpretive commentary on tool output, or end-of-episode "candidates to promote" / "watch list" summaries — edits to `SESSION-NOTES.md` are where such findings go.
6. **Expect each episode to require 3+ turns.** A FULL pass to completion often takes 3+ turns.
