# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not a conventional software project — it is an LLM-driven subtitle-production pipeline. The repo is the durable artefact of a conversational workflow: each episode is processed in a Claude.ai chat session that uploads a handoff bundle (scripts + reference docs + per-episode sources), runs the Python pipeline, and leans on the model to examine every subtitle against three source tracks. The Python code handles mechanical work (parsing, alignment, substitution, romanisation, linting); the model does the translation judgment.

Output goal: three SRT variants per episode of *Legend of the Condor Heroes 1983* — `eng-hybrid` (English prose with CJK for names/titles/idioms), `eng-jyutping` (full Jyutping romanisation), `eng-yale` (full Yale romanisation). Inputs per episode: `{N}-eng.csv`, `{N}-chi_tra.csv`, `{N}-yue.json` (WhisperX ASR of the Cantonese track).

## Layout

All working files live in `CondorHeroes83/`. The root holds only `README.md` and `LICENSE`.

## Authoritative docs — read before doing anything substantive

The four consolidated documents in `CondorHeroes83/` are load-bearing and take precedence over anything summarised here:

- `PIPELINE.md` — the 9-step process (Step 0 context estimate → Step 9 ending report), quality outcomes (FULL / PARTIAL / MECHANICAL-ONLY), handoff-files checklist, stop-and-ask protocol.
- `STYLE.md` — every style decision: the priority chain (yue HIGH > chi > eng), the Yue-Authority Rule (A/B split), name/title/idiom tables, banned terms, recurring CJK-leak fix patterns.
- `REFERENCE.md` — context-dependent judgment calls, error taxonomy, Five Greats (五絕) framework, minor-character notes.
- `SESSION-NOTES.md` — per-episode completion status, pending-episode previews, watch list of names/terms/oddities not yet promoted into the consolidated docs.

When a style or pipeline question arises, cite these docs rather than re-deriving answers. Promote stabilised entries from `SESSION-NOTES.md` into `STYLE.md` / `REFERENCE.md` when they're settled across episodes.

## The Prime Directive

**Priority chain: yue (HIGH) > chi (semantic authority) > eng (draft).** Yue is the actual spoken Cantonese (via ASR — subject to homophone errors); chi is a written translation that sometimes flattens register; eng is an OCR'd fan-sub rough draft. Rule A (register/vividness override) lets yue beat chi when they're synonyms differing only in colour. Rule B (semantic disagreement) defaults to chi unless yue has independent corroboration. See `STYLE.md` §2 for the full treatment.

## Common commands

Pipeline scripts are invoked in order with an episode number argument. They expect Claude.ai artifact paths (`/mnt/user-data/uploads`, `/home/claude`, `/mnt/user-data/outputs`) — running locally requires those directories or script edits.

```bash
# Full episode pipeline
python3 pipeline.py <N>          # Step 1: parse + chi-spine align → ep{N}_aligned.json, ep{N}_dump.txt
python3 shared_extras.py <N>     # Merge extras_baseline.json + optional ep{N}_extras_add.json overlay
python3 auto_override_v2.py <N>  # Step 3: mechanical CJK preprocessing + AUTO-KEEP flags → ep{N}_h_all.json, ep{N}_confidence.json
python3 apply_overrides.py <N>   # Step 4: apply reviewer's ep{N}_overrides.tsv
python3 lint_overrides.py <N>    # Step 5.5: scan for known CJK-leak concat traps
python3 build.py <N>             # Step 6: emit 3 SRT variants, stamped with VERSION
python3 cjk_fix_v2.py <N>        # Step 7: strip residual CJK from romanised outputs

# Tests
python3 -m unittest test_pipeline.py -v
```

The `VERSION` file (single integer) is read at runtime by `build.py` and `cjk_fix_v2.py` to stamp output SRT filenames (`{N}-eng-{variant}-v{VERSION}.srt`). Bump it when the rule-set materially changes.

## Architecture notes that aren't obvious from one file

- **Chi is the entry spine.** Output entry count and timestamps come from `{N}-chi_tra.csv`, not eng. Eng content is reflowed onto chi entries: multi-eng-into-one-chi merges; one-eng-across-multi-chi splits proportionally (sentence → newline → char-proportion). This is why eng timings don't appear in output and why "double-subs" from timestamp-overlap alignment can't happen. See `STYLE.md` §16.
- **Yue confidence tiers drive override logic.** `auto_override_v2.py` reads Whisper `avg_logprob` and tags each sub HIGH (≥−0.3) / MEDIUM (≥−0.8) / LOW (<−0.8). HIGH is a *candidate* for overriding chi — the reviewer still applies the intelligibility gate. LOW yue is discarded.
- **AUTO-KEEP is a priority signal, not a gate.** The heuristic in `auto_override_v2.py` flags subs that passed seven conservative fidelity gates. A reviewer still reads every sub in Step 4, but concentrates examination time on the NEEDS REVIEW set. Designed for false-negative bias: a missed flag costs a quick re-examination; a false positive would silently degrade quality.
- **Baseline/overlay split for romanisation extras.** `extras_baseline.json` ships with the handoff bundle. Per-episode overlays (`ep{N}_extras_add.json`) add new terms. `shared_extras.py` is just the merger. Promote overlay entries to baseline once they're stable across 2+ episodes.
- **FULL quality is the only acceptable outcome.** PARTIAL and MECHANICAL-ONLY exist as honest failure-mode labels, not as targets. The Step 4 examination loop is mandatory; if context won't cover it, the protocol is to stop and ask rather than silently produce degraded output.
- **One episode per session.** Batching isn't supported. See `PIPELINE.md` "Quality Control" for the context-budget decision protocol.
