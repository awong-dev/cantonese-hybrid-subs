#!/usr/bin/env python3
"""Pre-build lint for ep{N}_h_all.json and ep{N}_extras_add.json.

Two checks:

1. **Concat-trap patterns** — scans the finalised hybrid overrides for known
   CJK-leak concat patterns catalogued in STYLE.md §19 and the SESSION-NOTES
   Watch List. Flags each potential issue with a sub index and a suggested fix.
   The patterns here are ones that prior sessions discovered produce leaks
   AFTER build.py's prefix-ordering guard fires.

2. **Overlay entries unknown to STYLE.md** — scans `ep{N}_extras_add.json`
   entries and flags any CJK key that isn't in STYLE.md's §5 / §6 / §8 / §10
   catalogues. STYLE.md §7 says those lists are exhaustive: if a phrase isn't
   on them, it stays in English. Overlay entries that don't match any catalogue
   need reviewer attention — either promote the entry to STYLE.md (if it's a
   legitimate addition) or drop it from the hybrid (if it should have been
   English all along). This check catches the Ep20-style "如意燈 kept as CJK
   when it should have been 'lucky lanterns' in English" failure.

Does NOT modify any files — output is diagnostic only.

Usage:
    python3 lint_overrides.py <episode_number>

Exit status:
    0  no issues
    1  issues found (non-fatal — reviewer should inspect and decide)
"""

import sys, json, re, os

WORK = '/home/claude'

# ============================================================
# Common-noun-rendering heuristic (Check 2)
# ============================================================
# STYLE.md §7 says hybrid CJK is for names / titles / places / idioms / terms-
# of-art. Common nouns ("lucky lanterns", "a bank", "the court") should render
# as English. The heuristic below checks an overlay entry's English rendering
# and returns True if it looks like a common noun — flagging the CJK key as a
# probable §7 violation.
#
# Definition of "looks common":
#   - Starts with a lowercase word (excluding articles), OR
#   - Starts with "the"/"a"/"an" followed by lowercase words only, OR
#   - First word is Capitalized but ONLY first word (Capital + lowercase words)
#
# Definition of "looks proper":
#   - Contains a capitalized word at position ≥ 1 (after first word) —
#     signals name/place/title ("Lord Ngok", "Uncle Ngok", "the Lantern Festival",
#     "the Ceoi-hung Brothel", "Elder Paang", "Young Master")
#   - Is a single capitalized word ("Boss", "Waiter", "Madam" — address terms)
#
# This is heuristic, not rule-based. It catches the Ep20 如意燈 case by noting
# that "lucky lanterns" has no capitalized second word, whereas 岳王廟's
# rendering "the Ngok Wong Temple" has "Ngok Wong Temple" capitalized after
# the article. False-positive rate on Ep20: 1 out of 35 tested renderings.

def _looks_like_common_noun(eng):
    """True if the English rendering looks like a common noun that probably
    should have stayed English rather than being preserved as CJK in hybrid."""
    eng = eng.strip().strip('"\'')
    if not eng:
        return False
    tokens = eng.split()
    if not tokens:
        return False
    # Normalise tokens by stripping punctuation for capitalisation checks
    clean = [re.sub(r"[^a-zA-Z]", "", t) for t in tokens]
    # If ANY token past position 0 starts with a capital letter, this looks
    # like a proper-noun rendering.
    for t in clean[1:]:
        if t and t[0].isupper():
            return False
    # Only the first word can be capitalized. A single capitalized word is
    # typically an address-term category ("Boss", "Waiter", "Master") and
    # shouldn't flag. Multi-word with only first word capitalized ("Lucky
    # lanterns") IS the common-noun pattern we want to flag.
    if clean and clean[0] and clean[0][0].isupper() and len(clean) == 1:
        return False
    # First word lowercase OR Capital+lowercase-multiword → looks common
    return True

# ============================================================
# CONCAT-TRAP RULES (Check 1)
# ============================================================
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

    # Check 1 — concat-trap pattern scan
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

    check1_had_issues = bool(issues)
    if not issues:
        print(f"Ep{ep} concat-trap lint: ✓ no known concat-trap patterns found")
    else:
        print(f"Ep{ep} concat-trap lint: ⚠ {len(issues)} potential concat-trap issue(s)")
        print("=" * 70)
        from collections import defaultdict
        by_rule = defaultdict(list)
        for idx, desc, matched, fix, text in issues:
            by_rule[desc].append((idx, matched, fix, text))
        for desc, entries in by_rule.items():
            print(f"\n■ {desc}  ({len(entries)} occurrence(s))")
            print(f"  Fix: {entries[0][2]}")
            for idx, matched, _, text in entries[:5]:
                snippet = text.replace('\n', ' // ')[:80]
                print(f"    sub {idx}: matched '{matched}' in: {snippet}")
            if len(entries) > 5:
                print(f"    ... and {len(entries) - 5} more")
        print("\nThese are NON-FATAL warnings. Fix by registering the compounds in")
        print(f"ep{ep}_extras_add.json, then re-run shared_extras.py and build.py.")

    # ============================================================
    # Check 2 — overlay entries whose English rendering looks like a common noun
    # ============================================================
    # STYLE.md §7: "The CJK requirements above are exhaustive — if a phrase
    # isn't on one of these lists, it stays in English." Since enumerating those
    # lists exhaustively at lint time is brittle, this check uses a heuristic:
    # if an overlay entry's English rendering looks like a common noun ("lucky
    # lanterns", "a bank", "the court"), the CJK was probably preserved by
    # mistake — Ep20 如意燈 → "lucky lanterns" is the canonical example.
    # Renderings that look proper-noun-shaped ("Lord Ngok", "the Ceoi-hung
    # Brothel", "Elder Paang") are not flagged.
    check2_had_issues = False
    print()  # blank line between checks
    if not overlay_keys:
        print(f"Ep{ep} common-noun lint: ✓ no overlay file (nothing to check)")
    else:
        # Only flag overlay entries that are actually used as CJK in the hybrid.
        # Dead entries (registered in overlay but the reviewer rendered the
        # English directly in the override) don't violate STYLE.md §7.
        hybrid_text = ' '.join(h_all.values())

        # Build lookup from overlay: CJK → English rendering (prefer jy; yl
        # typically carries the same English for common nouns).
        overlay_eng = {}
        if os.path.exists(overlay_path):
            try:
                with open(overlay_path, 'r', encoding='utf-8') as f:
                    overlay = json.load(f)
                overlay.pop('__comment__', None)
                overlay_eng = dict(overlay.get('jy', {}))
                # Merge yl entries that aren't already in jy (rare)
                for k, v in overlay.get('yl', {}).items():
                    overlay_eng.setdefault(k, v)
            except json.JSONDecodeError:
                pass

        flagged = []
        for k in sorted(overlay_keys):
            if k not in hybrid_text:
                continue  # dead entry; skip
            eng = overlay_eng.get(k, '')
            if _looks_like_common_noun(eng):
                flagged.append((k, eng))

        if not flagged:
            print(f"Ep{ep} common-noun lint: ✓ no overlay entries look like "
                  f"common-noun renderings")
        else:
            check2_had_issues = True
            print(f"Ep{ep} common-noun lint: ⚠ {len(flagged)} overlay "
                  f"entr{'y' if len(flagged) == 1 else 'ies'} whose English "
                  f"rendering looks like a common noun")
            print("=" * 70)
            print("STYLE.md §7 rule: 'The CJK requirements above are exhaustive — if a phrase")
            print("isn't on one of these lists, it stays in English.' Entries below were kept")
            print("as CJK in the hybrid, but their English rendering looks like a common noun —")
            print("suggesting they should have been rendered as English in the hybrid instead.")
            print()
            for k, eng in flagged:
                using_subs = [int(idx) for idx, txt in h_all.items() if k in txt]
                sub_summary = (
                    f"subs {using_subs[:3]}" +
                    (f" +{len(using_subs)-3} more" if len(using_subs) > 3 else "")
                )
                print(f"  {k:<10} → {eng!r:<40}  ({sub_summary})")
            print()
            print("Action for each entry:")
            print("  (a) Genuine idiom/term-of-art → promote to STYLE.md §8/§10 and ")
            print("      verify the hybrid rendering fits the CJK+gloss convention if applicable.")
            print("      BEFORE choosing (a), confirm the phrase meets STYLE §10 admission-gate")
            print("      criteria 1–4: fixed 四字成語 in standard idiom dictionaries; specific")
            print("      classical-text source (論語, 左傳, 史記, etc.); named 俗語 with cultural")
            print("      weight English can't carry; poetic/elegiac couplet from identifiable")
            print("      literary tradition. Historical provenance alone does NOT qualify —")
            print("      the Ep1 莫須有 slip was a phrase with historical pedigree (秦檜's")
            print("      trumped-up charge against 岳飛) that nonetheless failed the admission")
            print("      gate because its standard English rendering is a plain adjective")
            print("      (\"trumped-up\"), not a culturally-weighted literary allusion.")
            print("  (b) Common noun kept in CJK by mistake → drop from overlay, edit the")
            print("      affected hybrid subs to use the English rendering instead.")
            print("  (c) Character voice / flavour phrase (like 臭要飯的) → judgment call;")
            print("      promote to STYLE.md §5/§8 if recurring enough to warrant catalogue entry.")
            print()
            print("  Default stance: when the rendering test suggests (b), choose (b).")
            print("  The temptation to keep CJK-for-fidelity is real but over-using CJK trains")
            print("  readers to skim past the Chinese (STYLE.md §7 rule of thumb).")

    if check1_had_issues or check2_had_issues:
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
