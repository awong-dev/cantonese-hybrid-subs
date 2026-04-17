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
1. **Yue (HIGH confidence)** — the actual spoken words. Match their register, tone, and specificity. If yue is blunt, be blunt. If yue is elaborate, be elaborate.
2. **Chi** — the semantic authority. If the yue looks like ASR garble, fall back to chi meaning. If yue is MEDIUM confidence, chi drives the meaning but use yue for register, tone, and emotional nuance.
3. **Eng (original)** — a rough draft. Override when it diverges from yue/chi; keep when it's already faithful.

### The Yue-Authority Rule (added Ep27 session)

**When yue gives a more vivid, specific, or colloquial word than chi, and yue passes the intelligibility gate (coherent syntax, parseable as real speech), yue overrides chi.** The yue track is the actual spoken Cantonese dialogue of a Cantonese show. The chi (Mandarin) track is a written translation that sometimes flattens the spoken register. But Whisper can be HIGH-confident on garbled output, so yue only earns authority when it actually makes sense on its own.

**Examples:**
- **古惑** (yue: crafty/street-smart) overrides **鬼主意** (chi: cunning schemes) — 古惑 is what's actually spoken
- **淒涼** (yue: desolate/forlorn) overrides **可憐** (chi: pitiful) — 淒涼 is emotionally stronger
- **開心** (yue: happy) overrides **瞑目** (chi: rest in peace) — 開心 is warmer, more colloquial
- **好像** (yue: seemed) vs **非常** (chi: very) — yue preserves the correct certainty level
- **抵死** (yue: deserve to die, Cantonese colloquial) — inject as CJK with gloss
- **百世千孫** (yue: descendants for a hundred generations) — yue adds obsequious detail chi omits
- **叫化子 / 叫化** (chi: Mandarin for beggar) → always use Cantonese forms in hybrid: **老叫化子** → **乞兒仔**, **老叫化** → **老乞兒**, **叫化子窩** → **乞兒窩**. The show is Cantonese — 叫化 is a Mandarin subtitle artefact.
- **臭要飯的** (chi: stinking beggar) → actual Cantonese is **死乞兒** (damned/stupid beggar). Both chi and yue ASR transcribe this incorrectly. Render as **"stupid beggar"** in all three variants (not CJK in hybrid).

### How to apply
1. Read chi as primary authority.
2. Cross-check yue for register, specificity, and emotional tone.
3. If yue agrees semantically with chi, trust yue (regardless of surface Cantonese-vs-Mandarin form) and use it for register/wording nuance per rule 2.
4. **If yue diverges semantically from chi, apply the intelligibility gate:**
   - Is yue coherent on its own terms — does it parse as something a character would plausibly say? If **yes**, treat the divergence as authoritative (yue wins; apply rules 5–7 below).
   - Is yue garbled — broken syntax (missing particles, scrambled word order, non-words), or semantically incoherent (real words that don't form a sensible sentence)? If **yes to either**, treat yue as ASR noise, discard it for this sub, fall back to chi.
   - The confidence tier doesn't settle this. Whisper can be HIGH-confident on garbled output; a LOW-tier sub that happens to make sense can still be useful. The reviewer's own read of yue's coherence is the final test.
5. Where yue (passing the intelligibility gate) has a distinctly different word that is more vivid/specific/correct, use yue.
6. Where yue just has a Cantonese phonological variant (e.g. 家散人亡 vs 家破人亡), keep chi.
7. Where yue reveals an OCR error in chi, fix the error (already standard practice).

### Cross-check Mandarin ALWAYS
- Original English often flattens nuance from the Chinese.
- Compare every sub against chi column for lost meaning.
- Example: Ep20 sub 6 — English missed an entire clause present in Mandarin.

### Use Cantonese (yue) for register/tone
- Yue track guides emotional register, colloquial vs formal tone.
- If yue sounds blunt/casual, English should match.
- If yue sounds formal/poetic, English should elevate.

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
- Hybrid uses **娘親** (not 娘) — Cantonese-preferred form.
- "my 娘親" is WRONG (doubles possessive) — use bare 娘親 for address.
- Object context: just "娘親" or descriptive "mother".

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
| 駙馬 / 駙馬爺 | 駙馬 / 駙馬爺 | Prince Consort | Prince Consort |
| 金刀駙馬 | 金刀駙馬 | the Golden Prince Consort | the Golden Prince Consort |
| 晚輩 | 晚輩 | this junior | this junior |
| 後輩 | 後輩 | junior | junior |
| 小王爺 | 小王爺 | the Young Prince | the Young Prince |
| 王子 | 王子 | the Prince | the Prince |
| 公主 | 公主 | Princess | Princess |
| 玄風 (bare) | 玄風 | Jyun-fung | Yuhn-fung |
| 陳玄風 | 陳玄風 | Can Jyun-fung | Chahn Yuhn-fung |

Notes on specific entries:
- **老賊** — literally "Old Thief/Scoundrel", but 梅超風 uses it as an intimate term for her dead husband 陳玄風. Softened to "the Old Man" in romanised. See `REFERENCE.md` for context.
- **駙馬爺** — 蓉兒 uses it sarcastically toward 郭靖.
- **晚輩 / 後輩** — humble self-reference / peer reference when addressing a 前輩.
- **女魔頭** — 梅超風's own self-description in Ep23.

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
師父 · 師兄 · 師弟 · 師姊 · 師妹 · 師叔 · 師姑 · 前輩 · 莊主 · 少莊主 · 幫主 · 祖師爺 · 仙姑 · 駙馬爺 · 王爺 · 小王爺 · 大哥 · 七公 · 島主 · 老伯 · 少爺 · 弟子 · 長老 · 公子

### Address
父王 · 阿爹 · 爹 · 娘親 · 靖哥哥 · 蓉兒 · 靖兒 · 康兒 · 阿靖 · 阿康 · 週大哥 · 黃島主 · 藥師兄 · 歐陽世兄 · etc.

### Places
桃花島 · 桃花陣 · 白駝山 · 歸雲莊 · 牛家村 · 蒙古 · 臨安 · 大理 · 長白山 · 江南 · 岳王廟 · 翠紅樓 · 獅子林 · 山神廟 · 望江樓 · 清溪別院 · etc.

### Sects
全真教 · 丐幫 · 鐵掌幫 · 梅花五毒 · etc.

### Dynasties / countries
大宋 · 宋 · 金 · 金國 · 蒙古

### Terms
九陰真經 · 武穆遺書 · 降龍十八掌 · 蛤蟆功 · 左右互搏 · 空明拳 · 九陰白骨爪 · 輕功 · 江湖 · 武林 · etc.

### Nicknames
老頑童 · 老毒物 · 賴蛤蟆 · 黃老邪 · 老叫化子 · etc.

### Idioms
All 四字成語 found in chi must appear as CJK in hybrid. See §10 for the catalogue.

### Title + name compounds (always CJK as a unit)
岳老伯 · 岳王爺 · 岳大叔 · 黃大叔 · 洪師父 · 黃前輩 · 黃老伯 · etc. NOT "Uncle Yue" / "Uncle Wong" / etc.

### Temple/place full names (always CJK)
岳王廟 · 翠紅樓 · 獅子林 · 山神廟 (not "Yue's Temple" etc.).

### Address terms in direct speech
老伯 · 少爺 · 弟子 · 長老 · 幫主 · 公子 — keep CJK when spoken.

### Standalone idioms
大開殺戒 · 亡國奴 · 劫數難逃 · 各安天命 · 好自為之

---

## 8. Key Translation Conventions

Canonical English renderings for high-frequency terms:

| Chinese | Romanised English |
|---------|-------------------|
| 九陰真經 | the Jiuyin Manual |
| 九陰白骨爪 | the Jiuyin Baigu Claw |
| 武穆遺書 | the Book of Wu Mu |
| 降龍十八掌 | the Eighteen Dragon-Subduing Palms |
| 桃花島 | Peach Blossom Island |
| 全真教 | the Quanzhen Sect |
| 丐幫 | the Beggar Sect |
| 白駝山 | White Camel Mountain |
| 江湖 | the martial world |
| 武林 | the martial world |
| 武功 | martial arts |
| 蒙古 | Mongolia |
| 金國 | Jin |
| 大宋 / 宋 | the Song |
| 望江樓 | Wangjiang Inn |
| 清溪別院 | the Riverside Manor |
| 江南 | Gong-naam (jy) / Gong-naahm (yl) |
| 無毒不丈夫 | ruthlessness is the mark of a great man |
| 雪蓮玉露丸 | the Snow Lotus Jade Pill |
| 雪蓮 | Snow Lotus |
| 梅花五毒 | the Five Plum Blossom Venoms |

---

## 9. Idiom & Cultural Term Rules

### NEVER replace Chinese imagery with Western idioms (default)
- Preserve 四字成語 and 俗語 as Chinese concepts.
- **不見棺材不流淚** → "won't cry till you see the coffin" — NOT "won't believe till it's too late".
- **以牙還牙** → "an eye for an eye" — acceptable because the concept maps cleanly.
- **狗咬呂洞賓** → "biting the hand that feeds you" — acceptable because the concept maps (see `REFERENCE.md`).

Rule of thumb: use a Western equivalent only when the *meaning* maps 1:1; keep Chinese when the *imagery* is the point.

### Hybrid: keep Chinese characters inline

**Preferred format: `English gloss — 中文成語.`** (English first, em-dash, then the Chinese idiom.)

| RIGHT | WRONG |
|-------|-------|
| Who told him to look down on us — 狗眼看人低! | He looked down on us. 狗眼看人低. |
| Think it over carefully — 好自為之. | Think it over. 好自為之. |
| Looks like a major battle — 大開殺戒. | Looks like there's going to be a huge slaughter. |
| I fear my time has come — 劫數難逃. | I fear this is my fate — I won't escape it. |

Alternative inline format also accepted: `後生可畏. Young people are getting capable.` / `別再裝瘋賣傻. Stop playing the fool.`

**Rules:**
- **Never gloss an idiom twice** (once in Chinese AND as a separate English expansion). The English before the dash IS the gloss.
- **Idiom on its own is fine** — if the sub is just an exclamation: "豈有此理!" is acceptable standalone.
- **Don't inject idioms into subs where they don't appear in chi.** Only include idioms that are actually in the source text for that sub.

### Romanised: faithful English translation only
- No Chinese characters in jyutping/yale files.
- The idiom becomes its English rendering.

### Wuxia terms in hybrid
- **輕功** stays as 輕功 (qinggong in romanised).
- **降龍十八掌** stays Chinese in hybrid / "the Eighteen Dragon-Subduing Palms" in romanised.
- **九陰白骨爪** stays Chinese in hybrid / "the Jiuyin Baigu Claw" in romanised.
- **武林** stays Chinese in hybrid / "the martial world" in romanised.

---

## 10. Idioms Encountered (Full Catalogue)

Settled English renderings for idioms encountered across Eps 1–29 (especially the Ep22/23 FULL session). In hybrid, keep the Chinese; in romanised, use the rendering below.

### Military / warfare register
- **投鼠忌器** — "afraid to strike the rat for fear of breaking the vase"
- **敵不動我不動** / **兵家大忌** — "a cardinal error in warfare"
- **打草驚蛇** — "alerting the enemy / tipping them off"
- **單槍匹馬** — "single-handedly"
- **馬到成功** — "success at the first charge" (in hybrid, often as toast: *"To your success — 馬到成功."*)

### Moral/wisdom register
- **人之將死, 其言也善** — "When a man is dying, his words are kind" (hybrid: CJK + gloss on same line)
- **無毒不丈夫** — "ruthlessness is the mark of a great man"
- **不見棺材不流淚** — "won't cry till you see the coffin"
- **一人做事一人當** — "a man answers for his own deeds"
- **罪大惡極** — "utterly wicked"
- **假仁假義** — "false righteousness / hypocrisy"
- **沒齒難忘** — "never to be forgotten"
- **清理門戶** — "set my own house in order"
- **後會有期** — "we will meet again / until we meet again"
- **人死不能復生** — "the dead cannot return"

### Action / urgency
- **事不宜遲** — "we must act at once"
- **死到臨頭** — "in the face of death"
- **夜長夢多** — "delay breeds danger"
- **大功告成** — "the great work is accomplished"
- **碎屍萬段** — "tear to pieces" (keep as CJK in hybrid)
- **萬萬不能** — "absolutely not"

### State of mind / manner
- **婦人之仁** — "a woman's soft-heartedness"
- **死性不改** — "never changes his ways"
- **自身難保** — "I can barely save myself"
- **三番五次** — "time and again"
- **耿耿於懷** — "weighed on his heart"
- **糊裡糊塗** — "muddle-headed"
- **拖泥帶水** — "wishy-washy"
- **傻頭傻腦** — "dim-witted / blockhead"
- **蠻不講理** — "stubborn and unreasonable"
- **平心靜氣** — "calm and composed"
- **全神貫注** — "concentrate fully"
- **諸多顧忌** — "so many scruples"
- **不用拐彎抹角** — "come straight to the point"
- **舉手之勞** — "it was nothing"
- **知心朋友** — "true friend"

### Praise / status
- **寶刀未老** — "the precious blade hasn't aged"
- **彼此彼此** — "same to same" (peer banter between 五絕)
- **爐火純青** — "polished to perfection"
- **中看不中用** — "all show and no substance" (7公's self-deprecating use re 降龍十八掌)
- **英明神武** — "dashing heroism" (often mock-self-praise)
- **艷福** — "luck with women" (7公's wry vocabulary)
- **後生可畏** — "young people are getting capable"
- **臭名遠揚** — "infamous / notoriously known"
- **勢不兩立** — "at odds / cannot coexist"
- **防不勝防** — "impossible to guard against"

### Life / death / devotion
- **精忠報國** — "utmost devotion to the country"
- **延年益壽** — "prolongs one's life"
- **抱頭痛哭** — "embrace and weep"
- **亡國奴** — "slave of a fallen nation"
- **劫數難逃** — "cannot escape one's fate"
- **各安天命** — "each to their own fate"
- **好自為之** — "make your own choices wisely"

### Safety / prudence
- **不怕一萬, 只怕萬一** — "better safe than sorry" (in hybrid couplet: *"不怕一萬, 只怕萬一 — better safe than sorry."*)

### Special cases
- **狗咬呂洞賓** — "biting the hand that feeds you" (Western equivalent acceptable; concept maps)
- **狗眼看人低** — "look down on others"
- **以牙還牙** — "an eye for an eye"
- **大開殺戒** — "a major battle / huge slaughter"
- **豈有此理** — "outrageous / how can this be!"
- **邪中有三分正, 正中帶七分邪** — "three parts righteous in the heresy, seven parts heretical in the righteous" (黃藥師's couplet about 蓉兒). **Keep Chinese in hybrid; English translation only in romanised. Do NOT double-print Chinese + English in romanised.**
- **有失遠迎** — "forgive us for not welcoming you sooner" (standard courtesy)

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
In hybrid, format as CJK line + em-dash + English gloss on the next line. In romanised, English translation only (do not duplicate).

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
- Naming: `{episode}-eng-{variant}.srt`

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
- `瑤迦`, `冠英`, `孫不二` — recurring OCR/name leaks; fold into `cjk_fix_v2.py` properly (identified Ep28 session)
- Classical Chinese phrases left in romanised files → translate to English

### Hybrid-variant duplication trap (IMPORTANT — learned Ep22/23)

When an idiom-plus-gloss is written in the hybrid as `ENGLISH — CJK-idiom` or `CJK-idiom — ENGLISH`, `build.py`'s romanised conversion turns the CJK into English and leaves the English gloss alongside, producing visibly-duplicated lines like:

> "To your success — success at the first charge"
> "Retreat like a subdued dragon, steady and deep — Retreat like a subdued dragon, steady and deep"

**Prevention:** after `build.py` and `cjk_fix_v2.py`, run a targeted pass that looks for em-dash phrases with >60% word overlap on either side and collapses them. The Ep22/23 session built a small fixer for this — consider folding it into `cjk_fix_v2.py` properly.

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
2. **Don't inject idioms into subs where they don't appear in chi.** If 精忠報國 appears in sub 131's chi, put it in sub 131 — don't also scatter it into subs 130, 133, 136.
3. **Don't translate 老伯 / 少爺 / 公子 / 長老 to English in hybrid.** These are address terms.
4. **Don't write "the Song dynasty" when you can write 大宋.** Hybrid means use Chinese.
5. **Don't use excessive exclamation marks.** See §13 quota.
6. **Don't treat Step 3's output as a translation.** It's a mechanical preprocessing pass — CJK substitutions, address-term injection, idiom injection. You must still examine each sub against chi and yue for meaning and register per `PIPELINE.md` Step 4.
7. **Don't gloss an idiom twice** in hybrid (once in Chinese AND as a separate English expansion — see §9).
8. **Don't treat the original English as untouchable, and don't treat it as disposable either.** The priority chain is yue (HIGH) > chi > eng: examine every sub against both chi and yue, and override when content or register mismatches. When the draft is already faithful to both sources, leave it alone.
