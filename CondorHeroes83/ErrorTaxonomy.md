# Error Taxonomy — NewChat vs Experienced Session
## Based on 464 differences across 538 subs in Episode 28

This document catalogues real mistakes from a session that used the handoff documents but lacked deep processing experience. Add this to the handoff package so the new session can learn from these concrete examples.

---

## Summary of Error Types

| Category | Count | Severity |
|----------|-------|----------|
| FABRICATION | 2 | CRITICAL — invented content |
| CHI_MEANING_LOST | 159 | HIGH — original English kept when Chinese has richer/different meaning |
| NAME_TITLE_LEAK | 63 | HIGH — English names/titles where hybrid needs Chinese |
| IDIOM_MISSING | 18 | MEDIUM — Chinese idioms omitted from hybrid |
| FORMATTING_ONLY | 100 | LOW — just punctuation/line-break differences |
| MINOR_WORDING | 124 | LOW — small preference differences |

---

## CATEGORY 1: FABRICATION (CRITICAL)
The English track sometimes contains content NOT present in the Mandarin source. The new session MUST cross-check and remove fabricated content.

### Rule: The Mandarin (chi) is the authority text. If the English says something the Chinese doesn't, DELETE IT.

**Example — Sub 22:**
- WRONG: "But these are snakes from 白駝山 that are fed poisonous scorpions daily"
- CHI: 但實際上這些蛇,是白駝山用特殊的方法養大的蛇
- RIGHT: "But they're actually raised by 白駝山 using a special method."
- Note: "poisonous scorpions" appears NOWHERE in the Chinese. The English fabricated it.

**Example — Sub 316:**
- WRONG: Duplicates content already in Sub 315
- RIGHT: Empty (content already covered)

---

## CATEGORY 2: CHI_MEANING_LOST (HIGH — 159 instances)
This is the single biggest problem. The new session defaulted to keeping the original English, missing meaning present in the Mandarin.

### Rule: The original English is a ROUGH DRAFT to improve, NOT a base to preserve. Override EVERY sub — compare against chi and improve.

**Example — Sub 7:**
- WRONG: "Luckily, Miss Cheng threw a stool at him"
- CHI: 幸虧大小姐人奮不顧身 拿張飲子扔了過去
- RIGHT: "Luckily, the young mistress fought back bravely and threw a stool at him."
- Lost: 奮不顧身 (fought back bravely/risked her life), 大小姐 (young mistress, not "Miss Cheng")

**Example — Sub 10:**
- WRONG: "He became very angry"
- CHI: 他好像很生氣
- RIGHT: "He seemed very angry" (好像 = "seemed", not "became" — different certainty level)

**Example — Sub 12:**
- WRONG: "Who do you think is responsible?"
- CHI: 仙姑,依你看是哪路人馬幹的
- RIGHT: "仙姑, who do you think is responsible?" (drops the address term 仙姑)

**Example — Sub 36:**
- WRONG: "陸乘風 is a disciple of the lord of 桃花島"
- CHI: 陸乘風那個老賊 是桃花島島主的傳人
- RIGHT: "陸乘風, that old scoundrel, is a disciple of the master of 桃花島."
- Lost: 那個老賊 (that old scoundrel) — entire characterisation dropped

**Example — Sub 72:**
- WRONG: "Father is just waiting for teacher to go retrieve the antidote"
- CHI: 爹是一心一意去給我找解藥的
- RIGHT: "阿爹 is set on finding me the antidote." (一心一意 = single-mindedly determined)

**Example — Sub 135:**
- WRONG: "that old scoundrel Cheng wouldn't come and beg me for it"
- CHI: 程老頭也不會對我那麼低聲下氣了
- RIGHT: "that old scoundrel 程 wouldn't have grovelled so" (低聲下氣 = grovelling/humbling oneself)

---

## CATEGORY 3: NAME/TITLE LEAK (HIGH — 63 instances)
In hybrid mode, names and titles must be in Chinese characters. The new session frequently left English names where Chinese was needed.

### Rule: In hybrid, ALL names = Chinese characters. ALL titles = Chinese characters. No exceptions.

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

## CATEGORY 4: IDIOM MISSING (MEDIUM — 18 instances)
Hybrid subs should include Chinese idioms inline with English glosses. The new session dropped them.

### Rule: When a 四字成語 or common phrase appears in the Chinese, include it in hybrid format: "Chinese gloss."

**Examples of missed idioms:**
- 防不勝防 → should appear as "防不勝防." after "impossible to guard against"
- 臭名遠揚 → should appear after "infamous"
- 勢不兩立 → should appear after "at odds"
- 沒齒難忘 → should appear after "I will never forget"
- 不用拐彎抹角 → should appear before "Come straight to the point"
- 舉手之勞 → should appear after "It was nothing"
- 人死不能復生 → should appear before "The dead cannot return"
- 後會有期 → should appear instead of "We will meet again"
- 萬萬不能 → should appear after "Absolutely not"
- 知心朋友 → should appear after "true friend"

---

## CATEGORY 5: FORMATTING (LOW — 100 instances)
Just punctuation marks, em-dashes vs hyphens, line break placement. Not substantive.

---

## CATEGORY 6: MINOR WORDING (LOW — 124 instances)  
Small preference differences like "Don't worry. They won't fight" vs "Don't worry. / They won't fight." or "I have no reason to lie" vs "I don't have to lie to you". Both acceptable.

---

## KEY TAKEAWAYS FOR NEW SESSION

1. **Override EVERY sub.** Don't keep original English as default. Read every sub against chi, improve it, THEN write the override. The experienced session overrode all 538 subs; the new session effectively only overrode ~200.

2. **Chi is authority, English is draft.** When they conflict, chi wins. When English adds content not in chi, delete it. When English flattens chi meaning, restore it.

3. **Hybrid means Chinese characters.** Every name, every title, every place, every idiom — Chinese characters in hybrid. The system for checking is: after building, scan for any English proper nouns that should be Chinese.

4. **Idioms are not optional.** When chi contains a 四字成語, the hybrid MUST include it. Format: "English gloss. 中文成語." or "中文成語. English gloss."

5. **Read the detail.** 好像 ≠ became (it means "seemed"). 大小姐 ≠ "Miss Cheng" (it means "young mistress"). 一心一意 ≠ "just waiting" (it means "single-mindedly determined"). These nuances matter.
