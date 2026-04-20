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
| 20 | v13 | 587 | 臨安 / 元宵 arc with 岳文 and 武穆遺書 plot. First FULL firing for: 岳王廟, 岳王爺, 岳文, 岳老伯, 岳大叔, 武穆遺書, 碧玉富貴燈, 元宵佳節, 如意燈/吉祥燈/添丁燈, 翠紅樓, 獅子林, 山神廟, 林升 題臨安邸 quatrain, 精忠報國, 醉生夢死, 風流快活, 亡國奴, 半壁江山, 用兵如神, 行軍佈陣, 安邦定國, 雄霸天下, 居功至偉, 皇天不負有心人, 各安天命, 鬼哭狼嚎, 簡長老, 麻瘋病. Cross-episode: first on-screen 降龍十八掌 (vs 沙通天); first scene naming 東邪/西毒/南帝/北丐 together. Chi-OCR: 匡文/策老伯/品王爺→岳文/岳老伯/岳王爺; 土/犁/悍/幫紅樓→翠紅樓; 葵古/划古→蒙古; 梁子峰/梁子忠→梁子翁. Promotion flags: 岳王爺→岳Your Highness and 本姑娘→本姑Mother cross-stage traps → `cjk_fix_v2.py` `shared_concat_fixes` on next firing. |
| 21 | v12 | 501 | 洪七公 apprentice-acquisition (丐幫 business + 拖雷 宋-Mongol alliance mission). First FULL firing for: 梁子翁, 彭長老, 鄂州, 鄭州, 天香樓, 樞密院, 藏經閣, 禁軍, 百花雞/釀鴨舌/清蒸活鯉魚/珍珠魚眼羹/龍虎鳳會石斑, 百花蛇/果子狸/竹絲雞 (龍虎鳳), 七仔 (洪七公 self-naming, STYLE §5 NOT a general substitute), 成事不足敗事有餘, 不見棺材不流淚, 群龍無首, 後患無窮, 心腹大患, 尊師重道. Cross-episode: first on-screen 降龍十八掌 now attributed to Ep20, not Ep21. Chi-OCR: 其兒/鞭兒→蓉兒, 郭蜻→郭靖, 梁智翁/梁子仍→梁子翁, 語州/開州→鄂州, 權密院→樞密院, 藏真閣→藏經閣. |
| 22 | v12 | 463 | 洪七公 poisoning at 望江樓 + 降龍十八掌 death-bed transmission to 郭靖. First FULL firing for: 望江樓, 清溪別院, 博將軍/赤將軍, 沙通天, 彭連虎, 靈智上人, 降龍有悔/躍龍在淵, 一流絕頂高手, 時辰, 兵家大忌, 夜長夢多, 打草驚蛇, 狗咬呂洞賓, 好心遭雷劈, Dragon-chant quartet (去似天龍雲飛躍 / 收似降龍穩深沈 / 腳似飛龍騰萬里 / 拳似怒龍翻四海 — STYLE §10 format), 人之將死/其言也善. Cross-episode: 老賊 (梅超風's term for 陳玄風) second firing with Ep23 (→ REFERENCE §1). |
| 23 | v14 | 429 | 華箏 poisoning-cure + 梅超風 老賊 lament + 黃藥師 first appearance (邪中有三分正 couplet) + 華箏 法師 hairpin-suicide. First FULL firing for: 雪蓮玉露丸/雪蓮, 黃小邪 (蓉兒 self-name), 死老邪 (七公 insult to 黃藥師), 邪中有三分正/正中帶七分邪 couplet (STYLE §10), 女魔頭, 寶刀未老/彼此彼此/爐火純青/中看不中用/甘敗下風 (Five-Greats banter), 艷福, 抱頭痛哭, 罪大惡極, 一人做事一人當, 假仁假義, 清理門戶, 沒齒難忘, 延年益壽, 法師, 當今兩大高手, 黃世伯/世伯. Cross-episode: 老賊 second firing (Ep22+Ep23 → REFERENCE §1 confirmed). Chi-OCR: 其兒/鞭兒→蓉兒 (continuing pattern), 郭蜻→郭靖, 央馬爺→駙馬爺, 陳元鋒/袁風/元鋒→陳玄風/玄風, 駁→爹. Promotion flags: `黃前輩→Wongsenior` cross-stage trap (前輩→senior eats it); `死老邪→死Old Heretic` trap (worked around in English; STYLE §5 has 死老邪→damned Old Heretic). Both → `cjk_fix_v2.py` `shared_concat_fixes` on next firing. |
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
| 7–14 | — | Not yet processed. |
| 15 | 464 | Prior-session FULL. 楊康 identity crisis + 包惜弱 letter + 穆念慈 + 黃蓉 vs 七怪 + 歐陽克. |
| 16 | 452 | Prior-session FULL. 梅超風 ambush + 黃蓉/郭靖 reconciliation + 穆念慈/包惜弱 revelation + 楊康 武穆遺書 + rescue plan. |
| 17 | 409 | Prior-session FULL. 楊康/包惜弱 escape + boat betrayal + 段天德 confession + 穆念慈 fireball. |
| 18 | 515 | Prior-session FULL. 包惜弱 poison wine / suicide / nun + 丘處機 captures 楊康 + 九陰白骨爪 trail + family reunion. |
| 19 | 490 | Prior-session FULL. 楊康 final betrayal + 楊鐵心 suicide (滿江紅) + 包惜弱 death + 全真教 / 丘處機 internal-skills duel + 問世間情為何物. |
| 26 | 471 | Prior-session FULL. 歸雲莊 confrontation + 陸乘風 disciple reveal + 念慈/楊康 prison + 歐陽克/穆姑娘 + 裘千仞 false 黃藥師-death claim + 江南七怪 + 梅超風/陸乘風 grief reckoning (老賊). |
| 27 | — | Likely 陸乘風 manor aftermath + 歐陽克 scheming + 桃花島 connections. |
| 34–54 | — | Prior-session mechanical output only — below current FULL standard. Re-process. |
| 55–59 | — | Not yet processed. |

---

## Watch List — Names/Terms/Oddities

Items pending promotion. One-line format: `**term** (Ep firings) — note`. Promote to consolidated docs after two-episode confirmation without contradiction.

### 🟡 Single-episode — hold for one more firing

Candidates awaiting a second firing. On confirmation, promote to the appropriate target (`STYLE.md` §5/§6/§10, `REFERENCE.md`, `extras_baseline.json`, `cjk_fix_v2.py`) and delete here.

**Pilot-arc names (Ep1):**
- **顏烈** (Ep1+Ep2 confirmed — Ngaan Lit / Ngaahn Liht) — 完顏洪烈's first cover alias. **Two-ep confirmed — promote to `STYLE.md` §5 + CSV on next session.**
- **金閻旭** (Ep1) — minor Jin soldier; chi wins over yue ASR 金吉玉. Likely one-off.
- **焦木大師** (Ep2) — 法華寺 abbot, killed by 丘處機. One-episode-only plot-important character.
- **韓丞相 vs 韓宰相** (Ep1+Ep2, same office) — watch for third firing to decide consolidation.
- **江南七俠** (Ep2 sub 93) — honoured form; the rest of series uses 七怪.
- **燕京, 法華寺, 金必達** (Ep2) — recur in Jin-court / 楊康-adoption arcs. (哲別 promoted in Ep3.)
- **七怪 sibling-order vocatives** (大哥/二哥/三弟/四弟/五弟/六弟/七妹 — Ep2 subs 26–52) — two-ep confirmation candidate; promote to `extras_baseline.json` after next firing.
- **小康 vs 康仔** (Ep2) — chi written 小康, yue spoken 康仔; 康兒 is baseline vocative.
- **小靖** (Ep2+Ep3 two-ep confirmed — young-child diminutive distinct from vocative 阿靖) — **promote to `STYLE.md` §5 next bundle bump.**
- **楚河漢界** (Ep2) — dictionary idiom. Promote to STYLE §10 on next firing.
- **一日之恩/永世難忘** (Ep2) — classical kindness-debt compound. Promote to §10 on next firing.

**滿江紅 classical verse (Ep1 first firing):** subs 48–53, 74–75, 227–230 — 岳飛's poem. STYLE §10 Classical-laments format. Promote on 武穆遺書-arc recurrence (Ep15+).

**Ep3 single-firings (蒙古 arc origin + 陳玄風 death):**
- **鐵木真, 成吉思汗, 華箏, 拖雷, 窩闊台, 忽都虎, 王罕, 札木合, 博爾術** — Mongol court figures. 鐵木真/華箏/拖雷 recur heavily across Ep3–Ep5+; promote as second-firings confirm (Ep4 already fires 王罕/札木合 second).
- **塔塔克部族** — Tatar tribe, falls 1201. Named historical reference.
- **安答** (Ep3+Ep4 two-ep — cultural-concept loanword, `anda` lowercase romanised; 有福同享/有難同當 oath pair) — **promote to `extras_baseline.json` this session.**
- **銅屍陳玄風 / 鐵屍梅超風** — Bronze/Iron Corpse; 陳玄風 death scene. Nicknames will recur in 梅超風's grief invocations (Ep16, Ep22, Ep23).
- **飛天蝙蝠柯鎮惡 on-screen duel** (Ep2 named the nickname; Ep3 is first duel firing) — 柯鎮惡 blinded by 九陰白骨爪 skull-training (sub 378 self-reference for later-ep blindness recalls).
- **老賊 origin** (Ep3 subs 408, 418 — 桃花洞 vow 生則同窮/死則同穴) — **update REFERENCE §1** to cite Ep3 as origin; Ep22/Ep23 are later grief invocations, not first-firings.
- **桃花洞** — 陳玄風/梅超風 hideout; structural location for later-ep 梅超風 laments.
- **李萍** as active character (Ep3 蒙古 widow scenes) — first on-screen firing of the 郭靖 mother. Recurs throughout.
- **靖媽, 郭夫人** — address forms for 李萍. Watch for consistency.
- **成吉思汗's self-epithet 大漠的蒼狼** (Ep3 subs 75/76/77) — **novel chi-vs-yue divergence**: yue has 蒼狼 (wolf, canonical); chi has 蒼龍 (dragon, OCR drift). Rule A case study. Promote chi→yue override to `cjk_fix_v2.py` if pattern recurs.
- **鐵木真 chronology** — 1196 王罕 alliance, 1201 塔塔 fall, 1202 王罕/札木合 rivals. Canonical reference dates.
- **Idioms** 英雄豪傑, 天公地道 (baseline first FULL), 生死與共, 生死關頭, 高深莫測, 來日方長, 卻之不恭, 為民除害, 好勇鬥狠 — promote per §10 on second firing.
- **`<nickname>+<CSV-name>` concat trap family** (銅屍+陳玄風, 鐵屍+梅超風, 飛天蝙蝠+柯鎮惡 — six manual post-build fixes this session) — names stage 4 fires CSV name before extras stage 5, stranding the nickname. **Promote to `cjk_fix_v2.py` `shared_concat_fixes` this session** — same structural family as v13's `the Chief萬福` and v15's `張老Father`. Likely recurs wherever 江南七怪 nicknames + names co-occur.
- **`哲別 + 大人/叔叔` concat** (Ep3 subs 109, 127 — `Zit-BitSir/Zit-BitUncle`) — investigation pending; post-build sed'd. Watch for recurrence; promote to `cjk_fix_v2.py` on next firing.
- **窩辣台→窩闊台, 骨都虎→忽都虎 chi-OCR** — single-firings; promote to `OCR_NAME_COLLAPSE` on next firing.
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
- **`our the great Jin empire` article-collapse trap** (Ep4, multiple subs) — `build.py`'s regex covers `the/my/your/a + the` but not `our + the`. **Act this session**: extend `build.py` regex to include `our`, and add `cjk_fix_v2.py` `shared_concat_fixes` entry as a belt-and-suspenders.
- **啟桌→啟稟 OCR** — **3-ep confirmed (Ep1+Ep2+Ep4) — promote to `cjk_fix_v2.py` `OCR_NAME_COLLAPSE` this session.**
- **擒王→擒龍 yue ASR** (Ep4 sub 174) — Rule B case, chi wins. Informational only.
- **鐵木真's 義父 = 王罕** — cross-episode canonical relationship, distinct from 安答 institution. Structural note.

**Ep20 single-firings (old FULL row; most unresolved):**
- **岳王廟, 岳文, 岳老伯, 岳大叔, 碧玉富貴燈, 翠紅樓, 獅子林, 山神廟, 簡長老, 麻瘋病** — all single-ep places/characters. Promote as they recur.
- **林升 題臨安邸 quatrain** (Ep20 full + Ep1 compressed) — **two-ep confirmed, promote to STYLE §10.**
- **岳王爺 cross-stage trap** — `岳Your Highness → Lord Ngok/Ngohk`. Promote to `cjk_fix_v2.py` on next firing.
- **本姑娘 cross-stage trap** (Ep20+Ep25+implicit more) — `本姑Mother → this girl`. **Three firings — promote to `cjk_fix_v2.py` this session.**
- **武穆遺書** (Ep20 + Ep21 reference) — **two-ep confirmed, promote to `extras_baseline.json`.**
- **Idioms** 精忠報國, 醉生夢死, 風流快活, 亡國奴, 半壁江山, 用兵如神, 居功至偉, 皇天不負有心人, 各安天命, 鬼哭狼嚎 — single-ep; promote per §10 gate on next firing.

**Ep21 single-firings:**
- **梁子翁, 彭長老, 鄂州, 鄭州, 天香樓, 樞密院, 藏經閣, 禁軍** — places/characters; promote as they recur.
- **七仔** — 洪七公 self-naming per STYLE §5 (NOT a general substitute).
- **成事不足敗事有餘, 群龍無首, 後患無窮, 尊師重道** — idioms single-ep.

**Ep22 single-firings:**
- **沙通天, 彭連虎** — minor antagonists, recur.
- **降龍有悔, 躍龍在淵** — Dragon-palm names (Ep22 subs 301, 324).

**Ep23 single-firings:**
- **雪蓮玉露丸, 黃小邪, 死老邪, 邪中有三分正 couplet, 女魔頭, 法師** — as above.
- **Concat traps `黃前輩→Wongsenior`** and **`死老邪→死Old Heretic`** — both need `cjk_fix_v2.py` `shared_concat_fixes` on next firing.

**Ep24 single-firings:**
- **網康→阿康 OCR**, **燕尾甲→軟蝟甲 yue-ASR**, **華珍→華箏 yue-ASR** — promote to `OCR_NAME_COLLAPSE` on next firing.
- **Duplicate-gloss collapser misses** (後會有期, 忘恩負義, 視日無多) — post-cleaned manually; **Ep33 confirms with 碎屍萬段 — two-ep pattern, action this session**: lower Jaccard threshold to ~55%, or add stopword-ignoring subset check.

**Ep25 single-firings:**
- **羞花亭, 千年蔘王, 程耀宗, 方掌櫃, 程陸 family-address vocatives** — promote as they recur.
- **大衍數 step names** (零/地三/頤王/起/伏/定/已/和) — 頤王 needed sed; recurs at Ep26 歸雲莊.
- **遵命 → "Yes, sir"** (Ep25) — `extras_baseline.json` if it fires again.
- **和伯伽→瑤迦 OCR** — promote to `OCR_NAME_COLLAPSE` on next firing.

**Ep31 single-firings (many; most Ep31-specific flashbacks):** 一陽指, 華山論劍, 重陽真人, 激將法, 過目不忘, 玉石俱焚, 雞鳴狗盜, 水能載舟亦能覆舟, 李白 將進酒 couplet, 女大不中留, 夫復何言, 圓寂, 陽壽已盡, 冰窒, 起死回生, 入土為安. Promote per §10 gate on next firing.

**Ep32 single-firings:** 百步穿腸, 蛇杖, 鋼刺, 一代宗師, 狼心狗肺, 七孔流血, 易如反掌, 死無葬身之地, 好生之德, 不識抬舉, 恩將仇報, 死有餘辜, 自作孽不可活, 言出必行, 願賭服輸, 百毒攻心. Promote per §10 gate on next firing. **六個時辰 hybrid-gloss convention** (Ep32 sub 231: `six shichen (twelve hours)`) — decide policy after next firing.

**Ep33 single-firings (32 idioms, deserted-island episode):** 蓋世奇書, 千秋大業, 斷腳之仇, 塞外高人, 遠水救不了近火, 天作孽猶可恕/自作孽不可活, 素仰先生, 沖天炮, 粉身碎骨, 如花似玉, 碎屍萬段, 約法三章, 恩將仇報, 暗箭傷人, 血肉之軀, 綽綽有餘, 有志者事竟成, 死有餘辜, 斯文有禮. Promote per §10 on second firing.

### 🟡 Cross-stage concat traps — pending promotion

- **`周伯通大哥 → Zau Baak-tungBig Brother / Jau Baak-tungBig Brother`** (Ep33) — 大哥 titles stage eats it. Fix on next firing.
- **`19th-generation 幫主` adjectival** (Ep33) — produces "19th-generation the Chief"; worked around with "leader". Observation only.
- **`泰山北斗 + 武林` duplicate** (Ep33) — "of the martial world of the martial world". Structural fix: revise 泰山北斗 rendering, or enshrine "don't pair" rule in STYLE §8.
- **我柯鎮惡 / 我裘千仞** (Ep26) emphatic-self compounds. Fix when they fire again.
- **我們 + non-`the` compound** (Ep28) — only `我們the` handled; 我們蒙古 etc unhandled.
- **Compact-idiom + em-dash concats** (Ep31, Ep32) — bare short idioms leak as CJK; policy TBD.

### 🟡 Rule B territory (chi wins — informational only)

- **歐陽克 Whisper cluster**: 克/赫/黑/客 all `haak1` (→ REFERENCE §1).
- **Long-tail chi-OCR beyond v13 collapse table**: 若師兄/王老邪/蔡洪峰 (Ep30); 周伯仲/白通/伯東 (Ep31/32); 梅竹風 (Ep31); 陳元鳳 (Ep31); 旺銅銀 (Ep31); 准魚/徐魚/狡獨/無原無故 (Ep32). Catalogued in REFERENCE §1; promote variant-by-variant as each fires a second time.

---

## 🟢 Recent Promotions (last two bundle bumps)

Items promoted during the last two bundle bumps. **Do not re-register in episode overlays.** Older promotion history is compacted below.

### v16 (Ep6 FULL session)
- Seven new `<titles-key>+<suffix>` / `<CSV-name>+<title>` concat-trap entries → `cjk_fix_v2.py` `shared_concat_fixes` / `yale_concat_fixes`: `五Master → Fifth Master`, `七Master → Seventh Master`, `大Master → First Master` (Ep5+Ep6 two-ep confirmation; STYLE §19 §20 "大Master → First Master" pre-existing entry now has automation), `紅Mother → the Matchmaker`, `姑Mother → Miss`, `柯Big Brother → Brother O`, `Zit-BitMaster → Master Zit-Bit` (jy) / `Jit-BitMaster → Master Jit-Bit` (yl).
- Ep6 arc-keyed first firings kept in episode overlay (`ep6_extras_add.json`) pending second firing: 迴聲谷, 八字純陰, 紅娘, 一箭雙鵰, 奮勇殺敵, 欲速則不達, 東征西討, 指腹為婚, 賊眉鼠眼 — all passed STYLE §10 admission gate, promote on second firing.

### v15 (Ep1 FULL session)
- Four `<titles-key>+<suffix>` concat-trap entries → `cjk_fix_v2.py` `shared_concat_fixes` / `yale_concat_fixes`: `六Your Highness → the Sixth Prince`, `My Mother子 → my wife`, `張老Father → Old Zoeng` (jy) / `Old Jeung` (yl), `官字taels個口 → the official's mouth speaks both ways`.
- 滿江紅 quatrain format established (STYLE §10 Classical-laments precedent for 岳飛 verses).

### Compacted history (v11–v14)

The full per-bump item lists for these bumps lived in prior SESSION-NOTES; content is now reflected in the source files. Look there if a v11–v14 promotion appears to regress:

- **v14 bump** (user-rule clarifications: generic wuxia vocabulary English in hybrid 武功/武林/江湖/內力/內功/輕功/功力; 叫化子 banned; colloquial insult compounds English; descriptive common-noun metaphors English; STYLE §10 admission-gate criteria. STYLE §5 additions: 歐陽先生/公子/叔叔. `extras_baseline.json` additions: 歐陽先生/公子/叔叔, 打狗棒/打狗棒法, 易筋鍛骨篇, 空明拳, 老乞兒/乞兒, 泰山北斗. STYLE §10 Classical laments: 曹操 短歌行 couplet).
- **v13 bump** (STYLE §19 structural rule; `OCR_NAME_COLLAPSE` v13 batch; `<titles-key>+<suffix>` family fixes; 週-daai-go/daaih-go leading-週 strip; 時辰/氣聚丹田/內力/真經 baseline).
- **v12 bump** (一陽指, 內子, 圓寂, 李白 將進酒 couplet pattern).
- **v11 bump** (我爹/你爹, 週大哥, 陸乘風 OCR-variant collapse; 叔叔/武功/走火入魔 baseline; Luksenior/KauElder/我們the/Cing姑Mother concat fixes; STYLE §5 additions 瑤迦/冠英/孫不二; STYLE §8 積翠亭/梅花樁; STYLE §10 秦晉之好/泰山北斗/天作之合; 想逝者/天蓋高 lament; 天之道/損有餘而補不足 九陰真經; REFERENCE §3 周伯通 voice; REFERENCE §1 阿克 homophone cluster).

---

## How to Use This Log

At session close:

1. **Update the episode row.** Move FULL rows into the Completed table (sorted ascending by episode number). Leave PARTIAL/MECHANICAL rows in Pending with an outcome note.
2. **Add new Watch List items.** Skip anything already in `STYLE.md` §5/§6/§10 or `REFERENCE.md`.
3. **Promote when stable.** Two-episode confirmation without contradiction → move to the consolidated doc and delete from here.
4. **Hold the row budget.** Target ≤500 chars per Completed-table row body; hard cap 1000. If a row exceeds the cap, cut per-sub citations, who-said-what parentheticals, and validation summaries first.

This file is not a general changelog. Pipeline version bumps for script architecture belong in `PIPELINE.md`. The Recent Promotions section records Watch List graduations so future sessions don't re-register them; anything older than two bumps back should be compacted to a one-line pointer.
