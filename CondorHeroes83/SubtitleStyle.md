# Subtitle Style Guide — LOCH 1983 TVB
## Codified from the Ep20 reference version (old pipeline)

This document defines the target subtitle style. Read it BEFORE writing any overrides.

---

## 1. Match the Yue Register

The English phrasing should mirror the Cantonese spoken dialogue — its register, cadence, and level of detail. Fidelity to what's actually being said is the only goal.

### Priority chain
1. **Yue (HIGH confidence)**: the actual spoken words. Match their register, tone, and specificity. If yue is blunt, be blunt. If yue is elaborate, be elaborate.
2. **Chi**: the semantic authority. If the yue looks like ASR garble, fall back to chi meaning. If yue is MEDIUM confidence, chi drives the meaning but use yue for register, tone, and emotional nuance.
3. **Eng (original)**: a rough draft. Override when it diverges from yue/chi, keep when it's already faithful.

### Rules
- **Translate what's said, not more.** If the Cantonese is three words, the English should be comparably brief — not because "short is better" but because that's what the character actually said. Don't pad with filler the speaker didn't use.
- **Don't summarise away register.** If yue says "你這種人不見棺材不流淚" (elaborate insult), keep the elaboration. Don't compress to "You'll regret it." The length is the point — the speaker is being deliberately verbose/colourful.
- **Don't invent emphasis the source doesn't have.** If yue/chi is a flat statement, write a flat statement. Don't add exclamation marks, intensifiers, or dramatic phrasing.

### Examples — matching yue register

| Yue says | RIGHT | WRONG |
|---|---|---|
| 去叫東西吃我很快就回來的 (casual, quick) | Go order some food first. I'll be right back. | Why don't you go in and order something to eat first? I'll be back shortly |
| 又是你這臭要飯的 (chi OCR; actual Cantonese is 死乞兒 = damned beggar) | You again, you stupid beggar! | You again, you stinking beggar! |
| 大宋有救了 (short excited) | There is hope for 大宋! | 大宋 is saved! |
| 如果大宋有多位岳王爺嘅話咁就有救啦 (full conditional) | If we had another 岳王爺, there'd be hope. | If the great Song had a few more men like 岳王爺, there'd still be hope! |
| 我搜晒翠紅樓咩都冇 (搜晒 = exhaustive search, 咩都冇 = absolutely nothing) | I searched every corner of 翠紅樓. There was nothing there. | I searched all over 翠紅樓 just now but found nothing |
| 做人千萬不要太好心 好心遭雷劈 (千萬 = emphatic warning, proverbial) | It's extremely important that a person isn't too kind. Good hearts get struck by lightning — 好心遭雷劈. | Don't be too kind. 好心遭雷劈. |

---

## 2. CJK Scope in Hybrid — Keep More Chinese

The hybrid variant should lean heavily on CJK. If a term has emotional, cultural, or proper-noun weight, keep it Chinese. Don't translate it to English.

### Always CJK in hybrid (never translate)
- **Dynasty/country names**: 大宋, 金, 宋, 蒙古
- **Temple/place full names**: 岳王廟, 翠紅樓, 獅子林, 山神廟
- **Title+name compounds**: 岳老伯, 岳王爺, 岳大叔, 黃大叔 (NOT "Uncle Yue" etc.)
- **Address terms in direct speech**: 老伯, 少爺, 弟子, 長老, 幫主, 公子
- **Idioms as standalone units**: 大開殺戒, 亡國奴, 劫數難逃, 各安天命, 好自為之
- **All items already in the config's CJK requirements list**

### The 老伯 rule
When someone is ADDRESSED as 老伯 (vocative), keep 老伯 in CJK. Don't convert to "sir" or "old man". Example: "Don't worry, 老伯." NOT "Don't worry, sir."

### The 大宋/金 rule
Dynasty names stay CJK: "There is hope for 大宋!" NOT "There's hope for the Song dynasty." "The 金 are coming" NOT "The Jins are coming."

---

## 3. Idiom Presentation

### Format: "English — 中文成語."
Place the English gloss first, then em-dash, then the Chinese idiom.

| RIGHT | WRONG |
|---|---|
| Who told him to look down on us — 狗眼看人低! | He looked down on us. 狗眼看人低. |
| Think it over carefully — 好自為之. | Think it over. 好自為之. |
| Looks like a major battle — 大開殺戒. | Looks like there's going to be a huge slaughter |
| I fear my time has come — 劫數難逃. | I fear this is my fate — I won't escape it |

### Rules
- **Never gloss an idiom twice** (once in Chinese AND once as a separate English expansion). The English before the dash IS the gloss.
- **Idiom on its own is fine.** If the sub is just an exclamation: "豈有此理!" is acceptable by itself.
- **Don't inject idioms into subs where they don't appear in chi.** Only include idioms that are actually in the source text for that sub.

---

## 4. Formatting

### Punctuation
- **Don't end subtitles with periods unless needed for clarity or specific emphasis.** Most subs need no terminal punctuation — the viewer sees one sub at a time and the boundary is implicit.
- **Use ? and ! where the dialogue genuinely calls for it.** Reserve ! for actual shouts, commands, and exclamations in the source. Don't add excitement the source doesn't have.

### Dialogue dashes
- **Use em-dash (—)** for dialogue splits, not hyphen (-).
- Format: "— Line one.\n— Line two."

### Line breaks
- **Use 3-line subs when needed.** If a sub has three short clauses or a long address + two lines of dialogue, split to 3 lines rather than cramming into 2 long lines.
- **Target ~20 characters per line** for readability.
- **Break at natural clause boundaries**, not mid-phrase.

| WRONG (2 cramped lines) | RIGHT (3 clean lines) |
|---|---|
| 岳老伯, they said you're a descendant\nof 岳王爺. Is it true? | 岳老伯, they said\nyou're a descendant of 岳王爺.\nIs it true? |
| If I go back, I'll only drag my family down.\nJust leave me to fend for myself! | If I go back,\nI'll infect the whole family.\nLeave me alone. |

---

## 5. Translation Voice

### Match source register, don't normalise to English
The English should feel like the yue/chi, not like smoothed-out English prose. If the Cantonese is clipped, the English is clipped. If it's formal, the English is formal. If it's awkward or stilted in the source, it can be awkward in English — that's characterisation.

- 這麼緊張幹甚麼 → "Why so uptight?" (casual dismissal — match it)
- 不知道誰亂來 → "Who's the one trying something funny?" (accusatory question — match it)
- 不去了 → "Not going anymore" (abrupt — match it)
- 小姑娘過來放了我們 → "Have mercy!" is WRONG if yue actually says "Miss, please come let us go" — match the actual words

### Don't over-explain
- If chi says 大宋有救了, write "There is hope for 大宋!" Don't expand to "There's hope for the Song dynasty now."
- If chi says 武穆遺書, write 武穆遺書. Don't add "the Book of Wu Mu" in the same sub — the viewer either knows or they'll pick it up.
- Trust the viewer. Subtitles inform, they don't lecture.

### Register matches character
- 蓉兒: bratty, playful, sharp. Short sentences. "Pray till next year for all I care."
- 靖哥哥: earnest, simple, direct. "I don't want you doing that anymore."
- 洪七公: gruff, sly, colourful. "Want me to take off my trousers too?"
- Beggar (洪七公 in disguise): deliberately uncouth. "I'm tough enough. Don't worry about me."

---

## 6. What NOT to Do (Anti-Patterns)

1. **Don't pad short subs.** If chi is one short sentence, the English should be one short sentence. Not two.
2. **Don't inject idioms into subs where they don't appear in chi.** If 精忠報國 appears in sub 131's chi, put it in sub 131. Don't also scatter it into subs 130, 133, 136.
3. **Don't translate 老伯/少爺/公子/長老 to English** in hybrid mode. These are address terms.
4. **Don't write "the Song dynasty" when you can write 大宋.** Hybrid means use Chinese.
5. **Don't use excessive exclamation marks.** The reference uses 29 exclamation marks across 586 subs. That's ~5%. If you're using 76, you're shouting too much.
