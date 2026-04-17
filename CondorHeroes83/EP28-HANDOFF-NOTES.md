# Episode 28 Handoff Notes (Session 2)

## Session Summary
Processed episodes 21–26, 28 at GOLD quality. Episode 27 still PENDING.

## Pipeline Changes from v3 → v5
1. **pipeline.py v5**: Whisper JSON preprocessing — aligns yue words to chi_tra subs (NOT eng), strips credit songs, discards raw JSON from memory. Compact per-sub yue alignment.
2. **auto_override_v2.py v2.1**: Confidence-tier aware. HIGH/MEDIUM/LOW from avg_logprob. Generates ep{N}_confidence.json for review.
3. **credit_songs.json**: Official lyrics for 一生有意義 (opening) and 肯去承擔愛 (ending) with detection signatures. Song subs NOT currently inserted — timings need manual reference. Pipeline strips song segments from yue before alignment.

## Key Learnings This Session
- **Name swap bug**: When manually overriding opening subs with empty/bare-name chi, I projected wrong speaker. Fixed in ep23/24. Rule: for subs where chi is empty or just a name, KEEP the auto-override base rather than rewriting.
- **ErrorTaxonomy Sub 22 correction**: The "poisonous scorpions" previously flagged as fabrication is CONFIRMED by yue (HIGH confidence). Yue says 每日用一隻毒蝎嚟養大. The eng was right; the taxonomy was wrong on this specific sub.
- **Recurring CJK leaks**: 瑤迦, 冠英, 孫不二 need manual fixes in cjk_fix pass every time. Should be added to cjk_fix_v2.py.

## Updated Completion Status
| Episode | Status | Quality |
|---------|--------|---------|
| 1–2 | Done | GOLD |
| 15–20 | Done | GOLD |
| 21 | Done | GOLD |
| 22 | Done | GOLD |
| 23 | Done | GOLD |
| 24 | Done | GOLD |
| 25 | Done | GOLD |
| 26 | Done | GOLD |
| 27 | CSVs+JSON uploaded | PENDING |
| 28 | Done | GOLD |
| 29 | Done (prior session) | GOLD |
| 3–14 | Not yet processed |
| 30–59 | Not yet processed |

## Ep27 Content Preview
From handoff data: likely contains 陸乘風 manor continuation, 歐陽克 scheming, 桃花島 connections. CSVs and Whisper JSON already uploaded.

## Files in This Zip
### Config & Reference (7 files)
1. LOCH1983-Handoff-Config-v3.md
2. ProcessSpecification-v2.md
3. StyleRulings.md
4. TrickyInferences.md
5. ErrorTaxonomy.md
6. PersonalNamesUpdated.csv
7. credit_songs.json (NEW — song lyrics + detection signatures)

### Pipeline Scripts (5 files)
8. pipeline.py (v5 — Whisper preprocessing, song stripping)
9. auto_override_v2.py (v2.1 — confidence-tier aware)
10. build.py
11. cjk_fix_v2.py
12. shared_extras.py

### This file
13. EP28-HANDOFF-NOTES.md
