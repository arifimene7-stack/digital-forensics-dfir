import csv
from pathlib import Path

base = Path("blind-case/evidence")

print("=== ALERT ===")
print((base / "alert.log").read_text())

print("\n=== TASK INVENTORY ===")
with (base / "task-inventory.csv").open() as f:
    for row in csv.DictReader(f):
        print(row)

print("\n=== ADMIN NOTES ===")
print((base / "admin-notes.txt").read_text())
