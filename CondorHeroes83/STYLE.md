# Style — Legend of the Condor Heroes 1983 TVB

Consolidated from: `StyleRulings.md` (all sections, including yue-authority rule and Ep22–23 session decisions), `SubtitleStyle.md` (yue-register guide), and the style/reference tables in `LOCH1983-Handoff-Config-v3.md`.

> **Companion docs:** `PIPELINE.md` (mechanics) · `REFERENCE.md` (tricky cases, errors, Five Greats) · `SESSION-NOTES.md` (episode status + watch list).

---

## Table of Contents

1. [Three Output Variants](#1-three-output-variants)
2. [Priority Chain & The Yue-Authority Rule](#2-priority-chain--the-yue-authority-rule)
3. [Name Rules](#3-name-rules)
4. [Kinship & Address Terms](#4-kinship--address-terms)
5. [Name Rendering Table](#5-name-rendering-table)
6. [Title & Address Conversion Table](#6-title--address-conversion-table)
7. [Hybrid CJK Requirements](#7-hybrid-cjk-requirements)
8. [Key Translation Conventions](#8-key-translation-conventions)
9. [Idiom & Cultural Term Rules](#9-idiom--cultural-term-rules)
10. [Idioms Encountered (Full Catalogue)](#10-idioms-encountered-full-catalogue)
11. [Match the Yue Register](#11-match-the-yue-register)
12. [Translation Voice](#12-translation-voice)
13. [Formatting](#13-formatting)
14. [Conversion Order](#14-conversion-order-critical)
15. [Duration Extension System](#15-duration-extension-system)
16. [Index/Timecode Preservation](#16-indextimecode-preservation)
17. [Output Format](#17-output-format)
18. [Banned Terms](#18-banned-terms-auto-fix-after-every-build)
19. [Recurring CJK Fix Patterns](#19-recurring-cjk-fix-patterns-apply-via-sed-after-build)
20. [Known Recurring Issues](#20-known-recurring-issues)
21. [Anti-Patterns (What NOT to Do)](#21-anti-patterns-what-not-to-do)

---

## 1. Three Output Variants

| Variant | Names | Honorifics | Idioms | File suffix |
|---------|-------|------------|--------|-------------|
| **eng-hybrid** | Chinese characters (郭靖) | Chinese characters (師父) | Chinese inline + English gloss | `-hybrid.srt` |
| **eng-jyutping** | Jyutping romanisation (Gwok Zing) | Natural English (Master) | Faithful English only | `-jyutping.srt` |
| **eng-yale** | Yale romanisation (Gwok Jing) | Natural English (Master) | Faithful English only | `-yale.srt` |

### Variant rules

- **Hybrid**: English prose with CJK for personal names, titles, honorifics, idioms, places, martial arts terms. **No Pinyin.** No English proper nouns where CJK exists.
- **Jyutping / Yale**: Fully romanised. **Zero CJK characters allowed.**

---

## 2. Priority Chain & The Yue-Authority Rule

The English phrasing should mirror the Cantonese spoken dialogue — its register, cadence, and level of detail. Fidelity to what's actually being said is the only goal.

### Priority chain
1. **Yue (HIGH confidence)** — the actual spoken words. Source of register, tone, and specificity. Yue has **phonological authority** (what sound was made) but not semantic authority (what word was meant) — it reaches Claude through Whisper ASR, which can be HIGH-confident on homophones and garble alike.
2. **Chi** — the **semantic authority**. A written translation that sometimes flattens the spoken register but reliably preserves what word was meant. When yue and chi semantically disagree, chi wins by default.
3. **Eng (original)** — a rough draft. Override when it diverges from yue/chi; keep when it's already faithful.

### The Yue-Authority Rule — what it does and doesn't cover

The Yue-Authority Rule is for **register and vividness**, not for **semantic arbitration**. It answers the question *"chi picked a flatter synonym of what yue kept vivid — use yue"*. It does not answer *"yue and chi are different words — pick one"*.

Splitting the rule into its two real jobs avoids the failure mode where a HIGH-confidence yue homophone gets promoted over a correct chi reading (Ep24 sub 344: 推宮換血 chi vs 推功換血 yue — different compounds, not register variants; chi should win).

### Rule A — Register / vividness override (the real Yue-Authority Rule)

**When yue and chi agree semantically but yue is more vivid, more specific, more colloquial, or registers the emotional tone better than chi, yue overrides chi.** This is the narrow, original scope of the rule. The test: *yue's word and chi's word are synonyms* — they refer to the same thing, differing only in colour/register.

Examples:
- **古惑** (yue) overrides **鬼主意** (chi) — both = "cunning/crafty"; yue is the spicier street word
- **淒涼** (yue) overrides **可憐** (chi) — both = "pitiable"; yue is emotionally stronger
- **開心** (yue) overrides **瞑目** (chi) — both = "at peace"; yue is warmer, more colloquial
- **好像** (yue) vs **非常** (chi) — yue preserves the correct certainty level ("seemed" vs "very")
- **百世千孫** (yue) — yue adds obsequious detail chi omits
- **老乞兒** (yue Cantonese) over **老叫化子** (chi Mandarin) — same referent, Cantonese form matches what's actually spoken

For Rule A: **the synonym relationship is the gate.** If yue's word and chi's word aren't substitutable in a dictionary sense, Rule A doesn't apply.

### Rule B — Semantic disagreement defaults to chi

**When yue and chi disagree on *what word was said* (not how vividly the same thing is expressed), chi wins by default.** Yue only overrides chi semantically when there is independent evidence the chi is corrupted — e.g. the eng track confirms yue, or a **prior FULL-completed episode** has established the canonical form yue matches, or chi contains a visible OCR artefact.

The cross-episode clause is strict: it requires a prior FULL episode where the form was actually rendered a specific way, not a form the reviewer expects ought to be canonical. Absent that concrete prior precedent, chi wins. (Ep24 小保 case study: a v2 attempt to "correct" 小保 → 小寶 on canonicality grounds was wrong because no prior FULL episode had established 小寶. When in doubt, chi wins — see `REFERENCE.md` §2.)

The reasoning: yue reaches Claude via Whisper ASR and is subject to homophone errors (宮/功 both `gung1`; 保/寶 both `bou2`). Chi is a written translation — it doesn't have homophone errors. So when yue and chi produce different words that aren't synonyms, the presumption is that yue has an ASR error, not that chi is wrong.

Examples of Rule B in action:
- **推宮換血** (chi) vs **推功換血** (yue HIGH) — not synonyms; different compounds. 功/宮 are Cantonese homophones (`gung1`). Chi wins. (Ep24 sub 344.)
- **四字成語 / named wuxia techniques** generally — these are fixed compounds; a yue variant is almost always a homophone of the real term, not a new term. Default to chi.

Yue may semantically override chi when:
- **Eng confirms yue** (Ep28 Sub 22: yue 每日用一隻毒蝎嚟養大 confirmed eng's "fed poisonous scorpions daily" against a garbled chi).
- **Cross-episode canonicality confirms yue** (a name or term has been rendered consistently in prior FULL episodes and chi has slipped).
- **Chi has a visible OCR artefact** in the specific sub (garbled glyph, clearly wrong homophone in a direction chi can't produce without OCR damage).

### Rule C — The intelligibility gate (pre-requisite for either rule above)

Before either Rule A or Rule B can fire, yue has to be **intelligible** — coherent syntax, parseable as something a character would plausibly say. If yue is garbled (broken syntax, missing particles, scrambled word order, non-words) or semantically incoherent (real words that don't form a sensible sentence), treat it as ASR noise and fall back to chi regardless of confidence tier.

The confidence tier doesn't settle this. Whisper can be HIGH-confident on garbled output; a LOW-tier sub that happens to make sense can still be useful. The reviewer's own read of yue's coherence is the final test.

### Decision procedure for each sub

1. **Is yue intelligible?** (Rule C) No → chi wins, stop.
2. **Does yue semantically agree with chi?**
   - **Yes (same referent, possibly different register)** → go to step 3.
   - **No (different word entirely)** → Rule B: chi wins unless there's independent corroboration for yue (eng, cross-episode, visible OCR). Stop.
3. **Is yue more vivid / colloquial / register-appropriate than chi?** (Rule A)
   - Yes → use yue.
   - No → chi is already fine, keep chi.

### Special cases

- **臭要飯的** (chi OCR) → actual Cantonese is **死乞兒** (damned/stupid beggar). Both chi and yue ASR transcribe this incorrectly. Render as **"stupid beggar"** in all three variants (not CJK in hybrid).
- **Cantonese phonological/dialect variant** (e.g. 家散人亡 vs 家破人亡) — yue's form is the actually-spoken Cantonese variant of the same idiom. Keep yue. This is Rule A applied at the dialect-form level: same referent, yue matches what the character actually said. (Parallels 老乞兒 over 老叫化子: when chi and yue are the same thing in different dialect clothing, yue wins.)
- **抵死** (yue: deserve to die, Cantonese colloquial) — Rule A applies when chi flattens this to a tamer form. Render the register in English ("damn well deserves it", "serves him right", depending on context); **do not** use CJK-with-gloss. The CJK+gloss format is reserved for 四字成語, poetic couplets, and literary phrases — not for colloquial slang where English can carry the register alone. (See §9.)

### Cross-check Mandarin ALWAYS
- Original English often flattens nuance from the Chinese.
- Compare every sub against chi column for lost meaning.
- Example: Ep20 sub 6 — English missed an entire clause present in Mandarin.

### Use Cantonese (yue) for register/tone
- Yue track guides emotional register, colloquial vs formal tone (Rule A territory).
- If yue sounds blunt/casual, English should match.
- If yue sounds formal/poetic, English should elevate.
- But **not** for semantic arbitration — that's Rule B's domain, and chi wins there.

---

## 3. Name Rules

### 阿-prefix (CRITICAL)
- **ONLY** in direct address (vocative): "阿靖!" when calling someone.
- **NEVER** in object/possessive/descriptive context: "real father" not "real 阿爹" (descriptive modifier = object).
- Example: "阿爹!" (calling out ✓) vs "your father's temper" (reference ✓) vs "your 阿爹's temper" (WRONG ✗).

### 靖哥哥 / 蓉兒 romanisation
- Jyutping: **Zing-gogo / Jung-ji** (NO extra dash: `gogo` not `go-go`).
- Yale: **Jing-gogo / Yuhng-yi** (same rule).
- Hybrid: Chinese characters always.

### 七仔 vs 老七
- 洪七公 calls himself **七仔** in Cantonese (NOT 老七).
- Use 七仔 in hybrid **only** when dialogue explicitly says 老七/七仔.
- Romanised: "Little Seven" (not "Old Seven").
- Do **NOT** use 七仔 as a general substitute for 洪七公 elsewhere.
- Flag every occurrence for user checking.

### Rong-er must NEVER appear in hybrid
- Always **蓉兒** in hybrid. "Rong-er" is Pinyin leakage.

### Compound names convert before bare characters
- **梅師姊** → "Senior Sister Mui" must convert before bare 梅.
- **歐陽公子** → "Young Master Au-Joeng" before bare 歐陽.
- See §14 Conversion Order for the full rule.

---

## 4. Kinship & Address Terms

### 娘親 rule
- Hybrid uses **娘親** (not 娘) — Cantonese-preferred form. Renders as "mother" in romanised.
- Use bare 娘親 as vocative: "娘親!" "娘親, I'm home." English possessives ("my 娘親", "his 娘親") are fine in descriptive contexts — 娘親 is "mother", not "my mother", so there's no doubled possessive.

### Descriptive kinship terms
- **養父 / 義父** → "foster father" ALWAYS in all three variants.
- Never keep Chinese for descriptive kinship (養母 → "foster mother", etc.).

### 阿爹 in romanised files
- Converts to **"Father"** (not romanised).

### The 老伯 rule
When someone is ADDRESSED as 老伯 (vocative), keep **老伯** in CJK in hybrid. Don't convert to "sir" or "old man".
- Example: "Don't worry, 老伯." NOT "Don't worry, sir."

### The 大宋 / 金 rule (dynasty names stay CJK in hybrid)
- "There is hope for **大宋**!" NOT "There's hope for the Song dynasty."
- "The **金** are coming" NOT "The Jins are coming."
- Same for 宋, 蒙古, 金國. Romanised: "the Song" / "Mongolia" / "Jin".

---

## 5. Name Rendering Table

Canonical renderings for recurring name/nickname forms. Personal names proper live in `PersonalNamesUpdated.csv` — the table below captures nicknames and compound forms that need special handling.

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
| 黃小邪 | 黃小邪 | Little Heretic Wong | Little Heretic Wong |
| 死老邪 | 死老邪 | damned Old Heretic | damned Old Heretic |
| 老邪 | 老邪 | Old Heretic | Old Heretic |
| 黃島主 | 黃島主 | Island Lord Wong | Island Lord Wong |
| 藥師兄 | 藥師兄 | Brother Joek-si | Brother Yeuhk-si |
| 七兄 | 七兄 | Brother Seven | Brother Seven |
| 阿衡 | 阿衡 | Aa-Hang | Aa-Hahng |
| 歐陽世兄 | 歐陽世兄 | Brother Au-Joeng | Brother Au-Yeung |
| 歐陽兄 | 歐陽兄 | Brother Au-Joeng | Brother Au-Yeung |
| 歐陽先生 | 歐陽先生 | Mister Au-Joeng | Mister Au-Yeung |
| 歐陽公子 | 歐陽公子 | Young Master Au-Joeng | Young Master Au-Yeung |
| 歐陽叔叔 | 歐陽叔叔 | Uncle Au-Joeng | Uncle Au-Yeung |
| 父王 | 父王 | Royal Father | Royal Father |
| 閻王爺 | 閻王爺 | King of Hell | King of Hell |
| 梅師姊 | 梅師姊 | Senior Sister Mui | Senior Sister Mui |
| 老賊 | 老賊 | the Old Scoundrel | the Old Scoundrel |
| 念慈 | 念慈 | Nim-ci | Nihm-chih |
| 穆姑娘 | 穆姑娘 | Miss Muk | Miss Muk |
| 穆姊姊 | 穆姊姊 | Sister Muk | Sister Muhk |
| 楊大叔 | 楊大叔 | Uncle Yeung | Uncle Yeung |
| 楊大嫂 | 楊大嫂 | Mrs Yang | Mrs Yang |
| 阿康 | 阿康 | Aa-Hong | Aa-Hong |
| 大師父 | 大師父 | First Master | First Master |
| 黃姑娘 | 黃姑娘 | Miss Wong | Miss Wong |
| 郭大哥 | 郭大哥 | Brother Gwok | Brother Gwok |
| 洪師父 | 洪師父 | Master Hung | Master Huhng |
| 洪前輩 | 洪前輩 | Senior Hung | Senior Huhng |
| 黃前輩 | 黃前輩 | Senior Wong | Senior Wong |
| 黃老伯 | 黃老伯 | Old Uncle Wong | Old Uncle Wong |
| 老伯 (vocative) | 老伯 | old uncle | old uncle |
| 女魔頭 | 女魔頭 | she-demon | she-demon |
| 博將軍 | 博將軍 | General Bo | General Bo |
| 赤將軍 | 赤將軍 | General Chi | General Chi |
| 彭寨主 | 彭寨主 | Stockade Master Pang | Stockade Master Pahng |
| 丘道長 | 丘道長 | Taoist Jau | Taoist Yau |
| 馬道長 | 馬道長 | Taoist Maa | Taoist Ma |
| 王道長 | 王道長 | Taoist Wong | Taoist Wong |
| 駙馬 / 駙馬爺 | 駙馬 / 駙馬爺 | Prince Consort | Prince Consort |
| 金刀駙馬 | 金刀駙馬 | the Golden Prince Consort | the Golden Prince Consort |
| 晚輩 | 晚輩 | this junior | this junior |
| 後輩 | 後輩 | junior | junior |
| 小王爺 | 小王爺 | the Young Prince | the Young Prince |
| 王子 | 王子 | the Prince | the Prince |
| 公主 | 公主 | Princess | Princess |
| 玄風 (bare) | 玄風 | Jyun-fung | Yuhn-fung |
| 陳玄風 | 陳玄風 | Can Jyun-fung | Chahn Yuhn-fung |
| 程姑娘 | 程姑娘 | Miss Cing | Miss Ching |
| 瑤迦 (程瑤迦) | 瑤迦 | Jiu-gaa | Yiu-ga |
| 冠英 (陸冠英) | 冠英 | Gun-jing | Gun-ying |
| 孫不二 | 孫不二 | Syun Bat-ji | Syun Bat-ji |
| 顏烈 | 顏烈 | Ngaan Lit | Ngaahn Liht |
| 小靖 | 小靖 | Siu-Zing | Siu-Jing |

Notes on specific entries:
- **駙馬爺** — 蓉兒 uses it sarcastically toward 郭靖.
- **晚輩 / 後輩** — humble self-reference / peer reference when addressing a 前輩.
- **女魔頭** — 梅超風's own self-description in Ep23.
- **顏烈** — 完顏洪烈's cover alias in the Ep1 pilot / Ep2 醉仙樓 scene. Also present as the fuller address form 顏大爺 in Ep5's 蒙古-camp arc. Now in `PersonalNamesUpdated.csv`.
- **小靖** — young-child diminutive for 郭靖, used by 李萍 in the Ep3 蒙古 widow scenes. Distinct from the vocative **阿靖** (CSV entry: Aa-Zing / Aa-Jing).

---

## 6. Title & Address Conversion Table

Title and address conversions in romanised files (hybrid keeps CJK):

| Chinese | Jyutping / Yale English |
|---------|-------------------------|
| 師父 | Master |
| 師兄 | Senior Brother |
| 師弟 | Junior Brother |
| 師姊 | Senior Sister |
| 師妹 | Junior Sister |
| 師叔 | Martial Uncle |
| 師姑 | Martial Aunt |
| 大哥 | Big Brother |
| 前輩 | senior |
| 七公 | Seven Elder |
| 幫主 | the Chief |
| 莊主 | Manor Lord |
| 少莊主 | Young Manor Lord |
| 島主 | Island Lord |
| 祖師爺 | Grand Teacher |
| 仙姑 | Immortal Maiden |
| 王爺 | Your Highness / the Prince |
| 小王爺 | the Young Prince |
| 王子 | the Prince |
| 王妃 | the royal concubine |
| 公主 | Princess |
| 閻王爺 | the King of Hell |
| 老叫化子 | Old Beggar |
| 老乞兒 | Old Beggar (yue) |
| 乞兒仔 | beggar boy (yue) |
| 乞兒窩 | beggar's den (yue) |
| 阿彌陀佛 | Amitabha |

---

## 7. Hybrid CJK Requirements

**All of the following MUST be CJK in hybrid — never English.**

### Names
All character names from `PersonalNamesUpdated.csv`.

### Titles
師父 · 師兄 · 師弟 · 師姊 · 師妹 · 師叔 · 師姑 · 前輩 · 莊主 · 少莊主 · 幫主 · 祖師爺 · 仙姑 · 駙馬爺 · 王爺 · 小王爺 · 王妃 · 大哥 · 七公 · 島主 · 老伯 · 少爺 · 弟子 · 長老 · 公子

### Address
父王 · 阿爹 · 爹 · 娘親 · 靖哥哥 · 蓉兒 · 靖兒 · 康兒 · 阿靖 · 阿康 · 週大哥 · 黃島主 · 藥師兄 · 歐陽世兄 · etc.

### Places
桃花島 · 桃花陣 · 白駝山 · 歸雲莊 · 牛家村 · 蒙古 · 臨安 · 大理 · 長白山 · 江南 · 岳王廟 · 翠紅樓 · 獅子林 · 山神廟 · 望江樓 · 清溪別院 · etc.

### Sects
全真教 · 丐幫 · 鐵掌幫 · 梅花五毒 · etc.

### Dynasties / countries
大宋 · 宋 · 金 · 金國 · 蒙古

### Terms
九陰真經 · 武穆遺書 · 降龍十八掌 · 蛤蟆功 · 左右互搏 · 空明拳 · 九陰白骨爪 · 打狗棒法 · 易筋鍛骨篇 · etc.

Note: named techniques and canonical texts stay CJK. **Generic wuxia vocabulary — 武功 · 武林 · 江湖 · 內力 · 內功 · 輕功 · 功力 — stays English** (see "What does NOT get CJK" below).

### Nicknames
老頑童 · 老毒物 · 賴蛤蟆 · 黃老邪 · 老乞兒 · etc.

Note: use the Cantonese **老乞兒** in hybrid, not the Mandarin **老叫化子**. If the chi track transcribes as 叫化子, override to 乞兒 (Rule A — matches what the Cantonese speaker actually says). See §11 and REFERENCE §2.

### Idioms
All 四字成語 found in chi must appear as CJK in hybrid. See §10 for the catalogue.

### Title + name compounds (always CJK as a unit)
岳老伯 · 岳王爺 · 岳大叔 · 黃大叔 · 洪師父 · 黃前輩 · 黃老伯 · etc. NOT "Uncle Yue" / "Uncle Wong" / etc.

### Temple/place full names (always CJK)
岳王廟 · 翠紅樓 · 獅子林 · 山神廟 (not "Yue's Temple" etc.).

### Address terms in direct speech
老伯 · 少爺 · 弟子 · 長老 · 幫主 · 公子 — keep CJK when spoken.

### Standalone idioms
劫數難逃 (only 四字成語 with cultural weight that passes §10's plain-prose test). All other standalone idioms go English in hybrid.

### Five Greats (五絕) epithets
東邪 · 西毒 · 南帝 · 北丐 · 中神通 — canonical wuxia epithets naming the five supreme masters. Keep CJK in hybrid; see §10 for romanised renderings.

### What does NOT get CJK in hybrid

The CJK requirements above are exhaustive — if a phrase isn't on one of these lists, it stays in English. Specifically:

- **Generic wuxia vocabulary** — **武功** (martial arts), **武林** (the martial world), **江湖** (the martial world), **內力** (internal strength), **內功** (internal energy), **輕功** (qinggong / lightness skill), **功力** (internal force). These are common-noun wuxia-domain vocabulary that English carries cleanly; CJK here clutters without adding cultural weight. **Named techniques and canonical texts** (九陰真經, 降龍十八掌, 空明拳, 打狗棒法, etc.) remain CJK — they're proper-noun-like. Rule of thumb: if the term is "a martial art" rather than "*the* such-and-such martial art", it goes English.
- **Common-noun references using 俗 beggar-terms** — render as English:
  - **叫化子 / 乞兒 / 乞丐** → "beggar(s)". When keeping CJK in hybrid is warranted (e.g. 洪七公 self-naming), use the Cantonese **乞兒**, never 叫化子. The chi track often transcribes the Mandarin form; override to 乞兒 per Rule A.
  - **禁宮** → "the palace" / "the forbidden palace" (common-noun reference to imperial quarters).
- **Colloquial insult compounds** (intensifier + common noun) — render as English:
  - **臭丫頭** → "stinking girl" / "damned girl"
  - **死丫頭** → "damned girl"
  - **死乞兒** → "damned beggar" / "stupid beggar"
  - **臭乞兒** → "stinking beggar"
  - **臭要飯的** (chi OCR for 死乞兒) → "stupid beggar" (see §2 special cases)
  - **王八蛋** → "bastard" / "scoundrel"
  - Rule: **intensifier + common-noun-insult** (臭X / 死X / 老X where X is a common noun) goes English. Contrast with intensifier + proper-nickname (**死老邪**, **老毒物**, **老頑童**) which stays CJK because X is a proper nickname.
- **Colloquial slang and intensifiers** (抵死, 好彩, 乜嘢, 放肆, etc.) — render the register in English, no CJK.
- **Everyday vocabulary** that differs between Cantonese and Mandarin but isn't a proper noun, title, idiom, or term-of-art — Rule A in §2 picks which form to use, but the rendering is English.
- **Descriptive common-noun metaphors that sound idiomatic** — phrases that are Chinese-literary-sounding but are actually common-noun descriptors, not fixed compounds. Test: does the English rendering work as a plain English noun phrase? If yes, it's a descriptor, not an idiom.
  - **情蛇** ("love snake") — metaphor for a lecherous man; render as English ("lecher" / "that snake").
  - **一流高手** / **一流絕頂高手** ("first-rate expert" / "supreme master") — rank descriptors; render in English.
  - General **X+高手** / **X+高人** / **X+蛇** / **X+獸** / **X+物** compounds where X is an adjective rather than a proper qualifier. Contrast with **塞外高人** (CJK OK — 塞外 is a specific geographic qualifier, fixed phrase) and **老毒物** (CJK OK — it's a nickname for 歐陽峰). See §10's admission gate.
- **Emotional interjections** — match the tone in English.

Rule of thumb: CJK in hybrid is for content the English *can't* fully carry — proper names, titles of address, specific places, fixed idioms with cultural weight, classical allusions, literary phrases, named techniques. **Generic descriptors rendered in Chinese are not "more faithful"; they're noise.** When English does the job, use English. See §9 for the CJK+gloss format's scope, and §10's admission gate for what counts as a catalogue-worthy idiom.

---

## 8. Key Translation Conventions

Canonical English renderings for high-frequency terms. **This table gives the romanised rendering.** For hybrid, consult §7:
- **CJK in hybrid** for the named-technique / canonical-text / proper-noun entries (九陰真經, 降龍十八掌, 桃花島, etc.)
- **English in hybrid** for the generic wuxia vocabulary at the bottom of the table (武功, 武林, 江湖, 內力, 內功, 輕功, 功力) — see §7 "What does NOT get CJK".

| Chinese | Romanised English |
|---------|-------------------|
| 九陰真經 | the Jiuyin Manual |
| 九陰白骨爪 | the Jiuyin Baigu Claw |
| 武穆遺書 | the Book of Wu Mu |
| 降龍十八掌 | the Eighteen Dragon-Subduing Palms |
| 空明拳 | the Hollow Fist |
| 七十二路空明拳 | the 72 Forms of the Hollow Fist |
| 打狗棒 | the Dog-Beating Staff |
| 打狗棒法 | the Dog-Beating Staff Technique |
| 三十六路打狗棒法 | the 36 Forms of the Dog-Beating Staff |
| 易筋鍛骨篇 | the Muscle-Forging Bone-Tempering Chapter |
| 桃花島 | Peach Blossom Island |
| 全真教 | the Quanzhen Sect |
| 丐幫 | the Beggar Sect |
| 白駝山 | White Camel Mountain |
| 蒙古 | Mongolia |
| 金國 | Jin |
| 大宋 / 宋 | the Song |
| 望江樓 | Wangjiang Inn |
| 清溪別院 | the Riverside Manor |
| 江南 | Gong-naam (jy) / Gong-naahm (yl) |
| 積翠亭 | Zik-ceoi Pavilion (jy) / Jik-cheui Pavilion (yl) |
| 梅花樁 | the plum-blossom posts |
| 梅花陣 | the Plum Blossom Formation |
| 奇門八卦 | the Eight Trigram Formation |
| 奇門八卦之術 | the art of the Eight Trigram Formation |
| 神龍擺尾 | Divine Dragon Swishes Its Tail |
| 碧海潮生曲 | the Blue Sea Tide Melody |
| 文鬥 / 武鬥 | contest of arts / contest of arms |
| 內子 | my wife |
| 岳父大人 | father-in-law |
| 叔叔 | Uncle |
| 無毒不丈夫 | ruthlessness is the mark of a great man |
| 雪蓮玉露丸 | the Snow Lotus Jade Pill |
| 雪蓮 | Snow Lotus |
| 梅花五毒 | the Five Plum Blossom Venoms |

---

## 9. Idiom & Cultural Term Rules

### NEVER flatten imagery to an abstract moral (default)

When rendering an idiom in English, preserve the specific image or concept rather than collapsing to a generic abstract moral.

- **不見棺材不流淚** → "won't cry till you see the coffin" — NOT "won't believe till it's too late". The coffin image is the point; don't paraphrase it away even when the phrase is rendered fully in English.
- **以牙還牙** → "an eye for an eye" — 1:1 map; render plainly in English.
- **狗咬呂洞賓** → "biting the hand that feeds you" — concept maps cleanly; render plainly in English.

Rule of thumb: use a Western equivalent only when the *meaning* maps 1:1; preserve the specific imagery when it's the point. Note that this applies to English rendering in both hybrid and romanised — most idioms should render cleanly in English without CJK per §10's plain-prose test. Only §10-catalogued phrases keep CJK in hybrid.

### Paired / couplet proverbs — render each half literally (v16 Ep1 rule)

When chi carries a classical **paired proverb** (two balanced halves joined by a comma, typically 6+6 or 4+4 characters, each half a complete idiom-image), render **each half literally**; do not collapse both halves to a single abstract English equivalent.

- **天有不測風雲, 人有旦夕禍福** → "the heavens hold unforeseen storms, fortunes shift in a day" — NOT "disaster strikes without warning" (the single-abstract collapse discards both halves' imagery in favour of the shared abstract moral).
- **有福同享, 有難同當** → "share fortune together, share hardship together" — NOT "through thick and thin".
- **不怕一萬, 只怕萬一** — already a STYLE §10 catalogue entry; keeps its imagery ("not afraid of the ten thousand, only the one-in-ten-thousand") rather than collapsing to "better safe than sorry" alone.

Cue for this rule: chi presents two balanced halves separated by a comma where each half has its own imagery (storm/fortune, fortune/hardship, ten-thousand/one-in-ten-thousand). If either half would make sense on its own as an independent proverb, render both halves literally. The test: does the English rendering preserve the rhetorical parallelism that made the source a couplet? If it doesn't, the rendering is too abstract — rewrite to match the pair structure.

This is the pattern-specific form of the general §9 rule above, called out because paired proverbs are easier to collapse-by-accident than standalone 四字成語 — the second half reads as "redundant elaboration" to an English-trained eye, which tempts the reviewer to drop it in favour of a single abstract gloss. Don't.

### Hybrid: keep Chinese characters inline

**Preferred format: `中文成語 (English gloss)`** (Chinese idiom first, then the English gloss in parentheses.) This format is universal — use it for 四字成語, couplet idioms, classical allusions, and any entry in §10 that keeps CJK in hybrid.

**Scope of the CJK+gloss format.** Reserve this format for 四字成語, poetic couplets, classical allusions, and literary phrases where the Chinese form carries meaning the English gloss alone can't fully convey. **Do not** use it for:
- Colloquial slang or intensifiers (抵死, 好彩, 乜嘢) — render the register in English
- Everyday vocabulary that happens to differ between Cantonese and Mandarin — use Rule A to pick the form, render in English
- Emotional interjections — match the tone in English

The CJK+gloss format's job is to preserve cultural/literary content the English can only approximate. When English can do the full job on its own (as it can for most colloquial register), skip the CJK and just render cleanly in English. CJK-inclusion is not a badge of fidelity — over-using it clutters the hybrid and trains the reader to skim past the Chinese.

| RIGHT | WRONG |
|-------|-------|
| 狗眼看人低 (who told him to look down on us)! | He looked down on us. 狗眼看人低. |
| 劫數難逃 (I fear my time has come) | I fear this is my fate — I won't escape it. |
| He damn well deserves it | He deserves it — 抵死 |

**Rules:**
- **Never gloss an idiom twice** (once in Chinese AND as a separate English expansion). The English in parentheses IS the gloss; don't also write the English meaning outside the parens.
- **Idiom on its own is fine** — if the sub is just an exclamation and the idiom is §10-catalogued (e.g. "邪中有三分正!" or "泰山北斗!"), the CJK alone is acceptable. For non-catalogued idioms, render in English.
- **Don't inject idioms into subs where they don't appear in chi.** Only include idioms that are actually in the source text for that sub.

### Romanised: faithful English translation only
- No Chinese characters in jyutping/yale files.
- The idiom becomes its English rendering.

### Wuxia terms in hybrid
- **Named techniques** stay Chinese in hybrid: **降龍十八掌** / "the Eighteen Dragon-Subduing Palms" · **九陰白骨爪** / "the Jiuyin Baigu Claw" · **空明拳** / "the Hollow Fist" · **打狗棒法** / "the Dog-Beating Staff Technique" · **九陰真經** / "the Jiuyin Manual".
- **Generic wuxia nouns go English in hybrid** (see §7): 武功 ("martial arts") · 武林 ("the martial world") · 江湖 ("the martial world") · 內力 ("internal strength") · 內功 ("internal energy") · 輕功 ("qinggong") · 功力 ("internal force").

---

## 10. Idioms Encountered (Full Catalogue)

Settled renderings for idioms that earn CJK+gloss treatment in hybrid. In hybrid, keep the Chinese; in romanised, use the rendering below.

### What qualifies for this catalogue (admission gate)

Not every four-character Chinese phrase is a catalogue-worthy idiom. **Before adding a new entry, check that the phrase meets at least one of these criteria:**

1. **Fixed 四字成語** — a classical compound listed in standard idiom dictionaries, with a stable English rendering that preserves imagery the English can only approximate.
2. **Classical allusion** — references a specific classical source (e.g. **秦晉之好** from 左傳, **泰山北斗** from 史記, **人之將死, 其言也善** from 論語).
3. **Named proverb or 俗語** with cultural weight the English can't fully carry.
4. **Poetic / elegiac couplet** from an identifiable literary tradition (e.g. 曹操 短歌行 couplets, the Dragon-chant quartet).

**The primary test — the plain-prose rule.** Strip the CJK from the hybrid entry and read only the English rendering. *If it stands alone as plain prose without losing imagery or cultural weight, it does not belong in this catalogue — a consistency ledger is not reason enough to keep it.* Render in English, no CJK in hybrid. This catalogue is only for phrases whose Chinese form carries something the English gloss can't fully convey on its own: a specific image ("biting the hand" vs "狗咬呂洞賓"'s named 呂洞賓), a classical source, a poetic structure, or a culturally-weighted register. Everything else goes English.

**Descriptive common-noun phrases are NOT catalogue-worthy, even if they sound literary.** Test: strip the CJK and read the English rendering. If it works as a plain English noun phrase ("love snake" / "a first-rate expert" / "a top master" / "a strange creature"), it's a descriptor, not an idiom — render in English, no CJK in hybrid. Examples of what fails the admission gate:
- **情蛇** ("love snake" — descriptive metaphor, not a named creature or fixed compound)
- **一流高手** / **一流絕頂高手** ("first-rate expert" — rank descriptor; use "a top master", "a supreme master" in English)
- General X+高手 / X+高人 compounds where X is an adjective rather than a proper-noun qualifier

Phrases that **do** pass the gate (for reference): **塞外高人** passes as a set classical phrase meaning specifically "masters from beyond the frontier" (the 塞外 qualifier is geographic, not a general adjective); **一代宗師** passes as a fixed four-character compound with specific wuxia-world meaning ("master of a generation"). When in doubt, err toward English — the catalogue should stay tight.

### Catalogue entries

- **人之將死, 其言也善** — "When a man is dying, his words are kind" (hybrid: `人之將死, 其言也善 (when a man is dying, his words are kind)`). 論語 classical allusion.
- **婦人之仁** — "a woman's soft-heartedness". Classical compound; the rendering retains the distinctive gendered image.
- **劫數難逃** — "cannot escape one's fate". Buddhist 劫數 imagery; cultural weight English can't fully carry.
- **不怕一萬, 只怕萬一** — "better safe than sorry" (hybrid couplet: *"不怕一萬, 只怕萬一 (better safe than sorry)."*). Classical couplet; the ten-thousand / one-in-ten-thousand parallelism is the point, not the gloss.
- **狗眼看人低** — "look down on others". Named 俗語; the dog-eye image is the idiom.
- **邪中有三分正, 正中帶七分邪** — "The heretical are three parts righteous; the righteous are seven parts heretical!" (黃藥師's couplet about 蓉兒). Poetic couplet with named speaker. **Keep Chinese in hybrid; English translation only in romanised. Do NOT double-print Chinese + English in romanised.**
- **秦晉之好** — "the bond of 秦晉" (hybrid) / "the bond of Chun-Zeon" (jy) / "the bond of Chun-Jeun" (yl). Classical allusion (左傳) to the marriage alliance between the states of 秦 and 晉. These are idioms-of-reference, not modern place names.
- **泰山北斗** — "the authority of the martial world" (standard rendering). Classical allusion (史記): the authoritative figures in a field. **Pairing note:** do not write "泰山北斗 of 武林" in hybrid — 武林 goes English ("the martial world") per §7, and because 泰山北斗's rendering already contains "martial world", combining them in the same phrase produces "of the martial world of the martial world" duplicate in romanised. Drop 武林, rewrite (e.g. "...of our age", "...of our time"), or use an alternative rendering ("the Mount Tai of the Northern Dipper"). Observed twice: Ep30, Ep33 sub 356.

### Five Greats (五絕) epithets

The canonical wuxia epithets naming the five supreme masters of the 華山論劍. Fixed compounds with specific named referents (see REFERENCE.md §6 for the framework table); keep CJK in hybrid, render per the table below in romanised. These are epithets — proper-noun titles — not descriptions, and the Chinese form carries the literary-canonical register the English gloss alone cannot.

- **東邪** — "the Eastern Heretic" (黃藥師). Eastern cardinal + 邪 "heretic/unorthodox" epithet.
- **西毒** — "the Western Poison" (歐陽峰). Western cardinal + 毒 "poison/venom" epithet.
- **南帝** — "the Southern Emperor" (一燈大師, 段智興). Southern cardinal + 帝 "emperor" epithet.
- **北丐** — "the Northern Beggar" (洪七公). Northern cardinal + 丐 "beggar" epithet.
- **中神通** — "the Central Divine" (王重陽). Central position + 神通 "divine power" epithet.

Usage notes:
- Epithets appear both standalone ("東邪 黃藥師, only has one daughter") and as catalogue pairings ("東邪西毒, 南帝北丐"). Both forms keep CJK in hybrid.
- When a character refers to another by epithet rather than name (e.g. 蓉兒 calling her father "東邪" in third person), preserve the epithet form — it carries a different register than "my father" or "黃藥師".
- 中神通 is rare post-華山論劍 (王重陽 died before the series proper); most episodes pair only the four living Greats.
- For 一燈大師 specifically: the series uses both 南帝 (pre-ordination epithet) and 一燈 (post-ordination monastic name) — track which form the scene uses and preserve it.

### Classical laments / elegiac verse
- **想逝者之不罪兮, 惜形中之載道** / **天蓋高而無階, 懷此恨其最苦** (Ep28) — 陸乘風's lament for 瑤迦. Format as `CJK (English gloss)` — both halves on the same line if they fit, otherwise one couplet-half per line. Glosses: "my love runs deep, the dead beyond recall" / "Heaven is high but has no stair; this sorrow cuts deepest".
- **天長地久, 人生幾何** / **譬如朝露, 去日苦短** (Ep33 subs 173–174) — 黃藥師's lament for the supposedly-dead 蓉兒. Adapted from 曹操 短歌行. Format as `CJK (English gloss)` on the same line. Glosses: "Heaven and Earth endure; how brief a human life" / "like morning dew, the days gone are bitter and short".
- **林升 題臨安邸** (Ep20 full + Ep1 compressed form — two-ep confirmed) — Southern Song lament over the occupied capital. Quatrain format: four lines, each `CJK (English gloss)` on the same line. Canonical text: 山外青山樓外樓 / 西湖歌舞幾時休 / 暖風熏得遊人醉 / 直把杭州作汴州. Glosses: "beyond the green hills, more green hills; beyond the tower, yet another tower" / "when will the song and dance on 西湖 ever cease?" / "the warm breeze lulls the travellers drunk" / "they take 杭州 for 汴州". Ep1 uses a compressed two-line form invoking lines 2+4 as narration backdrop; render only the two lines that chi carries.
- **滿江紅 quatrain** (Ep1 first firing, Ep15+ 武穆遺書-arc reappearance expected) — 岳飛's 靖康恥 quatrain. Format as `CJK (English gloss)` on the same line, one quatrain-line per sub. Already a first-firing reference; established format under v15 (migrated to parenthetical gloss under v18).

### 九陰真經 quotations (from 周伯通's slap-memorise teaching, Ep29+)
- **天之道, 損有餘而補不足** — "Heaven's way: take from the surplus and replenish the lack". Adapted from 道德經 77. Hybrid: `天之道, 損有餘而補不足 (Heaven's way: take from the surplus and replenish the lack)` on the same line, or split across two lines if it doesn't fit; romanised: English only.
- Related meditation-text fragments (任督二脈, 氣聚丹田, 百會, 大椎, 足少陽/足少陰, 十二經筋) — render per the meditation/qi subsection below.

### 內功 / 內力 / 內傷 family
- **內力** — "internal strength"
- **內功** — "internal energy"
- **內傷** — "internal injury"

### Meditation / qi
- **氣聚丹田** — "Qi gathers at the dantian"
- **歸元丹田** — "return to the dantian"
- **神注印堂** — "Spirit focuses at the yintang"
- **任督二脈** — "the Ren and Du meridians"
- **靈台穴** — "the Lingtai point"
- **曲池穴** — "the Quchi point"
- **會陰** — "Huiyin"
- **陰柔** — "yin-soft"

### Dragon chant quartet — Ep22 subs 428–431
In hybrid, format as `CJK (English gloss)` on the same line, one line per chant-line. In romanised, English translation only (do not duplicate).

- 去似天龍雲飛躍 → "Go like a heavenly dragon soaring through clouds"
- 收似降龍穩深沈 → "Retreat like a subdued dragon, steady and deep"
- 腳似飛龍騰萬里 → "Kick like a flying dragon spanning ten thousand li"
- 拳似怒龍翻四海 → "Punch like an angry dragon overturning the four seas"

---

## 11. Match the Yue Register

The English should feel like the yue/chi — not like smoothed-out English prose.

### Rules
- **Translate what's said, not more.** If the Cantonese is three words, the English should be comparably brief — not because "short is better" but because that's what the character actually said. Don't pad with filler the speaker didn't use.
- **Don't summarise away register.** If yue says "你這種人不見棺材不流淚" (elaborate insult), keep the elaboration. Don't compress to "You'll regret it." The length is the point.
- **Don't invent emphasis the source doesn't have.** If yue/chi is a flat statement, write a flat statement. Don't add exclamation marks, intensifiers, or dramatic phrasing.

### Examples — matching yue register

| Yue says | RIGHT | WRONG |
|---|---|---|
| 去叫東西吃我很快就回來的 (casual, quick) | Go order some food first. I'll be right back. | Why don't you go in and order something to eat first? I'll be back shortly. |
| 又是你這臭要飯的 (chi OCR; actual yue is 死乞兒 = damned beggar) | You again, you stupid beggar! | You again, you stinking beggar! |
| 大宋有救了 (short excited) | There is hope for 大宋! | 大宋 is saved! |
| 如果大宋有多位岳王爺嘅話咁就有救啦 (full conditional) | If we had another 岳王爺, there'd be hope. | If the great Song had a few more men like 岳王爺, there'd still be hope! |
| 我搜晒翠紅樓咩都冇 (搜晒 = exhaustive; 咩都冇 = absolutely nothing) | I searched every corner of 翠紅樓. There was nothing there. | I searched all over 翠紅樓 just now but found nothing. |
| 做人千萬不要太好心, 好心遭雷劈 (千萬 = emphatic; proverbial) | It's extremely important that a person isn't too kind. Good hearts get struck by lightning — 好心遭雷劈. | Don't be too kind. 好心遭雷劈. |

---

## 12. Translation Voice

### Match source register, don't normalise to English
If the Cantonese is clipped, the English is clipped. If it's formal, the English is formal. If it's awkward or stilted in the source, it can be awkward in English — that's characterisation.

- 這麼緊張幹甚麼 → "Why so uptight?" (casual dismissal — match it)
- 不知道誰亂來 → "Who's the one trying something funny?" (accusatory question — match it)
- 不去了 → "Not going anymore" (abrupt — match it)
- 小姑娘過來放了我們 → "Miss, please come let us go" — NOT "Have mercy!" (render the actual words)

### Don't over-explain
- If chi says **大宋有救了**, write "There is hope for 大宋!" Don't expand to "There's hope for the Song dynasty now."
- If chi says **武穆遺書**, write 武穆遺書. Don't add "the Book of Wu Mu" in the same sub — the viewer either knows or picks it up.
- Trust the viewer. Subtitles inform; they don't lecture.

### Register matches character
Character voices reinforced across the Ep22/23 FULL session (fuller character notes in `REFERENCE.md`):

- **蓉兒** — bratty, playful, sharp. Short sentences. Bratty-but-loving-underneath. *"Pray till next year for all I care."*
- **靖哥哥** — earnest, simple, direct. *"I don't want you doing that anymore."*
- **洪七公** — gruff, sly, colourful. Self-mockery masks affection. *"Want me to take off my trousers too?"*
- **Beggar (洪七公 in disguise)** — deliberately uncouth. *"I'm tough enough. Don't worry about me."*
- **黃藥師** — prickly, anti-formality, witty. Comedy-of-register.
- **歐陽克** — smooth menace. Polite on the surface, deadly underneath. Doesn't raise his voice.
- **梅超風** — resentment-tinged loyalty. Don't flatten to generic villainy.
- **華箏** — 蒙古 directness. Plain, unmelodramatic.

### DO NOT use placeholder patterns
- Never use "— 蓉兒.\n— 靖哥哥." as a default placeholder — it caused 79 wrong subs in Ep20.

---

## 13. Formatting

### Punctuation
- **Don't end subtitles with periods unless needed** for clarity or specific emphasis. Most subs need no terminal punctuation — the viewer sees one sub at a time and the boundary is implicit.
- **Use `?` and `!` where the dialogue genuinely calls for it.** Reserve `!` for actual shouts, commands, and exclamations in the source. Don't add excitement the source doesn't have.
- **Quota check:** the Ep20 reference uses ~29 exclamation marks across 586 subs (~5%). If you're using 76, you're shouting too much.

### Dialogue dashes
- **Use em-dash (—)** for dialogue splits, not hyphen (`-`).
- Format: `— Line one.\n— Line two.`

### Line breaks
- **Use 3-line subs when needed.** If a sub has three short clauses, or a long address + two lines of dialogue, split to 3 lines rather than cramming into 2 long lines.
- **Target ~20 characters per line** for readability.
- **Break at natural clause boundaries**, not mid-phrase.

| WRONG (2 cramped lines) | RIGHT (3 clean lines) |
|---|---|
| 岳老伯, they said you're a descendant\nof 岳王爺. Is it true? | 岳老伯, they said\nyou're a descendant of 岳王爺.\nIs it true? |
| If I go back, I'll only drag my family down.\nJust leave me to fend for myself! | If I go back,\nI'll infect the whole family.\nLeave me alone. |

---

## 14. Conversion Order (CRITICAL)

Process in this order to avoid partial matches eating longer ones:

1. **Idioms** (longest first)
2. **Terms** (longest first)
3. **Titles / honorifics** (longest first — compounds before bare)
4. **Names** (longest first — compounds before single characters)

Example of why it matters: **梅師姊** must be converted to "Senior Sister Mui" **before** bare 梅 gets processed — otherwise 梅 becomes "Mui" and leaves 師姊 orphaned.

---

## 15. Duration Extension System

| Parameter | Value |
|-----------|-------|
| Target reading speed | 15 English characters/second |
| Minimum duration | 1000 ms |
| Yue speech guide | Use Cantonese track end times as reference |
| Hard cap | Never extend past the next subtitle's start time |
| Overlap rule | Zero overlaps allowed |

---

## 16. Index/Timecode Preservation

- Output must have EXACTLY the same subtitle count and indices as the **chi** track (`{N}-chi_tra.csv`). Chi is the entry spine.
- Start times are taken from chi. Timecodes may be extended (per §15 duration rules) but chi start times preserved.
- Output entry count will typically **differ from eng**'s entry count — this is intentional. Eng and chi are authored independently, often with different segmentation; chi-spine alignment reflows eng content onto chi entries to prevent the "double-subs" failure mode where the same spoken line appeared twice at offset timings.
- See `PIPELINE.md` Step 1 for the reflow algorithm.

---

## 17. Output Format

- Full SRT format
- UTF-8 encoding
- Saved to `/mnt/user-data/outputs/`
- Naming: `{episode}-eng-{variant}-v{VERSION}.srt` (e.g. `24-eng-hybrid-v9.srt`). The `{VERSION}` suffix comes from the `VERSION` file shipped in the handoff bundle and is stamped in by `build.py` and consumed by `cjk_fix_v2.py`. Every delivered SRT is thus traceable to the rule-set that produced it; a bundle with missing/malformed VERSION fails loudly rather than shipping unstamped files.

---

## 18. Banned Terms (auto-fix after every build)

Sweep hybrid and romanised outputs for these. All must be fixed before present:

- **"Old Imp"** → 老頑童 in hybrid; **"Overgrown Child"** in romanised (**no article**)
- **"Old Urchin"** → same as above
- **"Brother Zhou" / "Brother Zau" / "Brother Jau"** → 週大哥 in hybrid; 週-daai-go (jy) / 週-daaih-go (yl) in romanised
- **"the Overgrown Child"** → "Overgrown Child" (drop the article — proper noun)
- **"Rong-er"** → 蓉兒 in hybrid; Jung-yi (jy) / Yuhng-yih (yl) in romanised
- **"Guo Jing"** → 郭靖 in hybrid — never bare Pinyin
- **"Huang Rong"** → 黃蓉 in hybrid — never bare Pinyin
- Any other **Pinyin** (e.g. "Huang Yaoshi", "Mei Chaofeng") in hybrid — use CJK or Jyutping/Yale per variant
- **CJK for common wuxia vocabulary in hybrid** — any of 武功 · 武林 · 江湖 · 內力 · 內功 · 輕功 · 功力 left as CJK in hybrid. These must be English ("martial arts" / "the martial world" / "internal strength" / "internal energy" / "qinggong" / "internal force"). See §7 "What does NOT get CJK".
- **叫化子 in hybrid** — use Cantonese 乞兒 instead (or render as English "beggar"). The Mandarin form should never appear in our hybrid.
- **CJK for common-noun insults** in hybrid — any of 臭丫頭 · 死丫頭 · 死乞兒 · 臭乞兒 · 王八蛋 · 禁宮 left as CJK. These must be English.

---

## 19. Recurring CJK Fix Patterns (apply via sed after build)

These leaks appear episode after episode and need to be fixed in a targeted pass after `build.py` / `cjk_fix_v2.py`:

- `江南七怪` → "the Seven Freaks of Jiangnan"
- `大Master` → "First Master" (compound break)
- `康,` → "Hong," (bare 康 in vocative context)
- Bare `鐵心` → "Tiexin"
- `Brother 鐵心` → "Brother Tiexin"
- `Yeung叔叔` → "Uncle Yeung"
- `Yeung兄` → "Brother Yeung"
- Classical Chinese phrases left in romanised files → translate to English

The bulk of recurring concat-trap and OCR-collapse patterns are now handled automatically by `cjk_fix_v2.py` (`shared_concat_fixes`, `yale_concat_fixes`, `OCR_NAME_COLLAPSE` tables). The active set is the source of truth; consult the script directly. Promote new patterns to those tables once they fire in two or more episodes without a contradicting rendering.

### The `<titles-key>+<suffix>` cross-stage trap — structural rule (v13)

**Rule:** registering a compound in `extras_baseline.json` or an episode overlay is insufficient when `build.py`'s titles stage contains a shorter-key match that is a substring of the compound. The titles stage (stage 3) fires before the extras stage (stage 5), so the shorter key converts first and strands the remaining prefix/suffix as CJK.

**Examples of the trap firing (and how each was caught):**
- `爹` (titles: "Father") + overlay `我爹 → my father` ⇒ produces `我Father`, requires post-build `我Father → my father` in `cjk_fix_v2.py`.
- `幫主` (titles: "the Chief") + overlay `幫主萬福 → Good fortune to the Chief` ⇒ produces `the Chief萬福`, requires post-build strip.
- `金國` (baseline: "Jin") + overlay `大金國 → the great Jin empire` ⇒ produces `大Jin`, requires post-build strip.
- `公主` (titles: "the Princess") + overlay `報告公主 → Your report, Princess` ⇒ produces `報告the Princess`, requires post-build strip.
- `七公` (titles: "Seven Elder") + CSV name `洪七公 → Hung Cat-gung` ⇒ produces `洪Seven Elder`, fixed by `洪Seven Elder → Hung Seven Elder` in `cjk_fix_v2.py` `fixes` table.

**When to reach for which tool:**
1. If the compound's semantic target is the same as the titles-stage output plus a modifier (e.g. `我爹` = "my" + "Father"), a post-build `cjk_fix_v2.py` entry of the form `<stranded-CJK><titles-output> → <full-English>` is the cheap fix.
2. If the compound needs a wholly different English rendering, either (a) promote the compound entry into `build.py`'s idioms stage (stage 1) so it wins by ordering, or (b) post-build-fix in `cjk_fix_v2.py`.
3. Option (a) is structurally cleaner but requires editing `build.py` and re-checking that the compound doesn't break other idioms. Option (b) is lower-risk for one-off entries.

**Known firings and their current resolution:** see the worked examples above. New compounds of this family should be added to `cjk_fix_v2.py`'s `shared_concat_fixes` as they're discovered.

### Hybrid-variant duplication trap (IMPORTANT — learned Ep22/23; format updated v18)

When an idiom-plus-gloss is written in the hybrid using the `中文成語 (English gloss)` format (§9), `build.py`'s romanised conversion turns the CJK into English and leaves the parenthesised English gloss alongside, producing visibly-duplicated lines like:

> "Retreat like a subdued dragon, steady and deep (Retreat like a subdued dragon, steady and deep)"
> "better safe than sorry (better safe than sorry)"

The older pre-v18 em-dash form (`English gloss — 中文成語`) produced the same class of duplicate on the other side of the dash. The collapser in `cjk_fix_v2.py` handles both shapes: em-dash-separated `X — Y` where X and Y share ≥55% content words, and parenthesised `X (Y)` where the parens contents share ≥55% content words with the text preceding them. Under the parenthetical format the trap is more visually obvious (the parens make the duplication hard to miss), but the collapser catches it identically either way — when triggered, drop the parenthetical and keep the un-parenthesised side.

**Prevention:** the collapser in `cjk_fix_v2.py` handles both shapes automatically; reviewer attention is needed only when:
- The gloss and the English version of the CJK diverge (e.g. hybrid `劫數難逃 (I fear this is my fate)` produces romanised `cannot escape one's fate (I fear this is my fate)` — these are not content-word-identical but convey the same sense; the collapser will fire via subset-check and keep the longer side).
- A short idiom's gloss is too short to meet the 6-char minimum (older pre-v17 threshold problem; v17 lowered the threshold to 6 chars to catch these).

Also scan for `"the the "` (double article) and `"my the "` / `"your the "` — these happen when `降龍十八掌` → "the Eighteen Dragon-Subduing Palms" gets preceded by an existing English `my/your/the`. Simple string replacements suffice.

---

## 20. Known Recurring Issues

- **Pinyin leakage** — scan hybrid files after build for any Pinyin names (Guo Jing, Rong-er, etc.).
- **CJK in romanised files** — scan jyutping/yale files for any remaining Chinese characters after conversion.
- **`go-go` dash** — verify all `gogo` compounds have no extra dash.
- **Bare surname fragments** — `洪Seven Elder` → must be `Hung Seven Elder` (jyutping) / `Huhng Seven Elder` (yale).
- **康 bare character** — when 楊康 is called just 康, romanised must be "Hong" (NOT left as Chinese, NOT rendered as "Kang").

---

## 21. Anti-Patterns (What NOT to Do)

1. **Don't pad short subs.** If chi is one short sentence, the English should be one short sentence. Not two.
2. **Don't inject idioms into subs where they don't appear in chi.** If 劫數難逃 appears in sub 131's chi, put it in sub 131 — don't also scatter it into subs 130, 133, 136.
3. **Don't translate 老伯 / 少爺 / 公子 / 長老 to English in hybrid.** These are address terms.
4. **Don't write "the Song dynasty" when you can write 大宋.** Hybrid means use Chinese.
5. **Don't use excessive exclamation marks.** See §13 quota.
6. **Don't treat Step 3's output as a translation.** It's a mechanical preprocessing pass — CJK substitutions, address-term injection, idiom injection. You must still examine each sub against chi and yue for meaning and register per `PIPELINE.md` Step 4.
7. **Don't gloss an idiom twice** in hybrid (once in Chinese AND as a separate English expansion — see §9).
8. **Don't treat the original English as untouchable, and don't treat it as disposable either.** The priority chain is yue (HIGH) > chi > eng: examine every sub against both chi and yue, and override when content or register mismatches. When the draft is already faithful to both sources, leave it alone.
9. **Don't keep CJK for common wuxia vocabulary or colloquial insults.** 武功, 武林, 江湖, 內力, 內功, 輕功, 功力 go English in hybrid. Colloquial insults like 臭丫頭, 死乞兒, 王八蛋 also go English. CJK in hybrid is reserved for proper-noun-like content — named techniques, characters, places, titles, idioms with cultural weight. See §7.
10. **Don't use 叫化子 in hybrid.** If chi gives you 叫化子, either use the Cantonese 乞兒 form (when CJK is warranted) or render as English "beggar" — never leave the Mandarin 叫化子 in the hybrid.
