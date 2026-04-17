#!/usr/bin/env python3
"""Pre-build lint for ep{N}_h_all.json.

Scans the finalised hybrid overrides for known CJK-leak concat patterns
catalogued in STYLE.md §19 and the SESSION-NOTES Watch List. Flags each
potential issue with a sub index and a suggested fix. Does NOT modify
any files — output is diagnostic only.

The patterns checked here are the ones that prior sessions discovered
produce leaks AFTER build.py's prefix-ordering guard fires — so this
lint runs on ep{N}_h_all.json (the hybrid content) and catches patterns
whose leak manifests in the romanised output, not the hybrid one.

Usage:
    python3 lint_overrides.py <episode_number>

Exit status:
    0  no issues
    1  issues found (non-fatal — reviewer should inspect and decide)
"""

import sys, json, re, os

WORK = '/home/claude'

# Each rule: (regex, description, suggested fix).
# Regex operates on each hybrid sub's text. Matches mean a LIKELY leak
# in the romanised output unless the matched compound is already registered
# in ep{N}_extra.json.
RULES = [
    # --- v10 Ep26 findings promoted from Watch List ---
    (r'裘老前輩|裘前輩',
     '"裘老前輩" / "裘前輩" — surname + title compound',
     'Register "裘老前輩 → Elder Kau/Kauh" and "裘前輩 → Senior Kau/Kauh" '
     'in ep{N}_extras_add.json (both jy and yl). Otherwise produces '
     'KauElder / KauhElder concat in romanised.'),
    (r'(?<![\u4e00-\u9fff])[\u4e00-\u9fff]大哥(?![\u4e00-\u9fff])',
     '"<Surname>大哥" compound (X大哥 where X is a single CJK char)',
     'Register the full compound (e.g. "張大哥 → Brother Zoeng/Jeung") '
     'in ep{N}_extras_add.json. Bare 大哥 alone will leave the surname '
     'stranded in romanised output.'),
    (r'我爹|你爹|我娘|你娘',
     'possessive + bare-kinship compound (我爹/你爹/我娘/你娘)',
     'Register the compound ("我爹 → my father", etc.) in either '
     'extras_baseline.json (if globally relevant) or the episode overlay.'),
    (r'大金國|大宋(?=[，。！？,.\s]|$)',
     '"大金國" / "大宋" — 大- prefixed dynasty/nation compound',
     'Register "大金國 → the great Jin empire" and "大宋 → the great Song" '
     'in the overlay so "大" doesn\'t strand when 金國/宋 converts first.'),
    (r'我柯鎮惡|我裘千仞|我郭靖|我黃蓉|我歐陽',
     'emphatic-self compound ("我<FullName>" — a character announces themself)',
     'Register "我<FullName> → I, <RomanisedName>" in the overlay. '
     'Otherwise 我 strands as CJK when the name converts.'),
    # --- Pre-v10 patterns from STYLE.md §19 ---
    (r'(?<![\u4e00-\u9fff])大師父(?![\u4e00-\u9fff])',
     '"大師父" — "First Master" compound',
     'Register "大師父 → First Master" in the overlay; already known pattern '
     '(STYLE.md §19). Without it, 師父 converts first and leaves 大 stranded.'),
    (r'Yeung叔叔|Yeung兄|Wong叔叔|Wong兄|Luk兄|Gwok兄',
     '<RomanisedSurname><CJK suffix> — name-with-title concat',
     'This pattern suggests a surname converted but the trailing Chinese '
     'title didn\'t. Register the full compound (e.g. "楊叔叔 → Uncle Yeung") '
     'or verify the compound is in STYLE.md §6.'),
]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 lint_overrides.py <episode_number>")
        sys.exit(1)
    ep = int(sys.argv[1])

    h_path = f'{WORK}/ep{ep}_h_all.json'
    if not os.path.exists(h_path):
        raise SystemExit(f"ERROR: {h_path} not found. Run auto_override_v2.py first.")

    with open(h_path, 'r', encoding='utf-8') as f:
        h_all = json.load(f)

    # Load overlay (if any) so we can skip rules whose compounds are already registered
    overlay_path = f'{WORK}/ep{ep}_extras_add.json'
    overlay_keys = set()
    if os.path.exists(overlay_path):
        try:
            with open(overlay_path, 'r', encoding='utf-8') as f:
                overlay = json.load(f)
            overlay.pop('__comment__', None)
            overlay_keys = set(overlay.get('jy', {}).keys()) | set(overlay.get('yl', {}).keys())
        except json.JSONDecodeError:
            pass

    # Load baseline too
    baseline_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'extras_baseline.json')
    baseline_keys = set()
    if os.path.exists(baseline_path):
        try:
            with open(baseline_path, 'r', encoding='utf-8') as f:
                baseline = json.load(f)
            baseline.pop('__comment__', None)
            baseline_keys = set(baseline.get('jy', {}).keys()) | set(baseline.get('yl', {}).keys())
        except json.JSONDecodeError:
            pass

    registered = overlay_keys | baseline_keys

    issues = []
    for idx_str, text in h_all.items():
        idx = int(idx_str)
        for pattern, desc, fix in RULES:
            for m in re.finditer(pattern, text):
                matched = m.group(0)
                # If the exact match is registered in extras, skip — the compound
                # will resolve cleanly. (Not perfect — doesn't catch all variants —
                # but cuts false-positive noise.)
                if matched in registered:
                    continue
                issues.append((idx, desc, matched, fix, text))

    if not issues:
        print(f"Ep{ep} lint: ✓ no known concat-trap patterns found")
        return 0

    print(f"Ep{ep} lint: ⚠ {len(issues)} potential concat-trap issue(s)")
    print("=" * 70)
    # Group by description so the reviewer sees each rule together
    from collections import defaultdict
    by_rule = defaultdict(list)
    for idx, desc, matched, fix, text in issues:
        by_rule[desc].append((idx, matched, fix, text))
    for desc, entries in by_rule.items():
        print(f"\n■ {desc}  ({len(entries)} occurrence(s))")
        # Show the fix once per rule
        print(f"  Fix: {entries[0][2]}")
        # Show up to 5 example subs
        for idx, matched, _, text in entries[:5]:
            snippet = text.replace('\n', ' // ')[:80]
            print(f"    sub {idx}: matched '{matched}' in: {snippet}")
        if len(entries) > 5:
            print(f"    ... and {len(entries) - 5} more")
    print("\nThese are NON-FATAL warnings. Fix by registering the compounds in")
    print(f"ep{ep}_extras_add.json, then re-run shared_extras.py and build.py.")
    return 1

if __name__ == '__main__':
    sys.exit(main())
