# Session Notes — LOCH 1983 Subtitle Pipeline

Living document. Carries **episode status**, **pending-episode arc keywords**, and **names/terms/oddities** not yet stable enough to promote into `STYLE.md` or `REFERENCE.md`. When a term or pattern has been settled across a session without contradiction, promote it to the appropriate consolidated doc and delete it here.

**Row budget.** Each Completed-table row body targets **≤500 chars, hard cap ≤1000 chars**. A row is a pointer into consolidated docs, not a summary of them. If a row hits the cap, the first thing to cut is per-sub citations (sub 344, subs 48–53) and parentheticals explaining who-said-what — those belong in commit messages or SRTs, not here. If you find yourself writing "Outcome: FULL — every sub examined..." — write just `FULL` or omit entirely; FULL is the default for rows in the Completed table.

**Completed-table row body format.** In this order, nothing else:

1. Arc label — one clause (≤15 words), location/plot driver + key characters
2. `First FULL firing for:` — bare comma-separated CJK list; no parentheticals except disambiguation
3. Cross-episode precedents established or revised (omit if none) — pointer only, not re-explanation
4. Chi-OCR variants — compact arrow list `X/Y→Z` (omit if none)
5. Promotion flags — list of items ready for consolidation (omit if none)

Narrative plot detail does NOT belong here. Who said what, scene-by-scene beats, and dialogue color are out — the SRTs carry the plot. Full spec in `PIPELINE.md` Step 8.5.

**Pending-table rows** follow the same size constraint: location + arc-driver keywords only, no plot prose.

---

## Completion Status

### Completed (FULL)

Episodes FULL-processed under the consolidated pipeline. **Bundle** records the handoff version that produced the output; later bumps never invalidate prior rows. All rows remain valid precedent for Rule B in `STYLE.md` §2.

**Sort rule — KEEP SORTED BY EPISODE NUMBER ASCENDING.** Episode number is the stable key; Bundle varies by session.

| Episode | Bundle | Subs | Notes |
|---------|--------|------|-------|
| 1 | v15 | 438 | Pilot — 金/宋 narration (靖康恥), 牛家村 drunk-scene, 丘處機 rescue, 郭靖/楊康 naming, 段天德 raid, 法華寺 confrontation. First FULL firing for: 郭嘯天, 楊鐵心, 包惜弱, 丘處機, 長春子, 完顏洪烈, 顏烈, 段天德, 王道乾, 金閻旭, 張老爹, 牛家村, 臨安, 西湖, 汴梁, 慶元, 楊家槍, 全真派, 法華寺, 醉仙樓; 滿江紅 quatrain; 題臨安邸 compressed form (Ep20 second firing); idioms 天有不測風雲/人有旦夕禍福, 大開殺戒, 義不容辭, 一言為定, 可喜可賀, 英雄有後, 報仇雪恨, 家破人亡, 天緣巧合, 奸臣賊子, 莫須有; address cluster 道長/真人/貧道/道爺/道士, 大俠, 賢侄/賢侄女, 文定, 尊夫人/內子/娘子, 閣下, 公子, 長官. Chi-OCR: 盤噓汀梁→盤據汴梁, 汪州→汴州, 汪梁→汴梁 (新 汪/汴), 非畫即盜→非奸即盜, 錫頭→鋤頭, 希彰/希芯→希望. Promotion flags: 4 concat-trap fixes added to `cjk_fix_v2.py` v15 (六Your Highness, My Mother子, 張老Father, 官字taels個口); Taoist cluster + 大俠 → `extras_baseline.json` on next firing (Ep2 confirmed). |
| 2 | v16 | 410 | 醉仙樓 18-year wager (江南七怪 vs 丘處機) + 完顏洪烈 reveals identity + 包惜弱 燕京 marriage + 小康 naming + 蒙古 child-郭靖. First FULL firing for: 焦木大師, 江南七俠 (chi formal vs 七怪 common), 七怪 seven formal nicknames (飛天蝙蝠/妙手書生/馬王神/南山樵子/笑彌陀/鬧市隱俠/越女劍), 哲別, 燕京, 韓丞相, 金必達; idioms 楚河漢界, 光天化日, 狼子野心/路人皆知, 佛口蛇心, 無法無天, 無理取鬧, 勾結金狗, 咄咄逼人, 身懷六甲, 一意孤行, 一日之恩/永世難忘, 非分之想, 另結新歡, 背夫叛國, 罪有應得, 市井無賴, 狂蜂浪蝶; address 老衲/貧僧, 段兄, 王妃. Cross-episode: 顏烈 canonical (Ep1 sub 344 阿鰲 was OCR); 韓宰相 (Ep1) = 韓丞相 (Ep2) same office; 18-year wager is named structural event for Ep15+ flashbacks. Chi-OCR: 楊公子→顏公子 (novel 楊/顏), 段正德→段天德, 希章→希望 (two-ep w/ Ep1), 無理取同→無理取鬧, 大宋指紋→大宋子民. Promotion flags: **audit v15 Ep1 concat-trap promotions against current `cjk_fix_v2.py`** (Ep2 needed manual 六Your Highness fix); 希彰/希芯/希章→希望 → `OCR_NAME_COLLAPSE` (two-ep). |
| 3 | v16 | 488 | 蒙古 arc origin — child 郭靖 shelters 哲別, 鐵木真 adopts them, 郭靖 meets 拖雷/華箏, 江南七怪 find 郭靖, 柯鎮惡 duel with 銅屍/鐵屍 ending 陳玄風's death. First FULL firing for: 哲別 (Ep2 Watch → promoted), 鐵木真, 成吉思汗, 華箏, 拖雷, 窩闊台, 忽都虎, 王罕, 札木合, 博爾術, 塔塔克部族, 安答 (`anda` romanised), 銅屍陳玄風/鐵屍梅超風 death scene, 飛天蝙蝠柯鎮惡 on-screen duel (blinded by 九陰白骨爪), 老賊/臭婆娘 pet-name, 桃花洞 vow 生則同窮/死則同穴, 李萍 first on-screen, 靖媽, 郭夫人, 小靖 (**Ep2+Ep3 → STYLE §5**); 有福同享/有難同當 (安答 oath); idioms 英雄豪傑, 天公地道, 生死與共, 生死關頭, 高深莫測, 來日方長, 卻之不恭, 為民除害, 好勇鬥狠. Cross-episode: **老賊 origin pushed back to Ep3** — Ep22/Ep23 are later grief invocations (update REFERENCE §1); 成吉思汗's epithet 大漠的蒼狼 (chi OCR 蒼龍, Rule A yue wins); 鐵木真 chronology 1196/1201/1202; 七怪 9-year search dates 18-year wager at T+9. Chi-OCR: 量有此理→豈有此理 (3rd), 蒼龍→蒼狼, 窩辣台→窩闊台, 骨都虎→忽都虎. Promotion flags: **`<nickname>+<CSV-name>` concat trap** (銅屍/鐵屍/飛天蝙蝠 + CSV name — stage 4 fires before extras stage 5) → `cjk_fix_v2.py`; 哲別+大人/叔叔 concat post-build sed'd; 哲別 → drop Watch List. |
| 4 | v16 | 362 | 蒙古 childhood — 郭靖 vs 都史 wrestling, 乃蠻 ultimatum, 哲別 archery mission, 鐵木真 ginseng gift to 完顏洪烈. First FULL firing for: 都史, 桑昆大汗, 乃蠻/乃蠻大汗, 七拉河, 灰夾山, 王克罕山, 受封大典, 阿哥, 六弟/三哥/三太子/六太子/兩位太子, 洪烈 (bare); paired idioms 戰無不勝/攻無不克, 有勇無謀/烏合之眾, 忠心耿耿/視死如歸, 差之毫釐/失之千里, 人強馬壯/國運興隆; 賠了夫人又折兵 (三國演義); 受人恩惠千年記; 射人先射馬/擒賊先擒王 couplet. Cross-episode: 王罕/札木合/安答 second firings (Ep3 first); 好自為之 second firing (Ep2+Ep4); 事到如今 second firing (Ep24+Ep4). Chi-OCR: 啟桌→啟稟 (**3-ep → `OCR_NAME_COLLAPSE`**), 扎伯伯→札木合大汗 (chi OCR of 札; Ep3 canonical), 王漢→王罕 (yue ASR), 擒王→擒龍 (yue ASR, Rule B). Promotion flags: `our the great Jin empire` — extend `build.py` article-collapse to `our` + `cjk_fix_v2.py` entry; short-idiom dup-gloss collapser **3-ep (Ep24+Ep33+Ep4) → act**; 乃蠻/洪烈/太子 → `extras_baseline.json` next firing. |
| 5 | v16 | 435 | 蒙古 arc — 完顏洪烈/顏大爺 paternity reveal + 鐵木真 court + 華箏/都史 betrothal + 梅超風 sighting. First FULL firing for: 顏大爺 (蒙古-camp variant of 顏烈), 克烈部, 赤老溫, 四鬼, 四皇子 (柯鎮惡 form), 大汗 (bare), 郭大娘; idioms 姦淫擄掠, 無惡不作, 認賊作父, 喪心病狂, 令人髮指, 智勇雙全, 仁義為懷, 汗馬功勞, 狂妄自大, 愚昧無知, 虛有其表, 萬眾一心, 頂天立地, 弄巧成拙, 心高氣傲, 雞犬不寧. Cross-episode: 顏大爺 = 顏烈; 都史/桑昆/安答/六太子/野心勃勃 second firings (Ep4 first). Chi-OCR: 郭蜻→郭靖, 藥昆→桑昆, 克鰲部→克烈部. Promotion flags: concat traps `完NgaanYour Highness/NgaahnYour Highness→Prince Wanyan`, `大Master→First Master` (second firing), `Gwok大Mother→Mrs Gwok` → `cjk_fix_v2.py` `shared_concat_fixes` on next firing. **Outcome: PARTIAL.** |
| 6 | v16 | 438 | 迴聲谷 ambush of 梅超風 — 張阿生 mortally struck by 九陰白骨爪, deathbed marriage to 韓小螢 and death; 鐵木真 一箭雙鵰 scene + 金刀 gift to 郭靖; failed proposal for 華箏 / 都史; 尹志平 brings 丘處機 letter revealing 楊康 is male (Ep2 18-year-wager gender resolution); 柯鎮惡 half-year intensive-training decree. First FULL firing for: 張阿生 death + 小螢 deathbed marriage, 迴聲谷, 金刀 寶刀 gift (precursor to 金刀駙馬 title Ep23+), 尹志平 (first appearance, Wan Zi-ping / Wan Ji-ping), 紅娘 (朱聰 matchmaker banter), 八字純陰, 賊眉鼠眼, 指腹為婚, 一箭雙鵰, 奮勇殺敵, 欲速則不達, 東征西討, 雞犬不寧 (Ep5+Ep6 confirmed, promote §10). Cross-episode: 一心一意 second firing (Ep24+Ep6 — promote §10 canonical); Ep2 18-year-wager gender question resolved (楊康 male). Chi-OCR: 郭蜻→郭靖 (Ep3/4/5/6 — four-ep batch pattern, promote to `OCR_NAME_COLLAPSE`); 梅朝風/梅竹風→梅超風 (two-ep Ep5+Ep6); 洪良→紅娘 (yue ASR, Rule A); 節別→哲別 (yue ASR); 肉速不達→欲速則不達; 子夫和婚→指腹為婚; 雙周→雙鵰; 小營→小螢 (canonical per CSV); 射英→殺敵. Promotion flags: **six new `<titles-key>+<suffix>` concat-trap entries added to `cjk_fix_v2.py` `shared_concat_fixes` / `yale_concat_fixes` this session** (五Master→Fifth Master, 七Master→Seventh Master, 大Master→First Master (Ep5+Ep6 two-ep confirmation — also promote STYLE §19), 紅Mother→the Matchmaker, 姑Mother→Miss, 柯Big Brother→Brother O, Zit-BitMaster→Master Zit-Bit / Jit-BitMaster→Master Jit-Bit). Hybrid-variant dup-gloss trap fired on subs 76 (紅娘 tautology) and 413 (一心一意 dup-gloss) — post-fixed manually (dup-gloss collapser did not fire; Ep24+Ep33+Ep4+Ep6 — four-ep pattern, act on collapser threshold). |
| 7 | v16 | 396 | 蒙古 arc — 郭靖 returns home; 馬鈺 (disguised as 前輩) secretly teaches 全真教 內功心法; 郭靖 defeats 三師父 韓寶駒 via internal energy; 江南七怪 suspect 旁門左道 from 梅超風; 完顏洪烈/桑昆/都史 assassination plot vs 鐵木真; 馬鈺 reveals identity. First FULL firing for: 馬鈺 (first on-screen, 全真教 掌教真人, disguised-前輩 teaching arc — STYLE §5 next bundle), 馬道長, 掌教真人, 嘯天 (李萍 invokes 郭嘯天), 玉女劍法 / 玉女穿梭劍法 (全真教 technique 韓寶駒 teaches), 八卦步法, 兩儀, 內功心法, 牛不喝水/為甚麼牛要低頭 (proverb — 大師父 to 郭靖), 天下無難事/只怕有心人 paired 俗語, 清理門戶 (Ep23+Ep7 second firing — promote §10), 三生有幸, 名門正派, 旁門左道, 臨陣退縮, 問心有愧, 神不知鬼不覺, 婦人之仁, 壯志雄心, 要委屈求全, 霍將軍/霍叔叔 (Jin general sent by 完顏洪烈), 六太子/六王爺 (完顏洪烈 Jin address variants), 大汗 (Mongol ruler address — Rule A Khan rendering), 大金國. Cross-episode: 桑昆/都史/義兄 (Ep4 second firing confirmed); 婦人之仁 (Ep22 catalogue firing); 好自為之 (Ep2+Ep4+Ep7 third firing, STYLE §10 stable). Chi-OCR: 活將軍/活叔叔→霍將軍/霍叔叔 (chi-OCR of 霍; yue witness corroborates fok3, also 活 not a surname); 郭蜻→郭靖 (five-ep batch Ep3/4/5/6/7 — urgent promotion to `OCR_NAME_COLLAPSE`); 梅朝風→梅超風 (three-ep Ep5+Ep6+Ep7); 旺有此理→豈有此理 (already in collapse table); 節別→哲別 (yue ASR, continuing Ep6). Promotion flags: **v15/v16 concat-trap entries (大Master/四Master/七Master/五Master/六Your Highness) promoted to SESSION-NOTES as added to `cjk_fix_v2.py` but NOT actually present in shipped script** — applied via manual post-build sed this session; script edit needed next bundle bump. 馬鈺/馬道長/掌教真人 first-firing → STYLE §5 + `extras_baseline.json` on second firing (Ep8+ imminent — Ep7 is 馬鈺's introduction arc); 霍將軍/霍叔叔 + 活→霍 chi-OCR → `OCR_NAME_COLLAPSE` on second firing. |
| 8 | v17 | 444 | 蒙古 arc — 馬鈺 reveal + 桑昆 night-raid + 札木合 安答 suicide + 成吉思汗 declaration + 金刀駙馬 + 郭靖 rejects 華箏 + 梅超風 retells 老賊/桃花島 past + 馬鈺+五怪 fake 天罡北斗七星陣/斗轉星移 rescue + 九陰真經 玄關謹守/五心向天 bargain. First FULL firing for: 馬鈺, 馬道長, 木華黎, 博爾忽, 博爾朮, 素女劍, 天罡北斗七星陣, 北斗七星陣, 斗轉星移, 全真派, 志平, 郭大媽, 楊家叔叔; 君子報仇十年不晚, 兵不厭詐, 貪生怕死, 殺個片甲不留, 深仇大恨, 邪魔外道, 凶多吉少 (plain-prose). Cross-episode: 大汗 five-ep (Ep3+4+5+7+8, promote baseline); 婦人之仁 Ep7+22+8 (§10 non-gendered confirmed); 重陽真人 Ep31+8 (promote §5/baseline); 女魔頭 Ep23+8 (§5 stable, drop Ep23 Watch); 大漠的蒼狼 Ep3+8 (chi 蒼龍 OCR); 三生有幸 Ep7+8, 指腹為婚 Ep6+8, 虛有其表 Ep5+8 (plain-prose); 金刀 Ep6+8 (promote baseline); 安答 Ep3+4+8 (baseline). Chi-OCR: 蒼龍→蒼狼 (Ep3+8), 央馬/騎馬→駙馬 (Ep8+23+25 three-ep), 又顯/又昆→桑昆, 天踢→天罡. Promotion flags: **四Master → Fourth Master added to cjk_fix_v2.py this session** (completes 江南七怪 family — Ep6 大/五/七, Ep8 四); 博爾朮 resolves Ep3 博爾術 (朮/術 trad-vs-simp). |
| 9 | v17 | 428 | 郭靖 departs 蒙古 (華箏 vow / 娘親 duty talk / 拖雷 farewell) → 江南七怪 fake-kidnap lesson in ruined temple (江湖險惡 / 四字"打不過走") → 西毒/白駝山/赤頂青蛇 warning → 蓉兒 first on-screen as 小叫化子 at 醉仙樓 (傻哥哥 dish-ordering / dice grift / 黃河三鬼 chase / chicken-coop hide / "我叫黃蓉" name reveal). First FULL firing for: 西毒, 華山論劍, 赤頂青蛇, 大力金剛指, 妙手雙飛, 少林寺, 黃河三鬼, 醉仙樓 (Ep2 venue, Ep9 first 七怪-rendezvous naming), 嘉興, 金刀駙馬 (Ep6 金刀 + Ep8 駙馬 + Ep9 compound first firing, before the 駙馬爺 sarcastic variant Ep23+), 馬道長 (Ep7+Ep8+Ep9 three-ep → STYLE §5 + baseline), 釀鴨舌/珍珠魚目羹/豆腐絲擺麵/女兒紅 (precursors to Ep21 dish catalogue — keep-CJK per REFERENCE §4), 楊叔叔, 小叫化子 (蓉兒's disguise nickname — rendered "little beggar" in all three variants per STYLE §18 ban on 叫化子 CJK). Cross-episode: 六王爺 Ep1+Ep7+Ep9 three-ep; 後會有期 English-only rendering (§10-purged under v17 plain-prose). Chi-OCR: 郭蜻→郭靖 (six-ep batch Ep3+4+5+6+7+9 — `OCR_NAME_COLLAPSE` firing cleanly); 歐陽鹿/歐陽詣/歐陽當/歐陽之→歐陽峰 (subs 133/135/136/145 yue-witness 歐陽鋒 clean); 岩馬→駙馬 (sub 37, four-ep with Ep8 央/騎); 境負→辜負 (Ep7+Ep9); 同有此理→豈有此理 (two-ep with existing 量有/旺有); 痢一閱/閣一閱→闖一闖; 徹→出 (一聲不徹); 春→蠢; 蔣→莊; 恬鴨生→釀鴨舌. Promotion flags: **二/三/六Master concat-trap** (completes 江南七怪 master-address family begun Ep6 大/五/七 and Ep8 四; post-build sed'd this session) → `shared_concat_fixes` next bump. **六弟/二哥/七妹/saam哥 sibling-ordinal vocatives** (seven-ep pending since Ep2) — post-build sed'd; confirms the Ep2 Watch flag; promote full family to `shared_concat_fixes` or overlay baseline. Dish-names 釀鴨舌/珍珠魚目羹/豆腐絲擺麵/女兒紅 → `extras_baseline.json` on Ep21 second firing (REFERENCE §4 precedent). |
| 10 | v17 | 478 | 郭靖/蓉兒 escape 黃河三鬼 by river → 醉仙樓 brawl + 念慈's father 楊鐵心 mistake → 歐陽克 kidnaps 念慈 to 歸雲莊 secret-chamber (軟蝟甲 backs him off) → 梁子翁 small-town 木蓮子/小青蛇 fake-rescue → 蓉兒 girl-reveal in cave → 沙通天/靈智上人/歐陽克 王爺-summons conference → 雷雨 ambush plan → 大漠 future-plan dialogue → 金刀駙馬 confession + 蓉兒 banishment. First FULL firing for: 飛箱樓 (yue 飛箱; chi 飛艙樓 OCR), 蛤蟆功 (歐陽峰 named technique — first on-screen reference), 黃河三鬼 (Ep9 named in 七怪 warning, Ep10 first on-screen confrontation), 阿蓉 (郭靖's address for 蓉兒 in girl-reveal arc), 木蓮子 (蓉兒's invented herb deception of 梁子翁 — kept CJK per §8 雪蓮 precedent for invented-herb names; lint flagged but judgment-call (c)), 護法/白衣護法 (靈智上人's bodyguard ranks), 二師父 (朱聰; cjk_fix_v2 二Master→Second Master fired cleanly), 沙兄 (peer-address among 王爺's invited masters), 主人/少主人 (歐陽克 household), 上人 (Buddhist clergy address for 靈智上人), 公子 (formal address to 歐陽克), 大漠 (郭靖's poetic Mongolia form, distinct from 蒙古 — rendered "the Great Desert"). Cross-episode: 軟蝟甲 second firing (Ep24+Ep10, baseline stable); 華山論劍 second firing (Ep9+Ep10 — STYLE §8 stable); 金刀駙馬 second firing (Ep9+Ep10 → promote to `extras_baseline.json` next bump); 沙通天/靈智上人 (Ep22+Ep10 — promote-stable confirmed); 念慈 (Ep24+Ep10 cross-arc); 黃河三鬼 second firing (Ep9+Ep10 → promote to baseline). Chi-OCR: 阿藝/阿勇→阿蓉 (sub 182, 276, 280); 其兒/鞭兒→蓉兒 (subs 237, 350, 358, 387, 455 — continues Ep21+ pattern, OCR_NAME_COLLAPSE firing cleanly); 量有此理→豈有此理 (sub 128, four-ep batch — collapse table firing); 希彰→希望 (sub 202, four-ep batch w/ Ep1+Ep2+Ep33); 白陀山→白駝山 (subs 97, 99, 315 — yue witness 白駝山 clean); 歐陽鋒→歐陽峰 (subs 99, 100, 101, 316 — chi 歐陽峰 was actually correct here, yue had 歐陽鋒 the OCR-drift form); 飛艙樓→飛箱樓 (sub 391); 大滿→大漠 (sub 408); 廉詞→念慈 (subs 119, 120 yue ASR — Rule B chi wins). Promotion flags: 飛箱樓 → `extras_baseline.json` if recurs; 大漠 (Ep10 first; will recur in 蒙古 return arcs Ep15+) → baseline on second firing; 木蓮子 single-firing — judgment call (c) keep CJK like 雪蓮; 蛤蟆功 → STYLE §8 (already in baseline per build.py) confirmed correct; 護法/白衣護法 → STYLE §6 on second firing; 沙兄 single-firing peer-address; 阿蓉 → STYLE §5 + baseline on second firing (郭靖's intimate address form, distinct from 蓉兒 vocative). |
| 16 | v18 | 445 | 梅超風 courtyard ambush (六怪 hostages, 老賊-disciple-bond reveal) + 念慈 王府 infiltration + 包惜弱 confronts 楊康 about forged letter + 楊康 武穆遺書 motivation reveal to 念慈 + 包惜弱 begs 楊康 to leave 王府 (refused) + 蓉兒/靖 reconciliation (軟蝟甲 saves 蓉兒 in second 梅超風 attack) + 楊鐵心 rescue-plan with 蓉兒/靖/念慈. First FULL firing for: 穆念慈 (active ep — 王府 infiltration + 楊鐵心 daughter arc), 武穆遺書 (named artefact first on-screen naming — ties back to Ep1 岳飛 靖康恥 narration), 忍辱負重 (STYLE §10 crit 1 — 楊康's rationalising line), 功虧一簣 (Ep12+Ep16 two-ep — STYLE §10 confirmed). Cross-episode: 軟蝟甲 Ep10+Ep24+Ep16 three-ep stable; 老賊 (梅超風's term for 陳玄風) Ep3+Ep22+Ep23+Ep16 — REFERENCE §1 entry now four-ep-confirmed; 白骨爪/九陰真經 cave-theft flashback reprise of Ep3 原罪. Chi-OCR: 其兒/鞭兒→蓉兒 (continuing 8-ep batch — collapse table firing); 郭蜻→郭靖 (continuing 8-ep batch); 梅朝風→梅超風 (Ep5+6+7+16 four-ep — already flagged Ep7 three-ep); 侈→爹 (Ep23+Ep16 two-ep promote OCR_NAME_COLLAPSE); 家人天上/金吉人天相→吉人天相 (sub 122 chi mangles 吉 as 金吉); 軟衛甲/燕尾甲→軟蝟甲 (continuing Ep24 flag); 心滿意足→心滿意足 clean; 我要非→岳飛 (sub 165 yue ASR Rule B chi wins); 母母遺書→武穆遺書 (yue ASR — 穆/母 homophone cluster — Rule B chi wins). Promotion flags: 梅師姊/梅師姐 — chi+yue variant pair (姊/姐) stable rendering "Senior Sister Mui/Muhk" — promote to STYLE §5 (two-form acceptance) on next firing; 夫人 bare as 王府 servant-address vocative — added to overlay this ep, promote to baseline on next firing; 中原 as rendered "the Central Plains" in romanised — two+-ep stable (Ep15+Ep16), promote to baseline next bump; 鐵心 bare as 包惜弱 vocative for 楊鐵心 (Ep13+Ep14+Ep15+Ep16 four-ep — promote baseline); 吉人天相 (Ep14+Ep16 two-ep — STYLE §10 gate: plain-prose "the good are blessed by Heaven" fails — render English-only going forward, remove CJK variant from §10 consideration). |
| 17 | v18 | 372 | 包惜弱/楊鐵心 boat-escape + 楊康 betrayal + 丘處機 captures 段天德 + 完顏洪烈/金必達 confession + 穆念慈 steals 金國 map + 火流星 ambush prelude. First FULL firing for: 金必達, 震天雷, 火流星, 兒臣, 孩兒, 愛屋及烏, 三十六計/走為上計, 踏破鐵鞋無覓處/得來全不費工夫 (Ep12+17), 芙蓉帳暖/明月當空 (長恨歌), 家破人亡 (Ep1+3+14+17). Cross-episode: 鐵心 Ep13-17, 中原 Ep15-17, 大漠 Ep10+11+17, 楊夫人 Ep11+14+16+17 → baseline; 大金國 trap Ep11+14+17; 婦人之仁 4-ep; 金刀駙馬 5-ep. Chi-OCR: 會牲→畜生 (5 subs → OCR_NAME_COLLAPSE); 女→娘 (4 subs); 騎馬→駙馬 Ep8+14+17 → promote; 愛屋及人烏→愛屋及烏; 路下→跪下; 父→罵. Promotion flags: 震天雷/火流星 → baseline Ep18+; 兒臣/孩兒 → STYLE §5/§6 2nd; 金必達 → CSV 2nd; §10 candidates 愛屋及烏, 三十六計, 踏破鐵鞋, 芙蓉帳暖, 家破人亡 pass admission. |
| 18 | v18 | 454 | 完顏洪烈/包惜弱 王府 reunion-poison + 包惜弱 suicide-attempt → 法華寺 nun-vows + 楊康 chained by 丘道長 (acknowledge-爹 ultimatum) + 念慈 sword-rescue + 楊康 false-vow → 完顏洪烈/歐陽克/彭寨主 pursue via 九陰白骨爪 trail + 楊康 sees 包惜弱-as-nun reunion at 法華寺 + 完顏洪烈 arrives. **Per-user instruction this session: 娘→娘親 normalised throughout (STYLE §4 Cantonese-preferred; missed in Ep17). Same applies retroactively if Ep17 is re-processed; bare 爹→爹親 normalised in parallel.** First FULL firing for: 楊大嬸/大嬸 (王府-era 包惜弱 address by 楊鐵心 generation), 桃花鎮 (蓉兒's pre-桃花島 town), 醉月樓 (Lin'an inn — 丘道長 confronts 楊康), 正德 大街 (Jin/Song border road), 竇 小姐 (one-off bystander). Cross-episode: **人不風流枉少年 Ep14+Ep18 two-ep** (named 俗語; STYLE §10 admission gate passes — register cultural weight English flattens — promote on next firing); 法華寺 Ep1+Ep18 two-ep (canonical from Ep1 — promote to baseline); 牛家村 Ep14+15+18 three-ep stable (promote to baseline); 阿康/康兒/念慈/穆姑娘 cross-arc continued from Ep11–17. Chi-OCR: 楊大姥→楊大嬸 (4 subs; 姥/嬸 visual drift, yue clean — promote OCR_NAME_COLLAPSE on next firing); 希龐/希劑/希鹿/希單→希望 (continuing Ep1+2+10+33 batch — collapse table firing); 會牲/會牡→畜生 (Ep14+17+18 three-ep batch); 路下→跪下 (Ep17+Ep18 two-ep); 侈→爹 (Ep23+16+18 three-ep — promote OCR_NAME_COLLAPSE); 后飛→岳飛 (sub 216 single-firing); 哲頭→舉頭 (sub 302 chi novel OCR); 千道士→丘道士 (sub 94 chi-OCR — yue garbled, but 丘處機 identity confirmed by next-sub context); 元顏康→完顏康 (chi-OCR Ep18 novel, watch); 自做功→自作孽 (sub 233 single-firing). Promotion flags: **爹親 cross-stage trap → cjk_fix_v2 `Father親 → Father` added this session** (parallel to existing My Mother子→my wife pattern; first firing on bundle bump that introduces 爹親 normalisation rule); **歐陽公子 cross-stage trap** Ep33+Ep18 two-ep — added cjk_fix_v2 `Au-Joeng公子 → Young Master Au-Joeng` and yale `Au-Yeung公子 → Young Master Au-Yeung` this session (CSV 歐陽 stage 4 strands 公子); 大叔 bare → baseline next firing (compounds 楊大叔/穆大叔 already covered); 醉月樓 → baseline if recurs in Lin'an arcs; 卑鄙 single-firing colloquial English-only render. **Outcome: FULL.** |
| 20 | v13 | 587 | 臨安 / 元宵 arc with 岳文 and 武穆遺書 plot. First FULL firing for: 岳王廟, 岳王爺, 岳文, 岳老伯, 岳大叔, 武穆遺書, 碧玉富貴燈, 元宵佳節, 如意燈/吉祥燈/添丁燈, 翠紅樓, 獅子林, 山神廟, 林升 題臨安邸 quatrain, 精忠報國, 醉生夢死, 風流快活, 亡國奴, 半壁江山, 用兵如神, 行軍佈陣, 安邦定國, 雄霸天下, 居功至偉, 皇天不負有心人, 各安天命, 鬼哭狼嚎, 簡長老, 麻瘋病. Cross-episode: first on-screen 降龍十八掌 (vs 沙通天); first scene naming 東邪/西毒/南帝/北丐 together. Chi-OCR: 匡文/策老伯/品王爺→岳文/岳老伯/岳王爺; 土/犁/悍/幫紅樓→翠紅樓; 葵古/划古→蒙古; 梁子峰/梁子忠→梁子翁. Promotion flags: 岳王爺→岳Your Highness and 本姑娘→本姑Mother cross-stage traps → `cjk_fix_v2.py` `shared_concat_fixes` on next firing. |
| 21 | v12 | 501 | 洪七公 apprentice-acquisition (丐幫 business + 拖雷 宋-Mongol alliance mission). First FULL firing for: 梁子翁, 彭長老, 鄂州, 鄭州, 天香樓, 樞密院, 藏經閣, 禁軍, 百花雞/釀鴨舌/清蒸活鯉魚/珍珠魚眼羹/龍虎鳳會石斑, 百花蛇/果子狸/竹絲雞 (龍虎鳳), 七仔 (洪七公 self-naming, STYLE §5 NOT a general substitute), 成事不足敗事有餘, 不見棺材不流淚, 群龍無首, 後患無窮, 心腹大患, 尊師重道. Cross-episode: first on-screen 降龍十八掌 now attributed to Ep20, not Ep21. Chi-OCR: 其兒/鞭兒→蓉兒, 郭蜻→郭靖, 梁智翁/梁子仍→梁子翁, 語州/開州→鄂州, 權密院→樞密院, 藏真閣→藏經閣. |
| 22 | v12 | 463 | 洪七公 poisoning at 望江樓 + 降龍十八掌 death-bed transmission to 郭靖. First FULL firing for: 望江樓, 清溪別院, 博將軍/赤將軍, 沙通天, 彭連虎, 靈智上人, 降龍有悔/躍龍在淵, 一流絕頂高手, 時辰, 兵家大忌, 夜長夢多, 打草驚蛇, 狗咬呂洞賓, 好心遭雷劈, Dragon-chant quartet (去似天龍雲飛躍 / 收似降龍穩深沈 / 腳似飛龍騰萬里 / 拳似怒龍翻四海 — STYLE §10 format), 人之將死/其言也善. Cross-episode: 老賊 (梅超風's term for 陳玄風) second firing with Ep23 (→ REFERENCE §1). |
| 23 | v14 | 429 | 華箏 poisoning-cure + 梅超風 老賊 lament + 黃藥師 first appearance (邪中有三分正 couplet) + 華箏 法師 hairpin-suicide. First FULL firing for: 雪蓮玉露丸/雪蓮, 黃小邪 (蓉兒 self-name), 死老邪 (七公 insult to 黃藥師), 邪中有三分正/正中帶七分邪 couplet (STYLE §10), 女魔頭, 寶刀未老/彼此彼此/爐火純青/中看不中用/甘敗下風 (Five-Greats banter), 艷福, 抱頭痛哭, 罪大惡極, 一人做事一人當, 假仁假義, 清理門戶, 沒齒難忘, 延年益壽, 法師, 當今兩大高手, 黃世伯/世伯. Cross-episode: 老賊 second firing (Ep22+Ep23 → REFERENCE §1 confirmed). Chi-OCR: 其兒/鞭兒→蓉兒 (continuing pattern), 郭蜻→郭靖, 央馬爺→駙馬爺, 陳元鋒/袁風/元鋒→陳玄風/玄風, 駁→爹. Promotion flags: `黃前輩→Wongsenior` cross-stage trap (前輩→senior eats it); `死老邪→死Old Heretic` trap (worked around in English; STYLE §5 has 死老邪→damned Old Heretic). Both → `cjk_fix_v2.py` `shared_concat_fixes` on next firing. |
| 11 | v17 | 475 | 靈智上人/歐陽克 inn ambush + 楊鐵心-as-木易 reveal to 郭靖 + 完顏洪烈 voice-recognition of 包惜弱 + 梅超風 cave (97→99th victim, 功虧一簣 fails) + 比武招親 with 完顏康 incognito win. First FULL firing for: 楊鐵心-as-木易 disguise, 木大叔/穆世伯/楊大叔/楊叔叔/楊嬸嬸/穆姊姊/穆大叔/穆小姐 family-address cluster, 荷塘村, 土地廟, 玄門/奇門 internal-arts variants, 完顏康 incognito self-naming, 李公明, 功虧一簣, 父皇. Cross-episode: 大金國 cjk_fix concat trap recurred (stable); 郭大哥 overlay registration needed (CSV-name + 大哥 parallel to Ep33 周伯通大哥). Chi-OCR: 鞭兒/其兒→蓉兒 (Ep30-32 batch continuing), 郭蜻→郭靖, 題蝦虹→蛤蟆 (yue witness). Promotion flags: 大漠 (Ep10+Ep11 → baseline); 女大不中留 (Ep31+Ep11 two-ep → STYLE §10 validated); 上人 (Ep10+Ep11 two-ep → baseline "the Reverend"); 楊大叔 family cluster → baseline on Ep15-19 楊康 arc firing. |
| 12 | v18 | 533 | 王處一 poisoning arc — 燕京 + 包惜弱 death-anniversary mourning + 楊康/穆念慈 + 王府 banquet ambush + 九陰白骨爪 cave source revealed to 歐陽克. First FULL firing for: 王處一, 王道長, 長春真人/長春子, 五師叔/大師伯/三師兄/師叔/師伯/師兄 (全真七子 peer-order cluster), 忘年之交, 楊兄, 穆師伯/穆大叔, 彭某, 梁老先生/梁先生, 桑滿族, 千年參酒, 長白山, 恩師, 啟稟少爺, 窈窕淑女/君子好逑 (詩經·關雎 §10 crit-2), 踏破鐵鞋無覓處/得來全不費工夫 (夏元鼎 couplet §10 crit-4), 功虧一簣 (§10 crit-2), 調虎離山之計 (§10 crit-3), 完顏 bare, 春香. Cross-episode: 大漠 Ep10+11+12; 楊大叔/穆大叔/土地廟 Ep11+12; 燕京 Ep2+12; 醉仙樓 Ep2+9+12; 重陽真人 Ep8+12; 功虧一簣 Ep11+12 §10-confirmed — all → baseline. Promotion flags: 師叔/師伯/師兄/師弟 全真派 peer-address family Ep7/8/11/12 → baseline. |
| 13 | v18 | 366 | 王處一 poisoning aftermath — 王府 escape, 落日亭 蓉兒-trick, 靈蛇山莊 raid (歐陽克 drinks 寶蛇 blood; 蓉兒 trapped with 梅超風 mistaking 郭靖 for 尹志平), 楊鐵心-as-木易 identifies 包惜弱 as 王妃, ep ends at 蒼松道觀. First FULL firing for: 王妃, 王府, 落日亭, 靈蛇山莊, 試劍亭, 蒼松道觀, 惠清師太, 牛道士, 梅若華, 梁老怪, 毒沙掌, 毒蛇霧, 五心向天, 父皇, 鐵心 (bare). Cross-episode: 王處一/王道長 Ep12+Ep13 → §5/baseline; 楊大叔 Ep11+Ep12+Ep13 three-ep → baseline; 楊兄/春香 Ep12+Ep13; 父皇 Ep11+Ep13; 王府 Ep11+Ep12+Ep13 three-ep → baseline. Chi-OCR: 其兒/鞭兒→蓉兒 (continuing), 希彰→希望, 量有此理→豈有此理, 阿勇→阿蓉 (Ep10+Ep13 two-ep), 大難難逃→大難不逃 (sub 136 dittography), 牡→畜生 (sub 12 chi). Promotion flags: **本Miss third firing (Ep20+Ep25+Ep13) → structural fix `shared_concat_fixes` longest-first sort.** Lin'an府 single-firing cross-stage trap → `cjk_fix_v2.py` on second firing. 王妃/王府 lint judgment-call (c) keep CJK as court-rank/place parallel to 王爺/小王爺 and 歸雲莊/靈蛇山莊. |
| 14 | v18 | 396 | 王府 reunion arc — 包惜弱/楊鐵心-as-木易 reunion + 完顏康 paternity reveal (鐵槍 + 牛家村 origin) + 完顏洪烈 confronts 包惜弱 + 楊鐵心 ambush at 福來客棧 + 阿康 confrontation + 大金國 court visit. First FULL firing for: 福來客棧, 和字號房, 別院/別苑, 太醫, 嘉興, 西夏, 張老爹/張老爺, 春香, 師太 (generic), 金將軍, 餓死事小/失節事大, 求生不得/求死不能, 人不風流枉少年, 精誠所至/金石為開, 始亂終棄, 恩重如山/情至義盡, 卑躬屈膝, 三長兩短, 吉人天相, 要風得風要雨得雨, 大膽畜生, 以下犯上/尊卑不分, 放蕩不羈, 不成體統, 大恩大德, 垂手可得. Cross-episode: 福來客棧 + 完顏康 + 六弟 Ep4+Ep14; 楊大叔 Ep11/12/13/14 four-ep → baseline; 春香 Ep12+Ep14; 師太 Ep13+Ep14; 大金國 cross-stage trap Ep11+Ep14 (cjk_fix_v2 catches); 鐵心 (bare) Ep11+Ep13+Ep14 three-ep → baseline; 家散人亡 Ep3+Ep14. Chi-OCR: 章父王→望父王, 苦衷→苦夷/苦翰, 朝思暮想→朝思莫想, 始亂終棄→屎亂蹤氣 (yue ASR), 失節→失智 (yue ASR). Promotion flags: 鐵心/福來客棧/太醫 → baseline next bump; 大金國 trap → drop Watch List (two-ep cjk_fix_v2 confirmed). |
| 15 | v18 | 431 | 楊康 王府 identity-crisis arc — garden servant-humiliation, rooftop secret meeting with 穆念慈, faked-letter plot (with order to 父王 to silence 牛家村 witnesses), 五里坡 broken-temple disowning of 楊鐵心 ("我是畜生"), 包惜弱 letter-burning + falling-out with 完顏洪烈 over 養父 oath, 蓉兒 city thief-grift caught by blind 柯鎮惡, 七怪 expel 蓉兒 + push 穆念慈/郭靖 betrothal as 平妻, 西湖 boat (歐陽克 + 蓉兒 + 軟蝟甲), 梅超風 confronts 歐陽克, 七怪 lecture 郭靖 (父仇未報 / 黃藥師 condemnation), 穆念慈 missing → 蓉兒 returns. First FULL firing for: 五里坡, 開封府, 青龍寺, 趙王, 粘罕將軍, 韓女俠, 找死, 君子遭禍/孤燕入巢/思與君一場離恨/是乃天意/君子盛年/何患無妻 (楊康's faked elegiac letter — paste-up classical register, rendered as CJK+gloss in hybrid per STYLE §10 paired-couplet rule), 相請不如偶遇 (歐陽克 lake-pickup line), 貧賤夫妻百事哀, 人非草木/誰能無情, 飲水思源 (plain-prose), 平妻 (co-principal wife — 郭靖/穆念慈 betrothal proposal). Cross-episode: 楊大叔/楊叔叔 Ep11/12/13/14/15 five-ep — baseline confirmed; 燕京 Ep2+12+15 three-ep → baseline; 王妃/王府 Ep11/12/13/14/15 five-ep → baseline; 鐵心兄 Ep14+15 two-ep → baseline; 大師父/三師父 Ep5+6+15 three-ep cjk_fix concat-trap firing cleanly; 阿蓉 Ep10+13+15 three-ep → STYLE §5 + baseline; 父王 Ep11+13+15; 牛家村 Ep14+15 two-ep → baseline; 春香 Ep12+14+15; 軟蝟甲 Ep10+24+15 three-ep stable. Chi-OCR: 其兒/鞭兒→蓉兒 (continuing seven-ep batch — collapse table firing); 郭蜻→郭靖 (continuing); 找死'→找死 (sub 6 stray apostrophe); 苞→錯 (sub 158 dittography 做苞太多); 無她無恨→無怨無恨 (sub 177 chi 怨/她 OCR); 苦衷→苦夷 (Ep14+15 two-ep — promote to OCR_NAME_COLLAPSE). Promotion flags: 楊康 elegiac-letter classical block (subs 69-73) — judgment-call (c) per lint, single-ep firing — watch for recurrence in 楊康 deception arcs; **找死** colloquial register tag, plain-prose ("courting death") in romanised, hybrid CJK; single-firing. **平妻** common-noun rendered English; watch for 郭靖/穆念慈/華箏 arc recurrence. **柯大俠/韓女俠** vocative address forms (sub 400) — promote to baseline on second firing. **西湖** as 歐陽克 boat-scene venue — promote on second firing (likely Ep20 元宵 arc). |
| 24 | v14 | 364 | 蓉兒 boat departure + 華箏 drunken-proposition + 楊康 repentance with 穆念慈 + 黃帝內經 antidote diagnosis. First FULL firing for: 軟蝟甲 (first on-screen), 小保 (NOT 小寶 — REFERENCE §2 cross-episode-canonicality note), 推宮換血 (Rule B case study vs yue-HIGH 推功換血; genesis of STYLE §2 Rule A/B/C split, REFERENCE §2), 黃帝內經, 遊山玩水, 視日無多, 罪孽滿身, 故態復萌, 禽獸不如, 甘心被你欺騙. Cross-episode: 推宮換血 canonical vs yue homophone; genesis for STYLE §2 Rule A/B/C architecture. Chi-OCR: 網康→阿康 (novel 網/阿 OCR, watch), 華珍→華箏 (yue-ASR zing1/zan1), 燕尾甲→軟蝟甲 (yue-ASR, watch), 會牲→畜生, 九寶/小豪→小二, 境負→辜負. Promotion flags: collapser-miss family (後會有期, 忘恩負義, 視日無多) post-cleaned manually — candidate for lowering `cjk_fix_v2.py` collapser threshold or adding short-idiom entries. |
| 25 | v14 | 423 | 華箏 frees 郭靖 + 穆念慈/楊康 reunion + 蓉兒 jealousy + 太湖 boat + 歸雲莊 reveals 陸家's 桃花島 link. First FULL firing for: 羞花亭, 千年蔘王, 大衍數 step-names (零/地三/頤王/起/伏/定/已/和 — 陸乘風 copy of 桃花島 layout), 淫賊/奸夫淫婦/如狼似虎/年少無知 (陸家 duel scandal register), 姓陸的, 馮兄→陸兄 OCR correction. Cross-episode: 推宮換血 second firing (念慈/楊康 romantic-sacrifice context, parallels Ep24 Rule B). Chi-OCR: 央馬爺/騎馬爺→駙馬爺, 和伯伽/伯伽→瑤迦 (consistent chi drift), 冠英→滿英 (yue ASR), 馮兄→陸兄. Promotion flags: 本姑娘→本姑Mother trap **third firing** (Ep20+Ep25, Ep20 flagged) → promote to `cjk_fix_v2.py` `shared_concat_fixes`; 遵命→"Yes, sir" post-build sed — cjk_fix_v2 candidate if recurs; 和伯伽→瑤迦 → `OCR_NAME_COLLAPSE` on next firing. **Outcome: PARTIAL** (manual sed passes required beyond cjk_fix_v2). |
| 28 | v10 | 515 | 程家 snake-bite arc + 陸乘風 reveal at 黃藥師 reunion + 華箏 finds drunken 郭靖. First FULL firing for: 陸冠英/程瑤迦 betrothal, 想逝者/天蓋高 classical lament couplet (STYLE §10). Cross-episode: Sub 22 case study (PIPELINE §4, REFERENCE §8) — eng correct vs OCR-damaged chi, yue 每日用一隻毒蝎嚟養大 witness. Sub count 515 chi-spine. |
| 29 | v10 | 408 | 桃花島 drunken-郭靖 / 華箏 farewell + 周伯通 sworn-brotherhood + 歐陽峰/歐陽克 marriage proposal. First FULL firing for: 桃花陣 sworn-brotherhood (REFERENCE §3), Slap-Memorise-九陰真經 setup (天之道/損有餘而補不足 — STYLE §10), 秦晉之好 (STYLE §10). Cross-episode: confirmed 我爹/你爹 and 週大哥 promotions. |
| 30 | v11 | 507 | 桃花島 三試 (武鬥/文鬥/九陰真經) for 蓉兒's hand + 歐陽峰/歐陽克 ambush on 阿衡. First FULL firing for: 積翠亭, 梅花樁, 碧海潮生曲, 文鬥, 奇門八卦, 神龍擺尾. Promotion flags: 叔叔/武功/走火入魔 → `extras_baseline.json`; several cross-stage concat traps → v11 bundle. |
| 31 | v12 | 434 | 黃藥師 / 阿衡 / 王重陽 / 九陰真經 origin flashback; 冰窒 framing at 桃花島. First FULL firing for: 一陽指, 華山論劍, 王重陽, 重陽真人, 內子, 激將法, 過目不忘, 玉石俱焚, 雞鳴狗盜, 水能載舟亦能覆舟, 李白 將進酒 couplet (君不見高堂明鏡悲白髮 / 朝如青絲暮如雪), 女大不中留, 夫復何言, 圓寂, 陽壽已盡, 冰窒, 起死回生, 入土為安. Cross-episode: reused Ep28 天蓋高而無階/懷此恨其誰訴 lament pattern for 黃藥師 grieving 阿衡. |
| 32 | v12 | 396 | Sinking-boat 九陰真經 extortion + 洪七公 crippling by 歐陽峰. First FULL firing for: 願賭服輸, 默寫九陰真經, 七孔流血, 百毒攻心, 氣聚胸口 (郭靖 altered-fake variant), 好生之德, 百步穿腸, 蛇杖, 功力, 鋼刺, 死無葬身之地. Chi-OCR: 老頑童→老誠童/老顏童/老其童/老示童, 歐陽峰→歐陽蜂, 郭靖→郭蜻, 蓉兒→其兒/鞭兒, 豈有此理→量有此理, 鯊魚→准魚/徐魚, 狡猾→狡獨, 無緣無故→無原無故 (all continue Ep30/Ep31 batch; yue witness). |
| 33 | v14 | 376 | Deserted-island 打狗棒 transmission + 歐陽峰 cave bargain + raft escape + 歐陽峰/歐陽克 arrival at 完顏洪烈's palace. First FULL firing for: 打狗棒/打狗棒法/三十六路打狗棒法, 易筋鍛骨篇, 七十二路空明拳, 歐陽先生/歐陽公子/歐陽叔叔/歐陽世兄 cluster, 蓋世奇書, 粉身碎骨, 千金小姐, 如花似玉, 碎屍萬段, 約法三章, 一代宗師, 千秋大業, 斷腳之仇, 恩將仇報, 暗箭傷人, 天作孽猶可恕/自作孽不可活, 天長地久/人生幾何/譬如朝露/去日苦短 (曹操 短歌行, STYLE §10), 遠水救不了近火, 易如反掌, 血肉之軀, 塞外高人, 素仰先生, 沖天炮, 信鴿, 氣凝膻中/玉堂/神與氣合/十氣重脈 (易筋鍛骨篇 meditation formulas). Cross-episode: 泰山北斗 second firing (Ep30+Ep33 → STYLE §10 validated). Chi-OCR: 其兒/鞭兒→蓉兒 (continuing), 歐陽蜂→歐陽峰, 痢下→閣下, 間王爺→閻王爺, 章祖師→望祖師爺, 希彰→希望, 品陽先生→歐陽先生 (novel 品/歐). Promotion flags: `周伯通大哥→Zau Baak-tungBig Brother/Jau Baak-tungBig Brother` trap (大哥 eats it) → `cjk_fix_v2.py` on next firing; `碎屍萬段` collapser miss confirms Ep24 pattern, two-ep → lower threshold or add specific entries. |

### Pending — Needs FULL Processing

Prior-session FULL outputs below predate the current rule-set and are retained as content previews only; they do not count as established precedent.

**Subcount note.** The `Subs` column is an eng-derived approximation; chi-spine count is typically 5–15% smaller. Treat as rough sizing only; pipeline.py Step 1 reports the authoritative count.

| Episode | Subs (approx) | Status / Content Preview |
|---------|---------------|--------------------------|
| 19 | 490 | Prior-session FULL. 楊康 final betrayal + 楊鐵心 suicide (滿江紅) + 包惜弱 death + 全真教 / 丘處機 internal-skills duel + 問世間情為何物. |
| 26 | 471 | Prior-session FULL. 歸雲莊 confrontation + 陸乘風 disciple reveal + 念慈/楊康 prison + 歐陽克/穆姑娘 + 裘千仞 false 黃藥師-death claim + 江南七怪 + 梅超風/陸乘風 grief reckoning (老賊). |
| 27 | — | Likely 陸乘風 manor aftermath + 歐陽克 scheming + 桃花島 connections. |
| 34–54 | — | Prior-session mechanical output only — below current FULL standard. Re-process. |
| 55–59 | — | Not yet processed. |

---

## Watch List — Names/Terms/Oddities

Items pending promotion. One-line format: `**term** (Ep firings) — note`. Promote to consolidated docs after two-episode confirmation without contradiction.

**Note on "promote to STYLE §10" entries below (v17 onward).** Many existing Watch List items say "promote to STYLE §10 on second firing". Under v17's tightened admission gate, most idioms do NOT belong in §10 — only phrases whose English rendering loses imagery, cultural weight, or classical-source reference when read as plain prose. Before promoting any Watch List idiom to §10, apply the plain-prose rule: *strip the CJK and read only the English. If it stands alone without loss, do NOT promote to §10 — render in English in both hybrid and romanised, and remove from the Watch List without a §10 entry.* Promote to §10 only when the Chinese form carries something the English can't (named classical allusion, specific imagery the gloss abstracts away, poetic couplet structure, or §9 anti-flattening risk). Existing "promote §10" notes in the blocks below are from pre-v17 sessions — they describe where the term was last flagged, not where it should land.

### 🟡 Single-episode — hold for one more firing

Candidates awaiting a second firing. On confirmation, promote to the appropriate target (`STYLE.md` §5/§6/§10, `REFERENCE.md`, `extras_baseline.json`, `cjk_fix_v2.py`) and delete here.

**Pilot-arc names (Ep1/Ep2):**
- **金閻旭** (Ep1) — minor Jin soldier; chi wins over yue ASR 金吉玉. Likely one-off.
- **焦木大師** (Ep2) — 法華寺 abbot, killed by 丘處機. One-episode-only plot-important character.
- **韓丞相 vs 韓宰相** (Ep1+Ep2, same office) — watch for third firing to decide consolidation.
- **江南七俠** (Ep2 sub 93) — honoured form; the rest of series uses 七怪.
- **燕京, 法華寺, 金必達** (Ep2) — recur in Jin-court / 楊康-adoption arcs.
- **小康 vs 康仔** (Ep2) — chi written 小康, yue spoken 康仔; 康兒 is baseline vocative.
- **楚河漢界** (Ep2) — dictionary idiom. Promote to STYLE §10 on next firing.
- **一日之恩/永世難忘** (Ep2) — classical kindness-debt compound. Promote to §10 on next firing.

**Ep3 single-firings (蒙古 arc origin + 陳玄風 death):**
- **鐵木真, 成吉思汗, 華箏, 拖雷, 窩闊台, 忽都虎, 王罕, 札木合, 博爾術** — Mongol court figures. 鐵木真/華箏/拖雷 recur heavily across Ep3–Ep5+; promote as second-firings confirm (Ep4 already fires 王罕/札木合 second).
- **塔塔克部族** — Tatar tribe, falls 1201. Named historical reference.
- **銅屍陳玄風 / 鐵屍梅超風** — Bronze/Iron Corpse; 陳玄風 death scene. Nicknames will recur in 梅超風's grief invocations (Ep16, Ep22, Ep23).
- **飛天蝙蝠柯鎮惡 on-screen duel** (Ep2 named the nickname; Ep3 is first duel firing) — 柯鎮惡 blinded by 九陰白骨爪 skull-training (sub 378 self-reference for later-ep blindness recalls).
- **桃花洞** — 陳玄風/梅超風 hideout; structural location for later-ep 梅超風 laments.
- **李萍** as active character (Ep3 蒙古 widow scenes) — first on-screen firing of the 郭靖 mother. Recurs throughout.
- **靖媽, 郭夫人** — address forms for 李萍. Watch for consistency.
- **鐵木真 chronology** — 1196 王罕 alliance, 1201 塔塔 fall, 1202 王罕/札木合 rivals. Canonical reference dates.
- **Idioms** 英雄豪傑, 天公地道 (baseline first FULL), 生死與共, 生死關頭, 高深莫測, 來日方長, 卻之不恭, 為民除害, 好勇鬥狠 — promote per §10 on second firing.
- **`哲別 + 大人/叔叔` concat** (Ep3 subs 109, 127 — `Zit-BitSir/Zit-BitUncle`) — investigation pending; post-build sed'd. Watch for recurrence; promote to `cjk_fix_v2.py` on next firing.
- **嘶子大叔→鬍子大叔, 弛死→殺死, 祭你侈→祭你爹 chi-OCR** — novel single-firings this session; watch.

**Ep4 single-firings (蒙古 childhood arc):**
- **都史, 桑昆大汗, 乃蠻/乃蠻大汗** — Mongol politics figures; recur in Ep5+ Mongol arcs. Promote as they fire a second time. (Ep4 王罕/札木合 are second firings — see Ep3 above.)
- **七拉河, 灰夾山, 王克罕山** — Mongol geography; likely one-arc only.
- **受封大典** — 鐵木真 investiture; structural event, single-firing.
- **六弟/三哥/三太子/六太子/兩位太子** (Ep4 first on-screen two-prince scene) — Jin prince ranking; 完顏洪烈 is 六弟/六太子, unnamed brother 三哥/三太子. Watch for recurrence.
- **洪烈** (bare given-name, three太子 addressing 完顏洪烈) — needed overlay entry. Promote to `extras_baseline.json` on second firing.
- **太子** (bare) — register as `太子 → the Prince` in overlay. Promote on second firing.
- **射人先射馬/擒賊先擒王 couplet** (Ep4 sub 174, 鐵木真 quoting classical 兵書) — STYLE §10 candidate on second firing.
- **賠了夫人又折兵** (三國演義 proverb) — promote to STYLE §10 on second firing.
- **受人恩惠千年記** — classical kindness/debt proverb; promote to §10 on second firing.
- **Paired idioms** 戰無不勝/攻無不克, 有勇無謀/烏合之眾, 忠心耿耿/視死如歸, 差之毫釐/失之千里, 人強馬壯/國運興隆 — promote per §10 on second firing.
- **Routine 四字成語** 別開生面, 惹事生非, 言重, 以下犯上, 多多包涵, 不攻自破, 九死一生, 落花流水, 千方百計, 自取滅亡, 庸人自擾, 恭恭敬敬, 忠心耿耿 — promote per §10 admission-gate on second firing.
- **擒王→擒龍 yue ASR** (Ep4 sub 174) — Rule B case, chi wins. Informational only.
- **鐵木真's 義父 = 王罕** — cross-episode canonical relationship, distinct from 安答 institution. Structural note.

**Ep8 single-firings (蒙古 arc — 馬鈺 reveal + 桑昆 raid + 札木合 death + 成吉思汗 declaration + 金刀駙馬 + 梅超風/華箏 story):**
- **木華黎** (蒙古 general killed by 都史), **博爾忽, 博爾朮** (蒙古 generals — chi 博爾尤 is OCR of 博爾朮; note SESSION-NOTES Ep3 lists 博爾術 — same person, 朮/術 simplified-vs-traditional variant) — promote to `PersonalNamesUpdated.csv` on second firing.
- **素女劍** (梅超風's master's unfinished plan for her) — named technique. Flag if it recurs in 桃花島 flashbacks (Ep31 had 重陽真人/玉女劍法 context; 素女劍 may reappear).
- **天罡北斗七星陣 / 北斗七星陣 / 北斗七星** (全真七子 formation) + **斗轉星移** (its second form) — named techniques. 全真七子 formation appears centrally in later 歸雲莊 and 重陽宮 arcs — will recur.
- **郭大媽** (李萍 address form) — parallel to SESSION-NOTES Ep5 flag `Gwok大Mother→Mrs Gwok`; this session renders via overlay as "Mrs Gwok" directly. Promote to `extras_baseline.json` on second firing.
- **楊家叔叔** (郭靖 kinship reference to 楊鐵心's branch of the family). Flag if it recurs.
- **志平** (bare form of 尹志平 when addressed by 馬鈺) — parallel to bare 玄風 / bare 康 patterns in REFERENCE §1/§7.
- **全真派** (variant of 全真教 — both appear in Ep8). Flag if 全真派 becomes the preferred form.
- **Classical/idiom plain-prose-path confirmations** (Ep8 second/third firings of items that pass §7 plain-prose rule and stay English only): 三生有幸 (Ep7+Ep8), 指腹為婚 (Ep6+Ep8), 虛有其表 (Ep5+Ep8), 兵不厭詐 (Ep8), 君子報仇十年不晚 (Ep8), 殺個片甲不留 (Ep8), 深仇大恨 (Ep8), 邪魔外道 (Ep8), 貪生怕死 (Ep8). Record for reference; none earn §10 catalogue entry.

**Ep9 single-firings (蒙古 departure + 江南七怪 fake-kidnap + 蓉兒 first appearance):**
- **西毒, 華山論劍, 赤頂青蛇, 大力金剛指, 妙手雙飛, 少林寺, 嘉興, 醉仙樓** — Ep9-naming; 醉仙樓 recurs as the Ep1/Ep2 venue, Ep9 is first 七怪-rendezvous naming. Promote as they recur (西毒/華山論劍 especially central for Ep15+ arcs).
- **釀鴨舌, 珍珠魚目羹, 豆腐絲擺麵, 豆腐絲, 女兒紅** — 蓉兒's dish-ordering scene. Precursor to REFERENCE §4 Ep21 dish table; keep-CJK per that precedent. Promote overlay entries to `extras_baseline.json` on Ep21 second firing.
- **小叫化子 rendering policy** — 蓉兒's chosen nickname in the 醉仙樓 disguise scene. Per STYLE §18 ban on 叫化子 CJK, rendered as English "little beggar" across all three variants (not Cantonese 乞兒仔 which would render "beggar boy (yue)" per STYLE §7). Flag if future episode uses 乞兒仔 directly — that would be CJK-kept per STYLE §7 Cantonese form.
- **Classical/idiom plain-prose-path confirmations** (Ep9 plain-prose renderings): 後會有期 (second firing after Ep24; §10-purged under v17, plain-prose-English confirmed); 一聲不徹/一聲不出 (sub 165 — chi OCR 徹/出 two-ep flag).

**Ep10 single-firings (蓉兒/郭靖 girl-reveal arc):**
- **飛箱樓** — small-town inn 郭靖/蓉兒 lodge at; 歐陽克 sends 白衣護法 to scout it. Promote to `extras_baseline.json` on second firing.
- **木蓮子** — invented herb 蓉兒 uses to deceive 梁子翁 (who buys 10 taels of it as snake-feed). Kept CJK in hybrid per STYLE §8 雪蓮 precedent for invented-herb names; rendered "mulian seeds" in romanised. Lint flagged (judgment-call (c)) — single firing, watch.
- **大漠** — 郭靖's poetic Mongolia form (distinct from canonical 蒙古). Rendered "the Great Desert" in romanised. Will recur in 蒙古-return arcs Ep15+. Promote on second firing.
- **阿蓉** — 郭靖's intimate address for 黃蓉 in the cave girl-reveal arc + post-confession scenes (subs 182, 222–276 cluster, 358, 365, 387). Distinct from 蓉兒 (vocative). Promote to STYLE §5 + `extras_baseline.json` on second firing.
- **護法 / 白衣護法** — 靈智上人's bodyguard rank, 歐陽克's 白衣護法 scout. Promote to STYLE §6 on second firing.
- **沙兄** — peer-address among 王爺's invited masters (歐陽克 to 沙通天). Single-firing — watch.
- **大滿→大漠** chi-OCR (sub 408) — single firing; watch for recurrence.
- **廉詞→念慈** yue-ASR (subs 119, 120) — Rule B chi wins; informational only.
- **歐陽峰 vs 歐陽鋒** (chi has 歐陽峰 throughout this episode; yue HIGH consistently has 歐陽鋒 — Whisper homophone fung1). Rule B chi wins (canonical 歐陽峰).
- **大開殺戒/打是疼罵是愛/花開的招蜜蜂** — colloquial proverbs, plain-prose renderings (sub 86, 75); §10-purged confirmed.

**Ep13 single-firings (王處一 poisoning aftermath):**
- **靈蛇山莊** — 梁子翁's manor opposite the 王府. Promote to `extras_baseline.json` on second firing.
- **落日亭** — pavilion where 蓉兒 tricks 郭靖 to meet. Single-ep — watch.
- **試劍亭** — 桃花島 pavilion 黃藥師 cites by couplet. Single-ep — watch (recurs in 桃花島 arcs Ep30+).
- **蒼松道觀** — Taoist temple 郭靖/穆姑娘 take 王處一 to recover. Single-ep — watch.
- **惠清師太** — Taoist Nun running 蒼松道觀; missing/dead at ep-end. Single-ep — watch.
- **牛道士** (蓉兒's mock-form for 王處一, parallel to her general nickname-mocking habit) — single-ep — watch.
- **梁老怪** (蓉兒's nickname for 梁子翁) — single-ep — watch.
- **梅若華** — 黃藥師's name for 梅超風 before her marriage to 陳玄風 (the original 桃花島 disciple form). Single-ep — watch (will recur in 桃花島 flashbacks Ep30+).
- **毒沙掌** — 沙通天's named technique 王處一 was poisoned with. Single-ep — watch (recurs whenever 沙通天's poison-history is invoked).
- **毒蛇霧** — 梁子翁's snake-pit gas. Single-ep — watch.
- **五心向天** — meditation posture 梅超風 demands of 蓉兒/郭靖 (subs 291–293). Single-ep — watch (recurs in 九陰真經 arcs Ep29+).
- **鐵心** (bare) — STYLE §19 entry with no rendering yet beyond the surname concat. Sub 131 (包惜弱 vocative). Overlay rendered as Tit-sam (jy/yl). Promote to `extras_baseline.json` on second firing.
- **內功心法** — full compound for 全真教's internal-energy formulas 梅超風 demands (sub 268). Plain-prose rendering ("internal-energy formulas") — 內功 itself is §7-banned-CJK in hybrid. Watch.
- **大難難逃** chi-OCR (sub 136 — chi 難難 dittography for 大難不逃 / "this disaster won't be escaped"). Single firing — watch.
- **粗心 vs 畜生** (sub 12 yue 粗心 ASR for chi 會牡/畜生; chi has the OCR-damaged 會牡 — `會牲` in raw) — Rule B chi-sense wins, rendered "brute". 完顏康 referent. Watch.


- **岳王廟, 岳文, 岳老伯, 岳大叔, 碧玉富貴燈, 翠紅樓, 獅子林, 山神廟, 簡長老, 麻瘋病** — all single-ep places/characters. Promote as they recur.
- **Idioms** 精忠報國, 醉生夢死, 風流快活, 亡國奴, 半壁江山, 用兵如神, 居功至偉, 皇天不負有心人, 各安天命, 鬼哭狼嚎 — single-ep; promote per §10 gate on next firing.

**Ep21 single-firings:**
- **梁子翁, 彭長老, 鄂州, 鄭州, 天香樓, 樞密院, 藏經閣, 禁軍** — places/characters; promote as they recur.
- **七仔** — 洪七公 self-naming per STYLE §5 (NOT a general substitute).
- **成事不足敗事有餘, 群龍無首, 後患無窮, 尊師重道** — idioms single-ep.

**Ep22 single-firings:**
- **沙通天, 彭連虎** — minor antagonists, recur.
- **降龍有悔, 躍龍在淵** — Dragon-palm names (Ep22 subs 301, 324).

**Ep23 single-firings:**
- **雪蓮玉露丸, 黃小邪, 邪中有三分正 couplet, 法師** — as above.

**Ep24 single-firings:**
- **燕尾甲→軟蝟甲 yue-ASR**, **華珍→華箏 yue-ASR** — promote to `OCR_NAME_COLLAPSE` on next firing.

**Ep25 single-firings:**
- **羞花亭, 千年蔘王, 程耀宗, 方掌櫃, 程陸 family-address vocatives** — promote as they recur.
- **大衍數 step names** (零/地三/頤王/起/伏/定/已/和) — 頤王 needed sed; recurs at Ep26 歸雲莊.
- **遵命 → "Yes, sir"** (Ep25) — `extras_baseline.json` if it fires again.

**Ep31 single-firings (many; most Ep31-specific flashbacks):** 一陽指, 華山論劍, 激將法, 過目不忘, 玉石俱焚, 雞鳴狗盜, 水能載舟亦能覆舟, 李白 將進酒 couplet, 女大不中留, 夫復何言, 圓寂, 陽壽已盡, 冰窒, 起死回生, 入土為安. Promote per §10 gate on next firing.

**Ep32 single-firings:** 百步穿腸, 蛇杖, 鋼刺, 一代宗師, 狼心狗肺, 七孔流血, 易如反掌, 死無葬身之地, 好生之德, 不識抬舉, 恩將仇報, 死有餘辜, 自作孽不可活, 言出必行, 願賭服輸, 百毒攻心. Promote per §10 gate on next firing. **六個時辰 hybrid-gloss convention** (Ep32 sub 231: `six shichen (twelve hours)`) — decide policy after next firing.

**Ep33 single-firings (32 idioms, deserted-island episode):** 蓋世奇書, 千秋大業, 斷腳之仇, 塞外高人, 遠水救不了近火, 天作孽猶可恕/自作孽不可活, 素仰先生, 沖天炮, 粉身碎骨, 如花似玉, 碎屍萬段, 約法三章, 恩將仇報, 暗箭傷人, 血肉之軀, 綽綽有餘, 有志者事竟成, 死有餘辜, 斯文有禮. Promote per §10 on second firing.

**Ep14 single-firings (王府 paternity-reveal arc):**
- **福來客棧** — inn where 楊鐵心-as-木易 is staying when 完顏洪烈 sends assassins. Promote to `extras_baseline.json` on second firing.
- **太醫** — Imperial Physician (5+ firings in Ep14, 王府 illness scene). Promote to baseline next bump (likely recurs in any 王府/court arc).
- **別院 / 別苑** — country villa where 完顏洪烈 sends 楊康 to recover; both spellings appear. Plain-prose rendering ("country villa"); watch.
- **和字號房** — "the He-character room" (room name at 福來客棧). Single-firing — watch.
- **Sixth Brother address by elder brother** — the Emperor (三哥/三太子, who is 完顏洪烈's elder brother and the reigning Jin Emperor in this episode) calling 完顏洪烈 "六弟" appears repeatedly Ep14 (subs 352, 362, 388). Already in baseline; this is a confirmation of its high-frequency use in 大金國 court scenes.
- **餓死事小, 失節事大** — classical compound (女德觀 widow's-honour proverb), §10 catalogue candidate (criterion 1: fixed compound; criterion 3: 俗語 with cultural weight English flattens). Single-firing in Ep14 (sub 162). Promote to STYLE §10 on second firing.
- **求生不得, 求死不能** — paired-half compound describing the chopping-block fate of a commoner. §10 candidate (criterion 1: fixed 四字 paired; the parallelism is the point). Single-firing. Promote on second firing.
- **人不風流枉少年** — 完顏洪烈's defence of 楊康's marriage-to-singing-girl rebellion (sub 378). Named 俗語. Single-firing — promote to §10 on second firing.
- **精誠所至, 金石為開** — 包惜弱's classical couplet about her devotion (sub 155). 古諺. §10 candidate. Single-firing.
- **始亂終棄** — 完顏洪烈's accusation against 楊鐵心 (sub 287). Common 四字. Plain-prose rendering ("deceived and abandoned") — fails admission gate; watch only.
- **恩重如山, 情至義盡** — paired compound 包惜弱 uses for 完顏洪烈's 18-year care (sub 36). Plain-prose rendering — fails §10 gate; watch only.
- **家散人亡** Ep3+Ep14 two-ep — already in §10's "天有不測風雲" couplet entry under Ep1; appears here standalone. Plain-prose rendering ("homes broken, lives lost") — Ep3 was the first FULL firing. Watch.
- **三長兩短, 吉人天相, 大恩大德, 垂手可得, 卑躬屈膝, 大膽畜生, 以下犯上, 尊卑不分, 放蕩不羈, 不成體統, 要風得風要雨得雨** — 11 routine 四字成語; promote per §10 admission-gate on second firing.
- **張老爹/張老爺** — 牛家村 blacksmith in 楊鐵心's reminiscence flashback (subs 184, 186). Single-arc; concat-trap with 老爹/爺 needed overlay registration. Promote on second firing if 牛家村 flashbacks recur.
- **大金國 cross-stage trap** Ep11+Ep14 two-ep — `cjk_fix_v2.py` `shared_concat_fixes` already has `大Jin → the great Jin empire`; confirmed firing cleanly across both episodes. Promote out of Watch List.

**Ep16 single-firings (梅超風 ambush + 王府 infiltration + 武穆遺書 reveal + 楊鐵心 rescue-plan):**
- **忍辱負重** (sub 177 — 楊康's rationalising line to 念慈) — STYLE §10 crit 1 fixed 四字成語 with classical 三國志 provenance; gloss "swallow shame and bear the burden" preserves the 忍辱 + 負重 paired imagery. First FULL firing; CJK+gloss in hybrid. Promote to STYLE §10 catalogue on second firing.
- **功虧一簣** Ep12+Ep16 two-ep — STYLE §10 crit 1 confirmed (尚書·旅獒); gloss "one basket shy of the mountain" preserves the 簣/basket image. Promote to STYLE §10 formal catalogue entry on third firing.
- **得來全不費功夫** (sub 275 — 梅超風 gloating line) Ep12+Ep16 two-ep — second half of the 踏破鐵鞋無覓處 couplet used in isolation. Classical 俗語 (張燈·夏元鼎). Promote to STYLE §10 on third firing.
- **Idioms failing plain-prose test (render English-only; do NOT promote §10):** 形勢所逼, 紅顏知己, 用兵如神, 貪圖富貴, 榮華富貴, 頹垣敗瓦, 吉人天相 (Ep14+Ep16 two-ep confirmed — explicitly English-only going forward), 見死不救, 滅絕人性, 顧全大局, 戰無不勝, 始亂終棄-shape compounds. Reference for future-session §7 consistency.
- **鐵心 bare** (Ep13+Ep14+Ep15+Ep16 four-ep) — 包惜弱 vocative for 楊鐵心; rendered "Tit-sam" via overlay. **Promote to extras_baseline.json next bump.**
- **中原** ("the Central Plains") — Ep15+Ep16 two-ep stable. **Promote to extras_baseline.json next bump.**
- **楊夫人** compound — Ep11+Ep14+Ep16 three-ep stable. **Promote to extras_baseline.json next bump.**
- **夫人 (bare)** — 王府 servant-address vocative to 包惜弱 (subs 107–111); single-ep so far, rendered "my Lady". Watch for Ep17+ 王府 arcs. **Guard rail:** don't generalise this to other 夫人 contexts — the 王府 servant-caste register is specific.
- **梅師姊 / 梅師姐** variant pair — chi renders both 姊 and 姐; both should map to "Senior Sister Mui/Muhk". STYLE §5 already has 梅師姊; add note about 姐 variant on next firing.
- **大師父 concat-trap** Ep5+Ep6+Ep15+Ep16 four-ep — STYLE §19 already lists; stable resolution via overlay registration (First Master). **Drop from Watch List — resolution is documented-stable.**
- **老賊 four-ep precedent** Ep3+Ep22+Ep23+Ep16 — REFERENCE §1 entry confirmed stable (intimate pet-name for 陳玄風, used by 梅超風 in grief-or-vengeance contexts). No promotion action.
- **白骨爪 bare** (subs 304, 309 — 蓉兒 and 梅超風 both use it standalone) — short form of 九陰白骨爪; overlay rendered "the Baigu Claw". Ep1+Ep3+Ep16 three-ep; **promote to extras_baseline.json next bump.**
- **二女** (sub 102; 念慈 naming herself 楊鐵心's "second daughter") — family-position self-identification used to establish 念慈/包惜弱 familial relation. Single-ep — watch for Ep17+ 念慈/楊鐵心 arcs.
- **Chi-OCR recurrent**: 其兒/鞭兒→蓉兒 continuing 8-ep batch (promote to `OCR_NAME_COLLAPSE` reconfirmed); 郭蜻→郭靖 continuing 8-ep batch; 梅朝風→梅超風 Ep5+6+7+16 four-ep firing cleanly via overlay — **promote to OCR_NAME_COLLAPSE next bump**; 侈→爹 Ep23+Ep16 two-ep — **promote to OCR_NAME_COLLAPSE next bump**; 軟衛甲/燕尾甲→軟蝟甲 continuing Ep24 flag; 金吉人天相→吉人天相 (sub 122, chi 金吉 dittography — single-ep) watch.
- **Yue ASR Rule B subs**: 我要非→岳飛 (sub 165 — 我/岳 homophone cluster); 母母遺書→武穆遺書 (yue ASR 穆/母 homophone). Chi wins per Rule B; no action.
- **楊康's 武穆遺書 rationalising monologue** (subs 162–177) — classical-register political-deception monologue; 忍辱負重 anchors the register. Pattern precedent for future 楊康 deception arcs (Ep17–Ep19).
- **蓉兒 dagger-stabbing banter** (subs 267–270) — bratty-on-surface register per STYLE §12; "Don't go thinking there's nothing I daren't do" preserves the threat-as-flirt tone.
- **楊鐵心 drunken-despair register** (subs 326–349) — 爹 self-pity then pivot to 惜弱-innocence-confirmed beat. Register: plain despair, no padding, per STYLE §12.



- **`Lin'an府` cross-stage trap** (Ep13 single firing) — `臨安` is in `build.py` terms (stage 2), `臨安府` only in episode overlay (stage 5). Stage 2 fires first, strands 府. Worked around with post-build sed `Lin'an府 → Lin'an Prefecture`. Promote to `cjk_fix_v2.py` `shared_concat_fixes` on second firing. (Or move 臨安府 to `build.py` terms dict directly.)
- **六弟/二哥/七妹/三哥 sibling-ordinal vocatives** (Ep2+Ep9 two-ep) — promoted to `extras_baseline.json` (二哥/三哥/四弟/五弟/六弟/七妹). Drop on next-episode confirmation that the baseline path resolves them cleanly.
- **`19th-generation 幫主` adjectival** (Ep33) — produces "19th-generation the Chief"; worked around with "leader". Observation only.
- **`泰山北斗 + 武林` duplicate** (Ep33) — "of the martial world of the martial world". Structural fix: revise 泰山北斗 rendering, or enshrine "don't pair" rule in STYLE §8. (STYLE §10 already has a "don't pair" note under 泰山北斗 — enforcement lives in the reviewer's head; no code fix yet.)
- **我柯鎮惡 / 我裘千仞** (Ep26) emphatic-self compounds. Fix when they fire again.
- **我們 + non-`the` compound** (Ep28) — only `我們the` handled; 我們蒙古 etc unhandled.
- **Compact-idiom + em-dash concats** (Ep31, Ep32) — bare short idioms leak as CJK; policy TBD.

### 🟡 Rule B territory (chi wins — informational only)

- **歐陽克 Whisper cluster**: 克/赫/黑/客 all `haak1` (→ REFERENCE §1).
- **Long-tail chi-OCR beyond v13 collapse table**: 若師兄/王老邪/蔡洪峰 (Ep30); 周伯仲/白通/伯東 (Ep31/32); 梅竹風 (Ep31); 陳元鳳 (Ep31); 旺銅銀 (Ep31); 准魚/徐魚/狡獨/無原無故 (Ep32). Catalogued in REFERENCE §1; promote variant-by-variant as each fires a second time.

---

## 🟡 Pending audit — `build.py` / `extras_baseline.json` / `cjk_fix_v2.py` overlap

Several tables across these three files carry overlapping entries for the same CJK keys. Under the run-from-scratch pipeline, the ordering is terms-dict (stage 2) → titles (stage 3) → names (stage 4) → extras (stage 5) → post-build cjk_fix_v2. Earlier-stage entries silently override later-stage entries with the same key. Two risks: (a) dead code in later stages wastes audit attention, (b) silent divergence between duplicate renderings.

Known overlap clusters to audit in a future session:
- **`build.py` `terms` dict vs `extras_baseline.json`** — entries like 桃花島, 全真教, 九陰真經, 江湖, 降龍十八掌, 武林, 蒙古, 臨安, 大理 appear in both. Terms wins (stage 2 before stage 5). If renderings differ, baseline entry is dead code; worse, reviewer may read baseline and not realise terms overrides it.
- **`build.py` `titles_jy` / `titles_yl` vs `extras_baseline.json`** — same concern for title/address entries (駙馬爺, 王爺, 大哥, 師父, 黃島主, 閻王爺, etc.).
- **`cjk_fix_v2.py` `fixes` dict vs `extras_baseline.json`** — the `fixes` dict runs post-build so it's a true belt-and-suspenders catch; safe as-is but many entries may now be redundant if extras-stage firing is robust.

Recommended approach: audit by diffing keys across the three files, flag any entry whose rendering differs between sources, then delete redundant entries from the later-running source (baseline for terms/titles; fixes dict for post-build). Don't touch without the diff — some "redundant" entries may be the only correct one if another source has a stale rendering. Risk level: medium. Budget estimate: one full session just for the audit; save the actual edits for a follow-up. Not blocking anything; flagged so future sessions don't re-create the problem.

---

## How to Use This Log

At session close:

1. **Update the episode row.** Move FULL rows into the Completed table (sorted ascending by episode number). Leave PARTIAL/MECHANICAL rows in Pending with an outcome note.
2. **Add new Watch List items.** Skip anything already in `STYLE.md` §5/§6/§10 or `REFERENCE.md`.
3. **Promote when stable.** Two-episode confirmation without contradiction → move to the consolidated doc and delete from here.
4. **Hold the row budget.** Target ≤500 chars per Completed-table row body; hard cap 1000. If a row exceeds the cap, cut per-sub citations, who-said-what parentheticals, and validation summaries first.

This file is not a general changelog. Pipeline version bumps for script architecture belong in `PIPELINE.md`. The Recent Promotions section records Watch List graduations so future sessions don't re-register them; anything older than two bumps back should be compacted to a one-line pointer.
