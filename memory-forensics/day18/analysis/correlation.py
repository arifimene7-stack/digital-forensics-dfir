from pathlib import Path
import re

base = Path("memory-forensics/day8/live-triage")

process_text = (base / "processes.txt").read_text(errors="replace")
network_text = (base / "network-connections.txt").read_text(errors="replace")

processes = {}

for line in process_text.splitlines()[1:]:
    match = re.match(r"(\S+)\s+(\d+)\s+", line)
    if match:
        user, pid = match.groups()
        processes[pid] = user

references = set(re.findall(r'pid=(\d+)', network_text))

print("=== DAY 18: PROCESS-NETWORK CORRELATION ===")
print(f"Recorded processes: {len(processes)}")
print(f"Unique network PIDs: {len(references)}")

matched = 0
for pid in sorted(references):
    if pid in processes:
        print(f"PID {pid}: MATCHED | User: {processes[pid]}")
        matched += 1
    else:
        print(f"PID {pid}: NOT FOUND")

print(f"\nMatched processes: {matched}/{len(references)}")
print("Assessment: Process references were checked against the process snapshot.")
print("Limitation: This is live-triage correlation, not RAM image analysis.")
