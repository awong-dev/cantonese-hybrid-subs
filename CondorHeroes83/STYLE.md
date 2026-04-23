# Style — Legend of the Condor Heroes 1983 TVB

> **Companion docs:** `PIPELINE.md` (mechanics) · `REFERENCE.md` (tricky cases, Five Greats) · `SESSION-NOTES.md` (episode status).

---

## Table of Contents

1. Three Output Variants · 2. Priority Chain · 3. Name Rules · 4. Kinship & Address · 5. Name Rendering Table · 6. Title Conversion Table · 7. Hybrid CJK Requirements · 8. Key Conventions · 9. Idiom Rules · 10. Idioms Catalogue · 11. Yue Register · 12. Voice · 13. Formatting · 14. Conversion Order · 15. Duration · 16. Timecode · 17. Output · 18. Banned Terms · 19. Recurring Fix Patterns · 20. Known Issues · 21. Anti-Patterns

---

## 1. Three Output Variants

| Variant | Names | Honorifics | Idioms | File suffix |
|---------|-------|------------|--------|-------------|
| **eng-hybrid** | CJK (郭靖) | CJK (師父) | CJK inline + English gloss | `-hybrid.srt` |
| **eng-jyutping** | Jyutping (Gwok Zing) | English (Master) | English only | `-jyutping.srt` |
| **eng-yale** | Yale (Gwok Jing) | English (Master) | English only | `-yale.srt` |

- **Hybrid:** English prose with CJK for names, titles, honorifics, idioms, places, martial arts terms. No Pinyin. No English proper nouns where CJK exists.
- **Jyutping/Yale:** Fully romanised. **Zero CJK characters allowed.**

---

## 2. Priority Chain & The Yue-Authority Rule

English phrasing mirrors the Cantonese spoken dialogue — register, cadence, level of detail. Fidelity to what's being said is the only goal.

### Priority chain
1. **Yue (HIGH confidence)** — spoken words. Source of register. Has **phonological authority** (what sound was made), not **semantic authority** (what word was meant) — reaches Claude through Whisper ASR, which can be HIGH-confident on homophones and garble alike.
2. **Chi** — **semantic authority**. Written translation that sometimes flattens register but reliably preserves what word was meant. Chi wins by default on semantic disagreement.
3. **Eng (original)** — rough draft. Override when it diverges from yue/chi; keep when faithful.

### Rule A — Register / vividness override

**When yue and chi agree semantically but yue is more vivid, colloquial, or registers tone better, yue overrides chi.** Gate: yue's word and chi's word are synonyms (substitutable in a dictionary sense).

Examples: 古惑 (yue) over 鬼主意 (chi) — both "cunning"; yue spicier. 淒涼 (yue) over 可憐 (chi) — both "pitiable"; yue stronger. 老乞兒 (yue Cantonese) over 老叫化子 (chi Mandarin) — same referent, Cantonese form matches what's spoken.

### Rule B — Semantic disagreement defaults to chi

**When yue and chi disagree on *which word was said* (not how vividly the same thing is expressed), chi wins by default.** Yue only overrides semantically when there's independent evidence: eng confirms yue, a **prior FULL-completed episode** established the form yue matches, or chi has a visible OCR artefact.

Cross-episode clause is strict: requires a prior FULL episode where the form was actually rendered a specific way, not a form the reviewer expects ought to be canonical. Absent concrete prior precedent, chi wins. (Ep24 小保 case: v2 attempt to "correct" 小保 → 小寶 was wrong — no prior FULL episode established 小寶. See REFERENCE §2.)

Reasoning: yue reaches Claude via Whisper ASR, subject to homophone errors (宮/功 both `gung1`; 保/寶 both `bou2`). Chi is written — no homophone errors. When yue and chi produce different non-synonymous words, presumption is yue has an ASR error.

Examples: 推宮換血 (chi) vs 推功換血 (yue HIGH) — not synonyms; 功/宮 are homophones. Chi wins. 四字成語 / named wuxia techniques generally — fixed compounds; yue variant almost always a homophone of real term.

### Rule C — The intelligibility gate (pre-requisite for A and B)

Before Rule A or B fires, yue must be **intelligible** — coherent syntax, parseable as something a character would plausibly say. Garbled yue (broken syntax, missing particles, scrambled order, non-words) or semantically incoherent yue (real words in nonsensical order) → treat as ASR noise, fall back to chi regardless of confidence tier.

Confidence tier doesn't settle this — Whisper can be HIGH on garble; a LOW-tier intelligible sub can still be useful. Reviewer's read of yue's coherence is the final test.

### Decision procedure per sub

1. Yue intelligible? (Rule C) No → chi wins, stop.
2. Yue agrees semantically with chi? Yes → go to 3. No → Rule B: chi wins unless eng/cross-ep/OCR corroborates yue. Stop.
3. Yue more vivid/colloquial/register-appropriate than chi? Yes → use yue. No → keep chi.

### Citation discipline for Rule A

When Rule A fires — you override chi because yue is more vivid — the Step 4 log entry (`PIPELINE.md` Step 4) must quote the yue phrase that triggered the override. "Rule A applied" is a gesture; "yue 大蝦勢 (Cantonese 'bullying-posture') more vivid than chi 以大欺小" is the real application.

The citation requirement exists because Rule A is the most abusable rule in the priority chain: it permits chi to be overridden on register grounds, which sounds subjective and invites hand-waving. Forcing a quoted yue phrase in the log keeps Rule A honest — if you can't quote the yue phrase, you aren't applying Rule A, you're writing from plot memory.

### Special cases

- **臭要飯的** (chi OCR) → actual Cantonese is **死乞兒**. Both chi and yue ASR transcribe incorrectly. Render as **"stupid beggar"** in all three variants (not CJK in hybrid).
- **Cantonese phonological/dialect variant** (e.g. 家散人亡 vs 家破人亡) — yue's form is the actually-spoken Cantonese variant of the same idiom. Keep yue (Rule A at dialect-form level).
- **抵死** (Cantonese colloquial "deserve to die") — Rule A applies. Render register in English ("damn well deserves it", "serves him right"); do NOT use CJK+gloss. CJK+gloss format is reserved for 四字成語, poetic couplets, literary phrases — not colloquial slang English can carry alone.

---

## 3. Name Rules

### 阿-prefix (CRITICAL)
- **ONLY** in direct address (vocative): "阿靖!" when calling someone.
- **NEVER** in object/possessive/descriptive: "real father" not "real 阿爹".

### 靖哥哥 / 蓉兒 romanisation
- Jyutping: **Zing-gogo / Jung-ji** (NO extra dash: `gogo` not `go-go`).
- Yale: **Jing-gogo / Yuhng-yi**.
- Hybrid: CJK always.

### 七仔 vs 老七
- 洪七公 calls himself **七仔** (NOT 老七).
- Use 七仔 in hybrid **only** when dialogue explicitly says 老七/七仔.
- Romanised: "Little Seven".
- Do **NOT** use 七仔 as general substitute for 洪七公.

### Rong-er NEVER in hybrid
- Always **蓉兒**. "Rong-er" is Pinyin leakage.

### Compound names convert before bare characters
- **梅師姊** → "Senior Sister Mui" before bare 梅.
- **歐陽公子** → "Young Master Au-Joeng" before bare 歐陽.
- See §14.

---

## 4. Kinship & Address Terms

### 娘親 rule
- Hybrid uses **娘親** (not 娘) — Cantonese-preferred. Renders "mother" in romanised.
- Use as vocative: "娘親!" "娘親, I'm home." English possessives ("my 娘親") are fine — 娘親 is "mother" not "my mother".

### Descriptive kinship terms
- **養父 / 義父** → "foster father" ALWAYS in all three variants.
- Never keep CJK for descriptive kinship.

### 阿爹 in romanised
- Converts to **"Father"**.

### The 老伯 rule
When ADDRESSED as 老伯 (vocative), keep CJK in hybrid. Don't convert to "sir" or "old man".

### The 大宋 / 金 rule (dynasty names stay CJK in hybrid)
- "There is hope for **大宋**!" NOT "the Song dynasty."
- "The **金** are coming" NOT "the Jins."
- Same for 宋, 蒙古, 金國. Romanised: "the Song" / "Mongolia" / "Jin".

### The 道長 family — title-vs-vocation rule
Bare **道長** and address-form variants keep CJK. Common-noun **道士** (the vocation) renders English. Rule: address term to/by Taoist clergy → CJK; noun for the vocation → English.

Keeps CJK: **道長** (vocative), **道爺** (self-form), **貧道** (humble classical self-ref), **臭道長** (vocative+insult), compounds 丘道長/馬道長/王道長 (build.py titles dict).

Renders English: **道士** (the vocation), **道袍** ("Taoist robe").

---

## 5. Name Rendering Table

Canonical renderings for recurring name/nickname forms. Personal names live in `PersonalNamesUpdated.csv`; below captures nicknames and compound forms.

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

Notes: **駙馬爺** — 蓉兒 uses sarcastically toward 郭靖. **晚輩/後輩** — humble self-ref / peer ref when addressing 前輩. **女魔頭** — 梅超風's own self-description. **顏烈** — 完顏洪烈's cover alias (Ep1/Ep2); 顏大爺 fuller form (Ep5 蒙古). **小靖** — young-child diminutive (Ep3 蒙古 widow scenes). Distinct from vocative **阿靖**.

---

## 6. Title & Address Conversion Table

Title/address conversions in romanised (hybrid keeps CJK):

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
| 道長 | Taoist (vocative — CJK in hybrid) |
| 道爺 | Taoist (self-form — CJK in hybrid) |
| 貧道 | this poor Taoist (humble — CJK in hybrid) |
| 道士 | Taoist (vocation — English in hybrid too) |

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

Named techniques and canonical texts stay CJK. **Generic wuxia vocabulary — 武功 · 武林 · 江湖 · 內力 · 內功 · 輕功 · 功力 — stays English** (see below).

### Nicknames
老頑童 · 老毒物 · 賴蛤蟆 · 黃老邪 · 老乞兒 · etc.

Use Cantonese **老乞兒**, not Mandarin **老叫化子**. If chi transcribes 叫化子, override to 乞兒 (Rule A).

### Idioms
All 四字成語 in chi must appear as CJK in hybrid. See §10 catalogue.

### Title + name compounds (always CJK as a unit)
岳老伯 · 岳王爺 · 岳大叔 · 黃大叔 · 洪師父 · 黃前輩 · 黃老伯 · etc. NOT "Uncle Yue" / "Uncle Wong".

### Temple/place full names (always CJK)
岳王廟 · 翠紅樓 · 獅子林 · 山神廟.

### Address terms in direct speech
老伯 · 少爺 · 弟子 · 長老 · 幫主 · 公子 — keep CJK when spoken.

### Standalone idioms
劫數難逃 (only 四字成語 with cultural weight that passes §10's plain-prose test). All other standalone idioms go English in hybrid.

### Five Greats (五絕) epithets
東邪 · 西毒 · 南帝 · 北丐 · 中神通 — canonical wuxia epithets. Keep CJK; see §10 for romanised.

### What does NOT get CJK in hybrid

**The CJK requirements above are exhaustive — if a phrase isn't on one of these lists, it stays in English.**

- **Generic wuxia vocabulary** — **武功**, **武林**, **江湖**, **內力**, **內功**, **輕功**, **功力**. Common-noun wuxia-domain vocabulary English carries cleanly. Named techniques and canonical texts (九陰真經, 降龍十八掌) stay CJK. Rule: "a martial art" → English; "*the* such-and-such martial art" → CJK.
- **Common-noun beggar-terms** — **叫化子 / 乞兒 / 乞丐** → "beggar(s)". When CJK warranted (洪七公 self-naming), use Cantonese **乞兒**, never 叫化子.
- **禁宮** → "the palace" / "the forbidden palace".
- **Colloquial insult compounds** (intensifier + common noun):
  - **臭丫頭** → "stinking girl" / "damned girl"
  - **死丫頭** → "wretched girl"
  - **死乞兒** → "damned beggar" / "stupid beggar"
  - **臭乞兒** → "stinking beggar"
  - **臭要飯的** (chi OCR for 死乞兒) → "stupid beggar"
  - **王八蛋** → "bastard" / "scoundrel"
  - **畜生** → "beast" / "brute" (bare compound, not intensifier+noun, but same class — a common-noun insult that English carries fully. Often chi-OCR as 會牲.)
  - **淫賊** → "lecherous scoundrel" (occasional pairing **奸夫淫婦** → "adulterous lovers" / "adulterous pair" — plain prose, no CJK).
  - Rule: intensifier + common-noun-insult → English. Contrast intensifier + proper-nickname (**死老邪**, **老毒物**, **老頑童**) which stays CJK because X is a proper nickname.
- **Colloquial slang/intensifiers** (抵死, 好彩, 乜嘢, 放肆) — render register in English, no CJK.
- **Everyday Cantonese-vs-Mandarin vocabulary** that isn't a proper noun, title, idiom, or term-of-art — Rule A picks the form, rendering is English.
- **Descriptive common-noun metaphors that sound idiomatic** — Chinese-literary-sounding but actually common-noun descriptors. Test: does English rendering work as plain noun phrase? If yes, descriptor not idiom.
  - **情蛇** ("love snake") — metaphor for lecher; English ("that snake").
  - **一流高手** / **一流絕頂高手** — rank descriptor; English.
  - General **X+高手** / **X+高人** / **X+蛇** / **X+物** where X is adjective. Contrast **塞外高人** (CJK OK — specific geographic qualifier) and **老毒物** (CJK — 歐陽峰 nickname).
- **Emotional interjections** — match tone in English.

**Rule of thumb:** CJK is for content English *can't* fully carry — proper names, titles of address, specific places, fixed idioms with cultural weight, classical allusions, literary phrases, named techniques. Generic descriptors in Chinese are noise, not fidelity. When English does the job, use English.

---

## 8. Key Translation Conventions

Canonical English renderings for high-frequency terms. **Gives romanised rendering.** For hybrid, consult §7: CJK for named-technique/canonical-text/proper-noun entries; English for generic wuxia vocabulary at bottom.

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
Preserve the specific image/concept rather than collapsing to generic abstract moral.

- **不見棺材不流淚** → "won't cry till you see the coffin" — NOT "won't believe till it's too late". Coffin image is the point.
- **以牙還牙** → "an eye for an eye" — 1:1 map; render plainly.
- **狗咬呂洞賓** → "biting the hand that feeds you" — concept maps cleanly.

Rule: Western equivalent only when *meaning* maps 1:1; preserve specific imagery when it's the point. Applies to English rendering in both hybrid and romanised — most idioms render cleanly in English without CJK per §10's plain-prose test. Only §10-catalogued phrases keep CJK in hybrid.

### Paired / couplet proverbs — render each half literally

When chi carries a classical **paired proverb** (two balanced halves joined by comma, typically 6+6 or 4+4 chars, each half a complete idiom-image), render **each half literally**; do not collapse both halves to a single abstract English equivalent.

- **天有不測風雲, 人有旦夕禍福** → "the heavens hold unforeseen storms, fortunes shift in a day" — NOT "disaster strikes without warning".
- **有福同享, 有難同當** → "share fortune together, share hardship together" — NOT "through thick and thin".

Cue: chi presents two balanced halves separated by comma where each has its own imagery. If either half would make sense alone as an independent proverb, render both halves literally. Test: does the English preserve the rhetorical parallelism that made the source a couplet?

### Hybrid: keep Chinese characters inline

**Preferred format: `中文成語 (English gloss)`.** Chinese first, English gloss in parentheses. Universal for 四字成語, couplets, classical allusions, any §10 CJK-kept entry. **Do NOT use CJK+gloss for colloquial slang/intensifiers, everyday Cantonese-vs-Mandarin vocabulary, or emotional interjections** (see §7 for the full list of what stays English). CJK-inclusion isn't a badge of fidelity — over-using clutters the hybrid and trains readers to skim past the Chinese.

| RIGHT | WRONG |
|-------|-------|
| 狗眼看人低 (who told him to look down on us)! | He looked down on us. 狗眼看人低. |
| 劫數難逃 (I fear my time has come) | I fear this is my fate — I won't escape it. |
| He damn well deserves it | He deserves it — 抵死 |

**Rules:**
- **Never gloss an idiom twice** (CJK AND separate English expansion). Parenthesised English IS the gloss.
- **Idiom on its own is fine** — if sub is just exclamation and idiom is §10-catalogued ("邪中有三分正!"), CJK alone is acceptable. For non-catalogued, render English.
- **Don't inject idioms into subs where they don't appear in chi.**

### Romanised: faithful English only
- No CJK in jyutping/yale.
- Idiom becomes its English rendering.

### Wuxia terms in hybrid
- **Named techniques** stay CJK: 降龍十八掌 / 九陰白骨爪 / 空明拳 / 打狗棒法 / 九陰真經.
- **Generic wuxia nouns go English** (see §7): 武功 / 武林 / 江湖 / 內力 / 內功 / 輕功 / 功力.

---

## 10. Idioms Encountered (Full Catalogue)

Settled renderings for idioms that earn CJK+gloss treatment in hybrid. Hybrid: keep Chinese; romanised: use rendering below.

### Admission gate

Not every 四字 phrase is catalogue-worthy. Before adding a new entry, check at least one criterion:

1. **Fixed 四字成語** — classical compound in standard idiom dictionaries, stable English rendering that preserves imagery the English can only approximate.
2. **Classical allusion** — references specific classical source (秦晉之好 from 左傳, 泰山北斗 from 史記, 人之將死其言也善 from 論語).
3. **Named proverb / 俗語** with cultural weight English can't fully carry.
4. **Poetic / elegiac couplet** from identifiable literary tradition (曹操 短歌行, the Dragon-chant quartet).

**The primary test — the plain-prose rule.** Strip the CJK, read only the English. *If it stands alone as plain prose without losing imagery or cultural weight, it does not belong here — a consistency ledger is not reason enough.* This catalogue is only for phrases whose Chinese form carries something the English gloss can't. Descriptive common-noun phrases fail even if they sound literary (情蛇, 一流高手, general X+高手/高人 compounds where X is adjective). Pass the gate: **塞外高人** (set classical phrase — 塞外 geographic qualifier), **一代宗師** (fixed 四字 wuxia-world meaning). When in doubt, err toward English — catalogue stays tight.

### Gate-naming requirement (Step 4 discipline)

When Step 4 keeps a non-catalogued idiom as CJK+gloss in hybrid, the Step 4 log entry must name the criterion (1/2/3/4) it passes, OR mark it `plain-prose → English` and render the hybrid sub in English. There is no unnamed middle ground — every CJK-kept idiom has passed a specific criterion, or it should not be CJK.

The rule exists because the admission gate is easy to gesture at and skip. Ep1 莫須有 was the canonical failure: a phrase with real historical pedigree (秦檜's charge against 岳飛) that nonetheless failed the gate because its standard English ("trumped-up") is plain-prose. Historical provenance alone does not qualify. Naming the criterion forces the check to happen.

### Catalogue entries

- **人之將死, 其言也善** — "When a man is dying, his words are kind" (論語).
- **婦人之仁** — "a woman's soft-heartedness". Classical compound; gendered image.
- **劫數難逃** — "cannot escape one's fate". Buddhist 劫數 imagery.
- **不怕一萬, 只怕萬一** — "better safe than sorry". Classical couplet; ten-thousand/one-in-ten-thousand parallelism is the point.
- **狗眼看人低** — "look down on others". Named 俗語; dog-eye image.
- **邪中有三分正, 正中帶七分邪** — "The heretical are three parts righteous; the righteous are seven parts heretical!" (黃藥師's couplet). **Keep Chinese in hybrid; English only in romanised. Do NOT double-print.**
- **秦晉之好** — "the bond of 秦晉" (hybrid) / "the bond of Chun-Zeon" (jy) / "the bond of Chun-Jeun" (yl). 左傳 marriage alliance between 秦/晉. Idiom-of-reference, not modern place name.
- **泰山北斗** — "the authority of the martial world". 史記 classical allusion. **Pairing note:** don't write "泰山北斗 of 武林" — 武林 goes English per §7, and since 泰山北斗's rendering already contains "martial world", combining produces "of the martial world of the martial world". Drop 武林, rewrite ("...of our age", "...of our time").
- **好自為之** — "mind yourselves". Stable 4-ep (Ep2+4+7+20).
- **不見棺材不流淚** — "won't cry till you see the coffin". Coffin image is the point (§9).
- **精忠報國** — "utmost devotion to the country". 岳飛's tattoo motto; cultural weight.
- **好心遭雷劈** — "good hearts get struck by lightning". Named 俗語.
- **皇天不負有心人** — "Heaven never fails the determined". Named 俗語.
- **忘年之交** — "old friends despite their years". 2-ep stable (Ep12+Ep25). Age-crossing friendship — the specific image English gloss flattens to plain "old friends"; the 忘年 ("disregarding years") is the point. Format: `忘年之交 (old friends despite their years)` on first use; short form on later uses.

### Five Greats (五絕) epithets

Canonical wuxia epithets for five supreme masters of 華山論劍. Fixed compounds with specific named referents (REFERENCE §6); keep CJK in hybrid, render per table in romanised.

- **東邪** — "the Eastern Heretic" (黃藥師). Eastern cardinal + 邪.
- **西毒** — "the Western Poison" (歐陽峰). Western cardinal + 毒.
- **南帝** — "the Southern Emperor" (一燈大師, 段智興). Southern + 帝.
- **北丐** — "the Northern Beggar" (洪七公). Northern + 丐.
- **中神通** — "the Central Divine" (王重陽). Central + 神通.

Usage: epithets appear standalone ("東邪 黃藥師, only has one daughter") and paired ("東邪西毒, 南帝北丐"). Both keep CJK. When a character refers to another by epithet rather than name, preserve epithet form. 中神通 rare post-華山論劍 (王重陽 died before series proper). For 一燈大師 specifically: series uses both 南帝 (pre-ordination) and 一燈 (post-ordination monastic) — track which form the scene uses.

### Classical laments / elegiac verse

- **想逝者之不罪兮, 惜形中之載道** / **天蓋高而無階, 懷此恨其最苦** (Ep28) — 陸乘風's lament for 瑤迦. Format `CJK (English gloss)`. Glosses: "my love runs deep, the dead beyond recall" / "Heaven is high but has no stair; this sorrow cuts deepest".
- **天長地久, 人生幾何** / **譬如朝露, 去日苦短** (Ep33) — 黃藥師's lament for supposedly-dead 蓉兒 (曹操 短歌行 adaptation). Glosses: "Heaven and Earth endure; how brief a human life" / "like morning dew, the days gone are bitter and short".
- **林升 題臨安邸** (Ep1 compressed + Ep20 full — two-ep stable) — Southern Song lament over occupied capital. Quatrain, four lines, each `CJK (English gloss)`. Canonical: 山外青山樓外樓 / 西湖歌舞幾時休 / 暖風熏得遊人醉 / 直把杭州作汴州. Glosses: "beyond the green hills, more green hills; beyond the tower, yet another tower" / "when will the song and dance on 西湖 ever cease?" / "the warm breeze lulls the travellers drunk" / "they take 杭州 for 汴州". Ep1 uses compressed two-line form (lines 2+4 as narration backdrop).
- **滿江紅 quatrain** (Ep1+17+19 three-ep stable) — 岳飛's 靖康恥 quatrain. Format `CJK (English gloss)`, one line per sub. Canonical:
  - 憑欄處, 瀟瀟雨歇 → "I lean on the railing as the rain dies away"
  - 抬望眼, 仰天長嘯, 壯懷激烈 → "I lift my gaze, give a long cry to the sky, my heart fierce with passion"
  - 三十功名塵與土 → "thirty years of glory, all dust and earth"
  - 八千里路雲和月 → "eight thousand li of road, only cloud and moon"
  - 莫等閒, 白了少年頭, 空悲切 → "do not idle — when youthful hair turns white, the grief is empty"
- **元好問 摸魚兒「問世間情為何物」** (Ep19, closing line). Classical 詞 by 元好問:
  - 問世間, 情為何物, 值得生死相許 → "I ask the world: what is this thing called love, that it should bind life and death together"
  Famous opening from 摸魚兒·雁丘詞 that 金庸 also uses to open 神鵰俠侶.
- **白居易 長恨歌 fragment** (Ep17 compressed + Ep25 full — two-ep stable) — 唐 classical elegy for 楊貴妃; 蓉兒/郭靖 use it as poetry-practice banter in Ep25, 陸冠英/程瑤迦 tryst as backdrop. Format `CJK (English gloss)`, one line per sub or paired. Canonical lines encountered:
  - Ep17: 芙蓉帳暖度春宵 / 明月當空 → "the hibiscus-curtained bed is warm through the spring night" / "the bright moon stands in the sky"
  - Ep25: 淚濕羅巾夢不成 → "tears dampen the kerchief, no dream comes"
  - Ep25: 袍深前殿按歌聲 → "beyond the robes, the front palace sings on"
  - Ep25: 紅顏未老恩先斷 → "her youth unfaded, his favour already done"
  - Ep25: 斜倚薰籠坐到明 → "she leans on her incense pillow till dawn"
  Note: Ep25 sub 233–236 has 蓉兒 parodying 淚濕羅巾 as 淚濕羅布 ("tears dampen the laundry" — 巾/布 pun). Keep the parody CJK-preserved; 郭靖 corrects her 羅布 → 羅巾.

### 九陰真經 quotations (Ep29+ 周伯通 slap-memorise)
- **天之道, 損有餘而補不足** — "Heaven's way: take from the surplus and replenish the lack" (道德經 77).
- Related meditation-text fragments (任督二脈, 氣聚丹田, 百會, 大椎, 足少陽/足少陰, 十二經筋) — render per meditation/qi subsection.

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

### 鉛汞 meditation formulas (全真教 內功心法 — Ep19)
丘道長's 內功心法 transmission to 郭靖. Format `CJK (English gloss)` couplets.
- **鉛體沉墜, 以給腎火 / 汞性流動, 以行心水** → "the lead-body sinks heavy to feed the kidney-fire; the mercury-nature flows to course as the heart-water"
- **鉛體沉墜, 以給腎水 / 汞性流動, 以行心火** → "the lead-body sinks heavy to feed the kidney-water; the mercury-nature flows to course as the heart-fire" (corrected pairing as 郭靖 perfects formula)
- **此之謂鉛汞謹收藏** → "this is what is called keeping lead and mercury safely stored"

### Dragon chant quartet (Ep22)
Hybrid: `CJK (English gloss)` per line; romanised: English only.

- 去似天龍雲飛躍 → "Go like a heavenly dragon soaring through clouds"
- 收似降龍穩深沈 → "Retreat like a subdued dragon, steady and deep"
- 腳似飛龍騰萬里 → "Kick like a flying dragon spanning ten thousand li"
- 拳似怒龍翻四海 → "Punch like an angry dragon overturning the four seas"

---

## 11. Match the Yue Register

English should feel like yue/chi — not smoothed-out English prose.

- **Translate what's said, not more.** If Cantonese is three words, English should be comparably brief. Don't pad with filler the speaker didn't use.
- **Don't summarise away register.** If yue says 你這種人不見棺材不流淚 (elaborate insult), keep the elaboration. Don't compress to "You'll regret it." Length is the point.
- **Don't invent emphasis.** If yue/chi is flat, write flat. Don't add exclamation marks or intensifiers.

---

## 12. Translation Voice

### Match source register, don't normalise
Clipped yue → clipped English. Formal → formal. Awkward in source can be awkward in English — that's characterisation.

- 這麼緊張幹甚麼 → "Why so uptight?" (casual dismissal)
- 不知道誰亂來 → "Who's the one trying something funny?"
- 不去了 → "Not going anymore" (abrupt)
- 小姑娘過來放了我們 → "Miss, please come let us go" — NOT "Have mercy!"

### Don't over-explain
- 大宋有救了 → "There is hope for 大宋!" Don't expand to "Song dynasty."
- 武穆遺書 → write 武穆遺書. Don't add "the Book of Wu Mu" in same sub.

### Character voices (see REFERENCE for detail)

- **蓉兒** — bratty, playful, sharp. Short sentences. *"Pray till next year for all I care."*
- **靖哥哥** — earnest, simple, direct. *"I don't want you doing that anymore."*
- **洪七公** — gruff, sly, colourful. Self-mockery masks affection.
- **黃藥師** — prickly, anti-formality, witty. Comedy-of-register.
- **歐陽克** — smooth menace. Polite on surface, deadly underneath.
- **梅超風** — resentment-tinged loyalty. Don't flatten to generic villainy.
- **華箏** — 蒙古 directness. Plain, unmelodramatic.

### DO NOT use placeholder patterns
Never use "— 蓉兒.\n— 靖哥哥." as default placeholder — caused 79 wrong subs in Ep20.

---

## 13. Formatting

### Punctuation
- **No terminal periods unless needed** — viewer sees one sub at a time, boundary is implicit.
- **Use `?` and `!` where dialogue genuinely calls for it.** Reserve `!` for actual shouts. Don't add excitement source doesn't have.
- **Quota:** Ep20 reference uses ~29 `!` across 586 subs (~5%). 76 is shouting.

### Dialogue dashes
- **Use em-dash (—)** not hyphen. Format: `— Line one.\n— Line two.`

### Line breaks
- **Use 3-line subs when needed.** Three short clauses or long address + two lines → 3 lines rather than cramming 2 long lines.
- **Target ~20 chars/line.**
- **Break at natural clause boundaries.**

| WRONG (cramped) | RIGHT (3-line) |
|---|---|
| 岳老伯, they said you're a descendant\nof 岳王爺. Is it true? | 岳老伯, they said\nyou're a descendant of 岳王爺.\nIs it true? |

---

## 14. Conversion Order (CRITICAL)

Process in this order to avoid partial matches eating longer ones:

1. **Idioms** (longest first)
2. **Terms** (longest first)
3. **Titles / honorifics** (longest first — compounds before bare)
4. **Names** (longest first — compounds before single characters)

Why: 梅師姊 must convert to "Senior Sister Mui" **before** bare 梅 — otherwise 梅 becomes "Mui" and leaves 師姊 orphaned.

---

## 15. Duration Extension System

| Parameter | Value |
|-----------|-------|
| Target reading speed | 15 English chars/second |
| Minimum duration | 1000 ms |
| Yue speech guide | Use Cantonese end times as reference |
| Hard cap | Never extend past next subtitle's start |
| Overlap rule | Zero overlaps allowed |

---

## 16. Index/Timecode Preservation

- Output must have EXACTLY same subtitle count and indices as **chi** track. Chi is the entry spine.
- Start times from chi. Timecodes may extend (§15) but chi start times preserved.
- Output entry count will typically **differ from eng** — intentional. Eng/chi authored independently with different segmentation; chi-spine alignment reflows eng onto chi entries to prevent double-subs failure. See PIPELINE.md Step 1.

---

## 17. Output Format

- Full SRT, UTF-8, saved to `/mnt/user-data/outputs/`
- Naming: `{episode}-eng-{variant}-v{VERSION}.srt`. VERSION from handoff bundle, stamped by build.py, consumed by cjk_fix_v2.py. Bundle with missing/malformed VERSION fails loudly.

---

## 18. Banned Terms (auto-fix after every build)

Sweep hybrid and romanised. All must be fixed before present:

- **"Old Imp"** → 老頑童 in hybrid; **"Overgrown Child"** in romanised (**no article**)
- **"Old Urchin"** → same
- **"Brother Zhou" / "Brother Zau" / "Brother Jau"** → 週大哥 in hybrid; 週-daai-go (jy) / 週-daaih-go (yl) in romanised
- **"the Overgrown Child"** → drop article — proper noun
- **"Rong-er"** → 蓉兒 in hybrid; Jung-yi (jy) / Yuhng-yih (yl)
- **"Guo Jing"** → 郭靖 in hybrid — never bare Pinyin
- **"Huang Rong"** → 黃蓉 in hybrid — never bare Pinyin
- Any **Pinyin** (Huang Yaoshi, Mei Chaofeng) in hybrid — use CJK or romanisation
- **CJK for common wuxia vocabulary in hybrid** — 武功 · 武林 · 江湖 · 內力 · 內功 · 輕功 · 功力 must be English
- **叫化子 in hybrid** — use Cantonese 乞兒 (or "beggar"). Mandarin form should never appear.
- **CJK for common-noun insults** in hybrid — 臭丫頭 · 死丫頭 · 死乞兒 · 臭乞兒 · 王八蛋 · 禁宮 must be English.

---

## 19. Recurring CJK Fix Patterns (apply via sed after build)

Leaks that appear episode after episode (江南七怪→"Seven Freaks of Jiangnan", 大Master→"First Master", 康,→"Hong,", 鐵心→"Tiexin", Yeung叔叔→"Uncle Yeung", classical Chinese in romanised→translate) fix via targeted pass after build.py / cjk_fix_v2.py. Active set lives in `cjk_fix_v2.py`'s `shared_concat_fixes`, `yale_concat_fixes`, `OCR_NAME_COLLAPSE` — source of truth, consult script. Promote new patterns once fired in 2+ eps without contradiction.

### The `<titles-key>+<suffix>` cross-stage trap — structural rule

**Rule:** registering a compound in `extras_baseline.json` or episode overlay is insufficient when `build.py`'s titles stage contains a shorter-key match that is a substring of the compound. Titles (stage 3) fires before extras (stage 5), so shorter key converts first and strands remaining prefix/suffix as CJK.

Examples: `爹`/我爹, `幫主`/幫主萬福, `金國`/大金國, `公主`/報告公主, `七公`/洪七公, `大哥`/張大哥, `前輩`/裘老前輩, `將軍`/岳飛將軍.

Remediation: post-build `cjk_fix_v2.py` entry `<stranded-CJK><titles-output> → <full-English>` for the common case. If compound needs wholly different English, promote into build.py idioms stage (stage 1 wins by ordering). Promote via stage 1 for structural cleanliness; use cjk_fix_v2 for lower-risk one-offs. New compounds added to `cjk_fix_v2.py`'s `shared_concat_fixes` as discovered.

### Hybrid-variant duplication trap

When an idiom-plus-gloss is written as `中文成語 (English gloss)`, `build.py`'s romanised conversion turns CJK into English, leaving the parenthesised gloss alongside and producing "better safe than sorry (better safe than sorry)"-style duplicates. Older em-dash form (`English gloss — 中文成語`) produces the same on the dash's other side. Collapser in `cjk_fix_v2.py` handles both (≥55% content-word overlap triggers; drop parenthetical, keep longer side).

Reviewer attention needed when gloss and English-from-CJK diverge (`劫數難逃 (I fear this is my fate)` → romanised `cannot escape one's fate (I fear this is my fate)` — subset-check fires, keeps longer side) or when short-idiom gloss falls below v17's 6-char minimum.

Also scan `"the the "` (double article) and `"my the "` / `"your the "` — happen when 降龍十八掌 → "the Eighteen Dragon-Subduing Palms" follows existing English `my/your/the`. Simple string replacements suffice.

---

## 20. Known Recurring Issues

Scan hybrid for Pinyin leakage (Guo Jing, Rong-er); scan jyutping/yale for residual CJK; verify `gogo` compounds have no extra dash; check bare-surname fragments (洪Seven Elder → Hung Seven Elder jy / Huhng Seven Elder yl); 楊康 called just 康 → "Hong" in romanised (not CJK, not "Kang"). Full banned-term list §18; fix patterns §19.

---

## 21. Anti-Patterns (What NOT to Do)

1. **Don't pad short subs.** Match source length.
2. **Don't inject idioms into subs where they don't appear in chi.**
3. **Don't translate 老伯 / 少爺 / 公子 / 長老 / 大俠 to English in hybrid** (address terms — §7).
4. **Don't write "the Song dynasty" when you can write 大宋.** Hybrid means CJK for §7 content.
5. **Don't use excessive `!`.** ~5% quota; §13.
6. **Don't treat Step 3 output as a translation.** Mechanical preprocessing only — examine each sub against chi/yue per PIPELINE Step 4.
7. **Don't gloss an idiom twice** (CJK AND separate English expansion — §9).
8. **Don't treat original English as untouchable, or as disposable.** Priority yue > chi > eng: examine against both, override when mismatched. When draft is faithful, leave alone.
9. **Don't keep CJK for common wuxia vocabulary or colloquial insults** (武功/武林/江湖/內力/內功/輕功/功力 English; 臭丫頭/死乞兒/王八蛋 English). CJK reserved for proper-noun-like content (§7).
10. **Don't use 叫化子 in hybrid.** Use Cantonese 乞兒 or English "beggar".
