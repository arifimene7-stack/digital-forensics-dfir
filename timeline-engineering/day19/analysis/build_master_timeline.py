import csv
from pathlib import Path
from datetime import datetime

day9 = Path("timeline-engineering/day9/timeline.csv")
day12 = Path("disk-forensics/day12/analysis/day12-timeline.csv")
capture = Path("memory-forensics/day8/live-triage/capture-time.txt")

output = Path("timeline-engineering/day19/analysis/master-timeline.csv")

events = []

# Import Day 9 events
with day9.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        timestamp = row["timestamp"]
        events.append({
            "timestamp": timestamp,
            "timezone": row["timezone"],
            "event": row["event"],
            "source": row["source"],
            "evidence_type": row["evidence_type"],
            "confidence": row["confidence"],
            "notes": row["notes"]
        })

# Import Day 12 events
with day12.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        timestamp = row["Timestamp"]
        events.append({
            "timestamp": timestamp,
            "timezone": "+01:00",
            "event": row["Event"],
            "source": row["Source"],
            "evidence_type": "Synthetic activity/browser record",
            "confidence": "Medium",
            "notes": row["Details"]
        })

# Add the live-triage capture time as an acquisition event
capture_time = capture.read_text().strip()

events.append({
    "timestamp": capture_time,
    "timezone": "+01:00",
    "event": "Live triage snapshot captured",
    "source": "capture-time.txt",
    "evidence_type": "Live triage metadata",
    "confidence": "High",
    "notes": "Capture time only; not the timestamp of every recorded activity."
})

def sort_key(event):
    try:
        return datetime.fromisoformat(
            event["timestamp"].replace(" ", "T")
        ).timestamp()
    except ValueError:
        return float("inf")

events.sort(key=sort_key)

fields = [
    "timestamp", "timezone", "event",
    "source", "evidence_type", "confidence", "notes"
]

with output.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(events)

print("Master Timeline created successfully.")
print(f"Total events: {len(events)}")
print(f"Output: {output}")
print(f"Events with unknown timestamps: "
      f"{sum(e['timestamp'] == 'UNKNOWN' for e in events)}")
