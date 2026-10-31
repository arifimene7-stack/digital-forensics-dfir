# Digital Forensics and Incident Response
## Final Capstone Report

**Project:** DFIR-2026  
**Analyst:** DFIR Student  
**Environment:** Ubuntu Linux  
**Period:** 2026-10-31  
**Nature of Evidence:** Synthetic laboratory evidence

---

## 1. Executive Summary

This project demonstrates a structured Digital Forensics and
Incident Response workflow through controlled laboratory exercises.

The work covered evidence intake, integrity verification,
acquisition planning, disk imaging, filesystem analysis,
deleted-file recovery, live memory triage, timeline engineering,
hypothesis testing, and a final blind-case investigation.

No real-world system compromise was established.
The evidence was synthetic or generated during laboratory exercises.

## 2. Evidence Management and Integrity

Evidence was registered and documented using:
- Evidence register
- Scope and authority documentation
- Acquisition notes
- Chain-of-custody records

SHA-256 hashes were used to verify evidence integrity.

Three synthetic evidence files were compared with their working
copies. All integrity comparisons passed.

A controlled alteration test successfully demonstrated
mismatch detection.

## 3. Acquisition and Disk Forensics

An acquisition strategy was documented, comparing logical,
physical, and live-response approaches.

A 10 MiB synthetic raw image was created and copied.
The source and copy had identical SHA-256 hashes.

A FAT16 training image was created and examined.
Filesystem metadata and file timestamps were documented.

## 4. Deleted File Recovery

A working copy of the FAT16 image was used for a controlled
deletion and recovery experiment.

TestDisk 7.2 recovered the deleted events.log file.

Verification results:
- SHA-256 comparison: PASS
- Binary comparison: PASS
- Content verification: PASS

The recovered file was identical to the original.

## 5. Memory Forensics and Live Triage

Live triage examined system memory usage, processes,
and network sockets.

Firefox PID 5603 was examined. Its executable path,
process tree, command line, and cgroup were consistent
with a Firefox Socket Process.

Volatility 3 version 2.28.2 was installed.
LiME was built for the current kernel and its signature
metadata was inspected.

Limitations:
- No RAM image was acquired.
- No Volatility analysis of a memory image was performed.
- LiME was not loaded because its signing key was not enrolled.

Therefore, this phase represents live triage and preparation,
not completed memory-image analysis.

## 6. Timeline and Correlation

A timeline containing 10 events was created.

It combines synthetic host events, filesystem observations,
and documented laboratory activities.

Three events have unknown timestamps because exact times
were not recorded.

Three hypotheses were assessed:
- Failed login as possible unauthorized access.
- Firefox process as potentially malicious.
- Deleted events.log as possible destructive activity.

Available evidence did not establish a confirmed compromise.
The file deletion was an authorized laboratory action.

## 7. Blind Case Investigation

Case ID: DFIR-2026-002

An unfamiliar scheduled task named SystemHealthCheck
was examined using three synthetic evidence files.

The task was enabled and configured to run under SYSTEM.
Administrative notes mentioned planned maintenance,
but did not independently establish authorization.

Assessment: INCONCLUSIVE.

No confirmed malicious activity was established.
Additional authorization records, script metadata,
and task execution logs would be required.

Validation:
- Three SHA-256 checks: PASS
- Python unit tests: 2/2 PASS

## 8. Limitations

- All investigation scenarios used synthetic evidence.
- No real endpoint acquisition was performed.
- No full RAM image was analyzed.
- The blind-case evidence does not establish actual authorization.
- Timeline events with missing timestamps remain marked UNKNOWN.
- Findings are limited to the evidence collected in this project.

## 9. Final Conclusion

The project successfully demonstrated core DFIR procedures,
including evidence preservation, hashing, acquisition planning,
disk and filesystem examination, deleted-file recovery,
live triage, timeline construction, and hypothesis testing.

Integrity checks and laboratory validation tests passed.

No confirmed compromise was established in the synthetic cases.

The main outstanding technical limitation is the absence
of a RAM image for Volatility-based memory analysis.

The results demonstrate a documented laboratory workflow,
not certification that a real system is free from compromise.

---

**End of Report**
