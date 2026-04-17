#!/usr/bin/env python3
"""Apply manual overrides from a TSV file to ep{N}_h_all.json.

TSV format (tab-separated, one override per line):

    <index>\t<English text with \\n for embedded newlines>

Lines starting with '#' are treated as comments and ignored. Empty lines
are ignored. The index must be an integer matching an entry in
ep{N}_h_all.json. The text column's literal '\\n' sequences are converted
to real newlines on apply.

Rationale for the TSV format (v10):
  Prior bundle versions had the reviewer emit overrides as a Python
  literal dict inside a patch script. That pattern cost ~1.3× the raw
  text in context due to quoting/escaping/dict-syntax overhead. TSV is
  a flat 'index\\ttext' table — no escaping beyond literal '\\n' for
  newlines — so it's roughly the minimum viable format for this data.

Usage:
    python3 apply_overrides.py <episode_number>

Reads:   /home/claude/ep{N}_overrides.tsv
         /home/claude/ep{N}_h_all.json
Writes:  /home/claude/ep{N}_h_all.json   (merged in-place)
"""

import sys, json, os

WORK = '/home/claude'

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 apply_overrides.py <episode_number>")
        sys.exit(1)
    ep = int(sys.argv[1])

    h_path   = f'{WORK}/ep{ep}_h_all.json'
    tsv_path = f'{WORK}/ep{ep}_overrides.tsv'

    if not os.path.exists(h_path):
        raise SystemExit(f"ERROR: {h_path} not found. Run auto_override_v2.py first.")
    if not os.path.exists(tsv_path):
        raise SystemExit(
            f"ERROR: {tsv_path} not found.\n"
            f"Expected format: one override per line, tab-separated:\n"
            f"  <index>\\t<text with \\\\n for embedded newlines>\n"
            f"Lines starting with '#' are comments."
        )

    with open(h_path, 'r', encoding='utf-8') as f:
        h_all = json.load(f)

    overrides = {}
    with open(tsv_path, 'r', encoding='utf-8') as f:
        for lineno, raw in enumerate(f, 1):
            line = raw.rstrip('\n')
            if not line.strip() or line.startswith('#'):
                continue
            if '\t' not in line:
                raise SystemExit(
                    f"ERROR: {tsv_path} line {lineno}: no tab found.\n"
                    f"Expected: <index>\\t<text>.  Got: {line!r}"
                )
            idx_str, text = line.split('\t', 1)
            idx_str = idx_str.strip()
            if not idx_str.isdigit():
                raise SystemExit(
                    f"ERROR: {tsv_path} line {lineno}: "
                    f"index '{idx_str}' is not a positive integer."
                )
            if idx_str not in h_all:
                raise SystemExit(
                    f"ERROR: {tsv_path} line {lineno}: "
                    f"index {idx_str} not found in {h_path} "
                    f"(episode has {len(h_all)} subs)."
                )
            # Convert literal \n sequences to real newlines
            text = text.replace('\\n', '\n')
            overrides[idx_str] = text

    if not overrides:
        print(f"No overrides applied (empty or comment-only TSV).")
        return

    # Merge: overrides replace entries in h_all
    for k, v in overrides.items():
        h_all[k] = v

    with open(h_path, 'w', encoding='utf-8') as f:
        json.dump(h_all, f, ensure_ascii=False, indent=1)

    print(f"Ep{ep}: applied {len(overrides)} overrides from TSV "
          f"(of {len(h_all)} total subs)")
    print(f"Preserved Step 3 output for {len(h_all) - len(overrides)} subs")

if __name__ == '__main__':
    main()
