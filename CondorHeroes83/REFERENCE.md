# Reference — Tricky Cases, Error Taxonomy, Character Framework

Consolidated from: `TrickyInferences.md`, `ErrorTaxonomy.md`, character-specific scene entries from `StyleRulings.md`'s Ep22–23 append, and the Ep28 correction from `EP28-HANDOFF-NOTES.md`.

This document is lookup material — consult when you hit a specific name, idiom, scene, or error pattern. For rules, see `STYLE.md`. For pipeline mechanics, see `PIPELINE.md`.

---

## Table of Contents

1. [Context-Dependent Name Forms](#1-context-dependent-name-forms)
2. [Difficult Idiom Decisions](#2-difficult-idiom-decisions)
3. [Scene-Specific Judgment Calls](#3-scene-specific-judgment-calls)
4. [Dish Names (Ep21)](#4-dish-names-ep21)
5. [Martial Arts Terms Requiring Context](#5-martial-arts-terms-requiring-context)
6. [The Five Greats (五絕) Framework](#6-the-five-greats-五絕-framework)
7. [Minor Characters](#7-minor-characters)
8. [Error Taxonomy (NewChat vs Experienced Session)](#8-error-taxonomy-newchat-vs-experienced-session)
9. [Key Takeaways for New Session](#9-key-takeaways-for-new-session)

---

## 1. Context-Dependent Name Forms

### 康 (bare character)
- When 楊康 is addressed as just "康" or "阿康" — romanised files use **"Hong" / "Aa-Hong"**.
- When 念慈 or 梅超風 calls him — use the bare form.
- Hybrid: 康 or 阿康.

### 駙馬 / 駙馬爺 / 金刀駙馬
- **駙馬** = Prince Consort (the title given to 郭靖 by 成吉思汗)
- **金刀駙馬** = the Golden Prince Consort (fuller title)
- **蓉兒 uses it sarcastically**: "You're 駙馬爺 again"
- Romanised: "the Prince Consort" / "the Golden Prince Consort"

### 老賊 (梅超風 referring to her dead husband 陳玄風)
- Literally "Old Thief/Scoundrel" — but used as an **intimate term for the deceased**.
- Romanised: **"the Old Man"** (softened, since it's grief-tinged).
- Context example: 梅超風 says *"Ever since 老賊 died, I've been alone."*
- Reconfirmed Ep22 sub 151 and Ep23 sub 98.

### 黃老邪 / 黃小邪 / 老邪 / 死老邪
- **黃老邪** = Old Heretic Wong (黃藥師's nickname).
- **黃小邪** = Little Heretic Wong (蓉兒 playfully calls herself this).
- **老邪** = Old Heretic (informal short form used by 洪七公).
- **死老邪** = "damned Old Heretic" (洪七公's playful insult to 黃藥師, Ep23 sub 176).
- Hybrid: keep Chinese. Romanised: per the table above.

### 七兄 (黃藥師 addressing 洪七公)
- **"Brother Seven"** — a respectful peer-level address between the Five Greats.
- Romanised: "Brother Seven".

### 小弟 (黃藥師's self-deprecating form)
- **"this humble one"** — used when conceding a point in a duel.
- NOT a name — a pronoun of modesty.

### 晚輩 vs 後輩
- **晚輩** → "this junior" (self-referential humble form when addressing a 前輩).
- **後輩** → "junior" (peer/referent form).
- Hybrid keeps CJK.

---

## 2. Difficult Idiom Decisions

### 狗咬呂洞賓 (Ep22)
- Literal: "a dog biting Lü Dongbin" (biting the hand of a deity who helps).
- Used: **"biting the hand that feeds you"**.
- Decision: **Western equivalent acceptable here** because the concept maps perfectly.

### 投鼠忌器 (Ep22)
- Literal: "afraid to throw at the rat for fear of breaking the vase".
- Used: preserved as Chinese idiom with gloss in hybrid.
- Romanised: *"afraid to strike the rat for fear of breaking the vase"*.

### 敵不動我不動 (Ep22)
- Military maxim: "if the enemy doesn't move, neither do I".
- Kept as Chinese in hybrid; translated in romanised.

### 人之將死, 其言也善 (Ep22)
- **"When a man is dying, his words are kind."**
- From the *Analects*. 洪七公's deathbed line in Ep22 sub 469.
- Hybrid: Chinese + English on same line.

### 邪中有三分正, 正中帶七分邪 (Ep23)
- 黃藥師 describing his daughter: "The heretical are three parts righteous; the righteous are seven parts heretical!"
- Kept Chinese in hybrid; translated in romanised.
- **Do NOT double-print Chinese + English in romanised.**

### 精忠報國
- "Utmost devotion to the country."
- Ep20 sub 131 — the yue track restores this from the chi OCR.

### 臭要飯的 → 死乞兒
- chi (OCR) says 臭要飯的 "stinking beggar"; actual Cantonese is **死乞兒** "damned/stupid beggar". Both chi and yue ASR transcribe incorrectly.
- Render as **"stupid beggar"** in all three variants; **not CJK in hybrid** (because the chi is wrong and 死乞兒 never actually appears cleanly).

### 推宮換血 vs 推功換血 (Ep24 session — Rule B case study)
- Chi: **推宮換血** — the canonical wuxia technique for transfusing internal energy and exchanging blood. 宮 = the body's twelve main acupoints/palaces.
- Yue (HIGH): **推功換血** — a phonological ghost. 功 and 宮 are both `gung1` in Cantonese; Whisper heard the homophone.
- **Decision: chi wins.** These are different compounds, not register variants — Rule A doesn't apply. Rule B says chi wins semantic disagreements by default, and there's no independent corroboration (eng, cross-episode, visible OCR) for yue here.
- This is the prototypical Rule B case: a HIGH-confidence yue homophone of a fixed 四字成語. Named wuxia techniques are especially prone to this because they're fixed compounds where any one-character variation is almost certainly an ASR slip, not a real alternate reading.

### 小保 (Ep24 — cautionary note on cross-episode canonicality)
- Chi (Ep24 subs 155, 161): **小保** — this is the correct name of the boy whose cakes 楊康 stole.
- **The v2 attempt to "correct" this to 小寶 via cross-episode canonicality was wrong.** There was no prior FULL episode establishing 小寶 as this character's name; the reasoning appealed to a canonical form that didn't actually exist.
- Takeaway: the cross-episode-canonicality backstop (see Rule B in `STYLE.md` §2) is only valid when a prior FULL episode has actually established the canonical form. It is not a license to substitute a form the reviewer thinks ought to be canonical. If in doubt, chi wins — that's what Rule B defaults to, and Rule B got the right answer here before the spurious override.
- Use **小保** / **Siu-bou**.

---

## 3. Scene-Specific Judgment Calls

### 華箏 poisoning 洪七公's wine (Ep22)
- 華箏 is coerced by 歐陽克 to poison 洪七公 to save 拖雷.
- Her guilt dialogue must convey **genuine anguish**, not cold calculation.
- Example line: *"阿靖, if I ever do something to let you down — will you forgive me?"*

### 蓉兒 saving 華箏 (Ep23)
- 蓉兒 says she wants 華箏 to die sooner — but actually cures her.
- The key line: *"I'm curing her because I want you to be happy."*
- Register: **bratty on the surface, deeply generous underneath**.
- Her "I want her to die sooner" (Ep23 sub 37) is said *while curing* 華箏 — the contradiction IS the character. Don't soften; don't over-explain. Sub 43 is the emotional hinge.

### 華箏's suicide attempt (Ep23 subs 420–440)
- Comes from the folk-story logic she invokes (the 法師 story), not from melodrama.
- Render the 法師 story plainly. 蒙古 directness.

### 楊康's repentance arc (Ep24)
- His confession to 念慈: *"I was just toying with you. Using you. I never loved you."*
- This is 楊康 trying to push 念慈 away **to protect her** — NOT a genuine confession.
- 念慈's response: *"I was willing to be deceived"* (甘心被你欺騙).
- Register must convey that **both know the truth beneath the words**.

### 黃藥師 meeting 郭靖 (Ep23)
- 黃藥師 hates formality: *"前輩? 後輩? How annoying."*
- 郭靖 tries 黃老伯 → "Am I that old?"
- The comedy comes from **郭靖's earnest cluelessness vs 黃藥師's prickliness**.
- His *"前輩, 後輩 — how tedious"* (Ep23 212) and *"老邪, 老邪 — let the young ones off"* are comedy-of-register.
- His couplet about his daughter (263) is **genuine admiration dressed as taunt**.

### 洪七公's food-for-teaching bargain (Ep21)
- *"One dish, one move. Four dishes, four moves."*
- 洪七公 pretends to resist: *"I have my reasons for teaching him — I want him to learn enough to deal with you, you brat."*
- Register: **gruff affection masked as self-interest**.
- "Two things I fear — no food, and these love affairs" (Ep23 331–333) is self-mockery masking real care. His pretend-ignorance about romance is a bit.

### 歐陽克 coercing 華箏 (Ep22 11–32)
- Should read as **polite-on-the-surface / deadly-underneath**. He doesn't raise his voice. Smooth menace.

### 梅超風 (Ep23 dialogue)
- Her Ep23 dialogue about 老賊, 金國 upbringing, and being called 走狗 is **character-defining** — don't flatten to generic villainy. Resentment-tinged loyalty.

### 黃藥師 couplet about 蓉兒 (Ep23 sub 263)
- **邪中有三分正, 正中帶七分邪** — see §2. Genuine admiration in the form of a taunt.

---

## 4. Dish Names (Ep21)

These appear in 黃蓉's cooking scenes. **Keep Chinese in hybrid; translate in romanised.**

| Chinese | English |
|---------|---------|
| 百花雞 | Hundred Flowers Chicken |
| 釀鴨舌 | Stuffed Duck Tongue |
| 龍門活鯉 | Live Longmen Carp |
| 珍珠魚眼羹 | Pearl Fish-Eye Soup |
| 龍虎鳳燴石班 | Dragon-Tiger-Phoenix Garoupa |
| 龍 = 百花蛇 | flower snake |
| 虎 = 果子狸 | masked civet |
| 鳳 = 竹絲雞 | silkie chicken |

---

## 5. Martial Arts Terms Requiring Context

### 降龍十八掌 sub-moves (Ep22)
- **亢龍有悔** = the Regretful Dragon
- **躍龍在淵** = the Leaping Dragon in the Abyss

### Poetic chant (Ep22 subs 428–431)
- **去似天龍雲飛躍** = "Go like a heavenly dragon soaring through clouds"
- **收似降龍穩深沈** = "Retreat like a subdued dragon, steady and deep"
- **腳似飛龍騰萬里** = "Kick like a flying dragon spanning ten thousand li"
- **拳似怒龍翻四海** = "Punch like an angry dragon overturning the four seas"

In hybrid, format as CJK line + em-dash + English gloss on the next line. In romanised, English translation only — do not duplicate. See `STYLE.md` §19 (hybrid-variant duplication trap).

### Meditation / qi instructions (Ep21–22)
- **氣聚丹田** = "Qi gathers at the dantian"
- **神注印堂** = "Spirit focuses at the yintang"
- **會陰** = Huiyin (acupoint)
- **曲池** = Quchi (acupoint)
- **靈台穴** = the Lingtai point
- **乾位** = qian position (trigram)
- **全神貫注** = "concentrate fully"
- **歸元丹田** = "return to the dantian"
- **陰柔** = yin-soft (energy quality)

### 推宮換血 (Ep24)
- Blood transfusion technique from *黃帝內經*.
- The healer absorbs the patient's poison and dies.
- Keep Chinese in hybrid; **"a blood transfusion"** in romanised.

### 雪蓮玉露丸 / 雪蓮 (Ep23)
- **雪蓮玉露丸** = "the Snow Lotus Jade Pill" — 黃藥師's gift in Ep23.
- **雪蓮** alone = "Snow Lotus".

### 梅花五毒
- "The Five Plum Blossom Venoms" — the group of poisoners who once attacked 洪七公.

---

## 6. The Five Greats (五絕) Framework

| Title | Name | Jyutping | Yale |
|-------|------|----------|------|
| 東邪 Eastern Heretic | 黃藥師 | Wong Joek-si | Wong Yeuhk-si |
| 西毒 Western Venom | 歐陽峰 | Au-Joeng Fung | Au-Yeung Fung |
| 南帝 Southern Emperor | 一燈 | Jat-Dang | Yat-Dang |
| 北丐 Northern Beggar | 洪七公 | Hung Cat-gung | Huhng Chat-gung |
| 中神通 Central Divine | 王重陽 | Wong Cung-joeng | Wong Chung-yeung |

Peer-level address between the Five Greats uses **brother + ordinal** (e.g. **七兄** = "Brother Seven"), and their peer banter often uses **彼此彼此** (*"same to same"*).

---

## 7. Minor Characters

| Chinese | Hybrid | Romanised | Notes |
|---------|--------|-----------|-------|
| 博將軍 | 博將軍 | General Bo | 蒙古 officer |
| 赤將軍 | 赤將軍 | General Chi | 蒙古 officer |
| 彭寨主 | 彭寨主 | Stockade Master Pang (jy) / Pahng (yl) | |
| 沙通天 | (keep full name) | via PersonalNames | |
| 靈智上人 | 靈智上人 | via PersonalNames | keep CJK in hybrid |
| 彭連虎 | 彭連虎 | via PersonalNames | keep CJK in hybrid |
| 陳玄風 | 陳玄風 | Can Jyun-fung / Chahn Yuhn-fung | full name |
| 玄風 (bare) | 玄風 | Jyun-fung (jy) / Yuhn-fung (yl) | when called bare |

---

## 8. Error Taxonomy (NewChat vs Experienced Session)

Based on 464 differences across 538 subs in Episode 28 — concrete examples of what goes wrong when a session uses the handoff documents but lacks deep processing experience.

### Summary of Error Types

| Category | Count | Severity |
|----------|-------|----------|
| FABRICATION | 0 (audited) | CRITICAL — invented content. Original Ep28 taxonomy flagged 2, both were re-examined and neither was a true fabrication (Sub 22 confirmed by yue; Sub 316 was a reflow duplication, not invented content). Category retained because the error class is real and the pipeline must guard against it — see below. |
| CHI_MEANING_LOST | 159 | HIGH — original English kept when Chinese has richer/different meaning |
| NAME_TITLE_LEAK | 63 | HIGH — English names/titles where hybrid needs Chinese |
| IDIOM_MISSING | 18 | MEDIUM — Chinese idioms omitted from hybrid |
| FORMATTING_ONLY | 100 | LOW — just punctuation/line-break differences |
| MINOR_WORDING | 124 | LOW — small preference differences |

---

### CATEGORY 1 — FABRICATION (CRITICAL)

The English track sometimes contains content that is NOT supported by either the Mandarin source *or* the yue track. Cross-check against both and remove fabricated content.

**Rule:** If the English says something that appears in neither chi nor yue, delete it. Verify against **both** tracks before deleting — chi alone is not sufficient evidence.

**Ep28 Sub 22 case study (how this rule works correctly):** An earlier taxonomy flagged Sub 22 as a fabrication — *"But these are snakes from 白駝山 that are fed poisonous scorpions daily"* — on the basis that "poisonous scorpions" wasn't in chi. **But yue (HIGH confidence) had 每日用一隻毒蝎嚟養大.** Eng was right; chi had an OCR error or gap. Single-track (chi-only) comparison would have deleted correct content. Three-track comparison catches the OCR case and preserves what's real.

Two takeaways:
- **Yue is the witness when eng and chi disagree.** If yue confirms eng, treat chi as corrupted and keep eng.
- **The bar for "fabrication" is high.** If *any* source supports the content, it's not a fabrication — it may be a register mismatch or meaning shift (Category 2), but not an invention to be deleted.

---

### CATEGORY 2 — CHI_MEANING_LOST (HIGH — 159 instances)

This is the single biggest problem. A new session defaults to keeping the original English, missing meaning present in the Mandarin.

**Rule:** The original English is a draft, not a finished translation. Examine every sub against chi and yue; when the English misses meaning present in the sources (or register present in yue), override it to restore what's lost.

**Example — Sub 7:**
- WRONG: "Luckily, Miss Cheng threw a stool at him"
- CHI: 幸虧大小姐人奮不顧身 拿張飲子扔了過去
- RIGHT: "Luckily, the young mistress fought back bravely and threw a stool at him."
- Lost: **奮不顧身** (fought back bravely / risked her life), **大小姐** (young mistress, not "Miss Cheng")

**Example — Sub 10:**
- WRONG: "He became very angry"
- CHI: 他好像很生氣
- RIGHT: "He seemed very angry" (好像 = "seemed", not "became" — different certainty level)

**Example — Sub 12:**
- WRONG: "Who do you think is responsible?"
- CHI: 仙姑, 依你看是哪路人馬幹的
- RIGHT: "仙姑, who do you think is responsible?" (dropped address term)

**Example — Sub 36:**
- WRONG: "陸乘風 is a disciple of the lord of 桃花島"
- CHI: 陸乘風那個老賊 是桃花島島主的傳人
- RIGHT: "陸乘風, that old scoundrel, is a disciple of the master of 桃花島."
- Lost: **那個老賊** (that old scoundrel) — entire characterisation dropped

**Example — Sub 72:**
- WRONG: "Father is just waiting for teacher to go retrieve the antidote"
- CHI: 爹是一心一意去給我找解藥的
- RIGHT: "阿爹 is set on finding me the antidote." (**一心一意** = single-mindedly determined)

**Example — Sub 135:**
- WRONG: "that old scoundrel Cheng wouldn't come and beg me for it"
- CHI: 程老頭也不會對我那麼低聲下氣了
- RIGHT: "that old scoundrel 程 wouldn't have grovelled so" (**低聲下氣** = grovelling / humbling oneself)

---

### CATEGORY 3 — NAME/TITLE LEAK (HIGH — 63 instances)

In hybrid mode, names and titles must be in Chinese characters. New sessions frequently leave English names where Chinese was needed.

**Rule:** In hybrid, ALL names = Chinese characters. ALL titles = Chinese characters. **No exceptions.**

**Common leaks found:**
- "Father" → should be 阿爹 (when used as address)
- "teacher" / "my teacher" → should be 師父
- "Brother Lu" → should be 陸師兄 or 陸兄
- "Miss Huang" → should be 黃姑娘
- "Old Master Lu" → should be 陸前輩
- "White Camel Mountain" → should be 白駝山
- "Peach Blossom Island" → should be 桃花島
- "Lu family" → should be 陸 family (surname in Chinese)
- "Cheng family" → should be 程 family
- "Grand Teacher" → should be 祖師爺
- "Cloud Manor" → should be 歸雲莊

---

### CATEGORY 4 — IDIOM MISSING (MEDIUM — 18 instances)

Hybrid subs should include Chinese idioms inline with English glosses. New sessions tend to drop them.

**Rule:** When a 四字成語 or common phrase appears in the Chinese, include it in hybrid format: `"Chinese gloss."` or `"English gloss — 中文."`

**Examples of missed idioms (full catalogue in `STYLE.md` §10):**
- **防不勝防** → should appear as "防不勝防." after "impossible to guard against"
- **臭名遠揚** → should appear after "infamous"
- **勢不兩立** → should appear after "at odds"
- **沒齒難忘** → should appear after "I will never forget"
- **不用拐彎抹角** → should appear before "Come straight to the point"
- **舉手之勞** → should appear after "It was nothing"
- **人死不能復生** → should appear before "The dead cannot return"
- **後會有期** → should appear instead of "We will meet again"
- **萬萬不能** → should appear after "Absolutely not"
- **知心朋友** → should appear after "true friend"

---

### CATEGORY 5 — FORMATTING (LOW — 100 instances)

Just punctuation marks, em-dashes vs hyphens, line-break placement. Not substantive.

---

### CATEGORY 6 — MINOR WORDING (LOW — 124 instances)

Small preference differences like "Don't worry. They won't fight" vs "Don't worry. / They won't fight." or "I have no reason to lie" vs "I don't have to lie to you". Both acceptable.

---

## 9. Key Takeaways for New Session

1. **Examine every sub.** Read every sub against chi and yue (priority: yue HIGH > chi > eng); override when content or register mismatches, otherwise leave the English alone. The failure mode to avoid is the opposite pair: a new session overrode only ~200 of 538 subs in Ep28 because it treated the English as untouchable, while an over-eager session can degrade quality by rewriting subs that were already faithful. Examine all, override selectively.

2. **Chi is authority, English is draft.** When they conflict, chi wins. When English adds content not in chi, delete it (but first check yue — Ep28 Sub 22 above). When English flattens chi meaning, restore it.

3. **Hybrid means Chinese characters.** Every name, every title, every place, every idiom — Chinese characters in hybrid. Scan after building for any English proper nouns that should be Chinese.

4. **Idioms are not optional.** When chi contains a 四字成語, hybrid MUST include it. Format: `"English gloss — 中文成語."` (preferred) or `"中文成語. English gloss."`.

5. **Read the detail.** 好像 ≠ became (it means "seemed"). 大小姐 ≠ "Miss Cheng" (it means "young mistress"). 一心一意 ≠ "just waiting" (it means "single-mindedly determined"). These nuances matter.

6. **Preserve Step 3's output for empty/bare-name chi subs.** Don't project speakers when chi gives you nothing — see `PIPELINE.md` Step 4 (name-swap bug).

7. **Trust yue for register (Rule A), not for semantic arbitration (Rule B).** Yue wins when yue and chi are *synonyms* but yue is more vivid/colloquial (古惑 over 鬼主意, 淒涼 over 可憐). Yue does **not** win when yue and chi are *different words* — that's a semantic disagreement, and chi (the written semantic authority) wins by default, because yue reaches us through ASR and is subject to homophone errors (功/宮 both `gung1`; 保/寶 both `bou2`). Override chi semantically only when eng, cross-episode canonicality, or a visible chi OCR artefact corroborates yue. The intelligibility gate still gates both rules: if yue is garbled, ignore yue regardless of tier. See `STYLE.md` §2 for the full decision procedure.
