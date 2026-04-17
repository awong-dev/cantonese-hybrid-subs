import json, sys

ep = sys.argv[1]
extras = {
    'jy': {
        '歐陽': 'Au-Joeng', '郭': 'Gwok', '陸': 'Luk',
        '老頑童': 'Overgrown Child', '老毒物': 'Old Venom',
        '周大哥': '週-daai-go', '大哥': 'Big Brother',
        '賴蛤蟆': 'the Old Toad',
        '傻小子': 'that silly boy',
        '七兄': 'Brother Seven', '克兒': 'Hak-ji',
        '黃島主': 'Island Lord Wong', '島主': 'Island Lord',
        '靖兒': 'Zing-ji', '康兒': 'Hong-ji',
        '靈智上人': 'Ling-zi Soeng-jan', '仙翁': 'the Immortal Elder',
        '歐陽世兄': 'Brother Au-Joeng', '父王': 'Royal Father',
        '白駝山': 'White Camel Mountain',
        '閻王爺': 'the King of Hell',
        '藥師兄': 'Brother Joek-si',
        '阿衡': 'Aa-Hang',
    },
    'yl': {
        '歐陽': 'Au-Yeung', '郭': 'Gwok', '陸': 'Luk',
        '老頑童': 'Overgrown Child', '老毒物': 'Old Venom',
        '周大哥': '週-daaih-go', '大哥': 'Big Brother',
        '賴蛤蟆': 'the Old Toad',
        '傻小子': 'that silly boy',
        '七兄': 'Brother Seven', '克兒': 'Hak-yi',
        '黃島主': 'Island Lord Wong', '島主': 'Island Lord',
        '靖兒': 'Jing-yi', '康兒': 'Hong-yi',
        '靈智上人': 'Lihng-ji Seuhng-yahn', '仙翁': 'the Immortal Elder',
        '歐陽世兄': 'Brother Au-Yeung', '父王': 'Royal Father',
        '白駝山': 'White Camel Mountain',
        '閻王爺': 'the King of Hell',
        '藥師兄': 'Brother Yeuhk-si',
        '阿衡': 'Aa-Hahng',
    }
}
with open(f'/home/claude/ep{ep}_extra.json', 'w', encoding='utf-8') as f:
    json.dump(extras, f, ensure_ascii=False, indent=1)
print(f'Ep{ep} extras saved')
