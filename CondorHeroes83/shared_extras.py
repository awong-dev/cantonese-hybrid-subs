#!/usr/bin/env python3
"""Build ep{N}_extra.json by merging the shared baseline with an optional
episode-specific overlay.

Inputs:
  extras_baseline.json          — shared baseline (this file ships with bundle)
  ep{N}_extras_add.json         — episode overlay (OPTIONAL; create if the
                                   episode introduces new CJK terms not in
                                   the baseline)

Output:
  /home/claude/ep{N}_extra.json  — what build.py consumes

Overlay format (OPTIONAL file, same schema as baseline):
  {
    "jy": { "<CJK>": "<Jyutping rendering>", ... },
    "yl": { "<CJK>": "<Yale rendering>", ... }
  }

Overlay keys take precedence over baseline keys when they collide.

Rationale (v10):
  Prior bundle versions kept the entire baseline PLUS every episode's
  new entries inside shared_extras.py — so each episode's builder file
  duplicated the whole baseline. With ~90 baseline keys × 2 variants
  (jy + yl) that's ~180 lines of duplicated boilerplate per episode.
  Splitting baseline (data) from overlay (per-episode delta) cuts the
  per-episode file to just the new entries, typically 10–40 lines.

Usage:
  python3 shared_extras.py <episode_number>
  (kept as shared_extras.py for CLI compatibility with earlier bundles)
"""

import sys, json, os

WORK = '/home/claude'

def _load_baseline():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'extras_baseline.json')
    if not os.path.exists(path):
        raise SystemExit(
            f"ERROR: {path} not found. Every handoff bundle must ship "
            f"extras_baseline.json alongside this script."
        )
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Drop the comment key if present
    data.pop('__comment__', None)
    if 'jy' not in data or 'yl' not in data:
        raise SystemExit(
            f"ERROR: {path} malformed. Expected top-level keys 'jy' and 'yl'."
        )
    return data

def _load_overlay(ep):
    path = f'{WORK}/ep{ep}_extras_add.json'
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data.pop('__comment__', None)
    if 'jy' not in data or 'yl' not in data:
        raise SystemExit(
            f"ERROR: {path} malformed. Expected top-level keys 'jy' and 'yl'."
        )
    return data

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 shared_extras.py <episode_number>")
        sys.exit(1)
    ep = int(sys.argv[1])

    baseline = _load_baseline()
    overlay  = _load_overlay(ep)

    merged = {'jy': dict(baseline['jy']),
              'yl': dict(baseline['yl'])}

    added_jy = added_yl = 0
    if overlay:
        for k, v in overlay['jy'].items():
            if k not in merged['jy']:
                added_jy += 1
            merged['jy'][k] = v
        for k, v in overlay['yl'].items():
            if k not in merged['yl']:
                added_yl += 1
            merged['yl'][k] = v

    out_path = f'{WORK}/ep{ep}_extra.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=1)

    total_jy = len(merged['jy'])
    total_yl = len(merged['yl'])
    if overlay:
        print(f"Ep{ep} extras: baseline ({len(baseline['jy'])} jy, "
              f"{len(baseline['yl'])} yl) + overlay (+{added_jy} jy, "
              f"+{added_yl} yl new) = {total_jy} jy, {total_yl} yl total")
    else:
        print(f"Ep{ep} extras: baseline only ({total_jy} jy, {total_yl} yl). "
              f"No overlay ep{ep}_extras_add.json found.")

if __name__ == '__main__':
    main()
