# Episode Subtitle Revision - Multi-Source Processing
## 射鵰英雄傳 Episode 00 (Legend of the Condor Heroes)

### Processing Summary
**Date**: March 18, 2026
**Episode**: t00 (Episode 1)

**Source Files:**
- English subtitles: 446 entries
- Traditional Chinese (Mandarin): 438 entries  
- Cantonese ASR: 79 entries

**Processing Methodology:**
1. **Semantic Authority**: Traditional Chinese (Mandarin) subtitles used for accurate meaning
2. **Formality Detection**: Cantonese ASR analyzed for speech formality markers (貧道, 在下, 閣下, etc.)
3. **Character Replacements**: All character names, places, titles, and martial arts terms replaced with Chinese characters
4. **Pronoun Retention**: English pronouns (I, you, my, your, etc.) kept in English for readability

---

## Sample Transformations

### Historical Narration
**Before:**
```
In the South Song dynasty
Jin forces invaded Bianliang
```

**After:**
```
In the 南宋
金兵 invaded 汴梁
```

---

### Character Introduction
**Before:**
```
My name is Qiu Chuji
So you're the legendary Reverend Qiu of Quanzhen Sect!
```

**After:**
```
My name is 丘處機
So you're the legendary 真人 Qiu of 全真派!
```

---

### Political Terms
**Before:**
```
This bag contains the head of the traitor Wang Daoqian
He colluded with the Sixth Prince of Jin Wanyan Honglie
```

**After:**
```
This bag contains the head of the 漢奸 王道乾
He colluded with the 六王爺 of Jin 完顏洪烈
```

---

### Martial Arts Terms
**Before:**
```
I'll be fine once I use my 'qi' to force out the poison
```

**After:**
```
I'll be fine once I use my '氣' to force out the poison
```

---

## Categories of Chinese Character Replacements

### 1. Historical & Political Terms
- South Song dynasty → 南宋
- Song court → 宋廷
- Jin forces/soldiers → 金兵
- the Jins → 金人
- Emperor Qingyuan → 慶元皇帝
- Sixth Prince → 六王爺
- traitor → 漢奸
- patriotic → 愛國

### 2. Place Names
- Bianliang → 汴梁
- Linan → 臨安
- Xihu/West Lake → 西湖
- Liangshan → 梁山
- Peach Blossom Island → 桃花島

### 3. Character Names
- Qiu Chuji → 丘處機
- Wang Daoqian → 王道乾
- Wanyan Honglie → 完顏洪烈
- Yue Fei → 岳飛
- Qin Hui → 秦檜
- Han Shizhong → 韓世忠
- Guo Xiaotian → 郭嘯天
- Yang Tiexin → 楊鐵心
- Guo Jing → 郭靖
- Yang Kang → 楊康
- Huang Rong → 黃蓉
- Huang Yaoshi → 黃藥師
- Ouyang Feng → 歐陽鋒
- Hong Qigong → 洪七公
- Mei Chaofeng → 梅超風
- Zhou Botong → 周伯通

### 4. Martial Arts Honorifics & Titles
- Reverend → 真人
- Master → 師父
- Taoist (when title) → 道長
- Great hero/Hero → 大俠
- Elder → 長老
- Sect Leader/Chief → 掌門

### 5. Family & Brotherhood Terms
- Big Brother → 大哥
- Second Brother → 二哥
- Third Brother → 三哥
- Sworn brother → 結拜兄弟

### 6. Internal Cultivation & Martial Arts
- internal strength → 內力
- internal energy → 內功
- internal skills → 內功
- qi/chi → 氣
- qinggong/light skill → 輕功
- martial arts/wugong → 武功
- kungfu → 功夫
- martial artist → 武林中人

### 7. Martial World
- jianghu/martial world → 江湖
- wulin → 武林

### 8. Sects & Schools
- Quanzhen Sect → 全真派
- Beggar's Sect → 丐幫

### 9. Martial Arts Techniques & Texts
- Jiuyin Manual → 九陰真經
- Iron Palm → 鐵掌
- Eighteen Dragon-Subduing Palms → 降龍十八掌
- Dog Beating Stick → 打狗棒/打狗棒法

---

## Formality Analysis (From Cantonese ASR)

The Cantonese audio track was analyzed for formality markers, though in this revision pronouns remain in English. The system detected:

**Formality Markers Found:**
- 貧道 (humble Taoist self-reference) - detected in Qiu Chuji's dialogue
- 閣下 (respectful "you") - detected in formal exchanges
- 道長 (Taoist Master) - used as address
- 大俠 (Great Hero) - honorific title

**Formality Levels:**
- Very Formal: Qiu Chuji's self-introductions
- Formal: Exchanges between warriors
- Neutral: Casual family dialogue

---

## Technical Notes

1. **Time-Based Matching**: Entries matched across all three subtitle sources using timestamp overlap
2. **Cantonese ASR Limitations**: ASR contains transcription errors, used only for formality detection, not semantic content
3. **Mandarin Authority**: Semantic meaning derived from Traditional Chinese subtitles
4. **English Grammar Preserved**: Sentence structure remains English with Chinese noun substitutions
5. **Pronoun Retention**: All pronouns (I, you, my, your, he, she, etc.) kept in English

---

## Output Files

1. **t00-eng-revised.srt** - Standard SRT subtitle format
2. **t00-eng-revised.csv** - CSV format with formality level annotations

Both files contain identical subtitle text with Chinese character integration.

---

## Usage Recommendation

These revised subtitles are designed for viewers who:
- Understand English grammar and sentence structure
- Want authentic wuxia terminology in Chinese characters
- Appreciate seeing character names in original Chinese
- Prefer not to have pronouns translated (maintaining "I" instead of "貧道")

For maximum cultural authenticity while maintaining English readability.
