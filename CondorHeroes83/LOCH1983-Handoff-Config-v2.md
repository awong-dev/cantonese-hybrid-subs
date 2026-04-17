# Legend of the Condor Heroes 1983 TVB — Subtitle Pipeline Configuration v2

## CRITICAL: Read ErrorTaxonomy.md and ProcessSpecification-v2.md FIRST.

The single most important rule: **Chi is the authority text. English is a rough draft.** Every subtitle must be read against Chinese and rewritten. Do not preserve the original English as default. Override EVERY sub.

## Project Overview

Producing three SRT subtitle variants per episode from three CSV source tracks (eng, chi_tra, yue):
- `{N}-eng-hybrid.srt` — English with Chinese characters for names/titles/idioms
- `{N}-eng-jyutping.srt` — Full Jyutping romanisation
- `{N}-eng-yale.srt` — Full Yale romanisation

Source CSVs: `/mnt/user-data/uploads/{N}-eng.csv`, `{N}-chi_tra.csv`, `{N}-yue.csv`
Output SRTs: `/mnt/user-data/outputs/`
PersonalNames lookup: `/mnt/user-data/uploads/PersonalNamesUpdated.csv` (72 entries)

## Completion Status

**Episodes 1–54 DONE.** Episodes 25–31 are deep-processed (chi-authority rewriting). Episodes 32–54 have v2 mechanical fixes (name/title/idiom injection) but NOT full chi-meaning rewriting — they may need rework.
**Remaining: 55, 56, 57, 58, 59.**

---

## Pipeline Steps (per episode)

### Step 1: Parse & Align
```bash
python3 pipeline.py <N>
```

### Step 2: Read the Full Dump — MANDATORY
Read EVERY line of the dump. For each sub, compare eng (column 2) against chi (column 3). Note:
- Fabrications: eng says something chi doesn't → mark for deletion
- Meaning lost: chi has nuance eng flattens → mark for rewriting
- Address terms: chi has 仙姑/前輩/師父/etc → must appear as CJK in hybrid
- Idioms: chi has 四字成語 → must appear in hybrid
- Register: yue (column 4) reveals emotional tone and OCR errors in chi

### Step 3: Generate & Fix Overrides
```bash
python3 auto_override_v2.py <N>    # Mechanical fixes only
```
Then MANUALLY edit `ep{N}_h_all.json`:
- Fix every fabrication
- Fix every meaning-altering mistranslation
- Restore all dropped address terms and characterisation
- Inject all idioms

### Step 4-7: Build, Fix, Validate, Present
```bash
python3 shared_extras.py <N>
python3 build.py <N>
python3 cjk_fix_v2.py <N>
# Then banned-term sweep
```

---

## Handoff Files Checklist

Upload ALL of these to start a new session:

### Data Files
1. `PersonalNamesUpdated.csv` — 72-entry name lookup
2. `ProcessSpecification-v2.md` — pipeline spec with chi-authority rule
3. `StyleRulings.md` — accumulated style decisions
4. `TrickyInferences.md` — context-dependent judgment calls
5. `ErrorTaxonomy.md` — concrete error examples and fixes
6. `LOCH1983-Handoff-Config-v2.md` — this file

### Pipeline Scripts
7. `pipeline.py` — CSV parser and alignment
8. `auto_override_v2.py` — deep override with CJK injection + idioms
9. `build.py` — 230-line builder with all conversion tables
10. `shared_extras.py` — episode extras generator
11. `cjk_fix_v2.py` — comprehensive CJK cleanup for romanised files

---

## Style Rulings (Accumulated Eps 1–54)

### Variant Rules
- **Hybrid**: English prose with CJK for personal names, titles, honorifics, idioms, places, martial arts terms. No Pinyin. No English proper nouns where CJK exists.
- **Jyutping/Yale**: Fully romanised. Zero CJK characters allowed.

### Name Rendering

| Chinese | Hybrid | Jyutping | Yale |
|---------|--------|----------|------|
| 老頑童 | 老頑童 | Overgrown Child | Overgrown Child |
| 週大哥 | 週大哥 | 週-daai-go | 週-daaih-go |
| 老毒物 | 老毒物 | Old Venom | Old Venom |
| 賴蛤蟆 | 賴蛤蟆 | Old Toad | Old Toad |
| 靖哥哥 | 靖哥哥 | Zing-gogo | Jing-gogo |
| 蓉兒 | 蓉兒 | Jung-ji | Yuhng-yi |
| 靖兒 | 靖兒 | Zing-ji | Jing-yi |
| 康兒 | 康兒 | Hong-ji | Hong-yi |
| 七公 | 七公 | Seven Elder | Seven Elder |
| 黃老邪 | 黃老邪 | Old Heretic Wong | Old Heretic Wong |
| 黃島主 | 黃島主 | Island Lord Wong | Island Lord Wong |
| 藥師兄 | 藥師兄 | Brother Joek-si | Brother Yeuhk-si |
| 阿衡 | 阿衡 | Aa-Hang | Aa-Hahng |
| 歐陽世兄 | 歐陽世兄 | Brother Au-Joeng | Brother Au-Yeung |
| 父王 | 父王 | Royal Father | Royal Father |
| 閻王爺 | 閻王爺 | King of Hell | King of Hell |

### Banned Terms (auto-fix after every build)
- "Old Imp" → 老頑童 (hybrid) / Overgrown Child (romanised, NO article)
- "Old Urchin" → same
- "Brother Zhou" / "Brother Zau" / "Brother Jau" → 週大哥 (hybrid) / 週-daai-go (jy) / 週-daaih-go (yl)
- "the Overgrown Child" → "Overgrown Child" (drop article, proper noun)

### Hybrid CJK Requirements (ALL of these must be CJK in hybrid, never English)
**Names**: All character names from PersonalNamesUpdated.csv
**Titles**: 師父 師兄 師弟 師姊 師妹 前輩 師叔 師姑 莊主 少莊主 幫主 祖師爺 仙姑 駙馬爺 王爺 小王爺 大哥 七公 島主 etc.
**Address**: 父王 阿爹 爹 娘親 靖哥哥 蓉兒 靖兒 康兒 阿靖 阿康 週大哥 黃島主 藥師兄 歐陽世兄 etc.
**Places**: 桃花島 桃花陣 白駝山 歸雲莊 牛家村 蒙古 臨安 大理 etc.
**Sects**: 全真教 丐幫 鐵掌幫 etc.
**Terms**: 九陰真經 武穆遺書 降龍十八掌 蛤蟆功 左右互搏 空明拳 九陰白骨爪 輕功 江湖 etc.
**Nicknames**: 老頑童 老毒物 賴蛤蟆 黃老邪 老叫化子 etc.
**Idioms**: All 四字成語 found in chi must appear as CJK in hybrid

### Key Translation Conventions
- 九陰真經 → "the Jiuyin Manual"
- 武穆遺書 → "the Book of Wu Mu"
- 桃花島 → "Peach Blossom Island"
- 全真教 → "the Quanzhen Sect"
- 江湖 → "the martial world"
- 無毒不丈夫 → "ruthlessness is the mark of a great man"

---

## Quick-Start for New Chat

1. Upload all 11 handoff files plus episode CSVs
2. Say: "Recreate the 5 pipeline scripts at /home/claude/ from the handoff files, then process episodes N–M with full chi-authority rewriting"
3. The assistant MUST:
   - Create all scripts from uploaded sources
   - For EACH episode: run pipeline.py, READ THE FULL DUMP against chi, write manual overrides fixing meaning/fabrication/address terms, THEN build
   - Run banned-term sweep
   - Present output files

---

## Quality Tiers (Accurate Assessment)

| Episodes | Quality | Description |
|----------|---------|-------------|
| 1–24 | Unknown | Done in prior sessions, not auditable from this transcript |
| 25–26 | **GOLD** | Every sub manually overridden against chi. OCR corrections, yue cross-check, idiom injection, characterisation preserved |
| 27–28 | **SILVER** | Auto-override base + ~200 manual corrections per episode. Key subs rewritten against chi, but ~40% kept auto-generated text |
| 29–31 | **BRONZE** | Auto-override base + lighter manual corrections (~50-100 per episode). Name/title fixes good, but chi-meaning not systematically checked |
| 32–54 | **V2 MECHANICAL** | auto_override_v2.py (CJK injection, idiom injection, address terms) + banned-term fixes. No chi-meaning rewriting. ~30% of subs likely have CHI_MEANING_LOST issues |

**All episodes from 25 onwards need to be re-done to GOLD standard in future sessions.** Only Ep25-26 should be considered final.
