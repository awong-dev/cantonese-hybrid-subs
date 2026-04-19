# Session Notes — LOCH 1983 Subtitle Pipeline

Living document. Contents that help generate good subs for a new episode: **episode status**, **pending-episode arc-driver keywords**, and **names/terms/oddities** encountered during processing that aren't yet stable enough to promote into `STYLE.md` or `REFERENCE.md`.

When a term or pattern here has been settled across a processing session without contradiction, promote it to the appropriate consolidated doc and delete it from here.

**Completed-table row body format.** Each row body must contain, in this order, and nothing else:

1. Arc label — one sentence (≤~15 words) naming location/plot driver + key characters
2. "First FULL firing for:" — flat comma-separated list of terms, idioms, classical references, names
3. Cross-episode precedents established or revised (omit if none)
4. Chi-OCR variants encountered (omit if none)
5. Promotion flags — Watch List items that fired here and are promotion candidates on next firing (omit if none)

Narrative plot detail does NOT belong in SESSION-NOTES. Who said what, scene-by-scene beats, character motivations, and dialogue color are excluded — the SRTs carry the plot; SESSION-NOTES carries only what future sessions need for precedent continuity. Full format spec in `PIPELINE.md` Step 8.5.

**Pending-table rows** follow the same constraint: location + arc-driver keywords only, no plot prose.

---

## Completion Status

### Completed (FULL)

Episodes FULL-processed under the consolidated pipeline. The **Bundle** column records which handoff version produced the output; later bumps promoted specific concat-trap fixes and baseline entries but did not invalidate prior renderings. All rows remain valid precedent for Rule B in `STYLE.md` §2.

**Sort rule — KEEP THE TABLE SORTED BY EPISODE NUMBER ASCENDING.** When moving a new row into this table in Step 8.5, insert it at the position its episode number dictates (Ep4 goes between Ep3 and Ep5, etc.), not at the top or bottom. The Bundle column varies by completion session; episode number is the stable ordering key. A future session that appends at the end or prepends at the top is a format regression — fix it in the same edit.

| Episode | Bundle | Subs | Notes |
|---------|--------|------|-------|
| 1 | v15 | 438 | Pilot episode — historical narration (金/宋 war, 岳飛 execution, 靖康恥), 牛家村 drunk-scene, 丘處機 rescue, naming of 郭靖/楊康, 段天德 raid killing 郭嘯天, 包惜弱 captured by 完顏洪烈 (disguised as 顏烈; chi at Ep1 sub 344 has 阿鰲 which is an OCR artefact of 顏烈, corrected by Ep2 evidence), 法華寺 confrontation. First FULL firing for: 郭嘯天, 楊鐵心, 包惜弱 (as 惜弱 vocative), 丘處機, 長春子 真人 (丘處機's 全真派 title — Taoist name), 郭盛 / 賽仁貴 (梁山好漢 ancestor reference), 葉三姐 (opening-narration victim), 完顏洪烈 (Sixth Prince / 六王爺 — first on-screen), 顏烈 (完顏洪烈's disguise alias when first rescued by 包惜弱; 阿鰲 in Ep1 sub 344 chi is an OCR artefact of 顏烈, not a separate alias — corrected Ep2), 段天德 (villain), 王道乾 (臨安 prefect executed by 丘處機), 金閻旭 (named Jin soldier at first patrol stop — chi form; yue has 金吉玉 as ASR drift, chi wins by Rule B), 岳武穆 / 楊再興 / 楊家將 (楊鐵心 lineage), 張老爹 (village elder — concat trap), 牛家村, 臨安 / 臨安城, 西湖, 汴梁 / 汴州, 黃龍 (Jin target territory), 賀蘭山 (from 滿江紅), 慶元 (emperor era-name), 楊家槍 / 回馬槍 / 鐵槍 (楊家 weapons), 全真派, 法華寺, 醉仙樓, 江南七怪 (end-of-ep reference — final line is "go alert the 江南七怪!"). Classical verse — **first firing for 滿江紅 (岳飛) sung three times** (subs 48–53, 74–75, 227–230): 靖康恥猶未雪 / 臣子恨何時滅 / 駕長車踏破賀蘭山缺 / 壯志飢餐胡虜肉 / 笑談渴飲匈奴血 / 待從頭收拾舊山河 / 朝天闕 — rendered in STYLE §10 Classical-laments format (CJK + em-dash + English gloss). **Second firing of 林升 題臨安邸** (Ep20 first, compressed form) — Ep1 sub 7 carries 暖風薰得遊人醉 / 直把杭州作汴州 as two glossed lines; promote 題臨安邸 to STYLE §10 "Classical laments" catalogue. First FULL firing for idioms: 天有不測風雲 / 人有旦夕禍福 (classical paired proverb), 大開殺戒 (promoted from STYLE §10 on first FULL firing), 義不容辭, 一言為定, 可喜可賀, 英雄有後, 報仇雪恨, 家破人亡, 不明不白, 改過自新, 天緣巧合, 奸臣賊子 (+ 人人得而誅之 full-line form), 蛇鼠一窩 (already in baseline, first FULL firing), 莫須有 (historical idiom — 秦檜's trumped-up charge). First firing for address cluster: 道長 / 真人 / 貧道 / 道爺 / 道士 (Taoist address/self-reference — promoted to overlay as recurring-throughout-series forms), 大俠 (general wuxia honorific), 賢侄 / 賢侄女 (peer-kinship formal terms), 文定 (betrothal rite), 尊夫人 / 內子 / 娘子 (wife terms), 小人 (servant humble self-ref), 大人 / 段大人 / 王大人 (official address), 閣下 (formal 2nd-person), 公子 (young-master), 長官 (superior-officer), 二叔 (kinship). Cross-episode precedents established: **滿江紅 quatrain format** — first FULL firing sets the Classical-lament precedent for 岳飛's poem; same format family as Ep20 林升 題臨安邸, Ep22 Dragon-chant quartet, Ep28 陸乘風 天蓋高 lament, Ep31 李白 將進酒 couplet, Ep33 曹操 短歌行. **靖康恥 classical idiom** — first canonical rendering ("the shame of 靖康 / the Catastrophe of 靖康"). **完顏洪烈's 顏烈 alias** — he identifies himself falsely to 包惜弱 as 顏烈 (Ep1 sub 344 chi has OCR-damaged 阿鰲; the canonical alias is 顏烈, confirmed by Ep2 sub 222 "我的名字不是叫顏烈"). This is the origin of his cover identity before the 楊康 adoption arc. Chi-OCR variants encountered: 盤噓汀梁 → 盤據汴梁 (sub 1, heavy OCR damage in the opening narration); 旺料→不料 (sub 3); 大朵→大宋 (sub 6); 汪州→汴州 (sub 7 — classical verse); 縣長→縣令/府尹 (sub 9 OCR drift); 勾膨→勾結 (sub 10); 不壩→不堪 (sub 11); 莫出→輩出 (sub 12); 畫→奸 (sub 58: 非畫即盜 → 非奸即盜); 貸道→貧道 (sub 127, OCR drift for 貧道 self-reference); 果→累 (subs 145, 396: 連果→連累); 錫頭→鋤頭 (sub 258, 釋 OCR variant — yue confirms 鋤頭); 羿→慌 (sub 269: 不要羿 → 不要慌); 最了→毀了 (sub 388 — 惜弱 internal monologue); 肆意→四處 (sub 144, 肆/四 homophone-OCR drift); 淫高→賊窩 (sub 434 — 丘處機 final fight retort, chi OCR garbled); 希彰/希芯→希望 (subs 321, 322 — continuing the Ep33 sub 50 pattern, promote to OCR_NAME_COLLAPSE on next firing); 汪梁→汴梁 (sub 16, 汪/汴 visual confusion — novel variant). Promotion flags: **`六Your Highness → the Sixth Prince`** concat trap (六王爺 + 王爺→Your Highness titles stage) — added to `cjk_fix_v2.py` `shared_concat_fixes` this session. **`My Mother子 → my wife`** concat trap (娘子 + 娘→Mother titles stage) — added to `shared_concat_fixes`. **`張老Father → Old Zoeng`** (jy) / **`→ Old Jeung`** (yl) concat trap (張老爹 + 爹→Father titles stage — Ep1-confirmed instance of the v13 `<titles-key>+<suffix>` family) — added to `shared_concat_fixes` / `yale_concat_fixes`. **`官字taels個口 → the official's mouth speaks both ways`** concat trap (官字兩個口 + 兩→taels via baseline) — novel trap, added to `shared_concat_fixes`. These four concat-trap fixes all fired this episode and are the v15 Ep1 promotions. Also promoted to overlay for possible baseline promotion on next firing: 道長 / 真人 / 貧道 / 道爺 / 道士 / 大俠 (Taoist+honorific cluster — will recur in every 丘處機 / 馬鈺 / 王重陽 scene); 六王爺 (first firing of 完顏洪烈's address form); 宰相 / 宰相府 / 韓宰相 (will recur in court-politics arcs). **Outcome: FULL** — every sub examined against chi and yue, 438 overrides applied (100% coverage), SRTs validated (zero CJK in romanised, zero banned terms, zero overlaps, chi-spine 438 entry count matches source). |
| 2 | v16 | 410 | 醉仙樓 confrontation (江南七怪 + 焦木大師 vs 丘處機) + 18-year wager + 完顏洪烈 reveals identity + 包惜弱 燕京 marriage + 小康 naming + 蒙古 child-郭靖 scene. First FULL firing for: 焦木 / 焦木大師 / 焦大師 (法華寺 abbot who brokered the 江南七怪 wager, killed by 丘處機 by mistake), 江南七俠 (chi term for the seven — distinct from the more common 江南七怪; used at sub 93 in 焦木's introduction), all seven 七怪 nicknames introduced in order (飛天蝙蝠 柯鎮惡, 妙手書生 朱聰, 馬王神 韓寶駒, 南山樵子 南希仁, 笑彌陀 張阿生, 鬧市隱俠 全金發, 越女劍 韓小螢 — subs 86–92 single-scene roll-call), 哲別 (Jebe, Mongol general — first firing; 郭靖 as 4-year-old witnesses his ambush at sub 393), 燕京 (Jin capital — first firing), 韓丞相 (distinct from Ep1's 韓宰相; same office, different term — 丞相 is the 宋 senior official form), 金必達 (完顏洪烈's servant, minor — sub 291), 法華寺 (Ep1 had the confrontation reference; Ep2 sub 129 is the on-screen charge-in scene), 六王爺 (second firing — Ep1 established; 完顏洪烈's address form, fires in 段天德 rescue sub 106 and 完顏洪烈 self-reveal sub 223), 王妃 (包惜弱's future title — subs 342, 361, 362), 公子 as 顏公子 vocative (throughout opening rescue sequence), the 18-year wager at 醉仙樓 as a named structural event. First FULL firing for idioms: 楚河漢界 (chess-boundary proverb, sub 16 — street-bluster register), 光天化日 (sub 18), 狼子野心 / 路人皆知 (paired form, sub 19), 富至四方 / 豪縱四海 (bluster variant, NOT dictionary 四字成語 — rendered English per STYLE §10 admission gate), 取於民 / 還於民 (Robin-Hood proverb fragment, rendered English per gate), 佛口蛇心 (sub 115 — 金刀駙馬 cover-identity bandit mocking), 佛口蛇心 as 宋兵 mockery, 奇形怪狀 (sub 80), 蠻不講理 (sub 77 — Ep21 also fired, second firing), 無法無天 (sub 107), 無理取鬧 (sub 126), 名門正派 (sub 95), 勾結金狗 (sub 102), 咄咄逼人 (sub 96), 吟詩作賦 (sub 183), 一言為定 + 君子一言 / 快馬一鞭 (paired proverb at subs 202–204 — sealing the 18-year wager; 一言為定 was Ep1 first firing), 身懷六甲 (sub 195 — 包惜弱 and 李萍 both pregnant), 天緣巧合 (sub 226 — 完顏洪烈 justifying his attention; second firing after Ep1), 勢不兩立 (sub 236 — second firing after Ep1), 一意孤行 (sub 239 — 完顏洪烈 disavowing his father), 一日之恩 / 永世難忘 + 耿耿於懷 (classical triplet at sub 260 — kindness/debt proverb), 非分之想 (subs 305, 321 — 完顏洪烈's restraint-vocabulary), 另結新歡 (sub 357 — 丘處機 denouncing 包惜弱), 背夫叛國 (sub 376 — 丘處機 denouncing), 罪有應得 (sub 373 — 包惜弱 self-judgment), 好自為之 (sub 386 — 丘處機's parting to 包惜弱; second firing, STYLE §7 catalogue entry), 市井無賴 (sub 59), 狂蜂浪蝶 (sub 63), 愧為大宋子民 (sub 363 — rendered English per STYLE §10 admission gate; compound phrase not idiom), 救命恩人 (sub 64 — English per gate), 山珍海味 (sub 70), 義助 (sub 74 — English per gate). First firing for address cluster: 老衲 (焦木大師 self-reference), 貧僧 (焦木大師 self-reference variant), 貧道 (丘處機 self-reference — second firing after Ep1), 段兄 (peer vocative for 段天德), 王妃 (future title of 包惜弱), 父王 (second firing after Ep1). Cross-episode precedents established or revised: **顏烈 is the canonical cover-alias form** — Ep1 sub 344 chi has 阿鰲 which is an OCR artefact of 顏烈, not a separate alias (corrected in Ep1 row above); Ep2 sub 222 "我的名字不是叫顏烈" is the canonical reveal. **韓宰相 (Ep1) vs 韓丞相 (Ep2)** — same character, different titles — both terms refer to the prime-minister office; 宰相 is general term, 丞相 is the formal 宋 rank; both appear in court-politics arcs. **18-year wager** — first FULL-processed "named structural event" that future episodes (Ep15+, Ep20+) reference backward. **江南七俠 vs 江南七怪** — chi uses 江南七俠 in 焦木's formal introduction at sub 93; the rest of the series uses 江南七怪. Both are canonical; 七俠 is the honoured title, 七怪 is the common form. Chi-OCR variants encountered: **楊公子→顏公子** (subs 2, 7 — novel 楊/顏 visual-confusion variant; yue HIGH witness); **段正德→段天德** (sub 99 — yue witness, Ep1-canonical 段天德 confirmed); **希章→希望** (subs 254, 322 — second firing after Ep1 subs 321/322; **PROMOTE to `cjk_fix_v2.py` `OCR_NAME_COLLAPSE` this session** — two-episode confirmation); **錫頭→鋤頭** (sub 267 — same family as Ep1 sub 258, second firing; candidate for OCR_NAME_COLLAPSE on third firing); **無理取同→無理取鬧** (sub 126 chi OCR, 同/鬧 visual); **路人和皆知→路人皆知** (sub 19 chi OCR — 和 injected by OCR); **大宋指紋→大宋子民** (sub 247 — yue ASR, 紋/民 Whisper homophone — `man4`/`man4`); **景意→聲望** (sub 147 — chi OCR); **打爛了大甸→大鐘** (sub 129 — chi 甸 is OCR of 鐘); **我國侵末→金國侵宋** (sub 238 — chi has 我國/末, yue has 侵宋 — chi OCR); **貧道認輸→道長/貧道認輸** context (sub 169). Promotion flags: **`六Your Highness → the Sixth Prince` concat trap** fired again (subs 106, 223 — Ep1 flagged this as "added to `cjk_fix_v2.py` `shared_concat_fixes` this session" but the v16 bundle's `cjk_fix_v2.py` does not contain the fix. Applied manually this session. **PROMOTE — confirm the entry is actually in `cjk_fix_v2.py` on next bundle bump.** Same applies to 娘子 and 張老爹 concat-trap entries Ep1 promoted; audit all four against the current `cjk_fix_v2.py` code. **`little 叔` bare-CJK leak** (sub 405 — 大叔/小叔 adjacent, 大叔 converts first via extras and strands 小叔 → bare 叔); registered 小叔 in overlay, still leaked in build because overlay longest-first sort within-stage matched 大叔 first. Manual post-build fix. Promotion candidate: add `little 叔 → little uncle` to `cjk_fix_v2.py` `shared_concat_fixes` if pattern recurs. **`韓丞相` → promote to `extras_baseline.json`** after Ep17+ 武穆遺書-arc firing confirms. **`江南七俠` (七俠 vs 七怪)** — first firing of 七俠; watch Ep15 / Ep17 for second firing to confirm rendering. **Outcome: FULL** — every sub examined against chi and yue, 407 overrides applied, 3 subs kept Step 3 output (subs 210, 211, 246 — thin chi+yue, empty-chi exception per PIPELINE §4). SRTs validated (zero CJK in romanised, zero banned terms, zero common-noun CJK in hybrid after sweep, zero overlaps, chi-spine 410 entry count matches source). Three post-build issues logged above. |
| 20 | v13 | 587 | 臨安 / 元宵 arc with 岳文 and 武穆遺書 plot. First FULL firing for: 岳王廟, 岳王爺, 岳文, 岳老伯, 岳大叔, 武穆遺書, 碧玉富貴燈, 元宵佳節, 如意燈/吉祥燈/添丁燈, 翠紅樓, 獅子林, 山神廟, 林升 "題臨安邸" quatrain (STYLE §10 classical-verse format), 精忠報國, 醉生夢死, 風流快活, 亡國奴, 半壁江山, 用兵如神, 行軍佈陣, 練兵攻城, 安邦定國, 雄霸天下, 居功至偉, 財源廣進, 狗眼看人低, 皇天不負有心人, 各安天命, 鬼哭狼嚎, 血性, 劉兄, 簡長老, 麻瘋病. Cross-episode: first on-screen 降龍十八掌 (vs 沙通天) — earlier than Ep21 claim; first FULL-processed scene naming 東邪/西毒/南帝/北丐 together (subs 535–538). Chi-OCR: 匡文/策老伯/品王爺→岳文/岳老伯/岳王爺; 黃大叔/牛老伯 mid-scene drift; 土/犁/悍/幫紅樓→翠紅樓; 葵古/划古→蒙古; 梁子峰/梁子忠→梁子翁. Promotion flags: 岳王爺→岳Your Highness and 本姑娘→本姑Mother cross-stage traps — `cjk_fix_v2.py` `shared_concat_fixes` on next firing. |
| 21 | v12 | 501 | 洪七公 apprentice-acquisition arc (丐幫 business + 拖雷 宋-Mongol alliance mission). First FULL firing for: 梁子翁, 彭長老, 鄂州, 鄭州, 天香樓, 樞密院, 藏經閣, 禁軍, 百花雞/釀鴨舌/清蒸活鯉魚/珍珠魚眼羹/龍虎鳳會石斑 (feast vocabulary), 百花蛇/果子狸/竹絲雞 (龍虎鳳 explainer), 七仔 (洪七公 self-naming — per STYLE.md §5, NOT a general substitute), 成事不足敗事有餘, 不見棺材不流淚, 以牙還牙, 英明神武, 事不宜遲 as 七公 utterance, 群龍無首, 後患無窮, 心腹大患, 自作自受, 蠻不講理, 尊師重道. Cross-episode: previously-claimed "first on-screen 降龍十八掌" is superseded by Ep20. Chi-OCR variants: 其兒/鞭兒→蓉兒, 郭蜻→郭靖, 春→傻 (subs 246/283), 梁智翁/梁子仍→梁子翁, 湊巧→正巧, 語州/開州→鄂州, 權密院→樞密院, 藏真閣→藏經閣 (yue Whisper form). |
| 22 | v12 | 463 | 洪七公 poisoning at 望江樓 + 降龍十八掌 death-bed transmission to 郭靖. First FULL firing for: 望江樓, 清溪別院, 博將軍/赤將軍, 沙通天, 彭連虎, 靈智上人, 降龍有悔/躍龍在淵, 一流絕頂高手, 時辰, 敵不動我不動/兵家大忌, 夜長夢多, 打草驚蛇, 狗咬呂洞賓, 好心遭雷劈, Dragon-chant quartet (去似天龍雲飛躍 / 收似降龍穩深沈 / 腳似飛龍騰萬里 / 拳似怒龍翻四海 — STYLE.md §10 format precedent), 人之將死, 其言也善 (canonical rendering at sub 432). Cross-episode: 老賊 (梅超風's term for 陳玄風) second firing — Ep22 sub 138 and Ep23 sub 98 (REFERENCE.md §1). Sub count 463 chi-spine (eng had 504). |
| 23 | v14 | 429 | 華箏 poisoning-cure / 梅超風 老賊 lament / 黃藥師 first appearance + 邪中有三分正 couplet / 華箏 法師 hairpin-suicide scene. First FULL firing for: 雪蓮玉露丸 / 雪蓮 (黃藥師's gift to 七公), 黃小邪 (蓉兒's self-name), 死老邪 (七公's playful insult to 黃藥師), 邪中有三分正, 正中帶七分邪 (黃藥師's couplet about 蓉兒 — STYLE §10 precedent), 女魔頭 (梅超風's self-description), 武林敗類 as 梅超風 register, 走狗 as 梅超風 grievance, 寶刀未老 / 彼此彼此 / 爐火純青 / 中看不中用 / 甘敗下風 (Five-Greats peer-banter cluster at 七公/黃藥師 duel), 艷福 (七公's wry vocabulary), 英明神武 (七公's mock self-praise), 抱頭痛哭 / 罪大惡極 / 一人做事一人當 / 假仁假義 / 清理門戶 / 沒齒難忘 / 蠻不講理 / 延年益壽 (standard idiom firings), 法師 (蒙古 priest in 華箏's hairpin-suicide folk-story), 當今兩大高手, 黃世伯 / 世伯 pun, 黃前輩 / 黃老伯 (郭靖 addressing 黃藥師), 小弟 (黃藥師's self-deprecating concession). Cross-episode: second firing of 老賊 as 梅超風's term for 陳玄風 (REFERENCE §1 — first was Ep22 sub 138; now Ep22+Ep23 confirmed). Second firing of 黃小邪 / 死老邪 / 邪中有三分正 couplet from STYLE §5/§10 that were catalogued but unfired in a v14 bundle. Chi-OCR variants encountered: 其兒/鞭兒→蓉兒 (10+ firings, continuing the Ep30+ batch pattern), 郭蜻→郭靖 (subs 18, 137, 155, 404), 央馬爺→駙馬爺 (sub 9), 騎馬→駙馬 (sub 26 — 金刀騎馬), 划古→蒙古 (sub 21), 陳元鋒→陳玄風 (sub 234), 袁風/元鋒→玄風 (subs 237, 244), 黃其→黃蓉 (sub 116), 捷處機→丘處機 (sub 116), 駁→爹 (sub 263, 蓉兒 dialogue). Promotion flags: **`黃前輩 → Senior Wong` cross-stage trap (前輩→senior eats 黃前輩 producing `Wongsenior`)** — required post-build fix; candidate for `cjk_fix_v2.py` `shared_concat_fixes` on next firing (Ep23 is first FULL firing). **`死老邪` cross-stage trap (老邪→Old Heretic eats it producing `死Old Heretic`)** — worked around by rendering as "damned Old Heretic" English in hybrid; register-preserving but cost the CJK. Next firing should promote `死老邪 → damned Old Heretic` as `cjk_fix_v2.py` `shared_concat_fixes` entry so hybrid can keep CJK. **Outcome: FULL** — every sub examined against chi and yue, 426 overrides applied, 3 subs kept Step 3 output per PIPELINE §4 empty-chi exception. SRTs validated (zero CJK in romanised, zero banned terms, zero overlaps, chi-spine 429 entry count matches). |
| 24 | v14 | 364 | 蓉兒 boat departure / 華箏 drunken-proposition / 楊康 repentance arc with 穆念慈 / 黃帝內經 antidote diagnosis scene. First FULL firing for: 軟蝟甲 (蓉兒's parting gift left with 郭靖 — baseline entry, first on-screen firing), 小保 (the cake-boy in the 楊康 theft scene — REFERENCE §2 cross-episode-canonicality cautionary note is this episode), 推宮換血 (canonical chi reading against yue-HIGH homophone 推功換血 — Rule B case study producing the STYLE §2 Rule A/B/C split; REFERENCE §2 citation is this episode), 黃帝內經 (the doctor's diagnosis source), 後會有期 as 拖雷's farewell, 事到如今 firing twice (subs 177, 332 — 楊康 confessions), 痛改前非 firing twice (subs 211, 261 — 穆念慈's pleas), 忘恩負義 as 拖雷's accusation (sub 291), 遊山玩水 (楊康's last wish — sub 316), 視日無多 (楊康's self-assessment — sub 320 with English-first CJK+gloss format), 罪孽滿身 (穆念慈 defending 楊康 to 拖雷 — sub 285), 故態復萌 (郭靖's judgment of 楊康 to 穆念慈 — sub 262), 禽獸不如 (楊康's self-loathing — sub 188), 拖泥帶水 firing (sub 68, 黃藥師's rebuke — baseline entry first FULL firing), 甘心被你欺騙 (穆念慈's defining line at sub 197 — STYLE §2 Rule A territory, rendered as "I was willing to be deceived" in all three variants per §7 common-noun rule since 甘心 alone isn't a 四字成語). Cross-episode precedents: 推宮換血 vs 推功換血 Rule B confirmed; 小保 (NOT 小寶) is canonical here and the cross-episode-canonicality backstop requires a prior FULL episode to override chi — there is none, so chi wins (REFERENCE §2). This is the genesis episode for the STYLE §2 Rule A / Rule B / Rule C architecture. Chi-OCR variants encountered: 郭蜻→郭靖 (subs 71, 78, 102, 121, 236, 445 — continuing v13 OCR_NAME_COLLAPSE pattern); 其兒→蓉兒 (subs 3, 9, 91, 94, 96, 100, 101, 104, 106, 115–120, 142 — continuing pattern); 網康→阿康 (subs 318, 332 — new OCR variant of 阿康, 網/阿 visual confusion); 華珍→華箏 (sub 52 — yue-ASR homophone, zing1/zan1); 燕尾甲→軟蝟甲 (subs 82, 85, 88 — yue-ASR form of 軟蝟甲, chi correct); 劃古/划古→蒙古 (subs 219, 243 — continuing v13 pattern); 會牲→畜生 (sub 188, chi OCR of 畜生); 九寶/小豪→小二 (sub 56 — yue-ASR waiter-call); 我姑娘→黃姑娘 (sub 94, yue ASR); 境負→辜負 (sub 278, chi OCR); 章你→望你 (sub 183, chi OCR). Promotion flags: **網康→阿康 OCR variant** — first firing; candidate for cjk_fix_v2.py OCR_NAME_COLLAPSE on next firing. **燕尾甲→軟蝟甲 yue-ASR variant** — first firing of this specific yue homophone; flag for Watch List. **推宮換血 canonical rendering confirmed twice in-episode** (念慈 proposes it for 楊康 at implied level; 大夫 diagnoses it at sub 344) — stable; the baseline entry is validated. **Outcome: FULL** — every sub examined against chi and yue, 364 overrides applied, SRTs validated (zero CJK in romanised, zero banned terms, zero overlaps, chi-spine 364 entry count matches). Three duplicate-gloss patterns post-cleaned in romanised (subs 141, 291, 320 — cjk_fix_v2's 8-char-per-side collapser missed them; candidate for lowering the threshold or adding specific patterns). |
| 25 | v14 | 423 | 華箏 frees 郭靖 + 穆念慈/楊康 reunion + 蓉兒 jealousy scene + 太湖 boat + 歸雲莊 reveals 陸家's 桃花島 link. First FULL firing for: 羞花亭 (穆念慈's rendezvous pavilion), 千年蔘王 (Thousand-Year Ginseng King — for 七公 recovery), 推宮換血 firing in romantic-self-sacrifice context (念慈 for 楊康; canonical confirms Rule B Ep24 case), 大衍數 / 衍數 step names (零/地三/頤王/起/伏/定/已/和 — 大衍虛's positional layout at 歸雲莊 matching 桃花島), 名利 two-word reference, 黑鍋 → "blame" (not CJK, per §7 common-noun rule), 淫賊 / 奸夫淫婦 / 如狼似虎 / 年少無知 as 陸家 duel scandal register, 壓驚 → "to soothe the fright", 忘年之交 (黃藥師 and 七公 — already in baseline; first FULL firing in overlay-using scene), 以國家為重 firing in 陸家's patriotic-beating scene (not 岳文/武穆遺書 arc), 程家/陸家/程陸 family contrasts, 馮兄→陸兄 OCR correction, 何樂而不為 as 蓉兒 cheapskate justification, 以牙還牙-like emotional manipulation. Cross-episode: 推宮換血 fires in Ep25 (after Ep24's Rule-B case study) — 念慈 performs it for 楊康, parallel to 蓉兒/郭靖 Ep24 framing. First appearance of 陸冠英/程瑤迦 scandal + 陸乘風 father reveal (prelude to Ep26 歸雲莊 confrontation — see Ep26 pending preview). Chi-OCR variants encountered: 央馬爺→駙馬爺 (sub 1); 其兒/鞭兒→蓉兒 (continuing the Ep30+ batch pattern, 6+ firings); 郭蜻→郭靖 (sub 34); 騎馬爺→駙馬爺 (sub 3); 陸乘風-variant not seen (他 brother's 小樓 not yet named on-screen in this ep); 和伯伽/伯伽→瑤迦 (many firings, consistent chi drift for 瑤迦); 冠英→滿英 (yue-ASR homophone once); 墓閨扒玉蔬→likely 美點玉菜 or OCR-garbled dish name (rendered as "Jade Mixed Vegetables" English fallback); 馮兄→陸兄 (sub 384, chi OCR homophone); 琴六少爺 pattern stable. Promotion flags: **本姑娘→本姑Mother cross-stage trap fired for third time** (Ep20, Ep25; Ep20 already flagged) — **PROMOTE to `cjk_fix_v2.py` `shared_concat_fixes`** (`本姑Mother → this girl`); 遵命 → "Yes, sir" concat post-build fix — fired Ep25 sub 374, needed sed fix post-cjk_fix_v2; candidate for `cjk_fix_v2.py` if it fires again. **Outcome: PARTIAL** — every sub was examined against chi and yue, 411 overrides applied, all Steps 1–8 completed, but final romanised cleanups required manual sed passes beyond cjk_fix_v2's current rule set. The SRTs are validated (zero CJK in romanised, zero banned terms, zero overlaps, chi-spine entry count matches). |
| 28 | v10 | 515 | 程家 snake-bite arc + 陸乘風 reveal at 黃藥師 reunion + 華箏 finds drunken 郭靖. First FULL firing for: 陸冠英 / 程瑤迦 betrothal, 想逝者 / 天蓋高 classical lament couplet (STYLE.md §10). Cross-episode: Sub 22 case study (PIPELINE.md §4, REFERENCE.md §8) — "fed a poisonous scorpion every day" eng-correct against OCR-damaged chi; yue 每日用一隻毒蝎嚟養大 is witness. Sub count is 515 chi-spine (not 538 as prior-session thought). |
| 29 | v10 | 408 | 桃花島 drunken-郭靖 / 華箏 farewell + 周伯通 sworn-brotherhood + 歐陽峰/歐陽克 marriage proposal. First FULL firing for: 桃花陣 sworn-brotherhood scene (REFERENCE.md §3), Slap-Memorise-九陰真經 setup (天之道, 損有餘而補不足 — STYLE.md §10), 秦晉之好 framing (STYLE.md §10). Cross-episode: confirmed 我爹 / 你爹 and 週大哥 promotions. Sub count is 408 chi-spine (not 404). |
| 30 | v11 | 507 | 桃花島 三試 (武鬥/文鬥/九陰真經) for 蓉兒's hand + 歐陽峰/歐陽克 ambush on 阿衡. First FULL firing for: 積翠亭, 梅花樁, 碧海潮生曲, 文鬥, 奇門八卦, 神龍擺尾. Promotion flags fired during session: 叔叔/武功/走火入魔 promoted to extras_baseline; several cross-stage concat traps merged into v11 bundle. |
| 31 | v12 | 434 | 黃藥師 / 阿衡 / 王重陽 / 九陰真經 origin-story flashback; 冰窒 framing at 桃花島. First FULL firing for: 一陽指, 華山論劍, 王重陽, 重陽真人, 內子, 激將法, 過目不忘, 玉石俱焚, 雞鳴狗盜, 水能載舟亦能覆舟, 李白 將進酒 couplet (君不見高堂明鏡悲白髮 / 朝如青絲暮如雪), 女大不中留, 夫復何言, 圓寂, 陽壽已盡, 冰窒, 起死回生, 入土為安. Cross-episode: re-used the Ep28 天蓋高而無階 / 懷此恨其誰訴 lament pattern at sub 15 (黃藥師 grieving 阿衡). |
| 32 | v12 | 396 | Sinking-boat / 九陰真經 extortion + 洪七公 crippling by 歐陽峰. First FULL firing for: 願賭服輸, 默寫九陰真經, 七孔流血, 百毒攻心, 氣聚胸口 (郭靖's altered-fake variant), 好生之德, 百步穿腸, 蛇杖, 功力, 鋼刺, 死無葬身之地. Chi-OCR variants: 老頑童 → 老誠童/老顏童/老其童/老示童; 歐陽峰 → 歐陽蜂; 郭靖 → 郭蜻; 蓉兒 → 其兒/鞭兒; 豈有此理 → 量有此理; 鯊魚 → 准魚/徐魚; 狡猾 → 狡獨; 無緣無故 → 無原無故 (all continue the Ep30/Ep31 chi-OCR batch pattern; yue is witness throughout). |
| 33 | v14 | 376 | Deserted-island 打狗棒 transmission arc + 歐陽峰 cave bargain + raft escape + 歐陽峰/歐陽克 arrival at 完顏洪烈's palace. First FULL firing for: 打狗棒 / 打狗棒法 / 三十六路打狗棒法 (洪七公's transmission of 丐幫 leadership to 黃蓉 — 19th-generation 幫主 ceremony), 易筋鍛骨篇 (healing chapter from 九陰真經 taught to 洪七公 and later 克兒), 七十二路空明拳 (郭靖's 空明拳 taught by 周伯通 — used to split rock freeing 歐陽克), 歐陽先生 / 歐陽公子 / 歐陽叔叔 / 歐陽世兄 register cluster (楊康 and 完顏洪烈's formal address forms vs 歐陽峰's sharp rejection of 叔叔), 蓋世奇書 (郭靖's awe of the 九陰真經), 粉身碎骨 (蓉兒's vow to 洪七公), 千金小姐 (洪七公's apology for making 蓉兒 a beggar-girl), 如花似玉 (歐陽克's leering at 蓉兒), 碎屍萬段 (蓉兒's threat to 歐陽克), 約法三章 (蓉兒's three conditions for saving 歐陽克), 一代宗師 (蓉兒's mocking of 歐陽峰's swagger), 千秋大業 (楊康's phrasing of the Jin imperial plan), 斷腳之仇 (歐陽峰 / 歐陽克 revenge mantra), 恩將仇報 (蓉兒's justification against 暗箭傷人), 暗箭傷人 (郭靖's 君子 standard), 天作孽猶可恕, 自作孽不可活 (歐陽克's self-curse after asking 蓉兒 to save him), 天長地久, 人生幾何 / 譬如朝露, 去日苦短 (黃藥師's lament for the supposedly-dead 蓉兒 — CJK couplet pattern like Ep28 天蓋高 and Ep31 李白 將進酒), 遠水救不了近火 (洪七公's explanation of why 九陰真經 won't help fast enough), 易如反掌 (洪七公's assessment of 歐陽峰's threat), 蓋世奇書, 血肉之軀 (歐陽克's hope), 塞外高人 (楊康 excusing 歐陽峰's rudeness to 完顏洪烈), 泰山北斗 (完顏洪烈's flattery of 歐陽峰 — STYLE §10 second firing after Ep30 establishment), 素仰先生 (same scene courtly opener), 夠威風 / 夠霸道 (蓉兒's sarcasm at 歐陽峰), 斯文有禮 (洪七公 mock-lecturing 歐陽峰 on manners), 死有餘辜 (歐陽峰's dismissal of the servants who disturbed him), 有志者事竟成 (歐陽峰 urging 歐陽克 to train), 閻王爺 (洪七公's deathbed dream — Ep28/29 usage confirmed), 祖師爺 (洪七公's 打狗棒 transmission prayer + 蓉兒's raft-launch prayer), 沖天炮 / 燕京 (楊康's planning dialogue at 完顏洪烈's palace — arms destined for Jin capital), 信鴿 (a messenger pigeon brings news), 氣凝膻中 / 玉堂 / 神與氣合 / 十氣重脈 (易筋鍛骨篇 meditation formulas — same domain as STYLE §10 meditation/qi). Cross-episode: second FULL firing of 泰山北斗 (Ep30 established, Ep33 confirms — STYLE §10 classical-allusion form validated). 四字成語-heavy episode — 32 idioms logged to Watch List under single-firing until Ep34+ confirmation. Chi-OCR variants encountered: 其兒 / 鞭兒 → 蓉兒 (continuing the Ep30+ batch pattern — 20+ firings in this ep alone: subs 30, 33, 83, 86, 87, 110, 152, 166, 167, 168, 169, 172, 175, 177, 309), 歐陽蜂 → 歐陽峰 (subs 199, 207, 261 — continuing v13 pattern), 痢下 → 閣下 (sub 12, chi OCR homophone in 周伯通 introduction scene), 螞蟻尚且偷生 → chi has 螞蟻尚且偷生 ("even an ant clings to life", sub 69 — yue witness 劉毅都上車偷生 is garbled but chi's phrasing is standard classical), 間王爺 → 閻王爺 (sub 28, chi OCR), 章祖師 → 望祖師爺 (sub 48, chi OCR of the invocation), 希彰 → 希望 (sub 50), 品陽先生 → 歐陽先生 (sub 327, chi OCR with 品/歐 visual confusion — novel variant), 空心拳 → 空明拳 (subs 268, 269 — chi has 空心拳 but canonical 周伯通 term is 空明拳 per STYLE §8 / extras_baseline; chi drift, not OCR; stable canonical form used in overrides), 蓋世奇書 vs 曠世奇書 (sub 282 — chi has 蓋世 but yue has 曠世; both are valid four-character forms meaning "world-beating book", rendered as 蓋世奇書 per chi). Promotion flags: **`洪Seven Elder` cross-stage trap fired twice in-episode** (subs 341, 348) — already resolved by `cjk_fix_v2.py` under v10; pattern remains stable. **`周伯通大哥` compound** — Ep33 sub 268 needed hybrid to use bare 周伯通 instead of 周伯通大哥 to avoid cross-stage trap (大哥→Big Brother at titles stage 3 eats the compound). Candidate for `cjk_fix_v2.py` `shared_concat_fixes` if 周伯通大哥 fires in a future episode: `Zau Baak-tungBig Brother → Brother Zau Baak-tung` / `Jau Baak-tungBig Brother → Brother Jau Baak-tung`. **`19th-generation 幫主` adjectival-concat awkward in romanised** — produces "19th-generation the Chief" because 幫主 converts to "the Chief" via titles stage. Worked around by rewriting hybrid to "19th-generation leader of our 丐幫" using the "leader" English form for the descriptor role. Not yet worth a cjk_fix_v2 entry; flag for observation. **`泰山北斗 + 武林` duplicate** — 泰山北斗 converts to "the authority of the martial world" and 武林 converts to "the martial world"; when they appear in the same phrase they produce "of the martial world of the martial world" duplicate. Worked around by dropping 武林 from hybrid sub 356. Candidate for a structural fix: either revise 泰山北斗's rendering to "the Mount Tai and Northern Dipper" (STYLE §10 alternative gloss) to avoid the duplicate, or enshrine the workaround in STYLE §8. **`碎屍萬段 — torn-you-into-ten-thousand-pieces` duplicate-gloss collapser miss** (sub 82) — collapser's 70% Jaccard threshold misses this because of stopword asymmetry ("yet", "you into" on one side); post-cleaned via targeted sed in this session. Similar pattern-class to Ep24's three post-cleaned duplicates (後會有期, 忘恩負義, 視日無多). **Outcome: FULL** — every sub examined against chi and yue, 376 overrides applied (100% coverage), SRTs validated (zero CJK in romanised, zero banned terms, zero overlaps, chi-spine 376 entry count matches source). Two post-build sed cleanups: sub 82 dup-gloss (above) and the 洪Seven Elder known pattern handled by automation. |

### Pending — Needs FULL Processing

Prior-session FULL outputs below predate the current rule-set and are retained as content previews only; they do not count as established precedent.

**Subcount note (v16).** The `Subs` column in the Pending table is an **eng-derived approximation** — taken from the uploaded `{N}-eng.csv` or prior-session notes, not from the actual chi-spine alignment the current pipeline produces. The chi-spine count (`pipeline.py`'s output) is typically 5–15% *smaller* than the eng count because chi-spine alignment collapses reflowed eng entries onto their chi parents. Treat Pending-row subcounts as rough sizing hints for Step 0 context-budget estimation; the authoritative count is whatever `pipeline.py` reports at Step 1. Ep1 was a clean example: the Pending row said 446 (eng-derived); the actual chi-spine count was 438.

| Episode | Subs (approx) | Status / Content Preview |
|---------|---------------|--------------------------|
| 3–14 | — | Not yet processed. |
| 15 | 464 | Prior-session FULL. 楊康 identity crisis + 包惜弱 letter + 穆念慈 + 黃蓉 vs 七怪 + 歐陽克. |
| 16 | 452 | Prior-session FULL. 梅超風 ambush + 黃蓉/郭靖 reconciliation + 穆念慈/包惜弱 revelation + 楊康 武穆遺書 + rescue plan. |
| 17 | 409 | Prior-session FULL. 楊康/包惜弱 escape + boat betrayal + 段天德 confession + 穆念慈 fireball. |
| 18 | 515 | Prior-session FULL. 包惜弱 poison wine / suicide / nun + 丘處機 captures 楊康 + 九陰白骨爪 trail + family reunion. |
| 19 | 490 | Prior-session FULL. 楊康 final betrayal + 楊鐵心 suicide (滿江紅) + 包惜弱 death + 全真教 / 丘處機 internal-skills duel + 問世間情為何物. |
| 26 | 471 | Prior-session FULL. 歸雲莊 confrontation + 陸乘風 disciple reveal + 念慈/楊康 prison + 歐陽克/穆姑娘 + 裘千仞 false 黃藥師-death claim + 江南七怪 + 梅超風/陸乘風 grief reckoning (老賊). |
| 27 | — | Likely 陸乘風 manor aftermath + 歐陽克 scheming + 桃花島 connections. Uploaded with Ep26/28 but deferred. |
| 34–54 | — | Prior-session mechanical output only — quality below current FULL standard. Re-process. |
| 55–59 | — | Not yet processed. |


---

## Watch List — Names/Terms/Oddities

Items encountered during processing that future sessions should keep an eye on. Promote to `STYLE.md` or `REFERENCE.md` once they're settled with a stable rendering.

### 🟡 Single-episode — hold for one more firing

Items with only one FULL firing. Promote to consolidated docs after the next firing confirms the rendering.

- **Ep1 single-firings:**
  - **滿江紅 quatrain** (Ep1 subs 48–53, 74–75, 227–230: 靖康恥猶未雪 / 臣子恨何時滅 / 駕長車踏破賀蘭山缺 / 壯志飢餐胡虜肉 / 笑談渴飲匈奴血 / 待從頭收拾舊山河 / 朝天闕) — 岳飛's poem, 郭嘯天/楊鐵心 chant it three times. Same classical-verse rendering format as Ep20 題臨安邸 quatrain / Ep22 Dragon-chant / Ep28 天蓋高 / Ep31 李白 將進酒 / Ep33 短歌行. Promote to `STYLE.md` §10 "Classical laments / elegiac verse" on next firing if 岳飛 verses recur (likely in 武穆遺書 arcs — Ep15, Ep20 onward).
  - **題臨安邸 compressed form** (Ep1 sub 7: 暖風薰得遊人醉 / 直把杭州作汴州) — Ep20 firing was the full quatrain (山外青山樓外樓 / 西湖歌舞幾時休 / 暖風薰得遊人醉 / 直把杭州作汴州). Ep1 has the final two lines only, compressed into one sub. Two-episode confirmation → **promote to `STYLE.md` §10** "Classical laments / elegiac verse" subsection.
  - **顏烈 (完顏洪烈's disguise alias)** (Ep1 sub 344; Ep2 sub 222) — first on-screen cover identity before the 楊康 adoption arc. **Two-episode confirmation — promote to `STYLE.md` §5 / `PersonalNamesUpdated.csv` on next session.** Rendering: Ngaan Lit (jy) / Ngaahn Liht (yl). Note: Ep1 sub 344 chi has 阿鰲 which is an OCR artefact of 顏烈, not a separate alias (Ep2 sub 222 "我的名字不是叫顏烈" is the witness).
  - **金閻旭 (Jin soldier name)** (Ep1 sub 38) — chi form; yue ASR renders 金吉玉 — Rule B territory, chi wins. Minor character, likely one-off.
  - **張老爹 concat trap** (Ep1 sub 259) — **confirmed firing of `<surname>老爹 + 爹→Father` trap family (same v13 `<titles-key>+<suffix>` pattern as 我爹/你爹)**. Added to `cjk_fix_v2.py` `shared_concat_fixes` this session as `張老Father → Old Zoeng` (jy) / `Old Jeung` (yl). Watch for 王老爹, 李老爹, etc. in later episodes — same family, same fix pattern.
  - **六王爺 concat trap** (Ep1 subs 43, 132) — `王爺→Your Highness` titles stage eats the compound. Added to `cjk_fix_v2.py` `shared_concat_fixes` as `六Your Highness → the Sixth Prince`. This is 完顏洪烈's initial address form; will recur in every Jin-court scene until 楊康 adoption.
  - **娘子 concat trap** (Ep1 sub 149) — `娘→Mother` titles stage eats 娘子. Added to `shared_concat_fixes` as `My Mother子 → my wife`. The 娘 titles entry is already a known compound-eating hazard (STYLE §19 family); 娘子 is one more victim.
  - **官字兩個口 concat trap** (Ep1 sub 276) — classical proverb "the official's mouth speaks both ways". `兩→taels` from baseline eats the 兩 in the middle, producing `官字taels個口`. Added to `shared_concat_fixes` as targeted fix. Proverb may recur in any court/prefecture-arc context.
  - **道長 / 真人 / 貧道 / 道爺 / 道士 (Taoist address cluster)** — fired Ep1 (throughout 丘處機 scenes) and Ep2 (throughout 丘處機 confrontation and 包惜弱 denouncement, subs 74+, 95–105, 142–172, 354–386). Two-episode confirmation reached. **PROMOTE to `extras_baseline.json`** on next bundle bump. Will recur in every 全真教 / 馬鈺 / 王重陽 / 丘處機 scene across the series.
  - **大俠 (general honorific)** — fired Ep1 sub 125 and Ep2 (柯大俠 at subs 146, 158, 162, 165). Two-episode confirmation. **PROMOTE to `extras_baseline.json`** on next bundle bump.
  - **賢侄 / 賢侄女 / 文定** (Ep1 subs 164, 178) — betrothal-ceremony vocabulary. 賢侄 likely recurs wherever adults address friends' children formally; 文定 is the specific betrothal-rite term. Single-firing.
  - **希彰 / 希芯 → 希望 chi-OCR** — fired Ep1 (subs 321, 322) and Ep2 (subs 254, 322). Two-episode confirmation reached this session. **PROMOTE to `cjk_fix_v2.py` `OCR_NAME_COLLAPSE`** (`希章 → 希望`, `希彰 → 希望`, `希芯 → 希望`) on next bundle bump.
  - **汪梁→汴梁 chi-OCR** (Ep1 sub 16) — novel 汪/汴 visual-confusion variant. Same-family as Ep20's 土紅樓/犁紅樓/悍紅樓/幫紅樓→翠紅樓 family. Watch for more 汪→汴 drift.
  - **韓宰相 / 宰相府 / 宰相 (court-politics vocabulary)** — first FULL firing of the Southern Song prime minister's household. Will recur in any 武穆遺書 / 楊康-at-Jin-court / 完顏洪烈 mission arc.

- **Ep2 single-firings:**
  - **焦木 / 焦木大師 / 焦大師 → Ziu Muk / Jiu Muhk** (Ep2 subs 74–84, 126–131, 159) — abbot of 法華寺 who brokered the 江南七怪 wager. Killed by 丘處機 by mistake in the same episode; referenced later only as "焦木大師's death" in 18-year-wager context. Plot-important one-episode-only character. Single-firing.
  - **七怪 sibling-order vocatives (大哥 / 二哥 / 三弟 / 四弟 / 五弟 / 六弟 / 七妹 / 五哥)** — first FULL-processed 江南七怪 training scene uses all sibling forms (subs 26–52). Will recur in every 七怪 scene across the series. **Two-episode confirmation candidate — promote to `extras_baseline.json` after next firing** (probably Ep3+).
  - **江南七俠 vs 江南七怪** (Ep2 sub 93) — chi uses the honoured form 七俠 in 焦木's formal introduction. The rest of the series uses 七怪. Both canonical. Single-firing of 七俠; rendering "the Seven Heroes of Jiangnan" vs 七怪 "the Seven Freaks of Jiangnan".
  - **哲別 → Zit-Bit / Jit-Bit** (Ep2 sub 393 first firing) — Jebe, Mongol general, future 郭靖 archery teacher. CSV has the rendering. Will recur heavily in Ep3+ as 郭靖's Mongolia arc begins.
  - **燕京 → Jin-ging / Yin-ging** (Ep2 subs 251, throughout the 完顏洪烈 courtship scenes) — Jin capital. Will recur in every Jin-court arc.
  - **法華寺 → Fat-faa Monastery / Faat-wah Monastery** (Ep2 sub 129) — the monastery 丘處機 charges into, killing 焦木. Plot-important only this episode; referenced later only by implication.
  - **金必達 → Gam Bit-daat / Gam Bit-daaht** (Ep2 sub 291) — 完顏洪烈's servant who picks 楊康's wet-nurse. Minor; likely one-off.
  - **韓丞相 → Chancellor Hon / Chancellor Hohn** (Ep2 sub 311) — 完顏洪烈 writes a letter to 韓丞相 for 包惜弱's safe passage. Distinct rendering from Ep1's 韓宰相 (same character, 宰相 vs 丞相 both refer to the prime-minister office; 丞相 is the formal 宋 rank). Two-firing across Ep1 and Ep2 — **watch for a third confirming firing**, then decide: consolidate under one rendering or keep both.
  - **飛天蝙蝠 / 妙手書生 / 馬王神 / 南山樵子 / 笑彌陀 / 鬧市隱俠 / 越女劍 (七怪 formal nicknames)** (Ep2 subs 86–92) — single-scene roll-call in 焦木's introduction. These formal nicknames likely recur only sporadically; the seven are usually referenced by rank (大哥 etc.) or bare name. Single-firing; hold for recurrence.
  - **醉仙樓 → Zeoi-sin Tower / Jeui-sin Tower** (Ep2 subs 69–73, 174, 206) — the inn where the 18-year wager is set and will be resolved. Named but not re-visited in Ep2; will recur at Ep15+ (wager resolution). Single-firing this session (Ep1 referenced it but 醉仙樓 itself first appears here).
  - **Ep2 chi-OCR variants** (catalogue): **楊公子→顏公子** (subs 2, 7 — novel 楊/顏 visual-confusion; promote to `OCR_NAME_COLLAPSE` if pattern recurs); **段正德→段天德** (sub 99, yue witness); **錫頭→鋤頭** (sub 267 — second firing of this family after Ep1 sub 258; **candidate for OCR_NAME_COLLAPSE on third firing**); **希章→希望** (subs 254, 322 — already being promoted this session, see above); **無理取同→無理取鬧** (sub 126, 同/鬧 visual); **路人和皆知→路人皆知** (sub 19 — 和 OCR injection); **大宋指紋→大宋子民** (sub 247 yue ASR, 紋/民 homophone `man4`); **景意→聲望** (sub 147); **打爛了大甸→大鐘** (sub 129 chi 甸/鐘); **我國侵末→金國侵宋** (sub 238 chi OCR); **不知道是誰放肆→不知道哪個大膽** register-drift (sub 18 yue vs chi); **量有此理→豈有此理** did not fire this episode.
  - **18-year wager structural event** — Ep2 subs 198–206 establish the named structural event that Ep15+ episodes reference back to. Cross-episode precedent anchor.
  - **小康 vs 康仔** (Ep2 sub 323) — chi 小康, yue 康仔. 丘處機 names the child at sub 380 as 小康. Hybrid uses 小康 (written form / chi-canonical); yue's 康仔 is the Cantonese diminutive as actually spoken. Same referent as 康兒 in baseline (康兒 is 包惜弱's address form; 小康 is 丘處機's naming; 康仔 is the spoken Cantonese). Single-episode observation.
  - **小靖 vs 阿靖** (Ep2 subs 388, 389) — 李萍 addresses young 郭靖 as 小靖 in the Mongolia-memory scene (not yet the 阿靖 vocative that's baseline). First firing. 小靖 is a young-child diminutive; 阿靖 is the general vocative used across the series. Watch for 小靖 recurrence in Ep3+ child-arc scenes before deciding to catalogue.
  - **楚河漢界 → the River Cou and the Han line / the River Cho and the Han line** (Ep2 sub 16) — classical 象棋 boundary idiom, used as street-bluster metaphor. Dictionary 四字成語. Single-firing; promote to STYLE §10 on next firing.
  - **富至四方 / 豪縱四海** (Ep2 sub 23) — bluster variant, NOT dictionary 四字成語 (per admission-gate review). Rendered English. If it recurs in different chi/yue wording it's a one-off stylistic phrase; if the same wording recurs, re-examine.
  - **取於民, 還於民** (Ep2 sub 25) — Robin-Hood proverb fragment, not a dictionary 四字成語. Rendered English per admission gate. Classical-sounding but the English renders as plain descriptive prose.
  - **一日之恩, 永世難忘** (Ep2 sub 260) — classical kindness-debt proverb; paired with 耿耿於懷 in the same sub. Dictionary-idiom compound. Single-firing; promote to STYLE §10 on next firing.

- **Ep2 concat-trap promotions (audit required):**
  - **`六Your Highness → the Sixth Prince`** — Ep1 row claimed this was "added to `cjk_fix_v2.py` `shared_concat_fixes` this session" but the v16 bundle's `cjk_fix_v2.py` does **not** contain the entry. Ep2 fired it again (subs 106, 223) and required manual post-build fix. **Audit all four Ep1 concat-trap promotions against current `cjk_fix_v2.py` source**: `六Your Highness → the Sixth Prince`, `My Mother子 → my wife`, `張老Father → Old Zoeng` (jy) / `Old Jeung` (yl), `官字taels個口 → the official's mouth speaks both ways`. If any are missing, add to `cjk_fix_v2.py` in the next bundle.
  - **`little 叔` bare-CJK leak** (Ep2 sub 405) — "大叔...小叔" adjacency where 大叔 converts via overlay-longest-first (matches 大叔 before the bare-小叔 extras entry fires), stranding 小叔 → bare 叔 after 小 converts. Registered `小叔 → little uncle` in overlay but the within-stage sort still matched `大叔` first in this context. Manual post-build fix applied. Single-episode observation; promote `little 叔 → little uncle` to `cjk_fix_v2.py` `shared_concat_fixes` only if pattern recurs.


- **Ep24 single-firings:**
  - **網康→阿康 chi-OCR variant** (Ep24 subs 318, 332) — new visual-confusion OCR (網/阿). Promote to `cjk_fix_v2.py` `OCR_NAME_COLLAPSE` on next firing.
  - **燕尾甲→軟蝟甲 yue-ASR variant** (Ep24 subs 82, 85, 88) — yue-Whisper form of 軟蝟甲. Chi has the canonical 軟蝟甲; yue persistently renders 燕尾甲 across three sequential subs. Single-episode Rule B observation; promote if it fires again.
  - **華珍→華箏 yue-ASR homophone** (Ep24 sub 52, also light drift across 蓉兒's drunken scene) — `zing1/zan1` pair. Rule B territory.
  - **九寶→小二 / 我姑娘→黃姑娘 yue-ASR variants** (Ep24 subs 56, 94) — waiter-call and 蓉兒 address-term homophones; not cataloguable as a systematic pattern yet.
  - **拖泥帶水 first FULL firing** (Ep24 sub 68) — 黃藥師 rebuking 歐陽克 to "stop being wishy-washy" before the departure scene. Baseline had this already; first on-screen firing confirms.
  - **Duplicate-gloss collapser misses on short-phrase idioms** — Ep24 subs 141 (`後會有期 — we'll meet again`), 291 (`忘恩負義 — ungrateful`), 320 (`視日無多 — my days are few`) all produced `ENGLISH — ENGLISH` duplicates in romanised after build.py's CJK→English conversion. `cjk_fix_v2.py`'s collapser has a 8-char-per-side minimum that misses these. Post-cleaned manually. **Candidate for cjk_fix_v2.py threshold lowering** to ~5 chars, OR for idiom-specific collapse entries for the short-rendering 四字成語 family (後會有期, 忘恩負義, 視日無多, 事到如今, 痛改前非 all render in ≤20 chars). Watch for more firings across Ep25/26 first — if the pattern persists, lower the threshold; if it's stable at these five, add specific collapse entries.

- **Ep20 single-firings:**
  - **岳王廟 → the Ngok Wong Temple / Ngohk Wong Temple** (Ep20 subs 26, 117, 135) — 岳飛 (岳武穆) temple in 臨安. Will recur wherever 岳飛 / 武穆遺書 arcs do.
  - **岳王爺 → Lord Ngok / Lord Ngohk** (Ep20, 18+ firings) — 岳飛 the historical figure. **Cross-stage trap:** 王爺→Your Highness (titles) eats 岳王爺 before extras fire. Fixed ad-hoc post-build in Ep20 via `岳Your Highness → Lord Ngok/Ngohk`. Promote to `cjk_fix_v2.py` `shared_concat_fixes` on next firing.
  - **武穆遺書 → the Book of Mou Muk / Mouh Muhk** (Ep20, 10+ firings; Ep21 also fires via 拖雷's 藏經閣 theft) — 岳飛's prison-written military manuscript. Already has two episodes of evidence after Ep20 — promote to `extras_baseline.json` this session.
  - **岳文 → Ngok-man / Ngohk-mahn** (Ep20 subs 115, 215, 227, 346; gravemarker visible) — **a real character**, genuine descendant of 岳飛, master of the house the 武穆遺書 plot orbits; killed by 歐陽克's snake mid-episode. Plot-important minor character; recurs only by reference via 武穆遺書 in later episodes.
  - **岳老伯 → Uncle Ngok / Uncle Ngohk** (Ep20, 15+ firings) — 郭靖's polite form of address for the elder 岳文. Kinship-form address pattern.
  - **岳大叔 → Uncle Ngok / Uncle Ngohk** (Ep20 sub 189) — 蓉兒's equivalent. Same referent (岳文).
  - **碧玉富貴燈 → the Jade Fortune Lantern** (Ep20 sub 102) — lantern-shop exchange.
  - **翠紅樓 → the Ceoi-hung Brothel / Cheui-hung Brothel** (Ep20, 5 firings) — brothel 洪七公 falsely claims to have given the 書 to.
  - **獅子林 → Si-zi Forest / Sih-ji Forest** (Ep20 sub 584) — where 歐陽克 claims 郭靖 is dying.
  - **山神廟 → the Local God Temple** (Ep20 sub 355).
  - **林升 "題臨安邸" quatrain** (Ep20 subs 112–115 and 154–157: 山外青山樓外樓 / 西湖歌舞幾時休 / 春風吹得遊人醉 / 直把杭州作汴州) — Southern Song political complaint verse; same classical-verse rendering format as Ep22 Dragon-chant, Ep28 天蓋高, Ep31 李白 將進酒. Catalogue under `STYLE.md` §10 "Classical laments / elegiac verse" after next firing.
  - **Five Greats framework explicitly named in one scene** (Ep20 subs 535–538) — 東邪 / 西毒 / 南帝 / 北丐 together; 歐陽克 refers to 歐陽鋒 as "my 叔叔". First FULL-processed such scene. Already in `REFERENCE.md` §3 framework.
  - **精忠報國 → utter loyalty to the nation** (Ep20 sub 132).
  - **醉生夢死 → drunkards dreaming through life** (Ep20 sub 127).
  - **風流快活 → lose themselves in pleasure** (Ep20 sub 135).
  - **亡國奴 → slaves of a conquered nation** (Ep20 sub 143).
  - **半壁江山 → half the empire** (Ep20 sub 140).
  - **用兵如神 → a master of strategy** (Ep20 sub 252).
  - **行軍佈陣 / 練兵攻城 → marching and formations / training troops and besieging cities** (Ep20 sub 250).
  - **安邦定國 / 雄霸天下 → pacify the realm and steady the state / rule the world** (Ep20 sub 254).
  - **居功至偉 → the greatest merit** (Ep20 sub 262).
  - **財源廣進 → bring you prosperity** (Ep20 sub 103).
  - **狗眼看人低 → looking down with dog's eyes** (Ep20 sub 110).
  - **皇天不負有心人 → Heaven does not fail the earnest** (Ep20 sub 372).
  - **各安天命 → leave it to fate** (Ep20 sub 527).
  - **鬼哭狼嚎 → wailing like ghosts and wolves** (Ep20 sub 289, 500).
  - **血性 → spirit** (Ep20 subs 134, 161).
  - **劉兄** (Ep20 sub 148) — unnamed minor character at 岳王廟; probably not recurring.
  - **簡長老 → Elder Gaan** (Ep20 sub 226) — 丐幫 elder dispatched alongside 彭長老.
  - **麻瘋病 → leprosy** (Ep20 subs 85, 88) — 蓉兒's cover story using stolen rags.
  - **公子 cover for 小王爺** (Ep20 subs 326–329) — 楊康 requires his men to drop 小王爺 for 公子 in 宋國 territory. Already in STYLE §6; flag the context pattern.
  - **本姑娘 → this girl** (Ep20, 3 firings). **Cross-stage trap:** 娘→Mother (titles) eats 本姑娘 before extras. Same structural fix as 岳王爺. Promote to `cjk_fix_v2.py` `shared_concat_fixes` on next firing.
  - **First on-screen 降龍十八掌** — Ep20 (against 沙通天), not Ep21 as previously logged. Ep21 is 洪七公's second use (against 梁子翁, to save 郭靖).
  - **Ep20 chi-OCR additions to the v13 long-tail list** (`REFERENCE.md` §1 candidate on second firing): 匡文/策老伯/品王爺 for 岳文/岳老伯/岳王爺; 黃大叔 (sub 189) and 牛老伯 (subs 290+) mid-scene drift for 岳大叔/岳老伯 — the chi track loses consistency for the old man's name after his death; 土紅樓/犁紅樓/悍紅樓/幫紅樓 for 翠紅樓 (four variants!); 葵古/划古 for 蒙古; 梁子峰/梁子忠 for 梁子翁 (second episode — Ep21 had 梁子仍). Confirms 量有此理 → 豈有此理 (fifth FULL ep: Ep20, Ep21, Ep30, Ep31, Ep32 — already in v13 OCR_NAME_COLLAPSE).
- **Ep25 single-firings:**
  - **羞花亭 → the Sau-faa Pavilion / Sau-fa Pavilion** (Ep25 subs 86, 97) — where 穆念慈 waits for 楊康's answer. Location minor, scene-limited.
  - **千年蔘王 → the Thousand-Year Ginseng King** (Ep25 subs 177, 178, 205) — the rare remedy 蓉兒 proposes to fetch for 七公 to force him to speak to 黃藥師. Likely referenced again in later episodes or replaced by other medicinal MacGuffin.
  - **大衍數 step-names at 歸雲莊** (Ep25 subs 407–415: 零 / 地三 / 頤王 / 起 / 伏 / 定 / 已 / 和) — 黃�eld-specific layout copied by 陸乘風 at 歸雲莊's forbidden small pavilion. 頤王 was not in baseline and had to be post-build-sed'd to `Yi-wong` / `Yih-wohng`. Will recur at Ep26's 歸雲莊 confrontation; candidate for baseline promotion once rendering is confirmed there.
  - **程耀宗 → Cing Jiu-zung / Ching Yiu-jung** (Ep25 sub 302) — 程家's second-round winner. Minor named character.
  - **何樂而不為 → why not?** (already in baseline) — first FULL firing in 蓉兒's "I make a scene and save a meal's worth" scam justification.
  - **遵命 → "Yes, sir"** (Ep25 sub 374) — 陸乘風's servant 阿雲 acknowledges order to beat 冠英. Post-build-sed'd; candidate for `extras_baseline.json` if it fires again.
  - **本姑娘 cross-stage trap fired second time** (Ep20, Ep25) — `本姑Mother` concat produced at Ep25 subs 285, 286. **PROMOTE to `cjk_fix_v2.py` `shared_concat_fixes`** on next session: `本姑Mother → this girl`. Ep20 flagged this already — Ep25 confirms.
  - **程耀宗 / 程大小姐 / 陸少爺 / 方掌櫃** — innkeeper name, Master Fong. Likely one-off (Innkeeper scene only).
  - **推宮換血 non-martial-teacher firing** — 念慈 performs it on 楊康 (not a healer teacher sacrificing for disciple). First time we see the technique in a romantic-sacrifice context. Ep24's Rule-B case study is still the reference.
  - **奸夫淫婦 → illicit lovers** (Ep25 subs 209, 309) — appears twice: first as 蓉兒's mockery of the 冠英/瑤迦 affair, then in the 比武 scene as public accusation. Single-episode stable rendering.
  - **黑鍋 → blame** (Ep25 sub 331) — rendered in English per §7 (common-noun rule). Not cataloguable as 四字成語.
  - **姓陸的 / 陸家 / 程家 / 程陸** — family-address patterns in a 比武 scandal scene. 陸家 / 程家 / 程陸 already in baseline; 姓陸的 single-episode vocative.
  - **和伯伽→瑤迦 OCR pattern** — promote to `cjk_fix_v2.py` `OCR_NAME_COLLAPSE` on next firing.
- **Ep21 single-firings:**
  - **梁子翁** — bare surname **子翁** (`Zi-jung / Ji-yung`) rendering. 梁子翁 itself already in `PersonalNamesUpdated.csv`.
  - **彭長老 → Elder Paang / Elder Pahng** (Ep21 subs 43–45).
  - **鄂州 / 鄭州 / 天香樓** — Rendered `Ngok-zau/Ngohk-jau`, `Zeng-zau/Jehng-jau`, `Tin-hoeng Tower/Tin-heung Tower`.
  - **樞密院 → the Privy Council / 藏經閣 → the Scripture Pavilion / 禁宮 → the Forbidden Palace / 禁軍 → the palace guard** — 宋 imperial institutions; will recur in 武穆遺書 arc.
  - **七仔 → Cat-zai / Chat-jai** (Ep21 subs 82, 87, 487) — 洪七公's self-naming. Per `STYLE.md` §5, NOT a general substitute for 洪七公.
  - **百花雞 / 釀鴨舌 / 清蒸活鯉魚 / 珍珠魚眼羹 / 龍虎鳳會石斑** — 蓉兒 seduction menu; 龍虎鳳 explainer (龍=百花蛇, 虎=果子狸, 鳳=竹絲雞).
  - **成事不足敗事有餘 → all damage, no use** (Ep21 sub 116).
  - **後患無窮 → endless trouble** (Ep21 sub 365).
  - **蠻不講理 → unreasonable** (Ep21 subs 200, 208).
  - **尊師重道 → respect for one's 師父** (Ep21 sub 233).
  - **群龍無首 → a leaderless sect** (Ep21 sub 42).
- **Ep22 single-firings:**
  - **沙通天 → Saa Tung-tin / Sa Tung-tin** — minor antagonist, recurs.
  - **彭連虎 → Pang Lin-fu / Pahng Lihn-fu** — 彭寨主 family recurs.
  - **降龍有悔 → Dragon Regrets / 躍龍在淵 → Leaping Dragon in the Abyss** (Ep22 subs 301, 324).
- **Ep30 terms** (積翠亭, 梅花樁, 碧海潮生曲, 文鬥, 奇門八卦 family, 神龍擺尾) — all in `STYLE.md` §8; single-episode. Ep31 did not fire any; still single-episode.
- **婦人之仁** — `STYLE.md` §10 has "a woman's soft-heartedness"; Ep30 sub 327 used "a soft heart" via em-dash gloss. Both valid; flag for consistency.
- **Ep31 single-firings:**
  - **一陽指 → the Single Yang Finger** (Ep31 subs 300, 323).
  - **華山論劍 → the Huashan duel** (Ep31 subs 258, 319).
  - **王重陽 → Wong Cung-joeng (jy) / Wong Chuhng-yeuhng (yl)**; **重陽真人 → Master Cung-joeng / Chuhng-yeuhng**.
  - **激將法 → provocation ploy** (Ep31 sub 340).
  - **過目不忘 → photographic memory** (Ep31 subs 358, 363).
  - **玉石俱焚 → destroy them all, jade and stone alike** (Ep31 sub 299).
  - **雞鳴狗盜 → petty thievery** (Ep31 sub 324).
  - **水能載舟亦能覆舟 → water bears the boat and can also capsize it** (Ep31 sub 291).
  - **李白 將進酒 couplet** (君不見高堂明鏡悲白髮 / 朝如青絲暮如雪) at Ep31 subs 233–234 — same pattern as Ep28 陸乘風 lament.
  - **圓寂 → passing** (Ep31 sub 293).
  - **陽壽已盡 → mortal years are spent** (Ep31 sub 277).
  - **冰窒 → ice chamber** (Ep31 sub 407).
  - **夫復何言 → what more can be said** (Ep31 sub 21).
  - **女大不中留 → a grown daughter cannot be kept** (Ep31 sub 39).
  - **入土為安 → laid to rest in the earth** (Ep31 sub 418).
  - **起死回生 → bring her back to life** (Ep31 sub 408).
- **Ep32 single-firings:**
  - **百步穿腸 → bowel-piercing within a hundred paces** (Ep32 sub 353).
  - **蛇杖 → snake staff** (Ep32 sub 355).
  - **鋼刺 → steel spike** (Ep32 sub 311).
  - **一代宗師 → a master of a generation** (Ep32 sub 29).
  - **狼心狗肺 → wolf-hearted, dog-lunged** (Ep32 sub 296).
  - **七孔流血 → bleed from every orifice** (Ep32 sub 218).
  - **易如反掌 → easy as flipping a palm** (Ep32 sub 346).
  - **死無葬身之地 → die without a place of burial** (Ep32 sub 348).
  - **好生之德 → Heaven values life** (Ep32 sub 382).
  - **不識抬舉 → does not know a favour** (Ep32 sub 383).
  - **恩將仇報 → return kindness with enmity** (Ep32 sub 292).
  - **死有餘辜 → deserves worse than death** (Ep32 sub 280).
  - **自作孽不可活 → the harm one brings upon oneself** (Ep32 sub 256).
  - **言出必行 → I keep my word** (Ep32 sub 240).
  - **願賭服輸 → a bet is a bet** (Ep32 sub 129).
  - **郭大俠 / 周大俠** (Ep32 sub 172) → Hero Gwok / Hero Jau.
  - **百毒攻心** (Ep32 sub 218) — used inline ("a hundred poisons ravage his heart").
  - **六個時辰 → six shichen (twelve hours)** (Ep32 sub 231) — Ep32 hybrid used `six shichen (twelve hours)` gloss; romanised used `six shichen` alone. May need a fixed convention; see also the 時辰 promotion below.
- **Ep33 single-firings:**
  - **蓋世奇書 → a book without equal in the world** (Ep33 sub 282) — 郭靖's awe at 九陰真經.
  - **千秋大業 → our great enterprise** (Ep33 sub 350) — 楊康's phrasing for the Jin imperial plan. Likely to recur as a 完顏洪烈/楊康 register marker.
  - **斷腳之仇 → the grudge of my broken legs** (Ep33 sub 307) — 歐陽克's revenge vow drilled into him by 歐陽峰. Recurs as a plot-driver phrase.
  - **塞外高人 → masters from beyond the frontier** (Ep33 sub 368) — 楊康 excusing 歐陽峰's rudeness to 完顏洪烈. Register marker for Jin-court formalities.
  - **遠水救不了近火 → water from afar cannot quench a fire nearby** (Ep33 sub 260) — 洪七公's standard 俗語. May recur.
  - **天作孽猶可恕, 自作孽不可活** (Ep33 sub 122) — 歐陽克's self-curse after begging 蓉兒. Classical doubled-clause idiom.
  - **素仰先生 → I have long admired you** (Ep33 subs 327, 356) — 完顏洪烈's courtly opener to 歐陽峰. Recurs in formal introductions.
  - **沖天炮 → sky-bursting cannon** (Ep33 sub 371) — named Jin-arsenal weapon shipped to 燕京. Plot-driver object for later episodes.
  - **燕京 → Yanjing** (Ep33 sub 371) — Jin capital. Recurs in later Jin-court arcs.
  - **品陽先生 → 歐陽先生 chi-OCR variant** (Ep33 sub 327) — novel 品/歐 visual confusion. First firing; promote to `cjk_fix_v2.py` `OCR_NAME_COLLAPSE` on next firing.
  - **Ep33 chi-OCR long-tail**: 痢下→閣下 (sub 12, homophone drift in 周伯通 intro); 間王爺→閻王爺 (sub 28, chi OCR); 章祖師→望祖師爺 (sub 48); 希彰→希望 (sub 50); 歐陽蜂→歐陽峰 (continuing v13 pattern, 3 firings this ep). All single-ep; watch for second firings.
  - **空心拳 vs 空明拳** (Ep33 subs 268, 269) — chi has 空心拳 but canonical 周伯通 term is 空明拳 (STYLE §8 / extras_baseline). Chi drift, not OCR; override to 空明拳. Watch for similar drift.
  - **Ep33 four-character idiom cluster** — 粉身碎骨, 如花似玉, 碎屍萬段, 約法三章, 一代宗師, 千秋大業, 恩將仇報, 暗箭傷人, 斷腳之仇, 易如反掌, 血肉之軀, 綽綽有餘, 有志者事竟成, 死有餘辜, 斯文有禮 — all single-firing. Per §10, these are legitimate CJK-in-hybrid entries; promote on second firing.

### 🟡 Cross-stage concat traps — Ep33 observations (still pending)

- **`周伯通大哥 → Zau Baak-tungBig Brother` cross-stage trap** (Ep33 sub 268 observation only — worked around by rewriting hybrid to bare 周伯通) — `大哥→Big Brother` (titles stage 3) fires before extras, leaves the full 周伯通 name with a concatenated "Big Brother". Same structural family as 週大哥 already in `cjk_fix_v2.py`. Fix on next firing: add `Zau Baak-tungBig Brother → Brother Zau Baak-tung` / `Jau Baak-tungBig Brother → Brother Jau Baak-tung` to `cjk_fix_v2.py` `fixes` / `yale_fixes`.
- **`19th-generation 幫主` adjectival-concat trap** (Ep33 subs 49, 53) — `幫主→the Chief` (titles stage 3) in an adjectival/appositional context produces "19th-generation the Chief" which reads ungrammatically. Worked around by rewriting hybrid to use "leader" in English for the descriptor role. Not itself a cross-stage CJK-leak; more a rendering-fit issue. Single observation; flag if the pattern recurs.
- **`泰山北斗 + 武林` duplicate-rendering** (Ep33 sub 356 observation) — `泰山北斗` converts to "the authority of the martial world" and `武林` converts to "the martial world"; when they appear in the same phrase the romanised output duplicates "of the martial world". Worked around by dropping 武林 from the hybrid. Structural fix candidates: (a) revise `泰山北斗`'s English to "the Mount Tai of the Northern Dipper" (STYLE §10 alternative gloss) to drop the "martial world" suffix, or (b) enshrine the workaround pattern in STYLE §8 (don't pair 泰山北斗 with 武林 in the same sub's hybrid).

### 🟡 Duplicate-gloss collapser gaps — pending investigation

- **`碎屍萬段 — torn-you-into-ten-thousand-pieces` miss** (Ep33 sub 82) — `cjk_fix_v2.py`'s collapser fires on >70% Jaccard overlap, but stopword asymmetry ("yet", "you into" on one side vs "to" on the other) drops the effective overlap below 70%. Post-cleaned via targeted sed. Same family as the Ep24 misses (後會有期, 忘恩負義, 視日無多). **Two-episode pattern now confirmed** (Ep24 + Ep33) — **candidate for action next session**: either lower the collapser's threshold to ~55%, or add a subset-check that ignores stopwords entirely. The Ep24 entry above has more detail on the specific failing idioms; Ep33 adds 碎屍萬段 to that list.

### 🟡 Stable items ready for promotion (two-episode confirmation)

*(v14 Ep33 session: all previously-listed items in this section have been promoted — see "Promoted under v14" changelog below.)*

### 🟡 Cross-stage concat traps — prior-session observations (still pending)

- **`黃前輩` → `Wongsenior` concat (Ep23 sub 206)** — `前輩→senior` (titles stage 3) fires before extras, leaves bare `黃` which then hits the names stage (surname `黃→Wong`), producing `Wongsenior`. Required post-build `Wongsenior → Senior Wong` fix. First firing; promote to `cjk_fix_v2.py` `shared_concat_fixes` on next firing. Yale form `Wongsenior → Senior Wong` is identical since `黃 → Wong` in both.
- **`死老邪` → `死Old Heretic` concat (Ep23 sub 174)** — `老邪→Old Heretic` (titles stage 3) eats it before extras, leaves bare `死`. STYLE §5 has `死老邪 → damned Old Heretic`; workaround was to render English in hybrid (costs the CJK). Promote to `cjk_fix_v2.py` `shared_concat_fixes` as `死Old Heretic → damned Old Heretic` on next firing so hybrid can keep `死老邪` CJK.
- **我柯鎮惡 / 我裘千仞** — emphatic-self compounds ("I, X"). Ep26 only. Fix when they fire again: add `我{FullName} → I, {FullName}` for top-5 characters.
- **我們 + (non-`the`) compound** — `我們the → our` handles the common case; `我們蒙古` etc would need a separate pattern. Single observation.
- **Compact-idiom + em-dash concats (Ep31).** Bare short idioms (胡說, 還抵賴, 真是有趣) leak as CJK when unregistered. Single-ep observation; decide on policy (baseline register vs. overlay-only) after next firing.
- **克... / 克 bare** (Ep32 sub 275). Single-ep observation; may or may not be generalisable.

### 🟡 Rule B territory (chi wins — informational only, no promotion)

- **歐陽克 Whisper cluster**: 克/赫/黑/客 all `haak1`; 歐陽黑/歐陽客/歐陽鹿 (Ep28), 阿赫/阿黑 (Ep29, Ep30). See `REFERENCE.md` §1 "阿克 Whisper homophone cluster" for the rendered rule.
- **Long-tail chi-OCR variants beyond the v13 collapse table**: 若師兄 / 王老邪 / 蔡洪峰 for 藥師兄 / 黃老邪 / 歐陽峰 (Ep30); 周伯仲 / 白通 / 伯東 variants for 周伯通 (Ep31, Ep32); 梅竹風 for 梅超風 (Ep31); 陳元鳳 for 陳玄風 (Ep31); 旺銅銀 for 王重陽 (Ep31); 准魚 / 徐魚 for 鯊魚, 狡獨 for 狡猾, 無原無故 for 無緣無故 (Ep32). All catalogued in `REFERENCE.md` §1 v13 entry but not yet added to `cjk_fix_v2.py` `OCR_NAME_COLLAPSE`. Promote variant-by-variant when it fires in a second episode.

### 🟢 Promoted under v15 (changelog)

Items promoted under the v15 bundle bump (Ep1 FULL session). **Do not re-register these in episode overlays** — if they leak, the promotion regressed and needs fixing in the consolidated location.

v14 → v15 bump:
- **四concat-trap family from Ep1** → `cjk_fix_v2.py` `shared_concat_fixes` / `yale_concat_fixes`. All four are `<titles-key>+<suffix>` family firings (the v13 structural rule in `STYLE.md` §19):
  - `六Your Highness → the Sixth Prince` (from 六王爺, 王爺 titles stage wins)
  - `My Mother子 → my wife` (from 娘子, 娘 titles stage wins)
  - `張老Father → Old Zoeng` (jy) / `張老Father → Old Jeung` (yl) (from 張老爹, 爹 titles stage wins — same family as 我爹/你爹 from v13)
  - `官字taels個口 → the official's mouth speaks both ways` (from 官字兩個口, 兩→taels baseline stage wins — novel trap, first bare-baseline eating observed)
- **滿江紅 verse rendering established** → first FULL firing of 岳飛's poem. Format established as STYLE §10 Classical-laments pattern. Held at single-firing in Watch List until 武穆遺書 arcs fire the poem again (likely Ep15 onward).
- **Ep1 row in Completed table** — arc label, first-FULL-firing list, chi-OCR variant list, and promotion flags follow the PIPELINE Step 8.5 row-body format.

### 🟢 Promoted under v14 (changelog)

Items promoted during the v14 Ep33 session. The bundle version is not bumped (still v14 — these are content promotions, not script changes). **Do not re-register these in episode overlays** — if they leak, the promotion regressed and needs fixing in the consolidated location.

User-rule clarifications (Ep33 session — now the permanent rule):
- **Generic wuxia vocabulary goes English in hybrid** — 武功 / 武林 / 江湖 / 內力 / 內功 / 輕功 / 功力. Promoted to `STYLE.md` §7 "What does NOT get CJK" (new "Generic wuxia vocabulary" bullet), §8 (table note distinguishing CJK-in-hybrid from English-in-both entries; 武功/武林/江湖 removed from table because they're English-in-both not CJK-in-hybrid→English-in-romanised), §9 "Wuxia terms in hybrid" (rewritten to distinguish named techniques from generic vocabulary), §18 Banned Terms (new hybrid-sweep entry), §21 Anti-Patterns (new item 9). Named techniques (九陰真經, 降龍十八掌, 空明拳, 打狗棒法, etc.) remain CJK.
- **叫化子 banned in hybrid — use Cantonese 乞兒 instead** (or English "beggar"). Promoted to `STYLE.md` §7 Nicknames (老乞兒 replaces 老叫化子 in the canonical list), §18 Banned Terms (new sweep entry), §21 Anti-Patterns (new item 10), `REFERENCE.md` §2 (new "乞兒 vs 叫化子 vs 臭要飯的" entry generalising the prior 臭要飯的 case).
- **Colloquial insult compounds go English in hybrid** — 臭丫頭 / 死丫頭 / 死乞兒 / 臭乞兒 / 王八蛋 / 禁宮. Promoted to `STYLE.md` §7 "What does NOT get CJK" (new "Colloquial insult compounds" bullet with the intensifier+common-noun-insult rule), §18 Banned Terms.
- **Descriptive common-noun metaphors go English in hybrid** — 情蛇, 一流高手, 一流絕頂高手, and the general X+高手/X+高人/X+蛇 pattern where X is an adjective rather than a proper qualifier. The test: strip the CJK and read the English rendering alone — if it works as a plain English noun phrase, it's a descriptor, not an idiom. Promoted to `STYLE.md` §7 "What does NOT get CJK" (new "Descriptive common-noun metaphors that sound idiomatic" bullet with contrast to 塞外高人 / 老毒物 which pass the gate), `STYLE.md` §10 (new admission-gate subsection listing the four criteria for catalogue-worthy idioms), `PIPELINE.md` Step 4 checklist item 10 (new bullet). **Watch List cleanup:** the Ep22 entry for `一流絕頂高手 → a supreme master` deleted — resolved by rule (English in hybrid, so no catalogue entry needed).

Name / title / place rows promoted to `STYLE.md` §5:
- **歐陽先生 → Mister Au-Joeng / Mister Au-Yeung** (Ep29 + Ep33).
- **歐陽公子 → Young Master Au-Joeng / Young Master Au-Yeung** (Ep33 confirms; Ep29 overlay had the form).
- **歐陽叔叔 → Uncle Au-Joeng / Uncle Au-Yeung** (Ep33 confirms; recurs whenever 歐陽克 addresses 歐陽峰 or vice-versa).

Name / title / place rows promoted to `extras_baseline.json`:
- **歐陽先生 / 歐陽公子 / 歐陽叔叔** — baseline entries for the 歐陽 address-term cluster.
- **打狗棒 / 打狗棒法 / 三十六路打狗棒法** — 洪七公's 丐幫-leadership regalia. Recurs throughout the 丐幫 arc (Ep34+ transmission scene, Ep38 canonical training). Also promoted to `STYLE.md` §8 table.
- **易筋鍛骨篇** — named healing chapter of 九陰真經. Also promoted to `STYLE.md` §8 table.
- **空明拳 / 七十二路空明拳** — 周伯通's 武功. 空明拳 was already in `STYLE.md` §7 Terms; promoted to baseline + §8 table for full-form consistency. `七十二路空明拳` is the Ep33-introduced numeric qualifier.
- **老乞兒 / 乞兒** — Cantonese forms (baseline) so the reviewer doesn't need to re-register them in overlays. Renders as "Old Beggar" / "beggar" in romanised.
- **泰山北斗 → the authority of the martial world** (Ep30 + Ep33). `STYLE.md` §10 already catalogued it; promoted to baseline for safety and annotated with the 武林-pairing trap caveat.

Classical couplets promoted to `STYLE.md` §10 "Classical laments / elegiac verse":
- **天長地久, 人生幾何 / 譬如朝露, 去日苦短** (Ep33 subs 173–174) — 黃藥師's lament for the supposedly-dead 蓉兒. From 曹操 短歌行. Format: CJK + em-dash + English gloss on same line. Same format family as Ep28 天蓋高 and Ep31 李白 將進酒.

Pipeline / doc cleanup:
- **`cjk_fix_v2.py` fixes** — `洪Seven Elder → Hung Seven Elder` / `Huhng Seven Elder` remains the working post-build fix for the 洪七公 cross-stage trap. Confirmed Ep33 (subs 341, 348).
- **Ep33 row in Completed table** — the arc label, first-FULL-firing list, chi-OCR variant list, and promotion flags follow the PIPELINE Step 8.5 row-body format.

### 🟢 Promoted under v13 (changelog)

Items promoted under the v13 bundle bump. **Do not re-register these in episode overlays** — if they leak, the promotion regressed and needs fixing in the consolidated location.

v12 → v13 bump:
- **時辰 → sichen** → `extras_baseline.json` (both jy and yl). Confirmed Ep21 (subs 21, 51, 302), Ep22 (subs 374, 391), Ep32 (sub 231). Ep32's `六個時辰 → six shichen (twelve hours)` hybrid-gloss convention remains in Watch List for one more firing.
- **氣聚丹田 → qi gathers at the dantian** → `extras_baseline.json`. Confirmed Ep21 (sub 241), Ep31 flashback, Ep32 (sub 249). Already in `STYLE.md` §10 meditation/qi.
- **內力 → internal force** → `extras_baseline.json`. Confirmed Ep21 (subs 321, 322), Ep22 (subs 320, 321, 342). Already in `STYLE.md` §10.
- **真經 → the Manual** → `extras_baseline.json`. Ep31 flashback repeatedly used bare 真經 without the 九陰 prefix; now covered pre-emptively for future flashback episodes.
- **`<titles-key>+<suffix>` cross-stage trap family** → `cjk_fix_v2.py` `shared_concat_fixes`. Confirmed Ep21 (four regressions from v11 baseline promotions defeated by build.py's stage-3 titles firing):
  - `我Father → my father` / `你Father → your father` (from 我爹/你爹)
  - `the Chief萬福 → Good fortune to the Chief` (from 幫主萬福)
  - `大Jin → the great Jin empire` (from 大金國)
  - `報告the Princess → Your report, Princess` (from 報告公主)
- **Structural rule — `<titles-key>+<suffix>` trap** → `STYLE.md` §19 (new subsection). Generalisable lesson: registering a compound in extras/baseline is insufficient when build.py's titles stage has a shorter-key substring match. Fix must be in `cjk_fix_v2.py` post-build or `build.py`'s idioms stage.
- **週-daai-go / 週-daaih-go leading-週 strip** → `cjk_fix_v2.py` `shared_concat_fixes` / `yale_concat_fixes`. Confirmed Ep31, Ep32 (14 occurrences). The baseline rendering carries the CJK 週 prefix, violating STYLE §1's zero-CJK rule in romanised; post-build strip leaves `daai-go` / `daaih-go`.
- **Ep30/Ep31/Ep32 chi-OCR batch damage** → `REFERENCE.md` §1 (new subsection with variant table); `cjk_fix_v2.py` `OCR_NAME_COLLAPSE` extended with the most-seen variants: 老頑童 cluster (老誠童 / 老顏童 / 老其童 / 老示童 / 老顛童 / 老和童 / 老基童 / 老阿棟 / 老誠和童); 歐陽蜂 / 歐陽鋒 → 歐陽峰; 郭蜻 → 郭靖; 阿蜻 → 阿靖; 其兒 / 鞭兒 → 蓉兒; 量有此理 → 豈有此理; 王老邪 / 羅老邪 → 黃老邪; 若師兄 → 藥師兄. Three-episode Rule B confirmation: for these tokens in these episodes, yue is the witness track.
- **瑤珈 → 瑤迦 OCR collapse** → `cjk_fix_v2.py` `OCR_NAME_COLLAPSE`. Ep28 single-firing, but canonical form is settled via `PersonalNamesUpdated.csv`. Mechanical collapse; safe to promote despite single-ep precedent.
- **Watch List cleanup** — the following were already catalogued in consolidated docs but still had sitting Watch List entries; deleted as part of the v13 cleanup (no file edits needed beyond SESSION-NOTES):
  - **博將軍 / 赤將軍** (Ep22, Ep21) — `STYLE.md` §5.
  - **洪七公 / 七公 cross-stage trap** (Ep22, Ep21) — already resolved by `cjk_fix_v2.py` `洪Seven Elder` rule under v10.
  - **望江樓 / 清溪別院** (Ep22) — `STYLE.md` §8.
  - **梅花五毒** (Ep22) — `STYLE.md` §8.
  - **靈智上人** (Ep22) — `extras_baseline.json`.
  - **老叫化子 → Old Beggar** (Ep21) — `build.py` `titles`.
  - **不見棺材不流淚** (Ep21), **以牙還牙** (Ep21), **事不宜遲** (Ep21/Ep32), **夜長夢多** (Ep22), **狗咬呂洞賓** (Ep22), **好心遭雷劈** (Ep22), **心腹大患** (Ep21), **自作自受** (Ep21), **英明神武** (Ep21) — all in `STYLE.md` §10 / §11.
  - **老賊 (二度)** (Ep22, Ep23) — `REFERENCE.md` §1.
  - **張大哥 / 馬大哥** (Ep26) — family catalogued in `STYLE.md` §19 v13 structural rule.

### 🟢 Promoted under v12 (changelog)

Items promoted under the v12 bundle bump. **Do not re-register these in episode overlays** — if they leak, the promotion regressed and needs fixing in the consolidated location.

v11 → v12 initial bump:
- **一陽指 → the Single Yang Finger** (Ep31) — registered in Ep31 overlay. Flashback episodes and later arcs involving 段智興 / 一燈大師 will re-use.
- **內子 → my wife** (Ep31 sub 330 first FULL firing; already in `STYLE.md` §8).
- **圓寂 → passing** (Ep31 sub 293 first FULL firing — 王重陽's own anticipatory use of Buddhist/Taoist register).
- **李白 將進酒 couplet pattern** (Ep31 subs 233–234, 君不見高堂明鏡悲白髮 / 朝如青絲暮如雪) — hold in Watch List for one more firing before promoting to `STYLE.md` §10 "Classical laments / elegiac verse". Format matches the Ep28 天蓋高而無階 pattern.

### 🟢 Promoted under v11 (changelog)

Items promoted out of the Watch List when the bundle was bumped from v10 to v11 (initial bump + Ep30 handoff merge). **Do not re-register these in episode overlays** — if they leak, the promotion regressed and needs fixing in the consolidated location.

v10 → v11 initial bump:
- **我爹 → my father** / **你爹 → your father** → `extras_baseline.json`. Confirmed Ep26, Ep28, Ep29.
- **週大哥 → 週-daai-go** (jy) / **週-daaih-go** (yl) → `cjk_fix_v2.py` fix tables (including post-build leak form `週Big Brother`). Also added to `extras_baseline.json`. Confirmed Ep28, Ep29.
- **陸乘風 OCR-variant collapse** (陸成風, 陸承鋒, 陸承峰, 陸勝鋒, 六成風 → 陸乘風; 六兄 → 陸兄) → `cjk_fix_v2.py` as a pre-pass on all three variants. Confirmed Ep26, Ep28.

Ep30 handoff merge (post-delivery, VERSION unchanged):
- **叔叔 → Uncle**, **武功 → martial arts**, **走火入魔 → go into the fiery madness** → `extras_baseline.json`. Confirmed Ep30.
- **Luksenior → senior Luk** / **Luhksenior → senior Luhk** (陸前輩 concat, Ep28) → `cjk_fix_v2.py` `shared_concat_fixes` / `yale_concat_fixes`.
- **KauElder → Elder Kau** / **KauhElder → Elder Kauh** (裘老前輩 concat) → `cjk_fix_v2.py`.
- **我們the → our** (我們 + term concat, Ep28) → `cjk_fix_v2.py`.
- **Cing姑Mother → Miss Cing** / **Ching姑Mother → Miss Ching** (程姑娘 concat, Ep28) → `cjk_fix_v2.py`. 程姑娘 also has an explicit row in `STYLE.md` §5.
- **瑤迦 / 冠英 / 孫不二** → `STYLE.md` §5 (explicit rendering rows).
- **積翠亭, 梅花樁, 梅花陣, 奇門八卦, 奇門八卦之術, 神龍擺尾, 碧海潮生曲, 文鬥 / 武鬥, 內子, 岳父大人** → `STYLE.md` §8.
- **秦晉之好, 泰山北斗, 天作之合** → `STYLE.md` §10 (new "Marriage alliance / classical references" subsection).
- **想逝者之不罪兮 / 天蓋高而無階** (Ep28 陸乘風 lament) → `STYLE.md` §10 (new "Classical laments / elegiac verse" subsection).
- **天之道, 損有餘而補不足** → `STYLE.md` §10 (new "九陰真經 quotations" subsection).
- **周伯通 voice entry** → `REFERENCE.md` §3 (sworn-brotherhood, Slap-Memorise, fake-suicide prank, test-rigging, 左右互搏 lament, "with me around" oath-breaking).
- **阿克 Whisper homophone cluster** (克/赫/黑/客 `haak1`) → `REFERENCE.md` §1.

---

## How to Use This Log

When closing a session, update the status section for each episode processed and add anything new to the Watch List. Specifically:

1. **Update the episode row.** If the episode completed FULL under the current bundle version, move it into the "Completed under v{VERSION}" table and replace prior-session content with the new summary. If it partially processed or the quality outcome was less than FULL, leave it in Pending and note the outcome.

2. **Surface new names, titles, idioms, or oddities** that came up during examination and don't yet have a settled rendering. Add them to the Watch List under a short descriptive heading. Skip anything already covered by `STYLE.md`'s name-rendering table (§5), title-conversion table (§6), or idiom catalogue (§10), or by `REFERENCE.md`'s character/context entries.

3. **Promote when stable.** Once a Watch List item has been rendered the same way across two or more episodes without re-debate, move it into the appropriate consolidated doc (name → `STYLE.md` §5; title → §6; idiom → §10; context-dependent judgment → `REFERENCE.md`; concat-trap fix → `cjk_fix_v2.py` or `extras_baseline.json`) and delete it from here.

This file is not a general changelog. Pipeline version bumps for script architecture, documentation consolidation, or vocabulary renames belong in `PIPELINE.md` or the script itself, not here. The one exception is the "Promoted under v{N}" section: when Watch List items graduate into consolidated docs/scripts during a version bump, record the graduation here so future sessions know (a) not to re-register the item in an overlay, and (b) where to look if the promotion appears to regress. Everything else here is content-level findings that bear on future episodes.
