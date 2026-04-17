# Style Rulings — Legend of the Condor Heroes (射鵰英雄傳) 1983 TVB
## Accumulated decisions from Episodes 1–24 and 27

---

## 1. Three Output Variants

| Variant | Names | Honorifics | Idioms | File suffix |
|---------|-------|------------|--------|-------------|
| **eng-hybrid** | Chinese characters (郭靖) | Chinese characters (師父) | Chinese inline + English gloss | `-hybrid.srt` |
| **eng-jyutping** | Jyutping romanisation (Gwok Zing) | Natural English (Master) | Faithful English only | `-jyutping.srt` |
| **eng-yale** | Yale romanisation (Gwok Jing) | Natural English (Master) | Faithful English only | `-yale.srt` |

---

## 2. Name Rules

### 阿-prefix (CRITICAL)
- **ONLY** in direct address (vocative): "阿靖!" when calling someone
- **NEVER** in object/possessive/descriptive context: "real father" not "real 阿爹" (descriptive modifier = object)
- Example: "阿爹!" (calling out ✓) vs "your father's temper" (reference ✓) vs "your 阿爹's temper" (WRONG ✗)

### 靖哥哥 / 蓉兒 romanisation
- Jyutping: Zing-gogo / Jung-ji (NO extra dash: gogo not go-go)
- Yale: Jing-gogo / Yuhng-yi (same: gogo not go-go)
- Hybrid: Chinese characters always

### 七仔 vs 老七
- 洪七公 calls himself 七仔 in Cantonese (NOT 老七)
- Use 七仔 in hybrid ONLY when dialogue explicitly says 老七/七仔
- Romanised: "Little Seven" (not "Old Seven")
- Do NOT use 七仔 as a general substitute for 洪七公 elsewhere
- Flag every occurrence for user checking

### Rong-er must NEVER appear in hybrid
- Always 蓉兒 in hybrid. Rong-er is Pinyin leakage.

### Compound names convert before bare characters
- 梅師姊 → "Senior Sister Mui" must convert before bare 梅
- 歐陽公子 → "Young Master Au-Joeng" before bare 歐陽

---

## 3. Kinship & Address Terms

### 娘親 rule
- Hybrid uses 娘親 (not 娘) — Cantonese-preferred form
- "my 娘親" is WRONG (doubles possessive) — use bare 娘親 for address
- Object context: just "娘親" or descriptive "mother"

### Descriptive kinship terms
- 養父/義父 → "foster father" ALWAYS in all three variants
- Never keep Chinese for descriptive kinship (養母→"foster mother", etc.)

### 阿爹 in romanised files
- Converts to "Father" (not romanised)

### Title conversion in romanised files
| Chinese | Jyutping/Yale English |
|---------|----------------------|
| 師父 | Master |
| 師姊 | Senior Sister |
| 師妹 | Junior Sister |
| 大哥 | Big Brother |
| 前輩 | senior |
| 七公 | Seven Elder |
| 幫主 | the Chief |
| 小王爺 | the Young Prince |
| 王子 | the Prince |
| 公主 | the Princess |
| 閻王爺 | the King of Hell |
| 老叫化子 | Old Beggar |
| 丘道長 | Taoist Jau (Jyutping) / Taoist Yau (Yale) |
| 阿彌陀佛 | Amitabha |
| 黃姑娘 | Miss Wong |
| 穆姑娘 | Miss Muk |
| 郭大哥 | Brother Gwok |
| 歐陽兄 | Brother Au-Joeng (J) / Brother Au-Yeung (Y) |
| 洪前輩 | Senior Hung (J) / Senior Huhng (Y) |
| 黃老邪 | Old Heretic Wong |
| 老邪 | Old Heretic |

---

## 4. Idiom & Cultural Term Rules

### NEVER replace Chinese imagery with Western idioms
- Preserve 四字成語 and 俗語 as Chinese concepts
- 不見棺材不流淚 → "'won't cry till you see the coffin'" NOT "won't believe till it's too late"
- 以牙還牙 → "an eye for an eye" (acceptable because the concept maps)

### Hybrid: keep Chinese characters inline
- Format: "Chinese English-gloss" e.g. "後生可畏. Young people are getting capable."
- Or: "別再裝瘋賣傻. Stop playing the fool."

### Romanised: faithful English translation only
- No Chinese characters in jyutping/yale files
- Idiom becomes its English rendering

### Wuxia terms in hybrid
- 輕功 stays as 輕功 (qinggong in romanised)
- 降龍十八掌 stays in Chinese (hybrid) / "the Eighteen Dragon-Subduing Palms" (romanised)
- 九陰白骨爪 → stays Chinese (hybrid) / "the Jiuyin Baigu Claw" (romanised)
- 武林 → stays Chinese (hybrid) / "the martial world" (romanised)

---

## 5. Translation Quality Rules

### Cross-check Mandarin ALWAYS
- Original English often flattens nuance from the Chinese
- Compare every sub against chi column for lost meaning
- Example: Ep20 sub 6 — English missed entire clause present in Mandarin

### Use Cantonese (yue) for register/tone
- Yue track guides emotional register, colloquial vs formal tone
- If yue sounds blunt/casual, English should match
- If yue sounds formal/poetic, English should elevate

### DO NOT use placeholder patterns
- Never use "— 蓉兒.\n— 靖哥哥." as a default placeholder — caused 79 wrong subs in Ep20

---

## 6. Conversion Order (CRITICAL)
Process in this order to avoid partial matches:
1. Idioms (longest first)
2. Terms (longest first)
3. Titles/honorifics (longest first, compounds before bare)
4. Names (longest first, compounds before single characters)

---

## 7. Duration Extension System

| Parameter | Value |
|-----------|-------|
| Target reading speed | 15 English characters/second |
| Minimum duration | 1000ms |
| Yue speech guide | Use Cantonese track end times as reference |
| Hard cap | Never extend past next subtitle's start time |
| Overlap rule | Zero overlaps allowed |

---

## 8. Index/Timecode Preservation
- Output must have EXACTLY the same subtitle count and indices as the original eng.csv
- Same number of SRT entries, same index numbers
- Timecodes may be extended (per duration rules) but start times preserved

---

## 9. Output Format
- Full SRT format
- UTF-8 encoding
- Saved to /mnt/user-data/outputs/
- Naming: `{episode}-eng-{variant}.srt`

---

## 10. Known Recurring Issues
- **Pinyin leakage**: Scan hybrid files after build for any Pinyin names (Guo Jing, Rong-er, etc.)
- **CJK in romanised files**: Scan jyutping/yale files for any remaining Chinese characters after conversion
- **go-go dash**: Check all gogo compounds have no extra dash
- **Bare surname fragments**: 洪Seven Elder → must be Hung Seven Elder (jyutping) / Huhng Seven Elder (yale)
- **康 bare character**: When 楊康 is called just 康, romanised must be "Hong" not left as Chinese

---

## Yue-Authority Rule (Added Ep27 session)

**When yue gives a more vivid, specific, or colloquial word than chi, and it is not an OCR error, yue overrides chi.** This is because the yue track is the actual spoken Cantonese dialogue of a Cantonese show. The chi (Mandarin) track is a written translation that sometimes flattens the spoken register.

### Examples:
- **古惑** (yue: crafty/street-smart) overrides **鬼主意** (chi: cunning schemes) — 古惑 is the word actually spoken
- **淒涼** (yue: desolate/forlorn) overrides **可憐** (chi: pitiful) — 淒涼 is emotionally stronger
- **開心** (yue: happy) overrides **瞑目** (chi: rest in peace) — 開心 is warmer, more colloquial
- **好像** (yue: seemed) vs **非常** (chi: very) — yue preserves certainty level
- **抵死** (yue: deserve to die, Cantonese colloquial) — inject as CJK with gloss
- **百世千孫** (yue: descendants for a hundred generations) — yue adds obsequious detail chi omits
- **叫化子/叫化** (chi: Mandarin for beggar) → always use Cantonese forms in hybrid: **老叫化子** → **乞兒仔**, **老叫化** → **老乞兒**, **叫化子窩** → **乞兒窩**. The show is Cantonese — 叫化 is a Mandarin subtitle artefact.
- **臭要飯的** (chi: stinking beggar) → actual Cantonese is **死乞兒** (damned/stupid beggar). Both chi and yue ASR transcribe this incorrectly. Render as "stupid beggar" in all three variants (not CJK in hybrid).

### How to apply:
1. Read chi as primary authority
2. Cross-check yue for register, specificity, and emotional tone
3. Where yue has a distinctly different word that is MORE vivid/specific/correct, use yue
4. Where yue just has a Cantonese phonological variant (e.g. 家散人亡 vs 家破人亡), keep chi
5. Where yue reveals an OCR error in chi, fix the error (this is already standard practice)

---

## Ep22–23 Session Decisions (Added 2026-04-15)

Micro-decisions made during the Ep22+23 GOLD session. Fold into relevant sections above when convenient; until then, treat as authoritative.

### Place names
- **望江樓** → "Wangjiang Inn" (romanised). Hybrid keeps CJK.
- **清溪別院** → "the Riverside Manor" (romanised). 歐陽克's hideout mentioned in Ep22.
- **白駝山** → already codified: keep CJK in hybrid; "White Camel Mountain" in romanised.
- **桃花島** → already codified: keep CJK in hybrid; "Peach Blossom Island" in romanised.
- **蒙古** → "Mongolia" in romanised. Hybrid keeps CJK (per dynasty/country rule).
- **金國** → "Jin" in romanised. Hybrid keeps CJK. Note: 金國太子 → "the Prince of Jin" in romanised; hybrid keeps the whole CJK string.
- **江南** → hybrid keeps CJK. Romanised: Gong-naam (jy) / Gong-naahm (yl).

### Titles and address
- **洪師父** → "Master Hung" (jy) / "Master Huhng" (yl). Used when 梅超風 addresses 洪七公 in Ep23 sub 4. Hybrid keeps CJK.
- **洪前輩** → "Senior Hung" / "Senior Huhng". Hybrid keeps CJK.
- **黃前輩** → "Senior Wong". Used by 郭靖 meeting 黃藥師.
- **黃老伯** → "Old Uncle Wong". Brief address 郭靖 tries before being mocked.
- **老伯** (vocative alone) → "old uncle". Hybrid keeps CJK per 老伯 rule.
- **駙馬 / 駙馬爺 / 金刀駙馬** → "Prince Consort" / "Prince Consort" / "the Golden Prince Consort" in romanised. Hybrid keeps CJK. 蓉兒 uses 駙馬爺 sarcastically.
- **晚輩** → "this junior" (romanised). Hybrid keeps CJK. Self-referential humble form when addressing a 前輩.
- **後輩** → "junior" (romanised). Hybrid keeps CJK.
- **小王爺** → already codified: "the Young Prince" in romanised.
- **老賊** → "the Old Man" in romanised (grief-softened for 梅超風's dead husband 陳玄風). Already in TrickyInferences — reconfirmed Ep22 sub 151 and Ep23 sub 98.
- **楊大叔 / 楊大嫂** → "Uncle Yeung" / "Mrs Yang". Already in config — reconfirmed Ep22 sub 478.

### Character-specific
- **黃小邪** → "Little Heretic Wong". Already in TrickyInferences; used by 蓉兒 self-referentially in Ep23 sub 14.
- **死老邪** → "damned Old Heretic". 洪七公's playful insult to 黃藥師 in Ep23 sub 176. CJK in hybrid, English in romanised.
- **女魔頭** → "she-demon". 梅超風's self-description in Ep23.
- **阿康** → already codified: Aa-Hong (jy) / Aa-Hong (yl). Reconfirmed Ep22 sub 422 (梅超風 calling 楊康).

### Idioms encountered and settled
- **狗咬呂洞賓** → "biting the hand that feeds you" (Western equivalent acceptable because the concept maps — already in TrickyInferences).
- **投鼠忌器** → "afraid to strike the rat for fear of breaking the vase". Kept as Chinese idiom with English gloss.
- **敵不動我不動** / **兵家大忌** → "a cardinal error in warfare" — the military register of the Five Greats / 歐陽克.
- **人之將死, 其言也善** → "When a man is dying, his words are kind". 洪七公's deathbed line in Ep22 sub 469. Hybrid: CJK + gloss together on same line.
- **馬到成功** → "success at the first charge" (romanised); in hybrid, use as toast: "To your success — 馬到成功."
- **事不宜遲** → "we must act at once" (romanised).
- **死到臨頭** → "in the face of death" (romanised).
- **夜長夢多** → "delay breeds danger" (romanised).
- **婦人之仁** → "a woman's soft-heartedness" (romanised).
- **死性不改** → "never changes his ways" (romanised).
- **有失遠迎** → "forgive us for not welcoming you sooner" (romanised). Standard courtesy phrase.
- **碎屍萬段** → "tear to pieces" (romanised). Kept as CJK idiom in hybrid.
- **自身難保** → "I can barely save myself" (romanised).
- **三番五次** → "time and again" (romanised).
- **耿耿於懷** → "weighed on his heart" (romanised).
- **糊裡糊塗** → "muddle-headed" (romanised).
- **拖泥帶水** → "wishy-washy" (romanised). 蓉兒 using it about 七公.
- **大功告成** → "the great work is accomplished" (romanised).
- **不怕一萬, 只怕萬一** → "better safe than sorry". The couplet form in hybrid: "不怕一萬, 只怕萬一 — better safe than sorry."
- **寶刀未老** → "the precious blade hasn't aged". 黃藥師 complimenting 七公.
- **彼此彼此** → "same to same". Peer banter between 五絕.
- **爐火純青** → "polished to perfection".
- **中看不中用** → "all show and no substance". Used self-deprecatingly by 七公 about his own 降龍十八掌.
- **一人做事一人當** → "a man answers for his own deeds". 郭靖's noble self-sacrifice line when facing 黃藥師.
- **罪大惡極** → "utterly wicked". 七公 defending 郭靖's killing of 陳玄風.
- **假仁假義** → "false righteousness / hypocrisy". 黃藥師's dismissal.
- **沒齒難忘** → "never to be forgotten". 梅超風's gratitude to 黃藥師.
- **清理門戶** → "set my own house in order". 黃藥師 about disciplining 梅超風.
- **延年益壽** → "prolongs one's life". Describes the 雪蓮玉露丸.
- **抱頭痛哭** → "embrace and weep". 蓉兒 teasing about what normal reunions look like.
- **傻頭傻腦** → "dim-witted / blockhead". 黃藥師 about 郭靖.
- **蠻不講理** → "stubborn and unreasonable". Self-description by 黃藥師.
- **英明神武** → "dashing heroism". 七公's mock self-praise.
- **艷福** → "luck with women" (romanised). 七公's wry vocabulary.
- **平心靜氣** → "calm and composed".
- **全神貫注** → "concentrate fully".
- **歸元丹田** → "return to the dantian".
- **單槍匹馬** → "single-handedly".
- **打草驚蛇** → "alerting the enemy / tipping them off".
- **諸多顧忌** → "so many scruples".
- **邪中有三分正, 正中帶七分邪** → "three parts righteous in the heresy, seven parts heretical in the righteous". 黃藥師's famous couplet about his daughter — already in TrickyInferences. Keep Chinese in hybrid; English translation only in romanised. **Do NOT double-print the Chinese+English in the romanised variant.**

### Martial arts / wuxia
- **九陰白骨爪** → "the Jiuyin Baigu Claw" (romanised).
- **九陰真經** → "the Jiuyin Manual" (romanised). Already codified.
- **降龍十八掌** → "the Eighteen Dragon-Subduing Palms" (romanised). Already codified.
- **亢龍有悔** → "the Regretful Dragon" (already in TrickyInferences).
- **躍龍在淵** → "the Leaping Dragon in the Abyss" (already in TrickyInferences).
- **內力** → "internal strength".
- **內功** → "internal energy".
- **內傷** → "internal injury".
- **武功** → "martial arts" (romanised). Already codified.
- **武林** → "the martial world" (romanised). Already codified.
- **任督二脈** → "the Ren and Du meridians".
- **靈台穴** → "the Lingtai point".
- **曲池穴** → "the Quchi point". Already codified.
- **陰柔** → "yin-soft".
- **梅花五毒** → "the Five Plum Blossom Venoms". The group of poisoners who once attacked 洪七公.
- **雪蓮玉露丸** → "the Snow Lotus Jade Pill". 黃藥師's gift in Ep23. 雪蓮 alone → "Snow Lotus".
- **Dragon chant quartet (Ep22 subs 428–431)** — already in TrickyInferences. In hybrid, format as CJK line + em-dash + English gloss on the next line. In romanised, English translation ONLY (do not duplicate).

### Sects / groups
- **丐幫** → "the Beggar Sect" (romanised). Hybrid keeps CJK.
- **乞兒** (yue form) → "beggar" (romanised). Hybrid keeps CJK when spoken.
- **乞姨婆** (yue: beggar woman) — 梅超風 uses this in Ep23 subs 110, 112.

### Other characters / minor
- **博將軍** → "General Bo". 赤將軍 → "General Chi". Both keep CJK in hybrid; both are 蒙古 officers.
- **彭寨主** → "Stockade Master Pang" (jy) / "Stockade Master Pahng" (yl).
- **沙通天** → name stays; romanised from PersonalNames.
- **靈智上人** → keep CJK in hybrid; romanise via PersonalNames.
- **彭連虎** → keep CJK in hybrid.
- **陳玄風** → keep CJK in hybrid; the full name. Bare 玄風 → Jyun-fung (jy) / Yuhn-fung (yl) in romanised.
- **王子** → "the Prince" (romanised). Used of 拖雷 by 歐陽克's faction.
- **公主** → "Princess" (romanised). Hybrid keeps CJK.

### Hybrid-variant duplication trap (IMPORTANT — learned Ep22/23)
When an idiom-plus-gloss is written in the hybrid as `ENGLISH — CJK-idiom` or `CJK-idiom — ENGLISH`, the build.py conversion for romanised files will convert the CJK into English and leave the English gloss alongside, producing a visibly-duplicated line like:
> "To your success — success at the first charge"
> "Retreat like a subdued dragon, steady and deep — Retreat like a subdued dragon, steady and deep"

**Prevention**: after `build.py` and `cjk_fix_v2.py`, run a targeted sed/python pass that looks for em-dash phrases with >60% word overlap on either side and collapses them. The Ep22/23 session built a small fixer for this — consider folding it into `cjk_fix_v2.py` properly.

Also scan for `"the the "` (double article) and `"my the "` / `"your the "` — these happen when `降龍十八掌` → `the Eighteen Dragon-Subduing Palms` gets preceded by an existing English `my/your/the`. Simple string replacements suffice.

### Character voices (reinforced)
- **蓉兒**: bratty-but-loving-underneath. Her "I want her to die sooner" (Ep23 sub 37) is said while curing 華箏 — the contradiction IS the character. Don't soften; don't over-explain. "I'm curing her because I want you to be happy" (43) is the emotional hinge.
- **華箏**: 蒙古 directness. Her suicide attempt with the hairpin (Ep23 420–440) comes from the folk-story logic she invokes, not from melodrama. Render the 法師 story plainly.
- **七公**: gruff-affection, deflects with humour. "Two things I fear — no food, and these love affairs" (Ep23 331–333) is self-mockery masking real care. His pretend-ignorance about romance is a bit.
- **黃藥師**: prickly, anti-formality, witty. His "前輩, 後輩 — how tedious" (Ep23 212) and "老邪, 老邪 — let the young ones off" are comedy-of-register. His couplet about his daughter (263) is genuine admiration dressed as taunt.
- **歐陽克**: smooth menace. His coercion of 華箏 (Ep22 11–32) should read as polite-on-the-surface / deadly-underneath. He doesn't raise his voice.
- **梅超風**: resentment-tinged loyalty. Her Ep23 dialogue about 老賊, 金國 upbringing, and being called 走狗 is character-defining — don't flatten to generic villainy.

