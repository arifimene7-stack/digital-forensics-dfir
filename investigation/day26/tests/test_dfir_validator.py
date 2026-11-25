import sys
import hashlib
import tempfile
import unittest
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "tool")
)

from dfir_validator import calculate_sha256, compare_files


class TestDFIRValidator(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_sha256_calculation(self):
        sample = self.root / "sample.txt"
        sample.write_text("DFIR evidence", encoding="utf-8")

        expected = hashlib.sha256(
            b"DFIR evidence"
        ).hexdigest()

        self.assertEqual(calculate_sha256(sample), expected)

    def test_identical_files(self):
        original = self.root / "original.txt"
        working = self.root / "working.txt"

        original.write_text("same evidence", encoding="utf-8")
        working.write_text("same evidence", encoding="utf-8")

        result = compare_files(original, working)

        self.assertTrue(result["match"])

    def test_modified_file(self):
        original = self.root / "original.txt"
        working = self.root / "working.txt"

        original.write_text("original", encoding="utf-8")
        working.write_text("modified", encoding="utf-8")

        result = compare_files(original, working)

        self.assertFalse(result["match"])

    def test_empty_file(self):
        sample = self.root / "empty.txt"
        sample.write_bytes(b"")

        expected = hashlib.sha256(b"").hexdigest()

        self.assertEqual(calculate_sha256(sample), expected)


if __name__ == "__main__":
    unittest.main()
