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

Bad (what the v10 first-pass produced):
> "Let me now read STYLE.md..."
> "Good — I have the full style and reference context. Now let me set up the working directory..."
> "Step 3 complete. Only 19 AUTO-KEEPs out of 503 — that's a low rate, which makes sense for an episode with lots of CJK-dense scenes..."
> "**Ep27 progress report — Ep27**  [paragraph of recap]"
> "**Summary of Step 4 work:** [bullet list of what was already visible in tool output]"
> "**Candidates to promote from Ep27 overlay → `extras_baseline.json`**: [long list]"
> "**Watch List additions** [another long list]"

The good version delivers the same work product with a small fraction of the conversational text.

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

**How to make the call (v10):** with the v10 efficiency changes (file-based dump, AUTO-KEEP pre-filter, TSV override format, overlay-based extras, pre-build lint), the conservative sub-count estimates are roughly ~25% of context for a 400-sub episode during Step 4, and ~40% for a 600-sub episode — down from ~35% / ~50% in v9. If `baseline + expected delta` exceeds ~90%, project the outcome as borderline or likely-degraded. These remain deliberately conservative; actual usage varies with episode density, and the efficiency gains depend on the reviewer actually using the file-based flow (reading `ep{N}_dump.txt` via `view` ranges rather than re-dumping via `python3 -c`).

### Step 1 — Parse & Align

```bash
cp /mnt/user-data/uploads/PersonalNamesUpdated.csv /home/claude/
python3 pipeline.py <N>
```

Parses the three source tracks and aligns them onto a **chi-spine skeleton**: the output's entry count and timestamps are taken from chi, not eng. Outputs `ep{N}_aligned.json` plus a compact summary to stdout.

**v14 change — the dump moves to Step 3.** Prior bundles (v10–v13) had `pipeline.py` write `ep{N}_dump.txt` alongside `ep{N}_aligned.json`. The dump now comes out of `auto_override_v2.py` instead, because the dump format carries per-sub flags (`•` AUTO-KEEP, `!` fabrication risk, `i` idiom, `@` missing address, `o` OCR noise) that depend on `auto_override_v2.py`'s heuristics. Colocating dump-writing with flag-computation avoids re-reading `aligned.json` in a separate pass. `pipeline.py`'s sole output is now the structural alignment.

**v10 precursor — file-based dump** (still applies): the dump is written once to disk and consumed by `view`ing line ranges in Step 2. In pre-v10 bundles it was printed to stdout and re-echoed via `python3 -c`, which cost context. That's still the rule — only the script that emits it has changed.

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

Each sub in the dump is annotated `[HIGH]` / `[MEDIUM]` / `[LOW]`, and `[T-ADJ]` marks subs whose start/end times were tightened to word boundaries (Whisper `score ≥ 0.7`). Per-sub confidence notes are written to `ep{N}_confidence.json` for the manual review pass.

### Step 2 — Read the Full Dump (MANDATORY)

Read EVERY line of `ep{N}_dump.txt` (written by Step 3 under v14). Use `view` with line ranges — typically 100–200 subs per range — rather than `cat` or `python3 -c` round-trips.

**v14 dump format.** Each sub occupies 3–4 lines:

```
<idx>|<conf>|<flags>[ T-ADJ]
E <eng>
C <chi>
Y <yue>                      (omitted if empty; may be "[see N]" for dedup)
```

The `<flags>` column is a 5-character padded string carrying per-sub priority signals computed by `auto_override_v2.py`:

- `•` — AUTO-KEEP (passed all seven faithful_heuristic gates; likely quick-confirm)
- `!` — eng has fabrication-risk markers (long parenthetical, `", which"` clause)
- `i` — chi contains an idiom from the injection set
- `@` — chi has an address term (師父, 前輩, 老伯…) missing from the Step 3 output
- `o` — chi contains an OCR artifact (garbled quote marks, stray Latin letters amid CJK)

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

**v10 change — baseline/overlay split for extras.** Prior bundles kept the entire baseline of shared romanisation mappings (plus every episode's new entries) inside `shared_extras.py`, so each episode's builder file duplicated ~180 lines of boilerplate. In v10, `shared_extras.py` is a thin merger: it reads `extras_baseline.json` (ships with the bundle) and optionally `ep{N}_extras_add.json` (per-episode overlay — the reviewer writes this in Step 5), merges them, and writes `ep{N}_extra.json` for `build.py` to consume. A reviewer with nothing new to add can skip the overlay file and `shared_extras.py` still works. Overlay keys override baseline keys on collision.

**v10 addition — AUTO-KEEP heuristic.** `auto_override_v2.py` now annotates each sub in `ep{N}_confidence.json` with an `auto_keep: true/false` flag. An `auto_keep: true` flag means the sub passed all seven conservative gates (all tracks non-empty, yue HIGH/MEDIUM, no fabrication-risk markers, no idioms in chi, no missing address terms, ≤1.5× length ratio, ≥0.7 content-word overlap) — indicating the Step 3 output is very likely already faithful. AUTO-KEEP is a **priority signal, not a gate**: the reviewer still reads every sub in Step 4, but concentrates examination time on the NEEDS REVIEW set (anything not flagged AUTO-KEEP). The heuristic is designed for false-negative bias: when in doubt, the heuristic does not flag. A false positive (flagging a sub faithful when it has a subtle meaning/register issue) would silently degrade quality; a false negative just costs a sub's worth of examination that was probably going to be quick anyway.

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
10. **Common-noun CJK sweep (v14 Ep33 rule).** Before finalising the hybrid entry, check that none of the following have been left as CJK in hybrid — they must all be English (see `STYLE.md` §7 "What does NOT get CJK"):
    - **Generic wuxia vocabulary** — 武功 / 武林 / 江湖 / 內力 / 內功 / 輕功 / 功力. These are common nouns; CJK here clutters without adding cultural weight. Named techniques (九陰真經, 降龍十八掌, 空明拳, 打狗棒法, etc.) remain CJK.
    - **Colloquial insult compounds** — 臭丫頭 / 死丫頭 / 死乞兒 / 臭乞兒 / 王八蛋 / 禁宮. Intensifier + common-noun-insult goes English. Contrast with intensifier + proper-nickname (死老邪, 老毒物) which stays CJK.
    - **叫化子** — render as Cantonese 乞兒 if CJK is warranted, otherwise English "beggar"; never leave the Mandarin 叫化子 in hybrid.
    - **Descriptive common-noun metaphors** — phrases like 情蛇, 一流高手, X+高人, X+蛇 where X is an adjective rather than a proper qualifier. Test: strip the CJK and read the English rendering alone. If it works as a plain English noun phrase ("a first-rate expert"), it's a descriptor, not an idiom — English in hybrid. See `STYLE.md` §10's admission gate for what qualifies as a catalogue-worthy idiom.
    This check is what `lint_overrides.py`'s "common-noun-rendering heuristic" tries to catch automatically, but the reviewer's judgment is the final arbiter. Step 3 preprocessing does not strip these — they're a pure Step 4 discipline.
11. If none of the above apply → **leave the sub alone**; the draft is faithful.
12. Collect your corrections into `ep{N}_overrides.tsv` (see below) and apply with `apply_overrides.py`.

**v10 — how to triage the examination.** `ep{N}_confidence.json` now carries an `auto_keep` flag per sub (see Step 3). Subs with `auto_keep: true` should still be read, but quickly — the heuristic has already checked for fabrication risk, idiom injection, address-term drops, and length divergence, and all of those gates passed. Treat AUTO-KEEP as "likely quick confirm". Subs with `auto_keep: false` are where examination time earns its keep: fabrications, meaning flattening, yue-authority overrides, register drift, idiom injection all concentrate in the NEEDS REVIEW set.

**v10 — how to write overrides.** Collect corrections into `/home/claude/ep{N}_overrides.tsv`, one per line, tab-separated:

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

This merges the TSV into `ep{N}_h_all.json`, replacing entries by index. Subs not listed in the TSV keep whatever Step 3 wrote — an empty TSV is a valid "trust Step 3 completely" signal (though unlikely to be the right call for a full episode). The TSV format replaces the prior pattern of emitting overrides as a Python literal dict inside a patch script, which cost ~1.3× the text size in context due to dict/quoting overhead.

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

**Check 1 — concat-trap patterns** (v10). Scans the hybrid for known CJK-leak concat patterns catalogued in `STYLE.md` §19 and the `SESSION-NOTES.md` Watch List. Catalogued patterns include `裘老前輩` / `裘前輩` (surname+title), `X大哥` (surname+Brother), `我爹` / `你爹` (possessive+kinship), `大金國` / `大宋` (dynasty prefix), `我<FullName>` (emphatic self-reference), `大師父`. Running this before `build.py` lets the reviewer register missing compounds in the overlay once rather than iterating after build.

**Check 2 — common-noun-rendering heuristic** (v14). Scans overlay entries (`ep{N}_extras_add.json`) and flags any whose English rendering looks like a common noun (lowercase-starting, or article-plus-lowercase, or Capital-plus-lowercase-words). Enforces STYLE.md §7's exhaustive-lists rule: hybrid CJK is for names/titles/places/idioms/terms-of-art, not common nouns. Catches the Ep20-style "如意燈 kept as CJK when it should have been 'lucky lanterns' in English" failure.

The heuristic has three action buckets:
- **(a) Genuine idiom/term-of-art** → promote to STYLE.md §8/§10.
- **(b) Common noun kept in CJK by mistake** → drop from overlay, rewrite affected hybrid subs in English.
- **(c) Character voice / flavour phrase** (like 臭要飯的) → judgment call; promote to STYLE.md only if recurring.

Both checks are **non-fatal** — the reviewer inspects each warning and decides. The lint exits 1 if either check surfaces issues, 0 only if both are clean.

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
- Grep hybrid file for **common-noun CJK** that should be English (v14 Ep33 rule, `STYLE.md` §18): 武功 · 武林 · 江湖 · 內力 · 內功 · 輕功 · 功力 · 叫化子 · 臭丫頭 · 死丫頭 · 死乞兒 · 臭乞兒 · 王八蛋 · 禁宮. Any of these as CJK in hybrid is a build-time error — fix the hybrid sub and rebuild.
- Validate: zero CJK in romanised files; zero banned terms; zero overlapping timestamps; same subtitle count and indices as source `{N}-chi_tra.csv` (chi is the entry spine; see `STYLE.md` §16).
- `present_files` with all three SRTs.

### Step 8.5 — Update and Present SESSION-NOTES.md

After the three SRTs are presented, update `SESSION-NOTES.md` and present the updated file so the user can drop it into the next session's handoff bundle. This replaces the prior flow where session findings were lost between chats unless the user remembered to ask for them.

What to update, in order:

1. **Move the episode's status entry.** If the episode completed FULL under the current bundle version, move its row out of the "Pending — Needs FULL Processing" table and into the "Completed under v{VERSION} (FULL)" table. Replace any prior-session content preview with a row body in the format specified below. If the outcome was PARTIAL or MECHANICAL-ONLY, leave the row in Pending and annotate the outcome honestly — don't promote a degraded delivery.

   **Completed-table row body format.** The body must contain, in this order, and nothing else:

   a. **Arc label** — one sentence naming the location or plot driver AND the key characters. Example: "臨安 / 元宵 arc with 岳文 and 武穆遺書 plot." Not "Opens with 郭靖/黃蓉 at an inn where 蓉兒's silver-note grift..." The label pins the episode for future precedent lookups; it is not a plot synopsis. No more than ~15 words.

   b. **"First FULL firing for:"** — flat comma-separated list of terms, idioms, classical references, and names that this episode is the first FULL-processed instance of. This is the load-bearing content that future sessions consult for cross-episode precedent.

   c. **Cross-episode precedents established or revised** — short callouts only when relevant: "first on-screen use of X", "first scene naming all four 五絕 together", "Ep21 summary previously said X fired first; Ep20 corrects that to Ep20 first." Omit this entire element if the episode established no such precedent.

   d. **Chi-OCR variants encountered** — flat list like `匡文/策老伯/品王爺→岳文/岳老伯/岳王爺`. Feeds future `cjk_fix_v2.py` `OCR_NAME_COLLAPSE` promotions. Omit if the episode had no notable OCR damage.

   e. **Promotion flags** — short pointers to Watch List items that fired here and are candidates for promotion on next firing (e.g. "岳王爺 and 本姑娘 cross-stage traps need promotion to `cjk_fix_v2.py` `shared_concat_fixes` on next firing"). Omit if none.

   **Narrative plot detail does not belong in SESSION-NOTES.** Who said what to whom, scene-by-scene beats, character motivations, and dialogue color are all excluded. The SRTs carry the plot; SESSION-NOTES carries only what future sessions need for precedent continuity.

   **Prior-session preview rows** in the Pending table follow the same constraint: location + arc-driver keywords only, no plot prose. These predate the current rule-set and do not count as established precedent — their only job is to let a future session know what the episode is about before processing it.

2. **Add new Watch List entries.** Anything encountered during processing that doesn't yet have a settled rendering goes under a short descriptive heading in the Watch List. Skip things already covered by `STYLE.md` §5 (names), §6 (titles), §10 (idioms), or `REFERENCE.md`. Recurring CJK leaks, name-variant OCR drift, cross-stage concat traps, and classical allusions are typical additions. If a concat-trap fix needed a post-build `sed` pass (rather than overlay registration working cleanly), log the mechanism and the fix — that's what the Watch List's "Cross-stage concat traps" section exists for.

3. **Promote stable items out of the Watch List.** Any Watch List entry that has now fired in two-or-more episodes without contradicting renderings should be moved into the appropriate consolidated doc (name → `STYLE.md` §5; title → §6; idiom → §10; context-dependent judgment → `REFERENCE.md`; concat-trap fix → `cjk_fix_v2.py` or `extras_baseline.json`) and deleted from `SESSION-NOTES.md`. If the promotion target is a script or JSON config rather than a markdown doc, note in the SESSION-NOTES edit that the companion file needs updating — but actually editing the script is not required if it wasn't part of this session's work.

4. **Call `present_files` on the updated `SESSION-NOTES.md`.** This is what makes the update reachable — without a present_files call, the edit sits in `/home/claude/` where the user can't retrieve it.

What NOT to do:

- Don't restate the SESSION-NOTES edits in chat. The user can read the file. Narration of what you changed costs context and duplicates what's in the file. One sentence — "Updated SESSION-NOTES with Ep{N} status and {N} new Watch List items" — is enough, and often even that is optional if the file speaks for itself.
- Don't add content-free edits (minor phrasing tweaks, reformatting, editorial prettification). SESSION-NOTES is append-mostly with targeted promotions; it's not a doc to polish.
- Don't promote something after only one episode's evidence. The two-episode threshold exists because single-episode patterns are often episode-specific and don't generalise.

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

## Context Awareness

There is no batch-processing shortcut. The examination loop in Step 4 is not optional and cannot be compressed. Step 3's preprocessing handles mechanical substitutions, but Error Taxonomy Categories 1 (FABRICATION) and 2 (CHI_MEANING_LOST) **always require reading against both chi and yue** — no mechanical pass can catch invented content or flattened nuance.

When context budget is tight relative to the expected delta, state the projected quality in the Step 0 report so the user can judge:

> "My context estimate is ~ZZ%, and Episode N has XXX subs. Projected quality at current context: borderline (may end PARTIAL)."

The user decides whether to proceed. A 70% baseline often still has room for one small episode; judge from the conservative sub-count estimates in Step 0.

See the [Quality Control](#quality-control--mandatory) section for the full diagnostic framework.

---

## Handoff Files Checklist

Upload ALL of these to start a new session:

### Config & Reference (4 consolidated documents)
1. `PIPELINE.md` — this file
2. `STYLE.md` — style decisions (variants, names, titles, idioms, yue register, formatting, anti-patterns)
3. `REFERENCE.md` — context-dependent judgment calls, error taxonomy, Five Greats framework
4. `SESSION-NOTES.md` — episode completion status, pending-episode previews, watch list of names/terms/oddities

### Version file
5. `VERSION` — single line containing the handoff bundle version (e.g. `10`). `build.py` and `cjk_fix_v2.py` read this at runtime and stamp it into output SRT filenames (`{EP}-eng-{variant}-v{VERSION}.srt`) so every delivered subtitle file is traceable to the rule-set that produced it. A bundle with missing or malformed VERSION will fail loudly rather than ship unstamped SRTs.

### Data files (2)
6. `PersonalNamesUpdated.csv` — name lookup (copy to `/home/claude/` first)
7. `extras_baseline.json` — shared romanisation baseline for terms beyond personal names (titles, places, sects, idioms, kinship). Loaded by `shared_extras.py`; merged with any `ep{N}_extras_add.json` overlay to produce `ep{N}_extra.json`.

### Pipeline scripts (7 files)
8. `pipeline.py` — CSV/JSON parser and chi-spine alignment (v6: Whisper preprocessing, chi-as-entry-spine). v10: writes the full dump to `ep{N}_dump.txt` rather than stdout. Importable module with `run()` and `main()`.
9. `auto_override_v2.py` — deep override with CJK injection + idioms (v2.1: confidence-tier aware; v10: AUTO-KEEP heuristic annotation)
10. `shared_extras.py` — thin merger: baseline + optional `ep{N}_extras_add.json` overlay → `ep{N}_extra.json`
11. `apply_overrides.py` (v10) — applies Step 4 reviewer overrides from `ep{N}_overrides.tsv` into `ep{N}_h_all.json`
12. `lint_overrides.py` (v10) — pre-build lint for known CJK-leak concat patterns
13. `build.py` — builder with all conversion tables. Fix path: `PersonalNamesUpdated.csv` → `/home/claude/PersonalNamesUpdated.csv`. Reads `VERSION` adjacent to itself for output filename stamping.
14. `cjk_fix_v2.py` — comprehensive CJK cleanup for romanised files. Reads `VERSION` to locate the SRTs build.py wrote.

### Tests (1 file)
15. `test_pipeline.py` — unittest suite covering synthetic reflow cases and a 17-row Ep24 real-data slice. Run with `python3 -m unittest test_pipeline.py -v`. Not required for sub generation, but verifies pipeline.py still works correctly after any edits.

### Per-episode inputs
16. `{N}-eng.csv`, `{N}-chi_tra.csv`, `{N}-yue.json`

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
   - Run `auto_override_v2.py` → `ep{N}_h_all.json` + `ep{N}_confidence.json` + `ep{N}_dump.txt` (with per-sub flags); `view` the dump file in ranges
   - Examine every sub; concentrate effort on subs whose flags column is non-blank
   - Collect corrections into `ep{N}_overrides.tsv`; run `apply_overrides.py <N>`
   - Write `ep{N}_extras_add.json` if new CJK terms introduced; re-run `shared_extras.py <N>` to merge
   - Run `lint_overrides.py <N>` — fix any concat-trap warnings by updating the overlay
   - Build, CJK-fix, validate (zero CJK in romanised, zero banned terms)
   - Present output files
   - **Update and present `SESSION-NOTES.md`** — move episode's row into Completed table, add new Watch List items, promote stable items out (see Step 8.5)
   - **Report Step 9 ending context** (informational)
4. **ONE EPISODE PER REQUEST for FULL quality.** If context is tight, state the projected quality in Step 0 and let the user decide.
5. **Follow Narration Discipline.** Run tools silently between the Step 0 and Step 9 reports; surface only actual issues (one line each) and the final `present_files`. Do not produce mid-turn progress recaps, interpretive commentary on tool output, or end-of-episode "candidates to promote" / "watch list" summaries — edits to `SESSION-NOTES.md` are where such findings go.
