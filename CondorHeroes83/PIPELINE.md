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

**One episode per request. FULL quality requires a fresh chat and the full dump read.** Batching is not a supported mode.

Before beginning work on any episode, the assistant MUST assess feasibility:
- Use the Step 0 context estimate together with the conservative sub-count defaults below to judge whether there's enough remaining budget to run Step 4 to completion.
- If the budget likely won't cover full Step 4 examination for this episode's sub count, **STOP and ask the user for instructions** rather than silently producing a PARTIAL or MECHANICAL-ONLY outcome.
- Say explicitly: "My context estimate is ~ZZ%, and Episode N has XXX subs. Step 4 would likely abort partway and produce PARTIAL rather than FULL quality. I recommend starting a fresh chat. Shall I proceed anyway, or would you prefer a new session?"
- If multiple episodes are requested in a single message, stop and ask the user to confirm which single episode to process first.

**Thresholds are not fixed.** A session at ~70% baseline that has processed smaller episodes can often still handle another small one; a session at ~40% starting fresh with a 600-sub episode might still be tight. Judge from the delta data, not a hard percentage.

### Quality Outcomes (Diagnostic)

FULL is the only acceptable quality target. PARTIAL and MECHANICAL-ONLY are named failure modes — they exist so a degraded delivery can be honestly labelled, not so they can be aimed for. Always aim for FULL; if PARTIAL or MECHANICAL-ONLY is the realistic outcome, stop and ask rather than proceeding silently.

| Outcome | Description | When it happens |
|---------|-------------|-----------------|
| **FULL** (target) | Every sub examined against chi and yue; overrides written where content or register mismatches; OCR corrections via yue-as-witness, yue-authority overrides applied, idiom injection, characterisation preserved. | Step 4 examination loop completed for every sub. |
| **PARTIAL** (failure mode) | Step 3 preprocessing applied to all subs; Step 4 examination completed for roughly 20–60% of subs before aborting. Names/titles/idioms mechanically correct throughout; the unexamined subs retain whatever Step 3 produced, unchecked against chi and yue for meaning/register. | Step 4 had to abort partway — typically because context ran out mid-examination, or the assistant hit an output-length limit on a large override pass. Acknowledge the outcome honestly in delivery; flag which sub-range was examined and which wasn't. |
| **MECHANICAL-ONLY** (failure mode) | Step 3 preprocessing applied to all subs; Step 4 examination barely started (<20% of subs examined) or didn't run at all. Mechanical CJK substitutions and idiom injections are good, but meaning and register are not systematically checked. | Step 4 aborted very early, or the session delivered output after only running Steps 1–3. Acknowledge the outcome honestly in delivery. |

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
• Assessment: feasible / borderline / should stop-and-ask
```

**How to make the call:** use conservative sub-count estimates — a 400-sub episode consumes roughly ~35% of context during Step 4; a 600-sub episode roughly ~50%. Stop-and-ask if `baseline + expected delta` would exceed ~90%. These estimates are deliberately conservative; actual usage varies with episode density, but it's safer to over-warn than to abort Step 4 partway through.

### Step 1 — Parse & Align

```bash
cp /mnt/user-data/uploads/PersonalNamesUpdated.csv /home/claude/
python3 pipeline.py <N>
```

Parses the three source tracks and aligns them onto a **chi-spine skeleton**: the output's entry count and timestamps are taken from chi, not eng. Outputs `ep{N}_aligned.json` plus a full dump to stdout.

**Chi as entry spine (pipeline.py v6):**
- Output entry count = chi entry count (not eng). See `STYLE.md` §16.
- For each chi entry, overlapping eng entries by timestamp window are reflowed onto the chi entry as the "draft content" field:
  - **Chi window spans multiple eng entries** → merge their content (joined with newlines, in eng-index order).
  - **One eng entry spans multiple chi entries** → split the eng text proportionally across the chi entries it covers. The split tries sentence boundaries first, then newlines, then character-proportion with space-snapping.
  - **Chi entry has no overlapping eng content** → look for a "dropped" eng entry (one that had no chi overlap) within 2000 ms and pull its text in. Otherwise leave eng empty; Step 3 and Step 4 will populate from chi.
- Yue words align to chi entries directly (chi timings are cleaner than eng).
- **Diagnostics printed at the end of alignment:** output-count vs chi-count, dropped-eng count (eng content that had no chi window and didn't get rescued), orphan-chi count (chi entries that ended up with empty eng).

**Why chi-spine:** eng and chi arrive with independently authored timings. Timestamp-overlap alignment using eng as the implicit skeleton produced "double-subs" — adjacent output entries with near-duplicate content when eng and chi both translated the same spoken line at offset times. Chi-spine makes structural duplication impossible: each spoken line has exactly one entry (chi's).

**Whisper JSON handling (pipeline.py v6):**
- Reads yue from `{N}-yue.json` (Whisper output) only — no CSV fallback.
- Aligns yue words to **chi_tra subs** (consistent with chi-spine principle).
- Discards raw JSON from memory after extraction; keeps compact per-sub yue alignment only.

**Confidence tiers from `avg_logprob` (auto_override_v2.py v2.1):**
- **HIGH** (≥ −0.3) — yue is *candidate* authoritative over chi; flagged for manual review, where the reviewer applies the intelligibility gate (see `STYLE.md` §2) to decide whether yue actually overrides.
- **MEDIUM** (≥ −0.8) — chi remains authority; yue consulted for tone/register/nuance.
- **LOW** (< −0.8) — yue text discarded entirely; prefixed with `[DISCARDED]` in dump.

Each sub in the dump is annotated `[HIGH]` / `[MEDIUM]` / `[LOW]`, and `[T-ADJ]` marks subs whose start/end times were tightened to word boundaries (Whisper `score ≥ 0.7`). A confidence summary section shows distribution and lists HIGH-authority and LOW-discarded subs. Per-sub confidence notes are written to `ep{N}_confidence.json` for the manual review pass.

### Step 2 — Read the Full Dump (MANDATORY)

Read EVERY line of the dump. For each sub, compare the three columns:
- Column 2 (eng) — the rough draft
- Column 3 (chi) — the semantic authority
- Column 4 (yue) — the actual spoken dialogue; at HIGH Whisper confidence, overrides chi on wording/register per the Yue-Authority Rule (`STYLE.md` §2)

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

### Step 4 — Examine Every Sub; Override When Warranted

Read `ep{N}_h_all.json` (now populated with Step 3's CJK substitutions) alongside the chi track, the yue track, and the `ep{N}_confidence.json` tier annotations from Step 3. Examine EVERY sub against the priority chain: **yue (HIGH) > chi (semantic authority) > eng (draft)**. If the text — with its mechanical substitutions applied — already matches the source content and register faithfully, default to it. Override only when content or register mismatches.

For a fuller treatment of the priority chain and the Yue-Authority Rule, see `STYLE.md` §2. The short version as it applies here:

- **Yue HIGH, semantically agrees with chi** — yue is the actual spoken dialogue at HIGH confidence. Apply the **intelligibility gate**: if yue is coherent on its own terms (parses as something a character would say), yue wins on register/wording nuance (Rule A); if yue is garbled — broken syntax or semantically incoherent — treat as ASR noise and fall back to chi. Confidence tier doesn't settle this; Whisper can be HIGH-confident on nonsense. Examples of legitimate yue-override (Rule A): 古惑 over 鬼主意; 淒涼 over 可憐. These are all cases where chi and yue are *synonyms differing in register*.
- **Yue HIGH, semantically disagrees with chi (different word, not a register variant)** — chi wins by default (Rule B). Yue reaches Claude via ASR and is subject to homophone errors (功/宮 both `gung1`; 保/寶 both `bou2`). Chi, being a written translation, doesn't have homophone errors. Override chi only when there's independent corroboration for yue: eng confirms yue (Ep28 Sub 22), or a **prior FULL-completed episode** has established the form yue matches, or chi has a visible OCR artefact. The cross-episode clause is strict — the prior episode must actually have been completed and rendered the form a specific way; it's not a license to substitute what the reviewer expects ought to be canonical. Named wuxia techniques and 四字成語 are especially prone to this failure mode — a yue variant of a fixed compound is almost always a homophone of the real term, not a new term.
- **Yue MEDIUM** — chi drives meaning; yue is consulted for tone, register, and emotional nuance.
- **Yue LOW** — yue discarded; chi-only processing.
- **Yue reveals OCR errors in chi** — fix the error; yue is the witness (but only when yue is genuinely the witness, per the rules above).

For every sub, walk this checklist:

1. Read the chi text as semantic authority.
2. Read yue for register, tone, and (if HIGH confidence) as a potential override of chi wording.
3. Compare against the Step 3 output.
4. If eng says something neither chi nor yue supports → **DELETE** the fabrication. (But if yue confirms what eng says and chi diverges, treat it as an OCR error in chi — see Ep28 Sub 22 in `REFERENCE.md` §8.)
5. If chi has nuance eng lacks → **REWRITE** to capture it.
6. If yue is HIGH and diverges from chi, first check yue is intelligible (coherent syntax, parseable as real speech). If garbled → fall back to chi, stop. Then ask: **are yue's word and chi's word synonyms, or different words entirely?**
   - **Synonyms, yue more vivid/colloquial/register-appropriate** → Rule A: **REWRITE** to match yue.
   - **Different words** → Rule B: chi wins by default. Only override chi if eng or cross-episode evidence corroborates yue, or chi has a visible OCR artefact.
7. If yue's emotional register is sharper, warmer, more colloquial, or more formal than the draft → **REWRITE** to match yue's register even if chi semantics are preserved (this is Rule A applied to a register-only difference).
8. If chi or yue has an address term Step 3 didn't catch → ensure it's **CJK in hybrid**.
9. If chi or yue has an idiom Step 3 didn't catch → ensure it's **in the hybrid sub**.
10. If none of the above apply → **leave the sub alone**; the draft is faithful.
11. Save any corrections to `ep{N}_h_all.json`.

Examining every sub is what makes FULL quality — not rewriting every sub. A faithful draft left untouched is a correct outcome.

**Exception — preserve Step 3 output when chi and yue are both empty/bare name.** For subs where chi is empty or just a bare name (opening-credits name cards, etc.) and yue offers no additional content, **keep the Step 3 output rather than rewriting.** Manually projecting a speaker from sparse sources caused a name-swap bug in prior sessions. If neither chi nor yue has content beyond a name, don't guess the speaker.

### Step 5 — Add Episode Extras

Add episode-specific romanisation entries to `ep{N}_extra.json` for all CJK that appears in the hybrid overrides but isn't already in `PersonalNamesUpdated.csv`.

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

- Grep romanised files for all **banned terms** (see `STYLE.md`).
- Grep hybrid file for **Pinyin leakage** (Guo Jing, Huang Rong, Rong-er, etc.).
- Validate: zero CJK in romanised files; zero banned terms; zero overlapping timestamps; same subtitle count and indices as source `{N}-chi_tra.csv` (chi is the entry spine; see `STYLE.md` §16).
- `present_files` with all three SRTs.

### Step 9 — Report Ending Context

After `present_files` completes, report the ending context estimate in the same format as Step 0, plus the delta.

Report format:

```
Context ending — Episode N
• Baseline (Step 0): ~ZZ%
• Ending estimate: ~WW%
• Delta consumed by this episode: ~ΔΔ%
• Episode size processed: XXX subs
• Ready for another episode this session: yes / borderline / no — recommend fresh chat
```

The delta is informational — useful for the user to judge whether to attempt another episode in the same session, but not persisted anywhere. Each session starts from the conservative defaults in Step 0.

---

## What "Examine Against Sources" Looks Like — Concrete Examples

Each example shows the three tracks plus the fix. When yue is present, it confirms or overrides.

### FABRICATION (delete content not in sources)
```
ENG: "He ran away laughing at her"
CHI: 他走了
YUE: 佢走咗
FIX: "He left"
WHY: "laughing at her" is nowhere in chi or yue. Delete it.
```

> **Cross-check yue before deleting — the Ep28 Sub 22 correction.** An earlier version of this doc flagged *"fed poisonous scorpions daily"* as a fabrication on the basis of chi alone. But yue (HIGH confidence) said 每日用一隻毒蝎嚟養大 — the eng was right; the chi had an OCR error. **When eng and chi disagree, check yue before deleting.** If yue confirms eng, treat chi as OCR-corrupted.

### MEANING FLATTENED (rewrite to match sources)
```
ENG: "He became very angry"
CHI: 他好像很生氣
YUE: 佢好似好嬲
FIX: "He seemed very angry"
WHY: 好像 / 好似 = "seemed/appeared", not "became". Both chi and yue preserve the certainty level eng collapsed.
```

```
ENG: "Father is just waiting for teacher to go retrieve the antidote"
CHI: 爹是一心一意去給我找解藥的
YUE: 爹一心一意去幫我搵解藥
FIX: "阿爹 is single-mindedly determined to find me the antidote"
WHY: 一心一意 = "wholeheartedly / single-mindedly", not "just waiting". Yue confirms chi.
```

### YUE OVERRIDES CHI (Yue-Authority Rule)
```
ENG: "He's got cunning schemes"
CHI: 佢有鬼主意
YUE: 佢好古惑     [HIGH]
FIX: "He's crafty — 古惑."
WHY: 古惑 is what's actually spoken. 鬼主意 is chi flattening the vivid Cantonese word.
```

```
ENG: "Poor thing"
CHI: 可憐
YUE: 淒涼        [HIGH]
FIX: "Desolate — 淒涼."
WHY: 淒涼 is emotionally stronger than 可憐 — register match matters even when chi semantics are close.
```

### REGISTER DRIFT (rewrite to match yue tone, even if chi meaning is preserved)
```
ENG: "You again, you stinking beggar!"
CHI: 又係你呢個臭要飯的      (OCR: chi-track mistranscribes)
YUE: 又係你呢個死乞兒        [HIGH]
FIX: "You again, you stupid beggar!"
WHY: Actual Cantonese is 死乞兒 ("damned/stupid beggar"), not 臭要飯的. Both chi and yue ASR get this wrong but yue is closer. Render the register the speaker actually used.
```

### ADDRESS TERM DROPPED (restore from sources)
```
ENG: "Who do you think is responsible?"
CHI: 仙姑, 依你看是哪路人馬幹的
YUE: 仙姑, 你睇係邊路人馬搞嘅
FIX: "仙姑, who do you think is behind this?"
WHY: The address term 仙姑 was dropped from the English. Both chi and yue have it.
```

### CHARACTERISATION DROPPED (restore from sources)
```
ENG: "Lu Chengfeng is a disciple of the lord of Peach Blossom Island"
CHI: 陸乘風那個老賊 是桃花島島主的傳人
YUE: 陸乘風嗰個老賊 係桃花島島主嘅傳人
FIX: "陸乘風, that old scoundrel, is a disciple of the master of 桃花島"
WHY: 那個老賊 / 嗰個老賊 (that old scoundrel) — entire characterisation dropped. Chi and yue agree.
```

(See `REFERENCE.md` → Error Taxonomy for the full catalogue of error categories and examples.)

---

## Fallback Protocol — Stop and Ask

There is no batch-processing shortcut. The examination loop in Step 4 is not optional and cannot be compressed. Step 3's preprocessing handles mechanical substitutions, but Error Taxonomy Categories 1 (FABRICATION) and 2 (CHI_MEANING_LOST) **always require reading against both chi and yue** — no mechanical pass can catch invented content or flattened nuance.

When Step 4 examination is unlikely to complete for this episode in the current session — because context budget is tight relative to the expected delta, or the assistant is already mid-session with prior episode artifacts loaded — **stop and ask the user for instructions.** Do not silently drop to a degraded outcome. Honest phrasing:

> "My context estimate is ~ZZ%, and Episode N has XXX subs. Step 4 would likely abort partway and produce PARTIAL rather than FULL quality. I recommend starting a fresh chat. Shall I proceed anyway, or would you prefer a new session?"

The frequent case: a 70% baseline often still has room for one small episode. Don't refuse reflexively on a percentage — judge from the conservative sub-count estimates in Step 0.

See the [Quality Control](#quality-control--mandatory) section for the full protocol.

---

## Handoff Files Checklist

Upload ALL of these to start a new session:

### Config & Reference (4 consolidated documents)
1. `PIPELINE.md` — this file
2. `STYLE.md` — style decisions (variants, names, titles, idioms, yue register, formatting, anti-patterns)
3. `REFERENCE.md` — context-dependent judgment calls, error taxonomy, Five Greats framework
4. `SESSION-NOTES.md` — episode completion status, pending-episode previews, watch list of names/terms/oddities

### Version file
5. `VERSION` — single line containing the handoff bundle version (e.g. `9`). `build.py` and `cjk_fix_v2.py` read this at runtime and stamp it into output SRT filenames (`{EP}-eng-{variant}-v{VERSION}.srt`) so every delivered subtitle file is traceable to the rule-set that produced it. A bundle with missing or malformed VERSION will fail loudly rather than ship unstamped SRTs.

### Data file
6. `PersonalNamesUpdated.csv` — name lookup (copy to `/home/claude/` first)

### Pipeline scripts (5 files)
7. `pipeline.py` — CSV/JSON parser and chi-spine alignment (v6: Whisper preprocessing, chi-as-entry-spine). Importable module with `run()` and `main()`.
8. `auto_override_v2.py` — deep override with CJK injection + idioms (v2.1: confidence-tier aware)
9. `shared_extras.py` — episode extras generator
10. `build.py` — builder with all conversion tables. Fix path: `PersonalNamesUpdated.csv` → `/home/claude/PersonalNamesUpdated.csv`. Reads `VERSION` adjacent to itself for output filename stamping.
11. `cjk_fix_v2.py` — comprehensive CJK cleanup for romanised files. Reads `VERSION` to locate the SRTs build.py wrote.

### Tests (1 file)
12. `test_pipeline.py` — unittest suite covering synthetic reflow cases and a 17-row Ep24 real-data slice. Run with `python3 -m unittest test_pipeline.py -v`. Not required for sub generation, but verifies pipeline.py still works correctly after any edits.

### Per-episode inputs
13. `{N}-eng.csv`, `{N}-chi_tra.csv`, `{N}-yue.json`

---

## Quick-Start for New Chat

1. Upload the handoff bundle — **4 reference docs + 1 VERSION file + 1 data file + 5 scripts + 1 test file = 12 files** (see [Handoff Files Checklist](#handoff-files-checklist) above) — plus the episode sources `{N}-eng.csv`, `{N}-chi_tra.csv`, `{N}-yue.json`.
2. Say: *"Process episode N with full source-authority rewriting (FULL standard)"* — i.e. examine every sub against chi and yue per the priority chain in `STYLE.md` §2.
3. The assistant MUST:
   - **Report Step 0 context baseline** before doing anything else
   - Copy `PersonalNamesUpdated.csv` to `/home/claude/`
   - Place/create all 5 scripts
   - Run `pipeline.py`, **READ THE FULL DUMP against chi and yue**
   - Examine every sub against chi and yue (including confidence tiers); write manual overrides where content or register mismatches
   - Add episode-specific extras
   - Build, CJK-fix, validate (zero CJK in romanised, zero banned terms)
   - Present output files
   - **Report Step 9 ending context** (informational)
4. **ONE EPISODE PER REQUEST for FULL quality.** If context is getting full, **ASK** before proceeding.
