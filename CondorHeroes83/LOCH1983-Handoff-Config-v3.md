# Legend of the Condor Heroes 1983 TVB — Subtitle Pipeline Configuration v3

## CRITICAL: Read ErrorTaxonomy.md and ProcessSpecification-v2.md FIRST.

The single most important rule: **Chi is the authority text. English is a rough draft.** Every subtitle must be read against Chinese and rewritten. Do not preserve the original English as default. Override EVERY sub.

## QUALITY CONTROL — MANDATORY

**One episode per request produces GOLD quality. Two is acceptable but degrades. Three or more causes significant quality loss.**

Before beginning work on any episode, the assistant MUST assess context budget:
- If processing would likely cause quality degradation (e.g. context is already >50% full, or multiple episodes are requested), **STOP and ask the user for instructions** rather than silently producing lower-quality output.
- Say explicitly: "My context is getting full. Processing this episode now would likely produce SILVER rather than GOLD quality. I recommend starting a fresh chat. Shall I proceed anyway, or would you prefer a new session?"
- Never batch 3+ episodes without warning the user about quality trade-offs first.
- If the user insists on batching, acknowledge the quality tier honestly in the delivery message (GOLD/SILVER/BRONZE).

## Project Overview

Producing three SRT subtitle variants per episode from three CSV source tracks (eng, chi_tra, yue):
- `{N}-eng-hybrid.srt` — English with Chinese characters for names/titles/idioms
- `{N}-eng-jyutping.srt` — Full Jyutping romanisation
- `{N}-eng-yale.srt` — Full Yale romanisation

Source CSVs: `/mnt/user-data/uploads/{N}-eng.csv`, `{N}-chi_tra.csv`, `{N}-yue.csv`
Output SRTs: `/mnt/user-data/outputs/`
PersonalNames lookup: `/home/claude/PersonalNamesUpdated.csv` (copy from uploads first)

## Completion Status — Updated 2026-03-30

### GOLD Standard (every sub individually written against chi)
| Episode | Subs | Key Content | Session |
|---------|------|-------------|---------|
| 1 | 446 | Historical narration, 丘處機, 郭嘯天/楊鐵心 | Current |
| 2 | 385 | 江南七怪, 丘處機 wager, 完顏洪烈 reveal, young 郭靖 | Current |
| 15 | 464 | 楊康 identity crisis, 包惜弱 letter, 穆念慈, 黃蓉 vs 七怪, 歐陽克 | Current |
| 16 | 452 | 梅超風 ambush, 黃蓉/郭靖 reconciliation, 穆念慈/包惜弱 revelation, 楊康 武穆遺書, rescue plan | Current |
| 17 | 409 | 楊康/包惜弱 escape, 楊康 boat betrayal, 完顏洪烈 despair, 段天德 confession, 楊康 birthday speech, 穆念慈 fireball | Current |
| 18 | 515 | 包惜弱 poison wine, suicide attempt, becoming nun, 丘處機 captures 楊康, 楊康 oath, 九陰白骨爪 trail, family reunion | Current |
| 19 | 490 | 楊康 final betrayal, 楊鐵心 suicide (滿江紅), 包惜弱 death, 全真教 scenes, 丘處機 teaches internal skills, duel, 問世間情為何物 | Current |
| 29 | 404 | 郭靖 at 桃花島, 周伯通 brotherhood, 黃藥師/黃蓉, 歐陽峰 proposal | Current |

### PENDING — Needs GOLD Processing
| Episode | Status |
|---------|--------|
| 20 | CSVs uploaded, parsed, auto-overridden. NOT chi-authority rewritten. 586 subs. |
| 3–14 | Not yet processed in current pipeline |
| 21–28 | Prior sessions, quality unknown/variable |
| 30–54 | Prior sessions, V2 MECHANICAL only |
| 55–59 | Not yet processed |

---

## Pipeline Steps (per episode)

### Step 1: Parse & Align
```bash
cp /mnt/user-data/uploads/PersonalNamesUpdated.csv /home/claude/
python3 pipeline.py <N>
```

### Step 2: Read the Full Dump — MANDATORY
Read EVERY line of the dump. For each sub, compare eng (column 2) against chi (column 3). Note:
- Fabrications: eng says something chi doesn't → mark for deletion
- Meaning lost: chi has nuance eng flattens → mark for rewriting
- Address terms: chi has 仙姑/前輩/師父/etc → must appear as CJK in hybrid
- Idioms: chi has 四字成語 → must appear in hybrid
- Register: yue (column 4) reveals emotional tone and OCR errors in chi

### Step 3: Auto-Override as Base
```bash
python3 shared_extras.py <N>
python3 auto_override_v2.py <N>
```

### Step 4: MANUALLY Override Every Sub
Write `ep{N}_h_all.json` with a manual override for EVERY sub — not just "critical" ones. Read each sub's chi text and write a fresh English translation. This is what makes GOLD quality.

### Step 5: Add Episode Extras
Add episode-specific romanisation entries to `ep{N}_extra.json` for all CJK that appears in the hybrid overrides.

### Step 6-8: Build, Fix, Validate, Present
```bash
python3 build.py <N>
python3 cjk_fix_v2.py <N>
# Then sed fixes for any remaining CJK in romanised files
# Then banned-term sweep: grep for Old Imp, Old Urchin, Brother Zhou, Rong-er, Guo Jing, Huang Rong
# Then present_files
```

---

## Handoff Files Checklist

Upload ALL of these to start a new session:

### Config & Reference (6 files)
1. `LOCH1983-Handoff-Config-v3.md` — this file
2. `ProcessSpecification-v2.md` — pipeline spec with chi-authority rule
3. `StyleRulings.md` — accumulated style decisions
4. `TrickyInferences.md` — context-dependent judgment calls
5. `ErrorTaxonomy.md` — concrete error examples and fixes
6. `PersonalNamesUpdated.csv` — 72-entry name lookup

### Pipeline Scripts (5 files)
7. `pipeline.py` — CSV parser and alignment
8. `auto_override_v2.py` — deep override with CJK injection + idioms
9. `build.py` — builder with all conversion tables (fix path: PersonalNamesUpdated.csv → `/home/claude/PersonalNamesUpdated.csv`)
10. `shared_extras.py` — episode extras generator
11. `cjk_fix_v2.py` — comprehensive CJK cleanup for romanised files

---

## Style Rulings (Accumulated Eps 1–19, 29)

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
| 蓉兒 | 蓉兒 | Jung-yi | Yuhng-yih |
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
| 梅師姊 | 梅師姊 | Senior Sister Mui | Senior Sister Mui |
| 老賊 | 老賊 | the Old Man | the Old Man |
| 念慈 | 念慈 | Nim-ci | Nihm-chih |
| 穆姑娘 | 穆姑娘 | Miss Muk | Miss Muk |
| 穆姊姊 | 穆姊姊 | Sister Muk | Sister Muhk |
| 楊大叔 | 楊大叔 | Uncle Yeung | Uncle Yeung |
| 楊大嫂 | 楊大嫂 | Mrs Yang | Mrs Yang |
| 阿康 | 阿康 | Aa-Hong | Aa-Hong |
| 大師父 | 大師父 | First Master | First Master |

### Banned Terms (auto-fix after every build)
- "Old Imp" → 老頑童 (hybrid) / Overgrown Child (romanised, NO article)
- "Old Urchin" → same
- "Brother Zhou" / "Brother Zau" / "Brother Jau" → 週大哥 (hybrid) / 週-daai-go (jy) / 週-daaih-go (yl)
- "the Overgrown Child" → "Overgrown Child" (drop article, proper noun)
- "Rong-er" → 蓉兒 (hybrid) / Jung-yi (jy) / Yuhng-yih (yl)
- "Guo Jing" → 郭靖 (hybrid) — never bare Pinyin
- "Huang Rong" → 黃蓉 (hybrid) — never bare Pinyin

### Hybrid CJK Requirements (ALL must be CJK in hybrid, never English)
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

### Recurring CJK Fix Patterns (apply via sed after build)
- `江南七怪` → "the Seven Freaks of Jiangnan"
- `大Master` → "First Master"
- `康,` → "Kang,"
- Bare `鐵心` → "Tiexin"
- `Brother 鐵心` → "Brother Tiexin"
- `Yeung叔叔` → "Uncle Yeung"
- `Yeung兄` → "Brother Yeung"
- Classical Chinese phrases in romanised files → translate to English

---

## Quick-Start for New Chat

1. Upload all 11 handoff files plus episode CSVs
2. Say: "Process episode N with full chi-authority rewriting (GOLD standard)"
3. The assistant MUST:
   - Copy PersonalNamesUpdated.csv to /home/claude/
   - Create all 5 scripts from uploaded sources
   - Run pipeline.py, READ THE FULL DUMP against chi
   - Write manual overrides for EVERY sub
   - Add episode-specific extras
   - Build, CJK fix, validate (zero CJK in romanised, zero banned terms)
   - Present output files
4. **ONE EPISODE PER REQUEST for GOLD quality.** If context is getting full, ASK before proceeding.

---

## Quality Tiers (Accurate Assessment)

| Tier | Description | How to achieve |
|------|-------------|----------------|
| **GOLD** | Every sub individually written against chi. OCR corrections, yue cross-check, idiom injection, characterisation preserved. | One episode per fresh chat, full dump read. |
| **SILVER** | Auto-override base + 20-60% manual fixes for critical subs. Names/titles/idioms correct but many subs keep auto-generated English. | Batching 2 episodes, or context >70% full. |
| **BRONZE** | Auto-override base + <20% manual fixes. Name/title fixes good, chi-meaning not systematically checked. | Batching 3+ episodes, or context nearly full. |
