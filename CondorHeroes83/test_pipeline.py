"""
Tests for pipeline.py — chi-as-entry-spine alignment (v6).

Run with:
    python3 -m unittest test_pipeline.py -v

Tests are organised in two classes:
  - TestSyntheticReflowCases: hand-built fixtures that isolate each
    alignment case (1:1, merge, split, orphan-rescue, dropped-eng).
  - TestRealDataSlice: a 17-row slice of Episode 24's real CSVs to catch
    regressions against actual production inputs, including empty-text
    chi rows, OCR errors, Pinyin in eng, and multiline eng text.

Both classes import pipeline.run() directly and pass in per-test paths.
"""

import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

# Import pipeline from the same directory as this test file
sys.path.insert(0, str(Path(__file__).parent))
import pipeline


class PipelineTestBase(unittest.TestCase):
    """Shared setup: per-test temp workspace, fixture writers, run invocation."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="pipeline_test_"))
        self.uploads = self.tmp / "uploads"
        self.work = self.tmp / "work"
        self.uploads.mkdir()
        self.work.mkdir()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write_csv(self, ep, track, rows):
        """
        Write a CSV in the production schema.

        rows: list of (index, time_in, time_out, text) tuples.
        time_in/time_out strings like '00:00:01,000'.
        """
        path = self.uploads / f"{ep}-{track}.csv"
        lines = ["Filename,lang,Sequence,TimeIn,TimeOut,Duration,Text"]
        for idx, tin, tout, text in rows:
            t = text.replace('"', '""')
            if "," in t or "\n" in t:
                t = f'"{t}"'
            lines.append(
                f'fixture/{track}.srt,lang,{idx},"{tin}","{tout}",00:00.00,{t}'
            )
        path.write_text("\r\n".join(lines) + "\r\n", encoding="utf-8")

    def run_pipeline(self, ep):
        """
        Invoke pipeline.run() with our temp workspace; suppress stdout
        (the pipeline prints the full dump by design). Return parsed
        aligned.json.
        """
        buf = io.StringIO()
        with redirect_stdout(buf):
            pipeline.run(
                ep,
                uploads=str(self.uploads),
                work=str(self.work),
                output=str(self.work),
            )
        aligned_path = self.work / f"ep{ep}_aligned.json"
        if not aligned_path.exists():
            self.fail(
                f"pipeline.run() didn't produce {aligned_path}.\n"
                f"stdout was:\n{buf.getvalue()}"
            )
        return json.loads(aligned_path.read_text())

    def assert_chi_spine(self, aligned, expected_chi_count, msg=""):
        """Core invariant: output count matches chi count."""
        self.assertEqual(
            len(aligned),
            expected_chi_count,
            f"chi-spine invariant violated: expected {expected_chi_count} "
            f"entries (= chi count), got {len(aligned)}. {msg}",
        )


# ==========================================================================
# SYNTHETIC TESTS — each method isolates one alignment case
# ==========================================================================


class TestSyntheticReflowCases(PipelineTestBase):
    """
    Hand-built fixtures exercising each reflow case in isolation. The fixture
    was originally developed as an ad-hoc smoke test during the v6 rewrite;
    it's preserved here so the cases remain locked in.
    """

    EP = 99

    def test_one_to_one_alignment(self):
        """Trivial case: eng sub and chi sub share the same time window."""
        self.write_csv(
            self.EP,
            "eng",
            [(1, "00:00:01,000", "00:00:03,000", "Hello there friend")],
        )
        self.write_csv(
            self.EP,
            "chi_tra",
            [(1, "00:00:01,000", "00:00:03,000", "你好朋友")],
        )
        aligned = self.run_pipeline(self.EP)
        self.assert_chi_spine(aligned, 1)
        self.assertEqual(aligned[0]["eng"], "Hello there friend")
        self.assertEqual(aligned[0]["chi"], "你好朋友")
        self.assertEqual(aligned[0]["start_ms"], 1000)
        self.assertEqual(aligned[0]["end_ms"], 3000)

    def test_many_eng_to_one_chi_merge(self):
        """
        The historical 'double-sub' case: two eng subs cover the window of
        one chi sub. Under chi-spine the two eng texts must merge into one
        aligned entry.
        """
        self.write_csv(
            self.EP,
            "eng",
            [
                (1, "00:00:05,000", "00:00:06,000", "How are you today"),
                (2, "00:00:06,500", "00:00:07,500", "I am well thanks"),
            ],
        )
        self.write_csv(
            self.EP,
            "chi_tra",
            [(1, "00:00:05,000", "00:00:07,500", "你今天好嗎? 我很好謝謝")],
        )
        aligned = self.run_pipeline(self.EP)
        self.assert_chi_spine(aligned, 1)
        self.assertIn("How are you today", aligned[0]["eng"])
        self.assertIn("I am well thanks", aligned[0]["eng"])

    def test_one_eng_spans_multiple_chi_sentence_split(self):
        """
        One eng sub with two sentences spans two chi windows. The
        sentence-boundary split path should give each chi window one
        sentence.
        """
        eng_text = "This is a longer sentence. And here is another one that follows."
        self.write_csv(
            self.EP,
            "eng",
            [(1, "00:00:10,000", "00:00:15,000", eng_text)],
        )
        self.write_csv(
            self.EP,
            "chi_tra",
            [
                (1, "00:00:10,000", "00:00:12,500", "這是一個長句子"),
                (2, "00:00:12,500", "00:00:15,000", "然後還有一句"),
            ],
        )
        aligned = self.run_pipeline(self.EP)
        self.assert_chi_spine(aligned, 2)
        self.assertIn("This is a longer sentence", aligned[0]["eng"])
        self.assertNotIn("another one", aligned[0]["eng"])
        self.assertIn("another one that follows", aligned[1]["eng"])

    def test_orphan_chi_proximity_rescue(self):
        """
        chi sub has no direct eng overlap, but a dropped eng sub sits within
        the 2000 ms proximity window. The rescue path should pull it in.
        """
        self.write_csv(
            self.EP,
            "eng",
            [
                (1, "00:00:01,000", "00:00:03,000", "Hello there friend"),
                # No chi overlap — will be dropped in Pass 2, then rescued
                # by the orphan-chi proximity check below
                (2, "00:00:30,500", "00:00:31,500", "Near the orphan chi"),
            ],
        )
        self.write_csv(
            self.EP,
            "chi_tra",
            [
                (1, "00:00:01,000", "00:00:03,000", "你好朋友"),
                # No direct eng overlap; eng#2 is ~500 ms away
                (2, "00:00:32,000", "00:00:33,500", "沒有英文的孤兒句"),
            ],
        )
        aligned = self.run_pipeline(self.EP)
        self.assert_chi_spine(aligned, 2)
        self.assertEqual(aligned[1]["chi"], "沒有英文的孤兒句")
        self.assertEqual(aligned[1]["eng"], "Near the orphan chi")

    def test_orphan_chi_no_rescue_when_out_of_range(self):
        """
        chi sub has no eng overlap and no dropped-eng candidate within
        2000 ms. Eng field should be empty; no crash.
        """
        self.write_csv(
            self.EP,
            "eng",
            [(1, "00:00:01,000", "00:00:03,000", "Only one eng sub here")],
        )
        self.write_csv(
            self.EP,
            "chi_tra",
            [
                (1, "00:00:01,000", "00:00:03,000", "只有這一個"),
                # Gap > 2000 ms from any eng
                (2, "00:01:00,000", "00:01:02,000", "孤兒沒救"),
            ],
        )
        aligned = self.run_pipeline(self.EP)
        self.assert_chi_spine(aligned, 2)
        self.assertEqual(aligned[1]["eng"], "")

    def test_dropped_eng_does_not_appear_in_output(self):
        """
        Eng sub that has no chi overlap (and isn't rescued) is simply
        absent from output. This is the expected loss of eng-only content.
        """
        self.write_csv(
            self.EP,
            "eng",
            [
                (1, "00:00:01,000", "00:00:03,000", "Has chi overlap"),
                (2, "00:00:20,000", "00:00:22,000", "No chi anywhere near"),
            ],
        )
        self.write_csv(
            self.EP,
            "chi_tra",
            [(1, "00:00:01,000", "00:00:03,000", "有英文對應")],
        )
        aligned = self.run_pipeline(self.EP)
        self.assert_chi_spine(aligned, 1)
        combined = " ".join(a["eng"] for a in aligned)
        self.assertNotIn("No chi anywhere near", combined)


# ==========================================================================
# REAL-DATA TESTS — first 17 subs of Ep24
# ==========================================================================


class TestRealDataSlice(PipelineTestBase):
    """
    Regression tests against the first 17 rows of Episode 24's real CSVs.
    This fixture reproduces the actual production input format, including:
      - empty-text chi rows (source has genuine blank subtitle entries)
      - OCR errors in chi (其兒 / 鞭兒 for 蓉兒) — pipeline passes through
        unchanged; correction is Step 4's job
      - Pinyin in eng (Rong-er, Huazheng) — same, passed through
      - multiline eng text with embedded newlines
    """

    EP = 24

    ENG_ROWS = [
        (1, "00:01:56,183", "00:01:57,793", "Rong-er..."),
        (2, "00:02:00,954", "00:02:02,443", "Will you stop following me?"),
        (3, "00:02:03,256", "00:02:05,976", "Rong-er, why are you leaving so suddenly?"),
        (4, "00:02:07,160", "00:02:08,889", "I've made it clear to Huazheng"),
        (5, "00:02:09,763", "00:02:11,933", "I know. You'd better go back"),
        (6, "00:02:13,233", "00:02:14,753", "She can't do without you"),
        (7, "00:02:15,969", "00:02:17,079", "She'll die"),
        (8, "00:02:18,972", "00:02:20,842", "What did she say to you? Rong-er"),
        (9, "00:02:23,777", "00:02:26,737", "Nothing. She didn't say anything\nYou should leave"),
        (10, "00:02:30,217", "00:02:31,417", "Father"),
        (11, "00:02:36,723", "00:02:38,153", "Stop following us"),
        (12, "00:02:38,992", "00:02:40,482", "Even if you are the old beggar's disciple"),
        (13, "00:02:41,161", "00:02:42,591", "| won't show you any mercy"),
        (14, "00:02:43,263", "00:02:44,963", "No, you mustn't leave"),
        (15, "00:02:47,668", "00:02:48,868", "Brother Jing"),
        (16, "00:03:26,339", "00:03:27,539", "You're back"),
        (17, "00:03:29,076", "00:03:31,036", "I've cooked some porridge\neat it while it's still warm"),
    ]

    # Rows 1 and 4 have empty text (the source actually has blank entries
    # at these positions). Rows 3 and 9 contain OCR errors in chi.
    CHI_ROWS = [
        (1, "00:01:56,183", "00:01:57,413", ""),
        (2, "00:02:00,954", "00:02:02,354", "你別老跟著我行不行 ?"),
        (3, "00:02:03,323", "00:02:04,193", "其兒"),  # OCR: should be 蓉兒
        (4, "00:02:05,158", "00:02:06,178", ""),
        (5, "00:02:07,194", "00:02:08,624", "我已經跟華箏說的很清楚了"),
        (6, "00:02:09,463", "00:02:11,513", "我知道,你還是回去吧"),
        (7, "00:02:13,367", "00:02:14,327", "她不能沒有你的"),
        (8, "00:02:15,902", "00:02:16,541", "她會死"),
        (9, "00:02:19,239", "00:02:20,789", "她跟你說了甚麼了?鞭兒"),  # OCR: 鞭 → 蓉
        (10, "00:02:23,744", "00:02:26,404", "沒有,她甚麼也沒說, 你走吧"),
        (11, "00:02:30,550", "00:02:31,100", "爹"),
        (12, "00:02:36,790", "00:02:37,660", "你別再跟著我們了"),
        (13, "00:02:39,192", "00:02:41,502", "就算你是老叫化子的徒弟\n我也不會手下留情"),
        (14, "00:02:43,397", "00:02:44,417", "不行,你不能走"),
        (15, "00:02:47,734", "00:02:48,254", "靖哥哥"),
        (16, "00:03:26,339", "00:03:26,978", "你回來啦 ?"),
        (17, "00:03:29,042", "00:03:30,532", "我煮了點粥,你趁熱吃了它"),
    ]

    def setUp(self):
        super().setUp()
        self.write_csv(self.EP, "eng", self.ENG_ROWS)
        self.write_csv(self.EP, "chi_tra", self.CHI_ROWS)

    def test_output_count_matches_chi_count(self):
        """The core chi-spine invariant on real data."""
        aligned = self.run_pipeline(self.EP)
        self.assert_chi_spine(aligned, len(self.CHI_ROWS))

    def test_output_timings_match_chi(self):
        """Each output entry's timing is inherited from chi, not eng."""
        aligned = self.run_pipeline(self.EP)
        for i, row in enumerate(self.CHI_ROWS):
            chi_start_ms = self._tc_to_ms(row[1])
            self.assertEqual(
                aligned[i]["start_ms"],
                chi_start_ms,
                f"entry {i+1}: expected chi start {chi_start_ms} ms, "
                f"got {aligned[i]['start_ms']} ms",
            )

    def test_empty_chi_rows_preserved(self):
        """Empty-text chi rows still produce output entries (don't get skipped)."""
        aligned = self.run_pipeline(self.EP)
        self.assertEqual(aligned[0]["chi"], "")  # chi row 1
        self.assertEqual(aligned[3]["chi"], "")  # chi row 4

    def test_ocr_errors_passed_through(self):
        """
        Pipeline must not 'auto-correct' chi OCR errors; Step 4 human review
        handles those. We assert the OCR'd forms reach aligned.json intact.
        """
        aligned = self.run_pipeline(self.EP)
        self.assertIn("其兒", aligned[2]["chi"])
        self.assertIn("鞭兒", aligned[8]["chi"])

    def test_pinyin_in_eng_passed_through(self):
        """
        Eng Pinyin (Rong-er, Huazheng) must reach aligned.json unchanged.
        Conversion to CJK is Step 3's job (auto_override_v2.py), not Step 1's.
        """
        aligned = self.run_pipeline(self.EP)
        self.assertIn("Rong-er", aligned[0]["eng"])
        self.assertIn("Huazheng", aligned[4]["eng"])

    def test_multiline_eng_preserved(self):
        """Newlines within eng text survive the reflow."""
        aligned = self.run_pipeline(self.EP)
        # entry 9 has the multiline eng; it aligned to chi row 10
        self.assertIn("Nothing", aligned[9]["eng"])
        self.assertIn("You should leave", aligned[9]["eng"])

    def test_no_adjacent_duplicates_in_slice(self):
        """
        The slice contains no repeated dialogue, so no two adjacent entries
        should have identical eng text. On the full episode, chi sometimes
        has genuine repetition (character calling a name) and duplicates
        are correct — this slice has none.
        """
        aligned = self.run_pipeline(self.EP)
        for i in range(len(aligned) - 1):
            a, b = aligned[i]["eng"].strip(), aligned[i + 1]["eng"].strip()
            if a and b:
                self.assertNotEqual(
                    a, b, f"Adjacent duplicate at entries {i+1}/{i+2}: {a!r}"
                )

    @staticmethod
    def _tc_to_ms(tc):
        """'00:01:56,183' → 116183"""
        hms, ms = tc.split(",")
        h, m, s = hms.split(":")
        return int(h) * 3_600_000 + int(m) * 60_000 + int(s) * 1000 + int(ms)


if __name__ == "__main__":
    unittest.main(verbosity=2)
