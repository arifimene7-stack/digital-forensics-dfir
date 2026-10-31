# Day 9 — Hypothesis Testing

## H1 — Failed Login Indicates Unauthorized Access

Evidence:
- host-events.log records one failed login attempt for testuser.
- No successful login or related authentication evidence is provided.

Assessment:
The failed attempt alone does not establish unauthorized access
or system compromise.

Status: Inconclusive.

## H2 — Firefox PID 5603 Is Malicious

Evidence:
- Executable path points to the Firefox installation.
- Process tree links PID 5603 to the Firefox main process.
- Command line and cgroup are consistent with Firefox.

Assessment:
The collected evidence is consistent with normal Firefox operation.
No confirmed malicious activity was identified.

Status: Not supported by current evidence.

## H3 — Deletion of events.log Was Malicious

Evidence:
- The file was deliberately deleted from a working FAT16 image.
- The deletion was part of the documented Day 7 recovery exercise.
- The recovered file matched the original SHA-256 hash.

Assessment:
The deletion was an authorized laboratory action, not evidence
of malicious activity.

Status: Rejected in the laboratory context.

## Overall Assessment

The available evidence is synthetic or generated during controlled
laboratory exercises. It does not establish a real system compromise.

Additional independent evidence would be required to assess any
real-world incident.
