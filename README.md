# Month 2 — Digital Forensics & Incident Response (DFIR)

## Project Overview
A 10-day practical training project covering digital evidence handling,
integrity verification, acquisition strategies, disk forensics,
deleted-file recovery, live memory triage, timeline analysis,
hypothesis testing, and incident investigation.

## Objectives
- Identify and document digital evidence.
- Preserve evidence integrity using SHA-256.
- Maintain evidence traceability and chain of custody.
- Understand logical, physical, and live acquisition.
- Examine filesystem metadata and recover deleted files.
- Perform live process and network triage.
- Build timelines and correlate evidence.
- Assess hypotheses using facts and documented limitations.
- Produce a structured DFIR investigation report.

## Investigation Principles
- Preserve original evidence.
- Analyze working copies whenever possible.
- Record SHA-256 hashes.
- Maintain chain-of-custody records.
- Separate observations from assumptions.
- Document confidence, limitations, and uncertainty.
- Use authorized training evidence only.

## Project Structure

| Directory | Purpose |
|---|---|
| case-management/ | Case intake, evidence register, custody records, tool validation |
| evidence-integrity/ | Original evidence, working copies, hashes, verification |
| disk-forensics/ | Acquisition, filesystem analysis, deleted-file recovery |
| memory-forensics/ | Live triage, process analysis, memory-forensics preparation |
| timeline-engineering/ | Event timeline and hypothesis correlation |
| detections-and-iocs/ | IOC assessment and detection findings |
| automation/ | Automated tests and validation |
| blind-case/ | Independent synthetic investigation |
| capstone/ | Final investigation report and supporting material |
| week1-case/ | First-week investigation summary |
| week2-case/ | Reserved for later case material |
| week3-case/ | Reserved for later case material |

## Ten-Day Training Summary

| Day | Subject | Status |
|---|---|---|
| 1 | Evidence intake and registration | Completed |
| 2 | Hashing and integrity verification | Completed |
| 3 | Acquisition strategy | Completed |
| 4 | Forensic disk acquisition | Completed |
| 5 | Chain of custody and tool validation | Completed |
| 6 | Filesystem forensics | Completed |
| 7 | Deleted-file recovery | Completed |
| 8 | Memory forensics and live triage | Partially completed |
| 9 | Timeline, correlation, and hypothesis testing | Completed |
| 10 | Blind case and capstone report | Completed |

## Validation Results
- Three original/working-copy hash comparisons passed.
- Tampering test detected a modified file.
- Forensic training image and its copy were identical.
- Deleted training file was recovered and matched the original SHA-256.
- Day 10 blind-case tests: 2 passed.
- Blind-case evidence hash verification: 3 files passed.

## Important Limitations
- All investigation datasets and scenarios are synthetic training evidence.
- No real endpoint compromise was investigated.
- No physical disk from a real system was acquired.
- Live memory triage was performed, but no RAM image was acquired.
- Volatility 3 was installed, but no memory-dump analysis was performed.
- The blind case conclusion is inconclusive because independent authorization evidence is unavailable.
- Findings are limited to the evidence collected during these exercises.

## Main Deliverable
`capstone/final-report/final-dfir-report.md`

## Environment
- Operating System: Ubuntu 26.04.1 LTS
- Architecture: x86_64
- Python: 3.14.4
- Volatility 3: 2.28.2
- Disk image format: Raw
- Filesystem laboratory: FAT16

## Final Conclusion
The ten-day DFIR training plan was completed with documented limitations.
The exercises demonstrate evidence handling, integrity verification,
disk analysis, deleted-file recovery, live triage, timeline construction,
and structured reporting.

Memory-dump acquisition and Volatility-based memory analysis remain
future practical work.
