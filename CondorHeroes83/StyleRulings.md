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
