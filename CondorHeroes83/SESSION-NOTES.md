# Session Notes — LOCH 1983 Subtitle Pipeline

Living document. Contents that help generate good subs for a new episode: **episode status**, **pending content previews**, and **names/terms/oddities** encountered during processing that aren't yet stable enough to promote into `STYLE.md` or `REFERENCE.md`.

When a term or pattern here has been settled across a processing session without contradiction, promote it to the appropriate consolidated doc and delete it from here.

---

## Completion Status

### Completed at FULL quality

Every sub examined against sources, overridden where needed.

| Episode | Subs | Key Content |
|---------|------|-------------|
| 1 | 446 | Historical narration, 丘處機, 郭嘯天 / 楊鐵心 |
| 2 | 385 | 江南七怪, 丘處機 wager, 完顏洪烈 reveal, young 郭靖 |
| 15 | 464 | 楊康 identity crisis, 包惜弱 letter, 穆念慈, 黃蓉 vs 七怪, 歐陽克 |
| 16 | 452 | 梅超風 ambush, 黃蓉/郭靖 reconciliation, 穆念慈/包惜弱 revelation, 楊康 武穆遺書, rescue plan |
| 17 | 409 | 楊康/包惜弱 escape, 楊康 boat betrayal, 完顏洪烈 despair, 段天德 confession, 楊康 birthday speech, 穆念慈 fireball |
| 18 | 515 | 包惜弱 poison wine, suicide attempt, becoming nun, 丘處機 captures 楊康, 楊康 oath, 九陰白骨爪 trail, family reunion |
| 19 | 490 | 楊康 final betrayal, 楊鐵心 suicide (滿江紅), 包惜弱 death, 全真教 scenes, 丘處機 teaches internal skills, duel, 問世間情為何物 |
| 21–23, 25–26 | — | Style decisions from these episodes are catalogued in `STYLE.md` §§5, 10, 11, 12 and `REFERENCE.md` §§2, 3. Not re-processed to current FULL standard. |
| 24 | 364 | 黃蓉 departure, 楊康 repentance arc with 穆念慈, 楊康 Mongolian poisoning, 拖雷 seizes 郭靖, 黃帝內經 antidote consultation. Produced the Rule A / Rule B / Rule C split in `STYLE.md` §2 via the 推宮換血 / 推功 homophone case study; also the 小保 cross-episode-canonicality cautionary note and the FABRICATION category rewrite in `REFERENCE.md` §8. |
| 28 | 538 | Produced the error taxonomy in `REFERENCE.md` §8 via comparison against an earlier version |
| 29 | 404 | 郭靖 at 桃花島, 周伯通 brotherhood, 黃藥師 / 黃蓉, 歐陽峰 proposal |

### Pending — Needs FULL Processing

| Episode | Status / Content Preview |
|---------|--------------------------|
| 20 | 586 subs. Parsed and auto-preprocessed in a prior session but never examined against sources. |
| 27 | Likely 陸乘風 manor continuation, 歐陽克 scheming, 桃花島 connections. |
| 3–14 | Not yet processed. |
| 30–54 | Prior-session mechanical output only — quality below current FULL standard. Re-process. |
| 55–59 | Not yet processed. |

---

## Watch List — Names/Terms/Oddities

Items encountered during processing that future sessions should keep an eye on. Promote to `STYLE.md` or `REFERENCE.md` once they're settled with a stable rendering.

### 🟡 Recurring CJK leaks in romanised output

These names consistently slip through as CJK in the Jyutping/Yale output and need manual fix every episode. Referenced in `STYLE.md` §19 as recurring patterns; keeping them here as a running watch list until they're either (a) handled by an explicit rendering row in `STYLE.md` §5, or (b) demonstrably resolved by existing conversion tables.

- **瑤迦** (程瑤迦)
- **冠英** (陸冠英)
- **孫不二**

Other recurring leaks that *are* handled by existing `sed` patterns are already catalogued in `STYLE.md` §19 — consult that list first during the validation step.

---

## How to Use This Log

When closing a session, update the Completion Status tables and add anything new to the Watch List. Specifically:

1. **Move completed episodes** from Pending to Completed. Add a one-line key-content summary for the episode in the Completed table (characters, scenes, plot threads) — this is what a future session references to understand the episode's texture before starting.

2. **Surface new names, titles, idioms, or oddities** that came up during examination and don't yet have a settled rendering. Add them to the Watch List under a short descriptive heading. Skip anything already covered by `STYLE.md`'s name-rendering table (§5), title-conversion table (§6), or idiom catalogue (§10), or by `REFERENCE.md`'s character/context entries.

3. **Promote when stable.** Once a Watch List item has been rendered the same way across two or more episodes without re-debate, move it into the appropriate consolidated doc (name → `STYLE.md` §5; title → §6; idiom → §10; context-dependent judgment → `REFERENCE.md`) and delete it from here.

This file is not a changelog. Pipeline version bumps, script changes, documentation consolidation, vocabulary renames — none of that belongs here. If a change affects how subs are produced, it lives in `PIPELINE.md` or `STYLE.md`; this file only records content-level findings that bear on future episodes.
