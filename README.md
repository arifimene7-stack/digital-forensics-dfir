# Digital Forensics & Incident Response (DFIR)
### 28-Day Practical Investigation & Forensic Analysis Portfolio

## Project Overview

A structured 28-day practical DFIR training project focused on digital evidence handling, forensic integrity, disk analysis, artifact examination, live triage, timeline engineering, hypothesis assessment, investigation reporting, and basic forensic automation.

The project uses controlled and synthetic datasets to demonstrate practical forensic workflows, evidence validation, analytical reasoning, and investigative documentation.

---

## Objectives

- Establish a structured digital forensic investigation workflow.
- Document evidence intake, traceability, and chain of custody.
- Calculate and validate SHA-256 hashes.
- Understand acquisition strategies and forensic working copies.
- Examine FAT16, NTFS, and ext4 filesystem artifacts.
- Perform controlled deleted-file recovery and file carving.
- Examine browser artifacts and metadata.
- Perform live process and network triage.
- Construct and correlate forensic timelines.
- Assess investigative hypotheses and evidence reliability.
- Develop and test a forensic integrity validation script.
- Produce structured investigation reports with documented limitations.

## Skills Demonstrated

| Category | Practical Activities |
|---|---|
| Evidence Handling | Evidence registration, documentation, traceability |
| Evidence Integrity | SHA-256 hashing and integrity verification |
| Chain of Custody | Evidence transfer and custody documentation |
| Disk Forensics | Filesystem examination and forensic extraction |
| Filesystem Analysis | FAT16, NTFS, and ext4 |
| Deleted-File Recovery | Controlled file recovery and validation |
| File Carving | File recovery using carving techniques |
| Artifact Analysis | Browser history, metadata, filesystem artifacts |
| Live Triage | Process and network snapshot examination |
| Timeline Engineering | Timeline construction, correlation, timestamp evaluation |
| Hypothesis Testing | Evidence-based assessment and documented uncertainty |
| DFIR Automation | Python integrity validation and automated tests |
| Reporting | Investigation reports, findings, limitations, and handoff |

## Repository Structure

| Directory | Description |
|---|---|
| `case-management/` | Case documentation, evidence management, custody records, and validation |
| `evidence-integrity/` | Hashing, evidence verification, and working-copy validation |
| `disk-forensics/` | Acquisition, filesystem examination, recovery, and disk analysis |
| `memory-forensics/` | Live triage, process analysis, and memory-forensics preparation |
| `timeline-engineering/` | Timeline construction and event correlation |
| `investigation/` | Investigative analysis and documented findings |
| `detections-and-iocs/` | IOC evaluation and detection-related observations |
| `blind-case/` | Independent synthetic blind investigation |
| `capstone/` | Final report, findings, evidence map, timeline, and validation |
| `final-submission/` | Final investigation reports and validation documentation |
| `week1-case/` | Week 1 investigation summary |
| `week2-case/` | Integrated disk investigation report |

## Key Deliverables

### Final Investigation Report

- [Final DFIR Investigation Report — Markdown](final-submission/reports/final-dfir-investigation-report.md)
- [Final DFIR Investigation Report — PDF](final-submission/reports/final-dfir-investigation-report.pdf)
- [Final DFIR Investigation Report — DOCX](final-submission/reports/final-dfir-investigation-report.docx)
- [Capstone Report](capstone/final-report/final-dfir-report.md)

### Final Validation

- [Day 28 Final Validation & Blind Investigation Closure](final-submission/reports/day28-final-validation.md)

### Investigation Summaries

- [Week 1 Summary](week1-case/weekly-summary.md)
- [Week 2 Integrated Disk Investigation](week2-case/reports/day14-integrated-disk-investigation.md)

## Validation Results

Selected validation activities completed during the project:

- SHA-256 calculations and original/working-copy comparisons.
- Successful identification of a modified file during an integrity test.
- Successful validation of a selected forensic training image and its working copy.
- Controlled deleted-file recovery with SHA-256 validation.
- File-carving validation against a controlled sample.
- Four automated tests for the Python integrity validator.
- Two blind-case automated tests passed.
- SHA-256 verification of three blind-case evidence files passed.

### Integrity Validator

A Python-based forensic integrity validator was developed to support:

- SHA-256 calculation.
- Original and working-copy comparison.
- JSON report generation.
- Exit status indicating match or mismatch.

The automated tests covered:

1. SHA-256 calculation.
2. Identical-file comparison.
3. Modified-file detection.
4. Empty-file handling.

## Blind Investigation

**Case ID:** DFIR-2026-002

The blind investigation examined a synthetic dataset containing an alert, task inventory, and administrative notes.

### Assessment

**Status: INCONCLUSIVE**

The available evidence did not independently establish malicious activity or confirmed authorization.

The assessment identified additional evidence required to strengthen the conclusion, including independent change-management records, script metadata and hash information, and task creation/execution logs.

The conclusion reflects the available evidence and does not overstate certainty.

## Investigation Principles

The project followed these principles:

- Preserve source evidence.
- Analyze working copies whenever possible.
- Validate evidence integrity where applicable.
- Document evidence sources and examination procedures.
- Maintain traceability.
- Separate observations from interpretations.
- Preserve unknown timestamps rather than inventing them.
- Evaluate hypotheses using available evidence.
- Document limitations and uncertainty.
- Avoid claiming compromise without sufficient corroborating evidence.
- Use controlled and authorized training datasets.

## Tools & Environment

- **Operating System:** Ubuntu
- **Architecture:** x86_64
- **Python:** 3.14
- **Volatility 3:** 2.28.2 (installed; command-line execution tested)
- **Filesystem Laboratory:** FAT16, NTFS, ext4
- **Disk Image Format:** Raw

### Tools Used

- `dd` — disk imaging utility
- `sha256sum` — SHA-256 integrity verification
- `cmp` — binary file comparison
- The Sleuth Kit (`fls`, `icat`)
- TestDisk — deleted-file recovery
- Foremost — file carving
- ExifTool — metadata analysis
- SQLite — browser database analysis
- Python — DFIR automation and analysis
- Volatility 3 — installed and command-line tested; no memory-image analysis performed

## Limitations

This project is a practical training portfolio and not a real-world incident investigation.

- All investigation datasets and scenarios are synthetic or controlled training evidence.
- No real endpoint compromise was investigated.
- No physical disk from a real system was acquired.
- Live memory triage was performed, but no forensic RAM image was acquired.
- No Volatility-based memory-dump analysis was performed.
- No packet capture was available.
- NTFS LogFile and ext4 journal transaction-level details were not successfully interpreted.
- Some timeline timestamps remain unknown.
- Historical hash verification of redacted host-events data did not pass against the historical manifest.
- Some datasets represent independent laboratory exercises and should not be interpreted as one real-world incident.

## Final Assessment

The project demonstrated practical work in digital evidence handling, integrity verification, disk forensics, recovery validation, artifact examination, live triage, timeline construction, hypothesis assessment, reporting, and forensic automation.

The available evidence does not establish a confirmed real-world security incident or host compromise.

**Final assessment: No confirmed compromise based on the available evidence.**

This conclusion is limited to the evidence examined and should not be interpreted as proof that no compromise occurred.
