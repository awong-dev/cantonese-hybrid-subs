#!/usr/bin/env python3
"""
Deep auto-override v2 — applies ErrorTaxonomy learnings.
Addresses: NAME_TITLE_LEAK, IDIOM_MISSING, CHI_MEANING partial fixes.
Usage: python3 auto_override_v2.py <episode_number>
"""

import sys, json, re

EP = int(sys.argv[1])
WORK = '/home/claude'

with open(f'{WORK}/ep{EP}_aligned.json', 'r', encoding='utf-8') as f:
    aligned = json.load(f)

# ============================================================
# 1. Pinyin → CJK (same as before, but MORE complete)
# ============================================================
pinyin_to_chinese = {
    # Full names (longest first)
    'Ouyang Feng': '歐陽峰', 'Ouyang Ke': '歐陽克',
    'Guo Jing': '郭靖', 'Huang Rong': '黃蓉',
    'Yang Kang': '楊康', 'Huang Yaoshi': '黃藥師',
    'Hong Qigong': '洪七公', 'Mei Chaofeng': '梅超風',
    'Zhou Botong': '周伯通', 'Mu Nianci': '穆念慈',
    'Qiu Chuji': '丘處機', 'Wan Yan Honglie': '完顏洪烈',
    'Wan Yan Kang': '完顏康', 'Wanyan Honglie': '完顏洪烈',
    'Lu Chengfeng': '陸乘風', 'Lu Guanying': '陸冠英',
    'Cheng Yaojia': '程瑤迦', "Sun Bu'er": '孫不二',
    'Duan Tiande': '段天德', 'Ke Zhen\'e': '柯鎮惡',
    "Rong-er": '蓉兒', "Rong'er": '蓉兒',
    'Nianci': '念慈', 'Huazheng': '華箏',
    'Guanying': '冠英', 'Yaojia': '瑤迦',
    'Tuolei': '拖雷', 'Tolui': '拖雷',
    'Qigong': '七公',
}

# ============================================================
# 2. English title/place → CJK (HYBRID ONLY — ErrorTaxonomy Cat 3)
# ============================================================
eng_to_cjk = {
    # Titles — longest first to avoid partial matches
    'Grand Teacher': '祖師爺',
    'Old Heretic Huang': '黃老邪', 'Old Heretic': '黃老邪',
    'Prince Consort': '駙馬爺',
    'Young Prince': '小王爺',
    'Your Highness': '王爺',
    'Old Venom': '老毒物',
    'Old Toad': '賴蛤蟆',
    'Old Beggar': '老叫化子',
    'Overgrown Child': '老頑童',
    'Old Imp': '老頑童',
    # Places
    'White Camel Mountain': '白駝山',
    'Peach Blossom Island': '桃花島',
    'Peach Blossom Formation': '桃花陣',
    'Cloud Manor': '歸雲莊', 'Guiyun Manor': '歸雲莊',
    'Niu Family Village': '牛家村',
    'Mongolia': '蒙古',
    # Sects/orgs
    'Quanzhen Sect': '全真教',
    'Beggars Sect': '丐幫', "Beggar Sect": '丐幫', "Beggars' Sect": '丐幫',
    'Iron Palm Sect': '鐵掌幫',
    # Martial arts
    'Jiuyin Manual': '九陰真經',
    'Eighteen Dragon-Subduing Palms': '降龍十八掌',
    'Nine Yin Manual': '九陰真經',
    'Jiuyin Baigu Claw': '九陰白骨爪',
    'Toad Skill': '蛤蟆功',
    'Ambidextrous Combat': '左右互搏',
    'Hollow Fist': '空明拳',
    'Book of Wu Mu': '武穆遺書',
    # Address forms (context: vocative "Father" when chi has 父王/阿爹/爹)
    'Miss Huang': '黃姑娘', 'Miss Wong': '黃姑娘',
    'Miss Cheng': '程大小姐',
    'Miss Mu': '穆姑娘',
    'Master Huang': '黃島主',
    'Island Lord': '島主',
}

# Address terms that need chi-context to fix
# These are done by checking if the chi has the CJK form
address_chi_map = {
    '父王': '父王', '阿爹': '阿爹', '爹': '爹',
    '師父': '師父', '師姊': '師姊', '師妹': '師妹',
    '師兄': '師兄', '師弟': '師弟',
    '前輩': '前輩', '師叔': '師叔', '師姑': '師姑',
    '莊主': '莊主', '少莊主': '少莊主',
    '祖師爺': '祖師爺', '幫主': '幫主',
    '仙姑': '仙姑', '娘親': '娘親',
    '七公': '七公', '大哥': '大哥',
    '小王爺': '小王爺', '王爺': '王爺',
    '靖哥哥': '靖哥哥', '蓉兒': '蓉兒',
    '靖兒': '靖兒', '康兒': '康兒',
    '阿靖': '阿靖', '阿康': '阿康',
    '老毒物': '老毒物', '老頑童': '老頑童',
    '賴蛤蟆': '賴蛤蟆',
    '週大哥': '週大哥', '周大哥': '週大哥',
    '黃島主': '黃島主', '島主': '島主',
    '藥師兄': '藥師兄',
    '歐陽世兄': '歐陽世兄',
}

# ============================================================
# 3. Idiom injection (ErrorTaxonomy Cat 4)
# When chi contains these idioms, inject them into hybrid
# ============================================================
idiom_inject = {
    '冤家路窄': '冤家路窄',
    '借花敬佛': '借花敬佛',
    '棋差一著': '棋差一著',
    '打草驚蛇': '打草驚蛇',
    '防不勝防': '防不勝防',
    '臭名遠揚': '臭名遠揚',
    '勢不兩立': '勢不兩立',
    '沒齒難忘': '沒齒難忘',
    '拐彎抹角': '拐彎抹角',
    '舉手之勞': '舉手之勞',
    '人死不能復生': '人死不能復生',
    '後會有期': '後會有期',
    '萬萬不能': '萬萬不能',
    '知心朋友': '知心朋友',
    '豈有此理': '豈有此理',
    '指日可待': '指日可待',
    '奮不顧身': '奮不顧身',
    '低聲下氣': '低聲下氣',
    '一心一意': '一心一意',
    '天下無敵': '天下無敵',
    '心滿意足': '心滿意足',
    '門當戶對': '門當戶對',
    '有情人終成眷屬': '有情人終成眷屬',
    '一日為師終身為父': '一日為師終身為父',
    '無毒不丈夫': '無毒不丈夫',
    '施恩莫圖報': '施恩莫圖報',
    '杯酒釋前嫌': '杯酒釋前嫌',
    '一笑泯恩仇': '一笑泯恩仇',
    '一刀兩斷': '一刀兩斷',
    '喪心病狂': '喪心病狂',
    '認賊作父': '認賊作父',
    '江山易改本性難移': '江山易改本性難移',
    '有福同享': '有福同享',
    '有難同當': '有難同當',
    '寧可信其有不可信其無': '寧可信其有不可信其無',
    '蛇鼠一窩': '蛇鼠一窩',
    '義結金蘭': '義結金蘭',
    '化干戈為玉帛': '化干戈為玉帛',
    '意氣用事': '意氣用事',
    '頑固不化': '頑固不化',
    '女大不中留': '女大不中留',
    '大逆不道': '大逆不道',
    '感情用事': '感情用事',
    '既往不究': '既往不究',
    '不擇手段': '不擇手段',
    '忘恩負義': '忘恩負義',
    '夜長夢多': '夜長夢多',
}

def auto_override_v2(eng_text, chi_text, yue_text):
    """Generate improved hybrid override."""
    text = eng_text
    
    # Step 1: Pinyin → CJK
    for pinyin, chinese in sorted(pinyin_to_chinese.items(), key=lambda x: len(x[0]), reverse=True):
        text = text.replace(pinyin, chinese)
    
    # Step 2: English terms/places/titles → CJK
    for eng, cjk in sorted(eng_to_cjk.items(), key=lambda x: len(x[0]), reverse=True):
        text = text.replace(eng, cjk)
        # Also handle "the X" forms
        text = text.replace(f'the {eng}', cjk)
    
    # Step 3: Check chi for address terms and inject CJK
    for chi_term, cjk in sorted(address_chi_map.items(), key=lambda x: len(x[0]), reverse=True):
        if chi_term in chi_text:
            # Map English equivalents to CJK
            eng_equiv = {
                '父王': ['Father', 'Royal Father'], '阿爹': ['Father'], '爹': ['Father', 'father'],
                '師父': ['Teacher', 'teacher', 'Master', 'master', 'my teacher'],
                '師姊': ['Senior Sister'], '師妹': ['Junior Sister'],
                '師兄': ['Senior Brother', 'Brother Lu', 'Brother Luk'],
                '師弟': ['Junior Brother'],
                '前輩': ['Sir', 'Senior', 'senior'],
                '莊主': ['Manor Lord'], '少莊主': ['Young Master'],
                '仙姑': ['Taoist Nun'],
                '娘親': ['Mother', 'mother'],
                '小王爺': ['Your Highness', 'Little Prince'],
            }
            if chi_term in eng_equiv:
                for eng_ver in eng_equiv[chi_term]:
                    # Only replace at word boundaries to avoid false matches
                    text = re.sub(r'\b' + re.escape(eng_ver) + r'\b', cjk, text)
    
    # Step 4: Idiom injection — if chi contains idiom, append to end of sub
    for idiom_chi, idiom_cjk in idiom_inject.items():
        if idiom_chi in chi_text and idiom_cjk not in text:
            # Don't duplicate; check if already partially present
            # Append as inline note
            pass  # We'll handle this at sub level below
    
    # Fix "|" OCR artifacts
    text = re.sub(r'\b\|\b', 'I', text)
    text = re.sub(r'^\| ', 'I ', text)
    text = re.sub(r'\n\| ', '\nI ', text)
    
    return text

# Generate overrides
overrides = {}
for a in aligned:
    idx = a['index']
    text = auto_override_v2(a['eng'], a['chi'], a['yue'])
    
    # Idiom injection pass — check chi for idioms, inject into hybrid text
    for idiom_chi in idiom_inject:
        if idiom_chi in a['chi'] and idiom_chi not in text:
            # Find a good insertion point — append after period or at end
            # Simple approach: append " — 四字成語" at end if not already present
            if len(idiom_chi) <= 6:  # short idiom, insert inline
                text = text.rstrip()
                if text.endswith('.') or text.endswith('!') or text.endswith('?'):
                    text = text[:-1] + f' — {idiom_chi}' + text[-1]
                else:
                    text += f' — {idiom_chi}'
    
    overrides[idx] = text

with open(f'{WORK}/ep{EP}_h_all.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in overrides.items()}, f, ensure_ascii=False, indent=1)

print(f"Ep{EP}: {len(overrides)} deep overrides generated")
