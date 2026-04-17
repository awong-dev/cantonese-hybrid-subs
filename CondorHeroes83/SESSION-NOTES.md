# Session Notes — LOCH 1983 Subtitle Pipeline

Living document. Contents that help generate good subs for a new episode: **episode status**, **pending content previews**, and **names/terms/oddities** encountered during processing that aren't yet stable enough to promote into `STYLE.md` or `REFERENCE.md`.

When a term or pattern here has been settled across a processing session without contradiction, promote it to the appropriate consolidated doc and delete it from here.

---

## Completion Status

### Completed under v10 (FULL)

Episodes below were FULL-processed under the current handoff bundle version and their rendered forms count as established precedent for the cross-episode-canonicality backstop (Rule B in `STYLE.md` §2).

| Episode | Subs | Notes |
|---------|------|-------|
| 28 | 515 | FULL under v10. 程家 snake-bite → 陸冠英 / 程瑤迦 betrothal scheme, 陸乘風's grief arc and the 想逝者 / 天蓋高 classical lament couplet, 黃藥師 reunion with expelled disciple 陸乘風, 蓉兒 forced back to 桃花島, 華箏 finds drunken 郭靖. Confirmed Ep28 Sub 20 "fed a poisonous scorpion every day" is eng-correct against OCR-damaged chi (yue 每日用一隻毒蝎嚟養大 is the witness) — the canonical Sub 22 case study per `PIPELINE.md` §4 and `REFERENCE.md` §8. **Sub count is 515 (chi-spine), not 538** — the 538 in prior notes was the eng track's count before chi-spine reflow. |

### Pending — Needs FULL Processing

Prior-session FULL outputs below predate the current rule-set and are retained as content previews only; they do not count as established precedent.

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

### 🟡 Cross-stage concat traps

Conversion artefacts where a longer compound in a later stage doesn't get matched intact because a shorter key in an earlier stage ate part of it. `build.py` has a prefix-ordering guard for this, but the patterns below slipped through and required post-build `sed` fixes. The common mechanism is: a short key inside `build.py`'s built-in `titles` stage (e.g. `前輩`, `娘`, `爹`) fires before the extras stage, which runs *last* in `build.py`'s `convert()` pipeline — so any overlay entry containing one of those keys as a substring loses its own CJK before extras ever gets a chance. The overlay can only catch compounds whose substrings aren't in an earlier stage.

Fix options, in rough order of preference:
1. Register the compound in the overlay under a pre-tokenised form (not viable in the current build chain).
2. Add a targeted `sed` post-pass (what Ep28 did for these).
3. Promote frequent concat fixes into `cjk_fix_v2.py` once stable across 2+ episodes.

- **裘老前輩 / 裘前輩** — `裘` converts to `Kau`/`Kauh` in the names pass, then `老前輩` / `前輩` converts to `Elder` / `senior` in a later pass, yielding concatenated output like `KauElder` / `KauhElder` instead of `Elder Kau` / `Elder Kauh`. Fix: add `KauElder → Elder Kau` and `KauhElder → Elder Kauh` patterns to `cjk_fix_v2.py`, OR register the compound `裘老前輩` explicitly in extras before the bare-surname pass.
- **陸前輩** (Ep28) — same mechanism as 裘前輩: `前輩 → senior` (titles stage) fires before overlay's `陸前輩 → Senior Luk`, yielding `Luksenior`. Fix Ep28 applied: overlay registration failed (wrong stage); post-build `sed` replacement `Luksenior → senior Luk`. Candidates to include: 陸前輩, 黃前輩, 洪前輩 (洪前輩 already canonical in `STYLE.md` §5; the wrapper makes it a cjk_fix_v2 candidate).
- **張大哥 / 馬大哥 / 郭大哥** — bare-surname + 大哥 compounds. `大哥` converts to `Big Brother` in the titles pass; if the episode uses `張大哥` / `馬大哥` without an explicit compound entry in extras, the output becomes `張Big Brother` / `馬Big Brother`. Already handled for `郭大哥` (canonical in `STYLE.md` §5) and `週大哥` (banned-term fix); needs explicit compound entries whenever a new `X大哥` appears. Ep26 had `張大哥` (張寨主 variant), `馬大哥` (馬青雄, 黃河四鬼 member).
- **我爹 / 你爹** — possessive-prefix + kinship compounds. In hybrid these are correctly rendered as CJK (they stay 我爹 / 你爹 — good), but in romanised the conversion produces `我Father` / `你Father` unless the compound is registered in extras ahead of the bare `爹` pass. Fired in Ep28 at three subs (152, 154, 342); fixed post-build with `我Father → my father`. Add `我爹 → my father` / `你爹 → your father` to shared_extras baseline (both jy and yl) — stable across 2+ episodes now (Ep26 and Ep28 both hit this).
- **我們 + (term)** — possessive-plural + term compound. Ep28 sub 36 had `我們全真教` in the hybrid; `全真教 → the Quanzhen Sect` (terms stage) fires before overlay's `我們全真教 → the Quanzhen Sect`, leaving `我們the Quanzhen Sect`. Fixed post-build with sed. Pattern will recur with any `我們X` where X is a term/sect. Candidates for cjk_fix_v2: `我們the → our`.
- **程姑娘 / 黃姑娘** — surname + 姑娘 (姑娘 → Miss via 姑 being inside `姑娘` — but wait, look closer: `娘 → Mother` is registered in `build.py` titles, and it *runs before extras*. So `程姑娘` → `程姑Mother` (娘 eaten) → extras `姑` not registered → leaves `程姑Mother` as the output. Ep28 sub 99 etc. hit this six times for `程姑娘` specifically; `黃姑娘` is rescued because build.py's titles has an explicit `黃姑娘 → Miss Wong` entry. Fix Ep28 applied: post-build `sed s/Cing姑Mother/Miss Cing/`. Fix in-pipeline: register `程姑娘 → Miss Cing / Ching` in build.py titles (cleanest) OR baseline extras (needs 娘 to not eat the 娘 in the compound — but within-stage longest-first on extras would grab `程姑娘` first, so as long as extras is the stage that does the match, this works). **Confirmed: the Ep28 overlay *does* have `程姑娘` — the issue is that `娘 → Mother` in titles runs *before* extras, so by the time extras runs, `程姑娘` is already `程姑Mother` and doesn't match.** Promote `程姑娘` / `程小姐` to baseline extras or into build.py titles after the next episode that needs 程 addresses.
- **我柯鎮惡 / 我裘千仞** — emphatic-self compounds (a character announcing their name: "I, X"). `柯鎮惡` / `裘千仞` convert to romanised first; the leading `我` is then stranded, producing `我O Jan-ngok` / `我Kau Cin-jan`. Fix: add `我{FullName} → I, {FullName}` patterns for the five most-referenced characters (裘千仞, 柯鎮惡 confirmed Ep26; 郭靖, 黃蓉, 歐陽峰 likely candidates). Ep28 didn't fire this — the dialogue had fewer emphatic-self moments.
- **大師父 / 大金國** — `大` + existing-compound prefixes. `師父 → Master` and `金國 → Jin` convert first (longest-first within stage), leaving `大Master` / `大Jin`. Already in `STYLE.md` §19 for `大師父 → First Master`; should also register `大金國 → the great Jin empire`.

### 🟢 Promote-ready — established across 2+ episodes (v10 Ep28 + prior)

These are Watch List items that have now fired in two-or-more episodes without contradicting renderings and are ready to promote out of this log:

- **我爹 → my father** / **你爹 → your father** — fired Ep26 and Ep28. Promote to `extras_baseline.json` (both jy and yl).
- **我們 + term → possessive + English term** — Ep28 sub 36. Not yet twice-confirmed; hold.
- **程姑娘 / 程小姐** rendering. Ep28 established as Miss Cing (jy) / Miss Ching (yl). Hold for one more episode with 程姑娘 references (possibly Ep29/30) before promoting.

### 🟡 Name-variant OCR drift (Ep26, Ep28)

The chi track spells 陸乘風 inconsistently across sub boundaries. **Ep26** showed 陸成風, 陸承鋒, 陸承峰, 陸勝鋒 alongside canonical 陸乘風. **Ep28** added 陸承峰 (yue) and 六成風 / 六兄 (yue Whisper homophones, 陸→六 `luk6`). All variants collapse to the canonical 陸乘風 in the hybrid. Canonical is **陸乘風**; Jyutping **Luk Sing-fung**, Yale **Luhk Sihng-fung**. **Now confirmed across Ep26 and Ep28 — promote the collapse rule into `cjk_fix_v2.py`.** Suggested entries: `陸成風|陸承鋒|陸承峰|陸勝鋒|六成風 → 陸乘風` in hybrid (pre-build pass), plus 六兄 → 陸兄 in the bare-form case.

Similar Ep28 drift affecting 瑤迦 (程瑤迦): chi uses **瑤珈** (with 珈 rather than 迦) throughout, 49 subs. `PersonalNamesUpdated.csv` has only 瑤迦. Ep28 resolved it by using canonical 瑤迦 in all hybrid overrides, collapsing 珈 → 迦. Promote the collapse rule after one more episode confirming the pattern. Also: yue ASR produced 姚家 (Jiu-gaa homophone) throughout — this got resolved by not lifting yue tokens into hybrid (chi-spine drove naming).

### 🟡 歐陽克 variant drift (Ep28)

Yue ASR produced **歐陽黑**, **歐陽客**, **歐陽鹿** (for 歐陽峰) across Ep28. All Whisper homophones — 克/黑/客 are all `haak1`, 峰/鹿 not strict homophones but share a phonetic environment in the sentence. Chi is canonical; mention only because the chi track's OCR spin `歐陽鹿` / `歐陽寧` for 歐陽峰 recurred (subs 42, 44, 57). Hybrid always 歐陽峰. No promotion needed — this is Rule B territory, handled by chi-authority.

### 🟡 Classical lament couplet (Ep28 subs 264–265)

陸乘風 quotes a classical lament for 瑤迦 (he thinks she's dead). The chi is OCR-damaged; the actual text is close to a paraphrase of 賈誼's *弔屈原*:

> 想逝者之不罪兮, 惜形中之載道
> 天蓋高而無階, 懷此恨其最苦

Ep28 rendered as CJK + em-dash + English gloss on the following line (Dragon-chant quartet pattern, `STYLE.md` §10). Gloss used: *"my love runs deep, the dead beyond recall"* / *"Heaven is high but has no stair; this sorrow cuts deepest"*. Not yet seen in another episode — if it recurs or if 黃藥師's 桃花島 scenes have similar classical laments, promote to the `STYLE.md` §10 idiom catalogue under a new "Classical laments / elegiac verse" subheading.

---

## How to Use This Log

When closing a session, update the status section for each episode processed and add anything new to the Watch List. Specifically:

1. **Update the episode row.** If the episode completed FULL under the current bundle version, move it into the "Completed under v{VERSION}" table and replace prior-session content with the new summary. If it partially processed or the quality outcome was less than FULL, leave it in Pending and note the outcome.

2. **Surface new names, titles, idioms, or oddities** that came up during examination and don't yet have a settled rendering. Add them to the Watch List under a short descriptive heading. Skip anything already covered by `STYLE.md`'s name-rendering table (§5), title-conversion table (§6), or idiom catalogue (§10), or by `REFERENCE.md`'s character/context entries.

3. **Promote when stable.** Once a Watch List item has been rendered the same way across two or more episodes without re-debate, move it into the appropriate consolidated doc (name → `STYLE.md` §5; title → §6; idiom → §10; context-dependent judgment → `REFERENCE.md`; concat-trap fix → `cjk_fix_v2.py` or `extras_baseline.json`) and delete it from here.

This file is not a changelog. Pipeline version bumps, script changes, documentation consolidation, vocabulary renames — none of that belongs here. If a change affects how subs are produced, it lives in `PIPELINE.md` or `STYLE.md`; this file only records content-level findings that bear on future episodes.
