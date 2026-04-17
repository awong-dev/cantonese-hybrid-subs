# Process Specification — Subtitle Production Pipeline
## Legend of the Condor Heroes (射鵰英雄傳) 1983 TVB

---

## Input Files (per episode)
- `{N}-eng.csv` — English subtitles (base)
- `{N}-chi_tra.csv` — Traditional Chinese (Mandarin) subtitles
- `{N}-yue.csv` — Cantonese subtitles
- CSV format: `Filename,lang,Sequence,TimeIn,TimeOut,Duration,Text`
- TimeIn/TimeOut format: `HH:MM:SS,mmm`

## Output Files (per episode)
- `{N}-eng-hybrid.srt`
- `{N}-eng-jyutping.srt`
- `{N}-eng-yale.srt`

---

## Pipeline Steps

### Step 1: Parse & Align
```
Parse all three CSVs → extract {index, timecode, start_ms, end_ms, text}
Align eng/chi/yue by timecode overlap (best-overlap matching)
Save to ep{N}_aligned.json
```

### Step 2: Full Dump (CRITICAL — DO NOT SKIP)
```
Print ALL subs into conversation in format:
{idx}|{eng}|{chi}|{yue}

Read every single sub carefully. Cross-check English against:
- Mandarin (chi) for lost meaning, flattened nuance, wrong translations
- Cantonese (yue) for register, emotional tone, colloquial vs formal

DO NOT use compact format. Full dump produces better quality.
```

### Step 3: Write Overrides
```
For EVERY sub (not just changed ones), write the hybrid text.
Default = original English. Override when:
- Names need Chinese characters (hybrid) or context correction
- Titles/honorifics need conversion
- English flattens or loses Chinese meaning
- Register doesn't match Cantonese tone
- Idioms present in Chinese but missing in English
- Kinship terms need correction (養父→foster father, etc.)
- 阿-prefix rules violated

Save to ep{N}_h_all.json as {index: text} mapping.
```

### Step 4: Build Three Variants
```
Hybrid: use override text directly (Chinese characters for names/titles/idioms)

Jyutping: convert from hybrid:
  1. Idioms → English
  2. Terms → English
  3. Titles → English
  4. Names → Jyutping romanisation
  (All conversions: longest match first)

Yale: same as Jyutping but with Yale romanisation table

Save to {N}-eng-{variant}.srt
```

### Step 5: Duration Extension
```
For each subtitle:
  chars = len(text.replace('\n', ' '))
  if chars == 0: skip
  needed_ms = max(chars / 15 * 1000, 1000)  # 15 chars/sec, min 1s
  if needed_ms <= current_duration: skip
  new_end = start + needed_ms
  # Extend using yue speech duration as guide
  for each yue sub overlapping this timeslot:
    new_end = max(new_end, yue_end_ms)
  # Hard cap: never extend past next subtitle's start
  new_end = min(new_end, next_sub_start)
  if new_end > current_end: extend
```

### Step 6: Validate
```
1. Count match: output has same number of subs as input eng.csv
2. Index match: same indices as original
3. CJK scan: romanised files must have ZERO Chinese characters
   - If found: apply targeted fixes (bare surname fragments, missed terms)
4. Pinyin scan: hybrid file must have ZERO Pinyin names
   - Check for: Guo Jing, Huang Rong, Rong-er, Yang Kang, etc.
5. gogo check: no "go-go" with extra dash
6. Zero overlaps: no subtitle extends past the next one's start
```

### Step 7: Output
```
Copy final files to /mnt/user-data/outputs/
Present to user with present_files tool
Provide scene summary with key content notes
```

---

## Quality Checklist (per episode)
- [ ] Every sub read against chi and yue
- [ ] All names converted (hybrid: Chinese chars, romanised: correct system)
- [ ] All titles converted per table
- [ ] All idioms preserved (hybrid: Chinese+gloss, romanised: English)
- [ ] 阿-prefix correct (vocative only)
- [ ] 娘親 rule followed
- [ ] 養父/義父 → "foster father"
- [ ] No Pinyin in hybrid
- [ ] No CJK in romanised
- [ ] No gogo dash errors
- [ ] Duration extensions applied
- [ ] Sub count matches original
- [ ] No overlaps

---

## Episodes Completed (as of this handover)
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27

## Episodes Remaining
25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45 (and any others in the series)
