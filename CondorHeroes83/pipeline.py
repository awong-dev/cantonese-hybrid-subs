#!/usr/bin/env python3
"""
Reusable pipeline for Legend of the Condor Heroes subtitle processing.
Usage: python3 pipeline.py <episode_number>

This handles Steps 1, 4-7 of the pipeline.
Step 2 (full dump) and Step 3 (overrides) are done externally and passed
via ep{N}_h_all.json.
"""

import sys, re, csv, io, json, unicodedata

EP = int(sys.argv[1])
UPLOADS = '/mnt/user-data/uploads'
WORK = '/home/claude'
OUTPUT = '/mnt/user-data/outputs'

# ============================================================
# PARSING
# ============================================================

def parse_timecode(tc_str):
    tc_str = tc_str.strip().strip('"')
    m = re.match(r'(\d+):(\d+):(\d+),(\d+)', tc_str)
    if not m: return 0
    return int(m.group(1))*3600000 + int(m.group(2))*60000 + int(m.group(3))*1000 + int(m.group(4))

def parse_csv_subs(filepath):
    subs = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read().replace('\r\n', '\n').replace('\r', '\n')
    reader = csv.DictReader(io.StringIO(content))
    for row in reader:
        subs.append({
            'index': int(row['Sequence']),
            'start_ms': parse_timecode(row['TimeIn']),
            'end_ms': parse_timecode(row['TimeOut']),
            'text': row['Text'].strip()
        })
    return subs

eng = parse_csv_subs(f'{UPLOADS}/{EP}-eng.csv')
chi = parse_csv_subs(f'{UPLOADS}/{EP}-chi_tra.csv')
yue = parse_csv_subs(f'{UPLOADS}/{EP}-yue.csv')

print(f"Ep{EP}: eng={len(eng)}, chi={len(chi)}, yue={len(yue)}")

# ============================================================
# ALIGNMENT
# ============================================================

def best_overlap(target, candidates):
    best = None; best_o = 0
    for c in candidates:
        o = max(0, min(target['end_ms'], c['end_ms']) - max(target['start_ms'], c['start_ms']))
        if o > best_o: best_o = o; best = c
    if not best:
        best_d = float('inf')
        for c in candidates:
            d = min(abs(target['start_ms']-c['start_ms']), abs(target['end_ms']-c['end_ms']))
            if d < best_d and d < 2000: best_d = d; best = c
    return best

def find_yue_blocks(e_sub, yue_blocks):
    results = []
    for y in yue_blocks:
        o = max(0, min(e_sub['end_ms'], y['end_ms']) - max(e_sub['start_ms'], y['start_ms']))
        if o > 0: results.append(y)
    if not results:
        for y in yue_blocks:
            d = min(abs(e_sub['start_ms']-y['start_ms']), abs(e_sub['start_ms']-y['end_ms']),
                    abs(e_sub['end_ms']-y['start_ms']))
            if d < 2000: results.append(y); break
    return results

aligned = []
for e in eng:
    cm = best_overlap(e, chi)
    ym = find_yue_blocks(e, yue)
    yue_end = max((y['end_ms'] for y in ym), default=0) if ym else 0
    yue_text = ' '.join(y['text'] for y in ym) if ym else ''
    aligned.append({
        'index': e['index'], 'start_ms': e['start_ms'], 'end_ms': e['end_ms'],
        'eng': e['text'], 'chi': cm['text'] if cm else '', 'yue': yue_text,
        'yue_end_ms': yue_end,
    })

# Save aligned
with open(f'{WORK}/ep{EP}_aligned.json', 'w', encoding='utf-8') as f:
    json.dump(aligned, f, ensure_ascii=False, indent=1)

# ============================================================
# FULL DUMP
# ============================================================

print(f"\n=== FULL DUMP Ep{EP} ({len(aligned)} subs) ===")
for a in aligned:
    e = a['eng'].replace('\n', ' // ')
    c = a['chi'].replace('\n', ' // ')
    y = a['yue'].replace('\n', ' // ')[:80] if a['yue'] else ''
    print(f"{a['index']}|{e}|{c}|{y}")

print(f"\n=== END DUMP ===")
