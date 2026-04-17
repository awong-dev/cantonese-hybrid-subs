#!/usr/bin/env python3
"""
Build three SRT variants from overrides.
Usage: python3 build.py <episode_number>
Requires: ep{N}_aligned.json and ep{N}_h_all.json in /home/claude/
"""

import sys, re, csv, io, json, unicodedata

EP = int(sys.argv[1])
WORK = '/home/claude'
OUTPUT = '/mnt/user-data/outputs'

# Load aligned data and overrides
with open(f'{WORK}/ep{EP}_aligned.json', 'r', encoding='utf-8') as f:
    aligned = json.load(f)
with open(f'{WORK}/ep{EP}_h_all.json', 'r', encoding='utf-8') as f:
    overrides = {int(k): v for k, v in json.load(f).items()}

assert len(overrides) == len(aligned), f"Override count {len(overrides)} != aligned {len(aligned)}"

# ============================================================
# CONVERSION TABLES
# ============================================================

names_jy = {}; names_yl = {}
with open('/home/claude/PersonalNamesUpdated.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ch = row['Chinese'].strip()
        names_jy[ch] = row['Jyutping'].strip()
        names_yl[ch] = row['Yale'].strip()

# Common idioms
idioms = {
    '死罪可免，活罪難逃': 'the death penalty is waived, but punishment cannot be escaped',
    '男歡女愛，天公地道': 'love between a man and a woman is perfectly natural',
    '幫人幫到底，送佛送到西': 'help a person to the end, escort the Buddha all the way west',
    '逢凶化吉': 'turn danger into fortune', '濟世扶危': 'helping those in danger',
    '傻頭傻腦': 'silly and dim-witted', '利字當頭': 'when gain comes first',
    '何樂而不為': 'why not?', '山水有相逢': 'paths will cross again',
    '推宮換血': 'a blood exchange', '名利': 'fame and gain',
    '不見棺材不流淚': "won't cry till you see the coffin",
    '以牙還牙': 'an eye for an eye', '投鼠忌器': "afraid to strike the rat for fear of breaking the vase",
    '人之將死其言也善': 'when a man is dying, his words are kind',
}

# Common terms
terms = {
    '桃花陣': 'the Peach Blossom Formation', '桃花島': 'Peach Blossom Island',
    '歸雲莊': 'Guiyun Manor', '千年蔘王': 'the Thousand-Year Ginseng King',
    '大衍數': 'the Dayan Numbers', '全真七子': 'the Seven Masters of Quanzhen',
    '全真教': 'the Quanzhen Sect', '江湖': 'the martial world',
    '降龍十八掌': 'the Eighteen Dragon-Subduing Palms',
    '九陰白骨爪': 'the Jiuyin Baigu Claw', '九陰真經': 'the Jiuyin Manual',
    '輕功': 'qinggong', '武林': 'the martial world',
    '丐幫': 'the Beggars Sect', '鐵掌幫': 'the Iron Palm Sect',
    '花雕': 'Huadiao', '女兒紅': 'Nu-er Hong',
    '太湖': 'Lake Tai', '宜興': 'Yixing', '臨安': "Lin'an",
    '大理': 'Dali', '蒙古': 'Mongolia',
}

# Titles
titles_jy = {
    '駙馬爺': 'the Prince Consort', '駙馬': 'the Prince Consort',
    '金刀駙馬': 'the Golden Prince Consort',
    '小王爺': 'the Young Prince', '王爺': 'Your Highness',
    '師父': 'Master', '師姊': 'Senior Sister', '師妹': 'Junior Sister',
    '大哥': 'Big Brother', '七公': 'Seven Elder', '幫主': 'the Chief',
    '前輩': 'senior', '二叔': 'Second Uncle',
    '少莊主': 'Young Master', '莊主': 'the Manor Lord',
    '閻王爺': 'the King of Hell', '老叫化子': 'Old Beggar',
    '阿彌陀佛': 'Amitabha',
    '靖哥哥': 'Zing-gogo', '蓉兒': 'Jung-ji', '康兒': 'Hong-ji',
    '靖兒': 'Zing-ji',
    '阿靖': 'Aa-Zing', '阿康': 'Hong',
    '郭大哥': 'Brother Gwok', '歐陽兄': 'Brother Au-Joeng',
    '洪前輩': 'Senior Hung', '黃老邪': 'Old Heretic Wong', '老邪': 'Old Heretic',
    '黃姑娘': 'Miss Wong', '穆姑娘': 'Miss Muk',
    '丘道長': 'Taoist Jau',
    '娘親': 'Mother', '阿爹': 'Father',
    '王子': 'the Prince', '公主': 'the Princess',
}
titles_yl = dict(titles_jy)  # Start with copy, override differences
titles_yl.update({
    '靖哥哥': 'Jing-gogo', '蓉兒': 'Yuhng-yi', '康兒': 'Hong-yi',
    '靖兒': 'Jing-yi',
    '阿靖': 'Aa-Jing',
    '歐陽兄': 'Brother Au-Yeung',
    '洪前輩': 'Senior Huhng',
    '丘道長': 'Taoist Yau',
})

# Episode-specific extra mappings (loaded if file exists)
extra_jy = {}; extra_yl = {}
try:
    with open(f'{WORK}/ep{EP}_extra.json', 'r', encoding='utf-8') as f:
        extras = json.load(f)
    extra_jy = extras.get('jy', {})
    extra_yl = extras.get('yl', {})
    print(f"Loaded {len(extra_jy)} extra Jyutping + {len(extra_yl)} extra Yale mappings")
except FileNotFoundError:
    pass

def convert(text, system):
    result = text
    # 1. Idioms (longest first)
    for k in sorted(idioms, key=len, reverse=True):
        result = result.replace(k, idioms[k])
    # 2. Terms
    for k in sorted(terms, key=len, reverse=True):
        result = result.replace(k, terms[k])
    # 3. Titles
    tbl = titles_jy if system == 'jy' else titles_yl
    for k in sorted(tbl, key=len, reverse=True):
        result = result.replace(k, tbl[k])
    # 4. Names from CSV
    ntbl = names_jy if system == 'jy' else names_yl
    for k in sorted(ntbl, key=len, reverse=True):
        result = result.replace(k, ntbl[k])
    # 5. Episode-specific extras
    etbl = extra_jy if system == 'jy' else extra_yl
    for k in sorted(etbl, key=len, reverse=True):
        result = result.replace(k, etbl[k])
    # Fix double articles
    result = result.replace('a the ', 'the ').replace('a The ', 'The ')
    return result

# ============================================================
# BUILD VARIANTS
# ============================================================

hybrid_subs = []; jy_subs = []; yl_subs = []
for a in aligned:
    idx = a['index']
    h = overrides[idx]
    j = convert(h, 'jy')
    y = convert(h, 'yl')
    for lst, txt in [(hybrid_subs, h), (jy_subs, j), (yl_subs, y)]:
        lst.append({'index': idx, 'start_ms': a['start_ms'], 'end_ms': a['end_ms'],
                     'text': txt, 'yue_end_ms': a.get('yue_end_ms', 0)})

# ============================================================
# DURATION EXTENSION
# ============================================================

def extend(subs):
    ext = 0
    for i, s in enumerate(subs):
        text = s['text'].replace('\n', ' ')
        chars = len(text)
        if chars == 0: continue
        needed = max(int(chars / 15 * 1000), 1000)
        if needed <= s['end_ms'] - s['start_ms']: continue
        new_end = s['start_ms'] + needed
        if s['yue_end_ms'] > 0:
            new_end = max(new_end, min(s['yue_end_ms'], s['start_ms'] + needed + 2000))
        if i + 1 < len(subs):
            new_end = min(new_end, subs[i+1]['start_ms'])
        if new_end > s['end_ms']:
            s['end_ms'] = new_end; ext += 1
    return ext

eh = extend(hybrid_subs); ej = extend(jy_subs); ey = extend(yl_subs)
print(f"Duration extended: h={eh}, j={ej}, y={ey}")

# ============================================================
# VALIDATION
# ============================================================

def ms_to_srt(ms):
    h = ms//3600000; ms %= 3600000; m = ms//60000; ms %= 60000
    s = ms//1000; ms %= 1000; return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def write_srt(subs, fp):
    with open(fp, 'w', encoding='utf-8') as f:
        for s in subs:
            f.write(f"{s['index']}\n{ms_to_srt(s['start_ms'])} --> {ms_to_srt(s['end_ms'])}\n{s['text']}\n\n")

errors = []

# Count
for name, subs in [('h', hybrid_subs), ('j', jy_subs), ('y', yl_subs)]:
    if len(subs) != len(aligned):
        errors.append(f"{name}: count {len(subs)} != {len(eng)}")

# CJK in romanised
for name, subs in [('jyutping', jy_subs), ('yale', yl_subs)]:
    cjk = [(s['index'], next((ch for ch in s['text'] if '\u4e00'<=ch<='\u9fff'), ''), s['text'][:60])
           for s in subs if any('\u4e00'<=ch<='\u9fff' for ch in s['text'])]
    if cjk:
        errors.append(f"{name}: {len(cjk)} CJK subs")
        for idx, ch, txt in cjk[:15]:
            print(f"  CJK {name} sub {idx}: '{ch}' in: {txt}")

# Pinyin in hybrid
pinyins = ['Guo Jing', 'Huang Rong', 'Rong-er', 'Yang Kang', 'Ouyang Feng', 'Ouyang Ke',
           'Hong Qigong', 'Huang Yaoshi', 'Nianci', 'Huazheng', 'Tuolei']
py = [(s['index'], pn) for s in hybrid_subs for pn in pinyins if pn in s['text']]
if py: errors.append(f"Pinyin in hybrid: {py[:5]}")

# go-go
gg = [s['index'] for v in [jy_subs, yl_subs] for s in v if 'go-go' in s['text']]
if gg: errors.append(f"go-go: {gg}")

# Overlaps
for name, subs in [('h', hybrid_subs), ('j', jy_subs), ('y', yl_subs)]:
    ov = sum(1 for i in range(len(subs)-1) if subs[i]['end_ms'] > subs[i+1]['start_ms'])
    if ov: errors.append(f"{name}: {ov} overlaps")

if errors:
    print(f"\n⚠ ERRORS ({len(errors)}):")
    for e in errors: print(f"  {e}")
    print("\nWriting files anyway — may need CJK fix pass")
else:
    print("\n✓ ALL VALIDATION PASSED")

# Write
write_srt(hybrid_subs, f'{OUTPUT}/{EP}-eng-hybrid.srt')
write_srt(jy_subs, f'{OUTPUT}/{EP}-eng-jyutping.srt')
write_srt(yl_subs, f'{OUTPUT}/{EP}-eng-yale.srt')

# Verify final file integrity
for variant in ['hybrid', 'jyutping', 'yale']:
    fp = f'{OUTPUT}/{EP}-eng-{variant}.srt'
    with open(fp, 'r') as f:
        count = len(re.findall(r'^\d+$', f.read(), re.MULTILINE))
    print(f"  {variant}: {count} entries written")

print(f"\n✓ Ep{EP} complete — files in {OUTPUT}/")
