import csv
import unittest
from pathlib import Path

BASE = Path("blind-case/evidence")

class TestBlindCase(unittest.TestCase):

    def test_evidence_files_exist(self):
        self.assertTrue((BASE / "alert.log").is_file())
        self.assertTrue((BASE / "task-inventory.csv").is_file())
        self.assertTrue((BASE / "admin-notes.txt").is_file())

    def test_task_inventory(self):
        with (BASE / "task-inventory.csv").open() as f:
            tasks = list(csv.DictReader(f))

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["task_name"], "SystemHealthCheck")
        self.assertEqual(tasks[0]["account"], "SYSTEM")
        self.assertEqual(
            tasks[0]["action"],
            "/usr/local/bin/health-check.sh"
        )

if __name__ == "__main__":
    unittest.main()
