import re, sys
ep = sys.argv[1]

# Comprehensive CJK→romanised fix table
fixes = {
    # Names
    "靖哥哥": "Zing-gogo", "靖兒": "Zing-ji", "靖": "Zing",
    "週大哥": "週-daai-go", "周大哥": "週-daai-go",
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
}

yale_fixes = {
    "靖哥哥": "Jing-gogo", "靖兒": "Jing-yi", "靖": "Jing",
    "週大哥": "週-daaih-go", "周大哥": "週-daaih-go",
    "周伯通": "Jau Baak-tung",
    "洪Seven Elder": "Huhng Seven Elder",
    "克兒": "Hak-yi", "康兒": "Hong-yi",
    "歐陽世兄": "Brother Au-Yeung",
    "靈智上人": "Lihng-ji Seuhng-yahn",
    "藥師兄": "Brother Yeuhk-si", "阿衡": "Aa-Hahng",
    "蓉兒": "Yuhng-yi", "阿靖": "Aa-Jing",
    "歐陽": "Au-Yeung", "洪": "Huhng", "周": "Jau",
    "完顏": "Yun-Ngaan", "程": "Ching",
    "丘道長": "Taoist Yau", "洪前輩": "Senior Huhng",
}

for variant in ["jyutping", "yale"]:
    fp = f"/mnt/user-data/outputs/{ep}-eng-{variant}.srt"
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    lookup = dict(fixes)
    if variant == "yale": lookup.update(yale_fixes)
    for k in sorted(lookup, key=len, reverse=True):
        content = content.replace(k, lookup[k])
    # Clean up double spaces
    content = re.sub(r'  +', ' ', content)
    # Collapse "X — Y" duplicate-gloss patterns (StyleRulings Ep22/23 learning).
    # Happens when hybrid uses "ENGLISH — CJK-idiom" and the CJK-idiom
    # converts to the same (or very similar) English. Two triggers:
    #   (a) Content words heavily overlap (>70% Jaccard).
    #   (b) One side's content words are a subset of the other's AND the
    #       smaller side has ≥2 content words. Catches "a blood exchange"
    #       being a subset of "perform a blood exchange on him".
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
        if jaccard > 0.7 or subset:
            # Keep the side with more content; drop the em-dash phrase entirely
            return left if len(left) >= len(right) else right
        return m.group(0)
    content = re.sub(
        r'([^\n—]{8,}?)(\s+—\s+)([^\n—.!?]{8,}?)(?=[.!?\n])',
        collapse_dupe, content
    )
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

for variant in ["hybrid", "jyutping", "yale"]:
    fp = f"/mnt/user-data/outputs/{ep}-eng-{variant}.srt"
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    cjk = [ch for ch in content if chr(0x4e00) <= ch <= chr(0x9fff)]
    count = len(re.findall(r"^\d+$", content, re.MULTILINE))
    status = "✓" if (not cjk or variant == "hybrid") else f"⚠ {len(cjk)}"
    print(f"Ep{ep} {variant}: {count} entries, {status}")
