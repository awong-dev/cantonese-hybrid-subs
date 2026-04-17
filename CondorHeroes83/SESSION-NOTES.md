# Session Notes — LOCH 1983 Subtitle Pipeline

Living document. Contents that help generate good subs for a new episode: **episode status**, **pending content previews**, and **names/terms/oddities** encountered during processing that aren't yet stable enough to promote into `STYLE.md` or `REFERENCE.md`.

When a term or pattern here has been settled across a processing session without contradiction, promote it to the appropriate consolidated doc and delete it from here.

---

## Completion Status

**All episodes are currently Pending.** Prior sessions produced FULL-quality output for some episodes, but those outputs predate the current rule-set / handoff bundle version and are not considered authoritative for the consolidated docs' cross-episode-canonicality backstop (Rule B in `STYLE.md` §2). A FULL-completed episode must have been rendered under the current bundle version for its forms to count as established precedent.

Content summaries for episodes processed in prior sessions are retained below as **pre-examination references** — they help a future session understand the episode's texture (characters, scenes, plot threads) before starting Step 1, but they do not exempt the episode from the full Step 4 examination loop.

### Pending — Needs FULL Processing

| Episode | Subs | Status / Content Preview |
|---------|------|--------------------------|
| 1 | 446 | Prior-session FULL. Historical narration, 丘處機, 郭嘯天 / 楊鐵心. |
| 2 | 385 | Prior-session FULL. 江南七怪, 丘處機 wager, 完顏洪烈 reveal, young 郭靖. |
| 3–14 | — | Not yet processed. |
| 15 | 464 | Prior-session FULL. 楊康 identity crisis, 包惜弱 letter, 穆念慈, 黃蓉 vs 七怪, 歐陽克. |
| 16 | 452 | Prior-session FULL. 梅超風 ambush, 黃蓉/郭靖 reconciliation, 穆念慈/包惜弱 revelation, 楊康 武穆遺書, rescue plan. |
| 17 | 409 | Prior-session FULL. 楊康/包惜弱 escape, 楊康 boat betrayal, 完顏洪烈 despair, 段天德 confession, 楊康 birthday speech, 穆念慈 fireball. |
| 18 | 515 | Prior-session FULL. 包惜弱 poison wine, suicide attempt, becoming nun, 丘處機 captures 楊康, 楊康 oath, 九陰白骨爪 trail, family reunion. |
| 19 | 490 | Prior-session FULL. 楊康 final betrayal, 楊鐵心 suicide (滿江紅), 包惜弱 death, 全真教 scenes, 丘處機 teaches internal skills, duel, 問世間情為何物. |
| 20 | 586 | Parsed and auto-preprocessed in a prior session but never examined against sources. |
| 21–23, 25 | — | Style decisions from these episodes are catalogued in `STYLE.md` §§5, 10, 11, 12 and `REFERENCE.md` §§2, 3. Not re-processed to current FULL standard. |
| 24 | 364 | Prior-session FULL. 黃蓉 departure, 楊康 repentance arc with 穆念慈, 楊康 Mongolian poisoning, 拖雷 seizes 郭靖, 黃帝內經 antidote consultation. Produced the Rule A / Rule B / Rule C split in `STYLE.md` §2 via the 推宮換血 / 推功 homophone case study; also the 小保 cross-episode-canonicality cautionary note and the FABRICATION category rewrite in `REFERENCE.md` §8. |
| 26 | 471 | Prior-session FULL. 歸雲莊 confrontation: 郭靖/黃蓉 arrive, 陸乘風 reveal as 黃藥師's expelled disciple (legs broken for letting 梅超風 steal 九陰真經), 黃蓉 critiques 小重山 painting — 廢人/壯志難伸/憂國憂民 exchange, 念慈 devotion scene at 楊康's prison (以國家為重 refusal of the 金 royal-concubine path), 歐陽克 smooth-menace coercion of 穆姑娘, 裘千仞 (鐵掌水上飄) arrives lying about 黃藥師's death at 全真七子, 江南七怪 arrive and 柯鎮惡 calls out 裘千仞, 梅超風 storms in — 陸乘風/梅超風 mutual-grief reckoning with 老賊 (intimate grief-term for 陳玄風) preserved. |
| 27 | — | Likely 陸乘風 manor aftermath, 歐陽克 scheming, 桃花島 connections. Uploaded with Ep26/28 but deferred. |
| 28 | 538 | Prior-session FULL. Produced the error taxonomy in `REFERENCE.md` §8 via comparison against an earlier version. |
| 29 | 404 | Prior-session FULL. 郭靖 at 桃花島, 周伯通 brotherhood, 黃藥師 / 黃蓉, 歐陽峰 proposal. |
| 30–54 | — | Prior-session mechanical output only — quality below current FULL standard. Re-process. |
| 55–59 | — | Not yet processed. |

---

## Watch List — Names/Terms/Oddities

Items encountered during processing that future sessions should keep an eye on. Promote to `STYLE.md` or `REFERENCE.md` once they're settled with a stable rendering.

### 🟡 Recurring CJK leaks in romanised output

These names consistently slip through as CJK in the Jyutping/Yale output and need manual fix every episode. Referenced in `STYLE.md` §19 as recurring patterns; keeping them here as a running watch list until they're either (a) handled by an explicit rendering row in `STYLE.md` §5, or (b) demonstrably resolved by existing conversion tables.

- **瑤迦** (程瑤迦)
- **冠英** (陸冠英)
- **孫不二**

Other recurring leaks that *are* handled by existing `sed` patterns are already catalogued in `STYLE.md` §19 — consult that list first during the validation step.

### 🟡 Cross-stage concat traps (Ep26 findings)

Conversion artefacts where a longer compound in a later stage doesn't get matched intact because a shorter key in an earlier stage ate part of it. `build.py` has a prefix-ordering guard for this, but these specific patterns slipped through in Ep26 and required post-build `sed` fixes. Promote to `STYLE.md` §19 / `cjk_fix_v2.py` once the fix is proven across another episode.

- **裘老前輩 / 裘前輩** — `裘` converts to `Kau`/`Kauh` in the names pass, then `老前輩` / `前輩` converts to `Elder` / `senior` in a later pass, yielding concatenated output like `KauElder` / `KauhElder` instead of `Elder Kau` / `Elder Kauh`. Fix: add `KauElder → Elder Kau` and `KauhElder → Elder Kauh` patterns to `cjk_fix_v2.py`, OR register the compound `裘老前輩` explicitly in extras before the bare-surname pass.
- **張大哥 / 馬大哥 / 郭大哥** — bare-surname + 大哥 compounds. `大哥` converts to `Big Brother` in the titles pass; if the episode uses `張大哥` / `馬大哥` without an explicit compound entry in extras, the output becomes `張Big Brother` / `馬Big Brother`. Already handled for `郭大哥` (canonical in `STYLE.md` §5) and `週大哥` (banned-term fix); needs explicit compound entries whenever a new `X大哥` appears. Ep26 had `張大哥` (張寨主 variant), `馬大哥` (馬青雄, 黃河四鬼 member).
- **我爹 / 你爹** — possessive-prefix + kinship compounds. In hybrid these are correctly rendered as CJK (they stay 我爹 / 你爹 — good), but in romanised the conversion produces `我Father` / `你Father` unless the compound is registered in extras ahead of the bare `爹` pass. Add `我爹 → my father` / `你爹 → your father` to shared_extras baseline (both jy and yl).
- **大師父 / 大金國** — `大` + existing-compound prefixes. `師父 → Master` and `金國 → Jin` convert first (longest-first within stage), leaving `大Master` / `大Jin`. Already in `STYLE.md` §19 for `大師父 → First Master`; should also register `大金國 → the great Jin empire`.
- **我柯鎮惡 / 我裘千仞** — emphatic-self compounds (a character announcing their name: "I, X"). `柯鎮惡` / `裘千仞` convert to romanised first; the leading `我` is then stranded, producing `我O Jan-ngok` / `我Kau Cin-jan`. Fix: add `我{FullName} → I, {FullName}` patterns for the five most-referenced characters (裘千仞, 柯鎮惡 confirmed Ep26; 郭靖, 黃蓉, 歐陽峰 likely candidates).

### 🟡 Name-variant OCR drift (Ep26)

The chi track spells 陸乘風 inconsistently across sub boundaries — **陸成風, 陸承鋒, 陸承峰, 陸勝鋒** all appear alongside canonical 陸乘風. Canonical is **陸乘風** (from `PersonalNamesUpdated.csv` and prior episodes); Jyutping **Luk Sing-fung**, Yale **Luhk Sihng-fung**. All variants collapse to the canonical form in the hybrid output. If this pattern recurs in Ep27's aftermath-at-the-manor material, promote the collapse rule into `cjk_fix_v2.py`.

---

## How to Use This Log

When closing a session, update the Pending table and add anything new to the Watch List. Specifically:

1. **Update the Pending row for each episode processed.** Replace a blank or bare-note row with a content summary and the `Prior-session FULL` tag (if the session completed FULL). The row stays in Pending — there is currently no Completed table, because no episode has been FULL-processed under the current bundle version yet. If the tag scheme changes (e.g. a "Completed under v9" separate table is introduced), reshape this section then.

2. **Surface new names, titles, idioms, or oddities** that came up during examination and don't yet have a settled rendering. Add them to the Watch List under a short descriptive heading. Skip anything already covered by `STYLE.md`'s name-rendering table (§5), title-conversion table (§6), or idiom catalogue (§10), or by `REFERENCE.md`'s character/context entries.

3. **Promote when stable.** Once a Watch List item has been rendered the same way across two or more episodes without re-debate, move it into the appropriate consolidated doc (name → `STYLE.md` §5; title → §6; idiom → §10; context-dependent judgment → `REFERENCE.md`) and delete it from here.

This file is not a changelog. Pipeline version bumps, script changes, documentation consolidation, vocabulary renames — none of that belongs here. If a change affects how subs are produced, it lives in `PIPELINE.md` or `STYLE.md`; this file only records content-level findings that bear on future episodes.
