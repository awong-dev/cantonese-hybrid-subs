#!/usr/bin/env python3
"""
Deep auto-override v2.1 — applies ErrorTaxonomy learnings.
Addresses: NAME_TITLE_LEAK, IDIOM_MISSING, CHI_MEANING partial fixes.
Now confidence-tier aware: reads yue_confidence from aligned.json.

Usage: python3 auto_override_v2.py <episode_number>

Confidence behavior:
  HIGH:   Flags sub as "YUE-AUTH" — yue text takes priority over chi
          during manual review. OCR corrections from yue applied automatically.
  MEDIUM: Normal chi-authority. Yue consulted for tone/register.
  LOW:    Yue text ignored entirely. Chi-only processing.
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
    # Address forms
    'Miss Huang': '黃姑娘', 'Miss Wong': '黃姑娘',
    'Miss Cheng': '程大小姐',
    'Miss Mu': '穆姑娘',
    'Master Huang': '黃島主',
    'Island Lord': '島主',
}

# Address terms that need chi-context to fix
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
# 3. Idiom injection
# ============================================================
idiom_inject = {
    '冤家路窄': '冤家路窄', '借花敬佛': '借花敬佛',
    '棋差一著': '棋差一著', '打草驚蛇': '打草驚蛇',
    '防不勝防': '防不勝防', '臭名遠揚': '臭名遠揚',
    '勢不兩立': '勢不兩立', '沒齒難忘': '沒齒難忘',
    '拐彎抹角': '拐彎抹角', '舉手之勞': '舉手之勞',
    '人死不能復生': '人死不能復生', '後會有期': '後會有期',
    '萬萬不能': '萬萬不能', '知心朋友': '知心朋友',
    '豈有此理': '豈有此理', '指日可待': '指日可待',
    '奮不顧身': '奮不顧身', '低聲下氣': '低聲下氣',
    '一心一意': '一心一意', '天下無敵': '天下無敵',
    '心滿意足': '心滿意足', '門當戶對': '門當戶對',
    '有情人終成眷屬': '有情人終成眷屬',
    '一日為師終身為父': '一日為師終身為父',
    '無毒不丈夫': '無毒不丈夫', '施恩莫圖報': '施恩莫圖報',
    '杯酒釋前嫌': '杯酒釋前嫌', '一笑泯恩仇': '一笑泯恩仇',
    '一刀兩斷': '一刀兩斷', '喪心病狂': '喪心病狂',
    '認賊作父': '認賊作父', '江山易改本性難移': '江山易改本性難移',
    '有福同享': '有福同享', '有難同當': '有難同當',
    '寧可信其有不可信其無': '寧可信其有不可信其無',
    '蛇鼠一窩': '蛇鼠一窩', '義結金蘭': '義結金蘭',
    '化干戈為玉帛': '化干戈為玉帛', '意氣用事': '意氣用事',
    '頑固不化': '頑固不化', '女大不中留': '女大不中留',
    '大逆不道': '大逆不道', '感情用事': '感情用事',
    '既往不究': '既往不究', '不擇手段': '不擇手段',
    '忘恩負義': '忘恩負義', '夜長夢多': '夜長夢多',
    # Ep20 precedents
    '精忠報國': '精忠報國',
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
        text = text.replace(f'the {eng}', cjk)

    # Step 3: Check chi for address terms and inject CJK
    for chi_term, cjk in sorted(address_chi_map.items(), key=lambda x: len(x[0]), reverse=True):
        if chi_term in chi_text:
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
                    text = re.sub(r'\b' + re.escape(eng_ver) + r'\b', cjk, text)

    # Step 4: Idiom injection handled below at sub level

    # Fix "|" OCR artifacts
    text = re.sub(r'\b\|\b', 'I', text)
    text = re.sub(r'^\| ', 'I ', text)
    text = re.sub(r'\n\| ', '\nI ', text)

    return text

# ============================================================
# FAITHFUL-SUB HEURISTIC (v10)
# ============================================================
# Purpose: a conservative pre-filter flagging subs where the Step 3 output
# is very likely already faithful to chi+yue. Reviewer defaults to keeping
# these; Step 4 examination time concentrates on NOT-flagged subs.
#
# The heuristic is CONSERVATIVE BY DESIGN. A sub is flagged AUTO-KEEP only
# if ALL seven gates pass. A false positive (flagging a sub faithful when
# it has a register or meaning issue) is worse than a false negative
# (re-examining an already-faithful sub). When in doubt, do NOT flag.
#
# Gates:
#  (a) eng, chi, and yue are all non-empty (no sparse-source ambiguity)
#  (b) no fabrication-risk markers in eng (long parentheticals, added
#      relative clauses introduced by "which", "who was", etc., that could
#      carry invented content)
#  (c) no 四字成語 present in chi (idiom injection is Step 4 territory)
#  (d) no address term in chi that's missing from the Step 3 output
#      (仙姑 / 前輩 / 師父 / etc. — Category 3 leaks)
#  (e) yue confidence is HIGH or MEDIUM (LOW and N/A stay in the review set)
#  (f) chi-content-word overlap with Step 3 output ≥ 0.7 (Jaccard on
#      content words, stop-word filtered)
#  (g) eng and chi lengths within 1.5× of each other (strong divergence
#      suggests compression / expansion worth examining)
#
# Even when flagged, the sub is STILL present in the dump and the reviewer
# can still examine it. "AUTO-KEEP" is a priority signal, not a gate.

_STOPWORDS = {
    'a','an','the','of','to','on','in','for','with','and','or','but','at',
    'is','was','were','be','been','being','it','you','we','he','she','him','her',
    'his','our','my','your','their','this','that','these','those','so','then',
    'i','me','us','them','do','does','did','have','has','had','not','no',
    'can','will','would','could','should','just','go','going','from','as',
    'by','if','up','down','out','about','what','who','why','how','where',
}
# Address terms that must appear in the hybrid output if present in chi
# (longer before shorter for substring matching)
_ADDRESS_TERMS = [
    '靖哥哥', '蓉兒', '靖兒', '康兒', '阿爹', '阿靖', '阿康',
    '父王', '娘親', '老夫', '莊主', '少莊主', '祖師爺', '幫主',
    '小王爺', '駙馬爺',
    '師父', '師姊', '師妹', '師兄', '師弟', '師叔', '師姑',
    '前輩', '仙姑', '娘子', '老伯', '少爺', '公子', '大哥', '七公',
    '爹', '娘',
]
# Cheap 四字成語 heuristic: look for the known idiom set from idiom_inject
# (defined in this file's vocabulary above). We'll reuse it directly.

def _content_words(s):
    """Extract lowercase alphanumeric words, minus stopwords."""
    if not s: return set()
    return {w for w in re.findall(r"[a-zA-Z]+", s.lower()) if w not in _STOPWORDS}

def _chi_has_idiom(chi_text):
    """True if chi contains any idiom in the injection set."""
    for idiom in idiom_inject:
        if idiom in chi_text:
            return True
    return False

def _chi_has_address_missing_from_output(chi_text, output_text):
    """True if chi has an address term that didn't land in the Step 3 output
    (as CJK or as an English equivalent rendering)."""
    for term in _ADDRESS_TERMS:
        if term in chi_text and term not in output_text:
            # Also allow common English equivalents that didn't auto-CJK-ify.
            # If eng_equiv for this term isn't in output either, it's missing.
            english_equivs = {
                '爹': ('Father', 'father', 'dad'),
                '娘': ('Mother', 'mother', 'mom'),
                '娘親': ('Mother', 'mother'),
                '阿爹': ('Father', 'father'),
                '父王': ('Royal Father', 'Father'),
                '師父': ('Master', 'Teacher', 'teacher'),
                '前輩': ('senior', 'Senior', 'Elder'),
                '仙姑': ('Taoist Nun', 'Immortal Maiden'),
                '莊主': ('Manor Lord',),
                '少莊主': ('Young Master',),
                '幫主': ('Chief',),
                '小王爺': ('Young Prince',),
                '大哥': ('Big Brother',),
                '七公': ('Seven Elder',),
            }
            eq = english_equivs.get(term, ())
            if not any(e in output_text for e in eq):
                return True
    return False

def _has_fabrication_risk_markers(eng_text):
    """Heuristic: long parentheticals or 'which'/'who' clauses that could
    be the site of fabrication. Not a detector of fabrication — a detector
    of subs that DESERVE manual examination for fabrication risk."""
    if not eng_text: return False
    # Parentheticals longer than 20 chars
    for m in re.finditer(r'\(([^)]+)\)', eng_text):
        if len(m.group(1)) > 20:
            return True
    # ", which" / ", who" / ", whom" clauses
    if re.search(r',\s+(which|who|whom)\b', eng_text, re.IGNORECASE):
        return True
    return False

# OCR-artifact markers that show up when the chi track was OCR'd from broadcast
# subtitles. These are not CJK characters the reviewer would expect in a clean
# transcript — they're typesetting noise or quote-mark garble that survived
# OCR. Seeing any of these in a chi sub is a signal that the chi for this sub
# is partially corrupted and yue may be the cleaner witness.
#
# The specific markers are from cross-episode observation:
#   -"   — partial dash/quote junk (Ep20 subs 24, 116, 133, etc.)
#   ”“   — unbalanced typographic quotes (Ep20 sub 158, 264, 387)
#   “    — lone opening curly quote (Ep20 sub 194)
#   Y    — Latin letter amid CJK (a frequent OCR misread of 丫 etc.)
#   |    — pipe character (appears in some OCR outputs as column separator)
#   --   — double hyphen, Ep20 subs 1, 147, etc.
# Claude should still cross-check yue; this flag is a priority signal, not a verdict.
_OCR_ARTIFACT_MARKERS = ['-"', '”“', '““', '“-', '---', '--', '"-', '" -']

def _chi_has_ocr_artifact(chi_text):
    """True if chi contains any of the known typesetting-noise markers."""
    if not chi_text: return False
    for m in _OCR_ARTIFACT_MARKERS:
        if m in chi_text:
            return True
    # Latin letters embedded in CJK are also a strong OCR-artifact signal
    # (common misreads: 丫 → Y, 一 → I/|/l, 八 → V, 口 → O).
    # Only flag if chi is mostly CJK AND contains a suspicious single Latin letter.
    cjk_chars = sum(1 for c in chi_text if '\u4e00' <= c <= '\u9fff')
    latin_letters = [c for c in chi_text if c.isalpha() and c.isascii()]
    if cjk_chars >= 3 and 0 < len(latin_letters) <= 3:
        # 1-3 stray Latin letters amid ≥3 CJK chars — likely OCR
        return True
    return False

def _length_ratio_ok(eng_text, chi_text):
    """True if eng and chi are within 1.5× in character length."""
    if not eng_text or not chi_text:
        return False
    le, lc = len(eng_text), len(chi_text)
    lo, hi = min(le, lc), max(le, lc)
    return lo > 0 and (hi / lo) <= 1.5

def faithful_heuristic(eng_text, chi_text, yue_text, output_text, conf):
    """Return True if ALL seven conservative gates pass."""
    # (a) all three tracks populated
    if not eng_text or not chi_text or not yue_text:
        return False
    # (e) yue confidence acceptable
    if conf not in ('HIGH', 'MEDIUM'):
        return False
    # (b) no fabrication-risk markers in eng
    if _has_fabrication_risk_markers(eng_text):
        return False
    # (c) no idiom in chi
    if _chi_has_idiom(chi_text):
        return False
    # (d) no missing address term
    if _chi_has_address_missing_from_output(chi_text, output_text):
        return False
    # (g) length ratio sanity
    if not _length_ratio_ok(eng_text, chi_text):
        return False
    # (f) content-word overlap between chi (translated transitively via
    #     eng as proxy — chi has CJK not words) ≥ 0.7. We use eng↔output
    #     content-word overlap as the proxy, since the Step 3 output is
    #     derived from eng with CJK substitutions layered on. A high overlap
    #     means Step 3 didn't silently reshape meaning.
    eng_cw = _content_words(eng_text)
    out_cw = _content_words(output_text)
    if not eng_cw or not out_cw:
        return False
    jac = len(eng_cw & out_cw) / len(eng_cw | out_cw)
    if jac < 0.7:
        return False
    return True

# ============================================================
# Generate overrides with confidence annotations
# ============================================================
overrides = {}
confidence_annotations = {}

for a in aligned:
    idx = a['index']
    conf = a.get('yue_confidence', 'N/A')

    # Get clean yue text (strip DISCARDED prefix if present)
    yue_raw = a.get('yue', '')
    yue_clean = re.sub(r'^\[DISCARDED[^\]]*\]\s*', '', yue_raw)

    # For LOW confidence, ignore yue entirely
    if conf == 'LOW':
        yue_for_override = ''
    else:
        yue_for_override = yue_clean

    text = auto_override_v2(a['eng'], a['chi'], yue_for_override)

    # Idiom injection pass
    for idiom_chi in idiom_inject:
        # Check both chi and (for HIGH confidence) yue for idioms
        sources_to_check = [a['chi']]
        if conf == 'HIGH' and yue_clean:
            sources_to_check.append(yue_clean)

        for source in sources_to_check:
            if idiom_chi in source and idiom_chi not in text:
                text = text.rstrip()
                if text.endswith('.') or text.endswith('!') or text.endswith('?'):
                    text = text[:-1] + f' — {idiom_chi}' + text[-1]
                else:
                    text += f' — {idiom_chi}'
                break  # Don't double-inject from both sources

    overrides[idx] = text

    # Build annotation for manual review
    ann = {'confidence': conf}
    # Apply the conservative AUTO-KEEP heuristic (v10).
    # This uses the finalised text (including idiom injection) so it reflects
    # the actual Step 3 output the reviewer will see.
    auto_keep = faithful_heuristic(a['eng'], a['chi'], yue_clean, text, conf)
    ann['auto_keep'] = auto_keep

    # Per-sub flags (v14). These drive the compact flags column in ep{N}_dump.txt.
    # Each flag is the output of a heuristic that ALREADY exists in this file
    # (the faithful_heuristic() gates below); we just surface the sub-tests
    # individually so the reviewer sees WHY a sub is flagged, not just THAT it is.
    # Flags:
    #   • AUTO-KEEP passed all seven gates (quick-confirm candidate)
    #   ! eng has fabrication-risk markers (parentheticals, ", which" clauses)
    #   i chi contains an idiom from idiom_inject
    #   @ chi has an address term missing from the Step 3 output
    #   o chi contains an OCR artifact (garbled glyph / stray typesetting noise)
    #
    # Note: _length_ratio_ok() is ALSO a faithful_heuristic() gate, but it's
    # deliberately NOT surfaced here. eng:chi character ratio is >1.5× on a
    # majority of subs simply because CJK characters are information-denser
    # than English words (confirmed on Ep20: would fire on 504/587 subs).
    # Using it as a flag was tried in v14-draft and produced uninformative noise.
    # Keep it as an internal faithful_heuristic gate only.
    flags = []
    if auto_keep:
        flags.append('•')
    if _has_fabrication_risk_markers(a['eng']):
        flags.append('!')
    if _chi_has_idiom(a['chi']):
        flags.append('i')
    if _chi_has_address_missing_from_output(a['chi'], text):
        flags.append('@')
    if _chi_has_ocr_artifact(a['chi']):
        flags.append('o')
    ann['flags'] = ''.join(flags)

    if conf == 'HIGH':
        ann['note'] = 'YUE-AUTH: yue is authoritative. Compare yue vs chi — prefer yue where they differ.'
        ann['yue'] = yue_clean
        ann['chi'] = a['chi']
    elif conf == 'MEDIUM':
        ann['note'] = 'CHI-AUTH: chi is authoritative. Use yue for tone/register guidance.'
        ann['yue'] = yue_clean
    elif conf == 'LOW':
        ann['note'] = 'YUE-DISCARDED: ASR unreliable. Chi-only.'
    if a.get('yue_avg_logprob') is not None:
        ann['avg_logprob'] = a['yue_avg_logprob']
    confidence_annotations[idx] = ann

with open(f'{WORK}/ep{EP}_h_all.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in overrides.items()}, f, ensure_ascii=False, indent=1)

# Save confidence annotations separately for manual review reference
with open(f'{WORK}/ep{EP}_confidence.json', 'w', encoding='utf-8') as f:
    json.dump({str(k): v for k, v in confidence_annotations.items()}, f, ensure_ascii=False, indent=1)

# ============================================================
# Emit ep{EP}_dump.txt — reviewer-facing examination artifact (v14 format)
# ============================================================
# Format (v14):
#   <idx>|<conf>|<flags>         (one-line header per sub; [T-ADJ] suffixed if timing adjusted)
#   E <eng>
#   C <chi>
#   Y <yue>                       (may be "[see N]" for dedup; omitted if empty)
#
# Blank-line-plus-scene-marker inserted wherever consecutive-sub end→start
# gap exceeds 5s: `—— gap Ns ——`
#
# Yue dedup: when a yue text is the same (after strip) across multiple
# consecutive chi subs, it's shown only at the sub whose chi-window has the
# STRONGEST timing overlap with the yue content; other subs in the cluster
# show `Y [see <idx>]`.
#
# Flags (single-character column, see the flag-construction block above):
#   •  AUTO-KEEP — all seven faithful_heuristic() gates passed
#   !  fabrication-risk markers in eng
#   i  chi contains an idiom
#   @  chi has an address term missing from the Step 3 output
#   o  chi has OCR-artifact noise
#   L  eng vs chi length ratio > 1.5×

# --- (a) Yue-dedup pass: for each non-empty yue string, find the sub with
#         the strongest timing overlap, and map every other sub with that same
#         yue string to `[see N]`.
yue_owner = {}  # sub_idx -> 'own' | int (the owning sub index)
# Group sub indices by the exact yue_clean text they carry.
by_yue = {}
for a in aligned:
    idx = a['index']
    yue_raw = a.get('yue', '')
    yue_clean = re.sub(r'^\[DISCARDED[^\]]*\]\s*', '', yue_raw).strip()
    if not yue_clean:
        continue
    by_yue.setdefault(yue_clean, []).append(idx)

# For each group of ≥2 subs sharing the same yue text, pick the owner: the sub
# whose chi-window [start_ms, end_ms] has the largest overlap with the yue
# time window [start_ms, yue_end_ms]. Tie-break by earliest sub.
aligned_by_idx = {a['index']: a for a in aligned}
for yue_text, idxs in by_yue.items():
    if len(idxs) == 1:
        yue_owner[idxs[0]] = 'own'
        continue
    best_idx, best_overlap = None, -1
    for i in idxs:
        a = aligned_by_idx[i]
        ys, ye = a['start_ms'], a.get('yue_end_ms', a['end_ms'])
        cs, ce = a['start_ms'], a['end_ms']
        overlap = max(0, min(ye, ce) - max(ys, cs))
        if overlap > best_overlap:
            best_overlap, best_idx = overlap, i
    for i in idxs:
        yue_owner[i] = 'own' if i == best_idx else best_idx

# --- (b) Emit the dump ---
dump_path = f'{WORK}/ep{EP}_dump.txt'
with open(dump_path, 'w', encoding='utf-8') as f:
    f.write(f"=== DUMP Ep{EP} ({len(aligned)} subs, v14 format) ===\n")
    f.write("Header: <idx>|<conf>|<flags>[ T-ADJ]   (flags: • AUTO-KEEP, ! fabrication-risk,\n")
    f.write("                                        i idiom, @ missing address, o OCR noise)\n")
    f.write("E/C/Y lines: eng / chi / yue; newlines shown as ' // '.\n")
    f.write("Y [see N]  means this sub shares yue with sub N — read yue there.\n")
    f.write("—— gap Ns ——  marks a scene boundary (>5s silence between subs).\n")
    f.write("=" * 70 + "\n")

    SCENE_GAP_MS = 5000
    prev_end = None
    for a in aligned:
        idx = a['index']
        # Scene gap marker
        if prev_end is not None and a['start_ms'] - prev_end > SCENE_GAP_MS:
            gap_s = (a['start_ms'] - prev_end) / 1000.0
            f.write(f"\n—— gap {gap_s:.1f}s ——\n\n")
        prev_end = a['end_ms']

        conf = a.get('yue_confidence', 'N/A')
        adj = ' T-ADJ' if a.get('timing_adjusted') else ''
        flags = confidence_annotations.get(idx, {}).get('flags', '')
        # Pad flags to 5 chars (the five possible flag characters) for alignment.
        flags_padded = flags.ljust(5)
        f.write(f"{idx}|{conf}|{flags_padded}{adj}\n")

        e = (a.get('eng') or '').replace('\n', ' // ')
        c = (a.get('chi') or '').replace('\n', ' // ')
        if e: f.write(f"E {e}\n")
        if c: f.write(f"C {c}\n")

        yue_raw = a.get('yue', '')
        yue_clean = re.sub(r'^\[DISCARDED[^\]]*\]\s*', '', yue_raw).strip()
        if yue_clean:
            owner = yue_owner.get(idx, 'own')
            if owner == 'own':
                y = yue_clean[:200]
                f.write(f"Y {y}\n")
            else:
                f.write(f"Y [see {owner}]\n")

    f.write("=== END DUMP ===\n")

print(f"\nDump written: {dump_path}")

print(f"Ep{EP}: {len(overrides)} deep overrides generated")

# Print confidence-aware summary
high_count = sum(1 for v in confidence_annotations.values() if v['confidence'] == 'HIGH')
med_count  = sum(1 for v in confidence_annotations.values() if v['confidence'] == 'MEDIUM')
low_count  = sum(1 for v in confidence_annotations.values() if v['confidence'] == 'LOW')
na_count   = sum(1 for v in confidence_annotations.values() if v['confidence'] == 'N/A')

print(f"\nConfidence tiers in overrides:")
print(f"  HIGH (yue-authority):  {high_count}")
print(f"  MEDIUM (chi-authority, yue for nuance): {med_count}")
print(f"  LOW (yue discarded):   {low_count}")
print(f"  N/A:                   {na_count}")

if high_count:
    print(f"\n⚠ {high_count} subs flagged YUE-AUTH — these need special attention during manual review.")
    print(f"  Check ep{EP}_confidence.json for details on each flagged sub.")

# v10 AUTO-KEEP summary (conservative pre-filter; see faithful_heuristic())
auto_keep_count = sum(1 for v in confidence_annotations.values() if v.get('auto_keep'))
review_count = len(confidence_annotations) - auto_keep_count
print(f"\n=== Step 4 triage (v10 AUTO-KEEP heuristic) ===")
print(f"  AUTO-KEEP (likely faithful, quick confirm): {auto_keep_count}")
print(f"  NEEDS REVIEW (examine in detail):           {review_count}")
print(f"  Per-sub annotations: ep{EP}_confidence.json['<idx>']['auto_keep']")
print(f"  AUTO-KEEP is a PRIORITY SIGNAL, not a gate. Still read every sub.")
