# Day 20 — Hypothesis Matrix

## 1. Objective
Evaluate investigation hypotheses by comparing supporting
and contradicting evidence, identifying limitations,
and assigning a confidence level.

## 2. Method
Previously documented hypotheses from Day 9 were reviewed.
Additional hypotheses were evaluated using findings from
Days 15–19.

Each hypothesis was assessed using:
- Supporting evidence
- Contradicting evidence
- Evidence limitations
- Status
- Confidence

## 3. Hypothesis Results

### H1 — Failed Login Indicates Unauthorized Access
Status: Inconclusive.
One failed login was recorded, but no successful login
or independent authentication evidence was available.

### H2 — Firefox PID 5603 Is Malicious
Status: Not supported by current evidence.
The executable path and process relationship were
consistent with Firefox. The process was also present
in the process snapshot.

### H3 — Deletion of events.log Was Malicious
Status: Rejected in the laboratory context.
The deletion was an authorized recovery exercise.
The recovered file matched the original SHA-256 hash.

### H4 — Network Connections Indicate Compromise
Status: Not supported by current evidence.
Five established TCP connections were associated with
Firefox. The two network-associated process IDs matched
the process snapshot. No malicious connection was confirmed.

### H5 — The Examined Host Was Compromised
Status: Not established.
The examined evidence did not confirm compromise.
However, the absence of a RAM image and other evidence
limits the strength of this conclusion.

## 4. Overall Assessment
No hypothesis currently establishes a confirmed compromise.

The strongest conclusions concern the controlled laboratory
activities. Other conclusions remain limited by incomplete
evidence and point-in-time collection.

## 5. Limitations
- No RAM image was acquired for memory analysis.
- No packet capture was available.
- Some evidence is synthetic and independently generated.
- Process and network records represent snapshots.
- Absence of detected malicious activity does not prove
  that compromise was impossible.

## 6. Conclusion
The hypothesis matrix documents five hypotheses and
distinguishes confirmed laboratory context from findings
that remain inconclusive or unsupported.

No real-world system compromise was established.

---
End of Day 20 Report
