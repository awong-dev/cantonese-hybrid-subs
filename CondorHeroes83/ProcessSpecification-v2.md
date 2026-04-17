# Process Specification v2 — Chi-Authority Pipeline

## CRITICAL RULE: Chi is the authority text. English is a rough draft.

Every subtitle must be read against the Chinese (chi_tra) track and rewritten to match chi meaning. The English track is an OCR'd fan-sub that frequently:
- Fabricates content not in the Chinese
- Flattens nuance (好像 "seemed" → "became", 奮不顧身 "risking one's life" → dropped)
- Drops address terms (仙姑, 前輩, 師父 → just "you" or nothing)
- Misses idioms (四字成語 present in chi but absent from English)
- Simplifies register (低聲下氣 "grovelling" → "begging")

## The 7-Step Pipeline

### Step 1: Parse & Align
```bash
python3 pipeline.py <N>
```
Parses three CSVs (eng, chi_tra, yue), aligns by timestamp overlap, outputs `ep{N}_aligned.json` and a full dump to stdout.

### Step 2: Read the Full Dump
The operator (human or LLM) MUST read the dump output. For every sub, compare:
- Column 2 (eng) — the rough draft
- Column 3 (chi) — the AUTHORITY text
- Column 4 (yue) — parallel Cantonese corpus for cross-checking

### Step 3: Generate Overrides
```bash
python3 auto_override_v2.py <N>
```
This does mechanical fixes only: Pinyin→CJK, English terms→CJK, address term injection, idiom injection. It does NOT fix meaning.

**THEN: The operator must review every override against chi and fix meaning.**

This means for every sub:
1. Read the chi text
2. Compare against the auto-generated override
3. If eng says something chi doesn't → DELETE the fabrication
4. If chi has nuance eng lacks → REWRITE to capture it
5. If chi has an address term → ensure it's CJK in hybrid
6. If chi has an idiom → ensure it's in the hybrid sub
7. Save corrections to `ep{N}_h_all.json`

### Step 4: Build 3 Variants
```bash
python3 shared_extras.py <N>
python3 build.py <N>
```

### Step 5: CJK Fix Pass
```bash
python3 cjk_fix_v2.py <N>
```

### Step 6: Banned-Term Sweep
Check for and fix: Old Imp, Old Urchin, Brother Zhou/Zau/Jau, the Overgrown Child, 周大哥.

### Step 7: Validate & Present
- Zero CJK in romanised files
- Zero banned terms
- Zero overlapping timestamps
- Present files

## What "Read Against Chi" Looks Like — Concrete Examples

### FABRICATION (delete content not in chi)
```
ENG: "But these are snakes from White Camel Mountain that are fed poisonous scorpions daily"
CHI: 但實際上這些蛇,是白駝山用特殊的方法養大的蛇
FIX: "But they're actually raised by 白駝山 using a special method"
WHY: "poisonous scorpions" is nowhere in the Chinese. Delete it.
```

### MEANING FLATTENED (rewrite to match chi)
```
ENG: "He became very angry"
CHI: 他好像很生氣
FIX: "He seemed very angry"
WHY: 好像 = "seemed/appeared", not "became". Different certainty level.
```

```
ENG: "Father is just waiting for teacher to go retrieve the antidote"
CHI: 爹是一心一意去給我找解藥的
FIX: "阿爹 is single-mindedly determined to find me the antidote"
WHY: 一心一意 = "wholeheartedly/single-mindedly", not "just waiting"
```

### ADDRESS TERM DROPPED (restore from chi)
```
ENG: "Who do you think is responsible?"
CHI: 仙姑,依你看是哪路人馬幹的
FIX: "仙姑, who do you think is behind this?"
WHY: The address term 仙姑 was dropped from the English
```

### CHARACTERISATION DROPPED (restore from chi)  
```
ENG: "Lu Chengfeng is a disciple of the lord of Peach Blossom Island"
CHI: 陸乘風那個老賊 是桃花島島主的傳人
FIX: "陸乘風, that old scoundrel, is a disciple of the master of 桃花島"
WHY: 那個老賊 (that old scoundrel) — entire characterisation dropped
```

## Batch Processing Protocol

For episodes where deep reading of every sub is not feasible, the v2 auto-override handles Categories 3 (NAME_TITLE_LEAK) and 4 (IDIOM_MISSING) mechanically. But Categories 1 (FABRICATION) and 2 (CHI_MEANING_LOST) ALWAYS require reading.

The minimum acceptable standard is:
- Read every sub where chi and eng clearly diverge
- Fix all fabrications (eng adds content not in chi)
- Fix all meaning-altering mistranslations
- Restore all dropped address terms and characterisation

The ideal standard (used for Eps 25-31) is:
- Read and manually override ALL subs
- Cross-check against yue for emotional register
- Fix OCR errors in chi using yue as witness
