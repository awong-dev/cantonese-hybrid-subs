import re, sys, os
ep = sys.argv[1]

# Handoff version — must match the suffix build.py wrote to the SRT filenames.
# See build.py for the rationale. Missing/malformed VERSION is a hard error.
def _load_version():
    vpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'VERSION')
    try:
        with open(vpath, 'r', encoding='utf-8') as f:
            v = f.read().strip()
    except FileNotFoundError:
        raise SystemExit(
            f"ERROR: VERSION file not found at {vpath}. "
            "cjk_fix_v2.py reads SRTs named {EP}-eng-{variant}-v{VERSION}.srt; "
            "the VERSION file is required to locate them."
        )
    if not re.fullmatch(r'\d+', v):
        raise SystemExit(
            f"ERROR: VERSION file at {vpath} contains '{v}', expected a bare integer."
        )
    return v

VERSION = _load_version()

# Comprehensive CJK→romanised fix table
fixes = {
    # Names
    "靖哥哥": "Zing-gogo", "靖兒": "Zing-ji", "靖": "Zing",
    "週大哥": "週-daai-go", "周大哥": "週-daai-go",
    # Post-build leak: build.py's titles stage converts 大哥→Big Brother
    # before extras runs, stranding the 週. Promoted from SESSION-NOTES
    # (confirmed Ep28, Ep29). See also: 陸乘風 name-variant collapse below.
    "週Big Brother": "週-daai-go", "周Big Brother": "週-daai-go",
    "周伯通": "Zau Baak-tung",
    "洪Seven Elder": "Hung Seven Elder",
    # Nicknames
    "老頑童": "Overgrown Child", "老毒物": "Old Venom",
    "賴蛤蟆": "Old Toad", "黃老邪": "Old Heretic Wong",
    # Address terms
    "克兒": "Hak-ji", "康兒": "Hong-ji",
    "黃島主": "Island Lord Wong", "島主": "Island Lord",
    "歐陽世兄": "Brother Au-Joeng",
    "父王": "Royal Father", "阿爹": "Father",
    "爹": "Father",
    "靈智上人": "Ling-zi Soeng-jan", "仙翁": "Immortal Elder",
    "師父": "Master", "師兄": "Senior Brother", "師弟": "Junior Brother",
    "師姊": "Senior Sister", "師妹": "Junior Sister",
    "師叔": "Martial Uncle", "師姑": "Taoist Nun",
    "公子": "Young Master", "姑娘": "Miss",  # v21 Ep27 promotion — §7 address terms missing from build.py titles
    "閻王爺": "King of Hell", "七兄": "Brother Seven",
    "藥師兄": "Brother Joek-si", "阿衡": "Aa-Hang",
    "前輩": "senior", "祖師爺": "Grand Teacher",
    "莊主": "the Manor Lord", "少莊主": "Young Master",
    "幫主": "the Chief", "仙姑": "the Taoist Nun",
    "娘親": "Mother", "小王爺": "the Young Prince", "王爺": "Your Highness",
    "大哥": "Big Brother", "七公": "Seven Elder",
    "蓉兒": "Jung-ji", "阿靖": "Aa-Zing", "阿康": "Hong",
    "黃姑娘": "Miss Wong", "穆姑娘": "Miss Muk",
    "郭大哥": "Brother Gwok",
    "駙馬爺": "the Prince Consort", "駙馬": "the Prince Consort",
    "豈有此理": "Outrageous",
    # Places
    "桃花島": "Peach Blossom Island", "桃花陣": "the Peach Blossom Formation",
    "白駝山": "White Camel Mountain", "歸雲莊": "Guiyun Manor",
    "牛家村": "Niu Family Village", "蒙古人": "the Mongolians", "蒙古": "Mongolia",
    "金國": "Jin",
    "臨安": "Lin'an", "大理": "Dali",
    # Terms
    "九陰真經": "the Jiuyin Manual", "九陰白骨爪": "the Jiuyin Baigu Claw",
    "武穆遺書": "the Book of Wu Mu",
    "降龍十八掌": "the Eighteen Dragon-Subduing Palms",
    "蛤蟆功": "the Toad Skill", "左右互搏": "Ambidextrous Combat",
    "空明拳": "the Hollow Fist",
    "全真教": "the Quanzhen Sect", "丐幫": "the Beggars Sect",
    "鐵掌幫": "the Iron Palm Sect",
    "江湖": "the martial world", "輕功": "qinggong",
    # Sects/orgs
    "全真七子": "the Seven Masters of Quanzhen",
    # Idioms (these get injected by v2 and need romanisation)
    "冤家路窄": "enemies meet on a narrow road",
    "借花敬佛": "presenting another's flowers to Buddha",
    "棋差一著": "one wrong move on the chessboard",
    "打草驚蛇": "alerting the enemy",
    "防不勝防": "impossible to guard against",
    "臭名遠揚": "infamous far and wide",
    "勢不兩立": "sworn enemies",
    "沒齒難忘": "I will never forget",
    "拐彎抹角": "beating around the bush",
    "舉手之勞": "it was nothing",
    "人死不能復生": "the dead cannot return",
    "後會有期": "we will meet again",
    "萬萬不能": "absolutely not",
    "知心朋友": "a true friend",
    "指日可待": "just around the corner",
    "奮不顧身": "risking one's life bravely",
    "低聲下氣": "grovelling",
    "一心一意": "wholeheartedly",
    "天下無敵": "invincible under heaven",
    "心滿意足": "fully satisfied",
    "門當戶對": "a proper match",
    "有情人終成眷屬": "lovers united at last",
    "一日為師終身為父": "a teacher for a day is a father for life",
    "無毒不丈夫": "ruthlessness is the mark of a great man",
    "施恩莫圖報": "a kind deed needs no repayment",
    "杯酒釋前嫌": "a cup of wine dissolves old grudges",
    "一笑泯恩仇": "one smile wipes away all grudges",
    "一刀兩斷": "cut all ties",
    "喪心病狂": "ruthless and deranged",
    "認賊作父": "calling a thief his father",
    "江山易改本性難移": "a leopard never changes its spots",
    "有福同享": "share fortune together",
    "有難同當": "share misfortune together",
    "蛇鼠一窩": "all in cahoots",
    "義結金蘭": "sworn brotherhood",
    "化干戈為玉帛": "burying the hatchet",
    "意氣用事": "acting on impulse",
    "頑固不化": "set in one's ways",
    "女大不中留": "a grown daughter cannot be kept",
    "大逆不道": "treasonous",
    "感情用事": "swayed by emotion",
    "既往不究": "letting bygones be bygones",
    "不擇手段": "by any means necessary",
    "忘恩負義": "ungrateful",
    "夜長夢多": "the longer we wait the more trouble",
    # Bare surnames
    "歐陽": "Au-Joeng", "郭": "Gwok", "陸": "Luk",
    "程": "Cing", "楊": "Yeung", "黃": "Wong",
    "洪": "Hung", "周": "Zau", "梅": "Mui",
    "穆": "Muk", "完顏": "Jyun-Ngaan",
    "黎": "Lai",  # v21 — Ep27 black-raven character 黎生
}

# Shared concat-trap post-build fixes (applied to BOTH romanised variants after
# the variant-specific passes below). Promoted to cjk_fix_v2 under v11:
#   - Luksenior   (陸前輩, Ep28)  — 前輩 converts before overlay
#   - KauElder    (裘老前輩, Ep26) — same mechanism for 裘
#   - 我們the     (Ep28 sub 36)   — 我們 + term compound
#   - Cing姑Mother (程姑娘, Ep28)  — 娘→Mother eats the 娘 before extras
# Promoted under v13 (the <titles-key>+<suffix> cross-stage trap family,
# confirmed Ep21). The generalisable lesson: registering a compound in
# extras/baseline is insufficient when build.py's titles stage has a
# shorter-key match. See STYLE.md §19.
#   - 我Father / 你Father  (我爹/你爹, Ep21)  — 爹→Father eats the 爹 before extras
#   - the Chief萬福        (幫主萬福, Ep21)   — 幫主→the Chief eats it first
#   - 大Jin                 (大金國, Ep21)     — 金國→Jin stranding 大
#   - 報告the Princess      (報告公主, Ep21)   — 公主→the Princess eats it first
#   - 週-daai-go / 週-daaih-go leading-週 strip (Ep31/Ep32) — the baseline
#     rendering includes the CJK 週 prefix which violates STYLE §1's
#     zero-CJK rule; strip it post-build.
# Yale variants appended to yale_concat_fixes below.
shared_concat_fixes = {
    "Luksenior": "senior Luk",
    "KauElder": "Elder Kau",
    "我們the ": "our ",
    "Cing姑Mother": "Miss Cing",
    # v13 <titles-key>+<suffix> family (Ep21):
    "我Father": "my father",
    "你Father": "your father",
    "the Chief萬福": "Good fortune to the Chief",
    "大Jin": "the great Jin empire",
    "報告the Princess": "Your report, Princess",
    # v13 週-daai-go leading-週 strip (Ep31/Ep32):
    "週-daai-go": "daai-go",
    "周-daai-go": "daai-go",
    # v17 — v15/v16 concat-traps flagged by Ep7 as added-to-SESSION-NOTES
    # but never landed in the shipped script. Recovering them now.
    # v15 family (Ep1 pilot narration + OCR-drift compounds):
    "六Your Highness": "the Sixth Prince",          # 六王爺; titles→Your Highness eats 王爺
    "My Mother子": "my wife",                        # 娘子; titles 娘→Mother strands 子
    "張老Father": "Old Zoeng",                       # 張老爹; bare 爹→Father strands 張老
    "官字taels個口": "the official's mouth speaks both ways",  # 官字兩個口; 兩→taels
    # v16 family (Ep5+Ep6 two-ep confirmation for 大Master; the rest Ep6):
    "大Master": "First Master",                      # 大師父 (Ep5+Ep6; also STYLE §19)
    "二Master": "Second Master",                     # 二師父 (江南七怪)
    "三Master": "Third Master",                      # 三師父 (江南七怪)
    "四Master": "Fourth Master",                     # 四師父 (江南七怪)
    "五Master": "Fifth Master",                      # 五師父 (江南七怪)
    "六Master": "Sixth Master",                      # 六師父 (江南七怪)
    "七Master": "Seventh Master",                    # 七師父 (江南七怪)
    "紅Mother": "the Matchmaker",                    # 紅娘; 娘→Mother strands 紅
    "姑Mother": "Miss",                              # bare 姑娘; 娘→Mother strands 姑
    "柯Big Brother": "Brother O",                    # 柯大哥; 大哥→Big Brother strands 柯
    "Zit-BitMaster": "Master Zit-Bit",               # 哲別師父 jy; 師父→Master eats 別
    # Ep20+Ep25+Ep25 three-firing cross-stage trap:
    "本姑Mother": "this girl",                       # 本姑娘; 娘→Mother strands 本姑
    # Ep20 cross-stage trap (岳王爺 compound):
    "岳Your Highness": "Lord Ngok",                  # 岳王爺; 王爺→Your Highness strands 岳
    # Ep23 two cross-stage traps:
    "Wongsenior": "senior Wong",                     # 黃前輩; 前輩→senior strands Wong
    "死Old Heretic": "damned Old Heretic",           # 死老邪 per STYLE §5
    # Ep3 <nickname>+<CSV-name> concat-trap family (names stage 4 fires
    # CSV name before extras stage 5, stranding the nickname):
    "銅屍Can Jyun-fung": "Bronze Corpse Can Jyun-fung",
    "鐵屍Mui Ciu-fung": "Iron Corpse Mui Ciu-fung",
    "飛天蝙蝠O Zan-ngok": "Flying Bat O Zan-ngok",
    # Ep33 Big Brother-family compound (大哥 titles stage eats it):
    "Zau Baak-tungBig Brother": "Brother Zau Baak-tung",
    # v21 — `<CSV-name>+大哥` concat class confirmed 3-ep (Ep22 華箏公主
    # first, Ep24 拖雷大哥 second, Ep26 張大哥/馬大哥 third). Structural
    # class: names stage 4 fires CSV name → romanised before extras stage 5
    # can match the compound. Promoted per SESSION-NOTES Ep24/Ep26 entries.
    "To-leoiBig Brother": "Brother To-leoi",         # 拖雷大哥 Ep24
    "ZoengBig Brother": "Brother Zoeng",             # 張大哥 Ep26
    "MaaBig Brother": "Brother Maa",                 # 馬大哥 Ep26
    # v21 — `<surname>+老+前輩` class (Ep26 裘老前輩; 前輩→senior in titles
    # eats the compound, stranding Kau-老). Partial prior form KauElder
    # above covered the Ep22-like no-老 form; this is the with-老 variant.
    "Kau老senior": "Elder Kau",                      # 裘老前輩 Ep26
    # v22 — Ep39 reveals literal-CJK-surname variant of the same class:
    # 裘 isn't a bare entry in CSV (only 裘千仞 full-name), so when chi
    # has bare-surname forms (裘老前輩 vs 裘千仞老前輩), 裘 stays CJK
    # and we get `裘老senior` rather than `Kau老senior`. Confirmed Ep26+Ep39 2-ep.
    "裘老senior": "Elder Kau",                       # 裘老前輩 Ep39 (literal-CJK 裘)
    # v21 — 岳飛將軍 (Ep26); 岳飛 in CSV converts first leaving 將軍
    # stranded. Novel `<CSV-full-name>+將軍` class.
    "Ngok Fei將軍": "General Ngok Fei",              # 岳飛將軍 Ep26
    # v21 — 謝幫主 / 報告幫主 (Ep20+Ep21 two-ep confirmation); 幫主→the Chief
    # in titles stage converts before the compound can resolve.
    "謝the Chief": "Thank you, Chief",                # 謝幫主
    "報告the Chief": "Reporting, Chief",              # 報告幫主
    # v21 — `<surname>+前輩` class additions (Ep23 黃前輩 already present
    # as Wongsenior above; Ep27 黎前輩 novel firing in same class).
    "黎senior": "Senior Lai",                         # 黎前輩 Ep27
    # v21 — `<surname>+師姊` class (Ep16+Ep26+Ep27 three-ep, 師姊→Senior
    # Sister in titles stage eats the compound).
    "梅Senior Sister": "Senior Sister Mui",          # 梅師姊 Ep16/26/27
    # v21 — `<Romanised-CSV-name>+姑娘` novel cross-stage (Ep27). 娘
    # bare-kinship in titles→Mother stage 3 converts FIRST, producing
    # `<Name>姑Mother`. `Cing姑Mother → Miss Cing` in the v11 block above
    # covered the English-only output; now add variants for full-name
    # compounds that build.py leaves as `<CSV-name>姑娘` where bare surname
    # plus 姑娘 → `<CSV-name>姑Mother`. Jyutping handled; Yale parallels
    # appended below.
}

yale_fixes = {
    "靖哥哥": "Jing-gogo", "靖兒": "Jing-yi", "靖": "Jing",
    "週大哥": "週-daaih-go", "周大哥": "週-daaih-go",
    "週Big Brother": "週-daaih-go", "周Big Brother": "週-daaih-go",
    "周伯通": "Jau Baak-tung",
    "洪Seven Elder": "Huhng Seven Elder",
    "克兒": "Hak-yi", "康兒": "Hong-yi",
    "歐陽世兄": "Brother Au-Yeung",
    "靈智上人": "Lihng-ji Seuhng-yahn",
    "藥師兄": "Brother Yeuhk-si", "阿衡": "Aa-Hahng",
    "蓉兒": "Yuhng-yi", "阿靖": "Aa-Jing",
    "歐陽": "Au-Yeung", "洪": "Huhng", "周": "Jau",
    "完顏": "Yun-Ngaan", "程": "Ching",
    "黎": "Laih",  # v21 — Ep27
    "丘道長": "Taoist Yau", "洪前輩": "Senior Huhng",
}

# Yale-specific concat-trap fixes (promoted under v11; companion to shared_concat_fixes)
yale_concat_fixes = {
    "Luksenior": "senior Luhk",
    "KauhElder": "Elder Kauh",
    "我們the ": "our ",
    "Ching姑Mother": "Miss Ching",
    # v13 週-daaih-go leading-週 strip (Ep31/Ep32):
    "週-daaih-go": "daaih-go",
    "周-daaih-go": "daaih-go",
    # v17 — Yale counterparts for v15/v16 entries above.
    # Most entries in shared_concat_fixes are variant-neutral (they operate
    # on English titles-stage output like "Your Highness", "Father", "Master")
    # so they don't need Yale overrides. Listed here are the few where Yale
    # spelling differs from Jyutping.
    "張老Father": "Old Jeung",                       # jy Zoeng → yl Jeung
    "Jit-BitMaster": "Master Jit-Bit",               # jy Zit-Bit → yl Jit-Bit
    # Ep3 <nickname>+<CSV-name> Yale spellings:
    "銅屍Chan Yun-fung": "Bronze Corpse Chan Yun-fung",
    "鐵屍Mui Chiu-fung": "Iron Corpse Mui Chiu-fung",
    "飛天蝙蝠O Jan-ngok": "Flying Bat O Jan-ngok",
    # Ep33 Yale counterpart:
    "Jau Baak-tungBig Brother": "Brother Jau Baak-tung",
    # v21 — Yale parallels for v21 <CSV-name>+<titles-key> promotions.
    # Most concat-trap English outputs are variant-neutral; Yale overrides
    # below are the ones where Yale spelling differs from Jyutping.
    "To-leuihBig Brother": "Brother To-leuih",       # 拖雷大哥 Ep24 yl
    "JeungBig Brother": "Brother Jeung",             # 張大哥 Ep26 yl
    "MaBig Brother": "Brother Ma",                   # 馬大哥 Ep26 yl
    "Kauh老senior": "Elder Kauh",                    # 裘老前輩 Ep26 yl
    # v22 — Yale parallel for literal-CJK 裘 variant (Ep39):
    "裘老senior": "Elder Kauh",                      # 裘老前輩 Ep39 yl (literal-CJK 裘)
    # 岳飛 and 謝/報告the Chief are variant-neutral — already handled.
    "黎senior": "Senior Laih",                        # 黎前輩 Ep27 yl
    "梅Senior Sister": "Senior Sister Muhk",         # 梅師姊 Ep27 yl
}

# Name-variant OCR collapse — runs on ALL THREE variants before variant-specific
# passes. Promoted from SESSION-NOTES (confirmed Ep26, Ep28). The chi track
# OCR-drifts 陸乘風 across a handful of visually-similar variants; yue Whisper
# additionally produces 六成風 / 六兄 via the 陸→六 homophone (both `luk6`).
# The Step 4 override process usually canonicalises to 陸乘風 in the hybrid,
# but this is a belt-and-suspenders catch for cases where a variant slipped
# into the hybrid SRT uncorrected — and it also protects romanised output
# since the bare-surname 陸 pass would otherwise convert only the Luk/Luhk
# part and strand the garbled second/third character.
#
# v13 additions — Ep30/31/32 chi-OCR batch damage (three-episode confirmation).
# The source chi-track OCR for mid-30s episodes was done in a single degraded
# batch; variants below appeared across Ep30/31/32 for the same canonical names.
# yue was the witness track; Step 4 override process canonicalised in hybrid,
# but the pre-pass catches any that slipped through.
OCR_NAME_COLLAPSE = {
    "陸成風": "陸乘風", "陸承鋒": "陸乘風", "陸承峰": "陸乘風",
    "陸勝鋒": "陸乘風", "六成風": "陸乘風",
    "六兄": "陸兄",
    # v13 — 老頑童 variants (Ep30/31/32):
    "老誠童": "老頑童", "老顏童": "老頑童", "老其童": "老頑童",
    "老示童": "老頑童", "老顛童": "老頑童", "老和童": "老頑童",
    "老基童": "老頑童", "老阿棟": "老頑童", "老誠和童": "老頑童",
    # v13 — 歐陽峰 variants (Ep30/31/32 — chi usually 歐陽蜂, yue 歐陽鋒):
    "歐陽蜂": "歐陽峰", "歐陽鋒": "歐陽峰",
    # v13 — 郭靖 / 阿靖 (Ep30/31/32):
    "郭蜻": "郭靖", "阿蜻": "阿靖",
    # v13 — 蓉兒 (Ep30/31/32, persistent):
    "其兒": "蓉兒", "鞭兒": "蓉兒",
    # v13 — 豈有此理 (Ep32 three firings):
    "量有此理": "豈有此理",
    # v13 — 黃老邪 variants (Ep30/31):
    "王老邪": "黃老邪", "羅老邪": "黃老邪",
    # v13 — 藥師兄 (Ep30):
    "若師兄": "藥師兄",
    # v13 — 瑤珈 → 瑤迦 (Ep28 single-ep; canonical form per CSV):
    "瑤珈": "瑤迦",
    # v17 — chi-OCR variants confirmed across 3+ episodes in early-arc batch
    # (Ep1–Ep7 shared OCR pipeline; yue track witness corroborates):
    "啟桌": "啟稟",                                  # Ep1+Ep2+Ep4 three-ep
    "希彰": "希望", "希芯": "希望", "希章": "希望",  # Ep1+Ep2+Ep33 three-ep
    "梅朝風": "梅超風", "梅竹風": "梅超風",          # Ep5+Ep6+Ep7 three-ep
    "節別": "哲別",                                  # Ep6+Ep7 yue-ASR two-ep
    "郭蜻": "郭靖",                                  # already in v13 batch but
                                                      # reaffirmed Ep3/4/5/6/7
    "窩辣台": "窩闊台", "骨都虎": "忽都虎",          # Ep3 novel; flagged two-ep
    "和伯伽": "瑤迦", "伯伽": "瑤迦",                # Ep25 chi-drift
    "網康": "阿康",                                  # Ep24 novel OCR
    "活將軍": "霍將軍", "活叔叔": "霍叔叔",          # Ep7 chi-OCR (活→霍);
                                                      # flagged for 2nd firing
    # v18 — additional Watch List promotions:
    "蒼龍": "蒼狼",                                   # 大漠的蒼龍 chi-OCR; Ep3+Ep8 two-ep.
                                                      # 成吉思汗's epithet 大漠的蒼狼 (wolf, canonical);
                                                      # chi drifts 狼→龍 (visually similar). yue
                                                      # witness confirms 蒼狼.
    "央馬": "駙馬", "騎馬": "駙馬",                    # 駙馬 chi-OCR; Ep8+Ep23+Ep25 three-ep.
                                                      # Both visual drifts of 駙. The wider compound
                                                      # 駙馬爺 is unaffected because the longer
                                                      # 央馬爺/騎馬爺 forms reduce by suffix.
    "阿勇": "阿蓉",                                   # Ep10+Ep13 two-ep chi-OCR; 郭靖's intimate
                                                      # form for 蓉兒. yue witness clean.
    "會牲": "畜生", "會牡": "畜生",                    # Ep14+Ep24+Ep17 three-ep chi-OCR of 畜生
                                                      # (insult "brute"). 會 OCR-corrupts 畜;
                                                      # 牲/牡 are 生 OCR variants. Both forms
                                                      # observed in Ep17.
}
for variant in ["hybrid", "jyutping", "yale"]:
    fp = f"/mnt/user-data/outputs/{ep}-eng-{variant}-v{VERSION}.srt"
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    for k, v in OCR_NAME_COLLAPSE.items():
        content = content.replace(k, v)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

for variant in ["jyutping", "yale"]:
    fp = f"/mnt/user-data/outputs/{ep}-eng-{variant}-v{VERSION}.srt"
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    lookup = dict(fixes)
    if variant == "yale": lookup.update(yale_fixes)
    for k in sorted(lookup, key=len, reverse=True):
        content = content.replace(k, lookup[k])
    # v11 concat-trap post-build fixes (see SESSION-NOTES v10 Watch List promotions).
    # Sort longest-first so multi-key compounds win over their substrings —
    # e.g. `本姑Mother → this girl` must fire before `姑Mother → Miss`,
    # otherwise the short key strands `本Miss`. (Three-ep firing Ep20+Ep25+Ep13
    # before this sort was added.)
    concat = dict(shared_concat_fixes)
    if variant == "yale": concat.update(yale_concat_fixes)
    for k in sorted(concat, key=len, reverse=True):
        content = content.replace(k, concat[k])
    # Clean up double spaces
    content = re.sub(r'  +', ' ', content)
    # Collapse "X — Y" duplicate-gloss patterns (StyleRulings Ep22/23 learning).
    # Happens when hybrid uses "ENGLISH — CJK-idiom" and the CJK-idiom
    # converts to the same (or very similar) English. Two triggers:
    #   (a) Content words heavily overlap (>55% Jaccard).
    #   (b) One side's content words are a subset of the other's AND the
    #       smaller side has ≥2 content words. Catches "a blood exchange"
    #       being a subset of "perform a blood exchange on him".
    # v17 threshold lowering: Jaccard 0.7 → 0.55, minimum phrase length
    # 8 → 6 chars. Four-ep miss pattern (Ep24+Ep33+Ep4+Ep6) for short
    # idioms — 後會有期, 忘恩負義, 視日無多, 碎屍萬段 — whose renderings
    # are only 3–5 content words, where even exact-synonym glosses were
    # falling below the 0.7 threshold because small-set Jaccard is jumpy
    # (e.g. {"meet","again"} vs {"meet","again","until"} = 2/3 = 0.67 passes,
    # but {"tear","pieces"} vs {"tear","them","pieces"} = 2/3 = 0.67 still
    # fine — the real misses were where one side picked up an extra
    # stopword-adjacent noun). Subset check is the more reliable catch for
    # these cases, but the lower Jaccard widens the safety net.
    STOPWORDS = {'a','an','the','of','to','on','in','for','with','and',
                 'is','was','be','it','i','you','we','he','she','him','her',
                 'his','our','my','your','this','that','these','those'}
    def content_words(s):
        return {w for w in re.findall(r'\w+', s.lower()) if w not in STOPWORDS}
    def collapse_dupe(m):
        left, sep, right = m.group(1), m.group(2), m.group(3)
        lc = content_words(left)
        rc = content_words(right)
        if not lc or not rc:
            return m.group(0)
        jaccard = len(lc & rc) / len(lc | rc)
        subset = (lc.issubset(rc) or rc.issubset(lc)) and min(len(lc), len(rc)) >= 2
        if jaccard > 0.55 or subset:
            # Keep the side with more content; drop the em-dash phrase entirely
            return left if len(left) >= len(right) else right
        return m.group(0)
    content = re.sub(
        r'([^\n—]{6,}?)(\s+—\s+)([^\n—.!?]{6,}?)(?=[.!?\n])',
        collapse_dupe, content
    )
    # v18: also collapse "X (Y)" duplicate-gloss patterns arising from the
    # STYLE §9 `中文成語 (English gloss)` hybrid format. When build.py converts
    # the CJK on the left of the parens, it produces an English rendering
    # that is usually content-identical (or near-identical) to the gloss
    # inside the parens. Example before collapse:
    #   "better safe than sorry (better safe than sorry)"
    #   "I've fallen short at the last gasp (I've fallen short at the last gasp)"
    # The collapser keeps the un-parenthesised side and drops the parens
    # phrase, using the same Jaccard-or-subset rule as the em-dash collapser.
    #
    # Scoping: the outer phrase match is anchored at word-start and runs up
    # to the opening paren; the parens content is captured without inner
    # parens. We don't fire on parens that carry genuinely new information
    # (speaker labels, asides, numeric references) — the ≥55% Jaccard
    # threshold protects those. We also require the parens content to be
    # ≥6 chars so one-word asides like "(again)" aren't folded.
    def collapse_paren_dupe(m):
        before, inside = m.group(1), m.group(2)
        bc = content_words(before)
        ic = content_words(inside)
        if not bc or not ic:
            return m.group(0)
        jaccard = len(bc & ic) / len(bc | ic)
        subset = (bc.issubset(ic) or ic.issubset(bc)) and min(len(bc), len(ic)) >= 2
        if jaccard > 0.55 or subset:
            # Drop the parens phrase entirely; keep the pre-parens text.
            return before.rstrip()
        return m.group(0)
    content = re.sub(
        r'([^\n()]{6,}?)\s*\(([^()\n]{6,}?)\)',
        collapse_paren_dupe, content
    )
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

for variant in ["hybrid", "jyutping", "yale"]:
    fp = f"/mnt/user-data/outputs/{ep}-eng-{variant}-v{VERSION}.srt"
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    cjk = [ch for ch in content if chr(0x4e00) <= ch <= chr(0x9fff)]
    count = len(re.findall(r"^\d+$", content, re.MULTILINE))
    status = "✓" if (not cjk or variant == "hybrid") else f"⚠ {len(cjk)}"
    print(f"Ep{ep} {variant}: {count} entries, {status}")
