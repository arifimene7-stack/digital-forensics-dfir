# Day 18 — Process and Network Correlation

## 1. Objective
Correlate process records with network process references
to identify which recorded processes were associated
with network activity.

## 2. Evidence Sources
- memory-forensics/day8/live-triage/processes.txt
- memory-forensics/day8/live-triage/network-connections.txt

Both sources were collected at:
2026-10-31T15:39:37+01:00

## 3. Method
A Python script extracted process IDs and usernames
from the process snapshot, then compared them with
process IDs referenced in the network snapshot.

## 4. Results
| Metric | Result |
|---|---:|
| Recorded processes | 288 |
| Unique network PIDs | 2 |
| Matched processes | 2 |
| Match rate | 100% |

Matched processes:
- PID 5389 — user imene
- PID 5603 — user imene

## 5. Assessment
Both network process references were found in the
process snapshot. This establishes consistency between
the two collected live-triage records.

No confirmed malicious process-network relationship
was identified from this correlation.

## 6. Limitations
- The analysis uses point-in-time live-triage records.
- Process IDs may be reused over time.
- No RAM image was available for memory-forensic analysis.
- The correlation does not establish the content or intent
  of network communications.
- A match does not prove that a process is benign.

## 7. Conclusion
The two network-associated process IDs were successfully
matched to recorded processes. No confirmed malicious
relationship was identified. The conclusion is limited
to the available snapshots.

---
End of Day 18 Report
