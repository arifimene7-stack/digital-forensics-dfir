# Digital Forensics and Incident Response
# Final Investigation Report

## 1. Executive Summary

This project conducted a structured Digital Forensics and Incident Response (DFIR) investigation using controlled laboratory evidence and synthetic datasets.

The investigation covered evidence acquisition and integrity, filesystem examination, deleted-file recovery, file carving, metadata analysis, process and network triage, timeline reconstruction, hypothesis assessment, incident response planning, and automation.

Several technical validation activities succeeded, including SHA256 comparisons, filesystem extraction, file recovery, file carving, and automated integrity tests.

No confirmed real-world compromise was established by the available evidence.

The investigation remains limited by the absence of a forensic RAM image, packet capture, and independently corroborated incident evidence.

## 2. Scope and Objectives

The project objectives were:

- Establish a documented forensic workflow.
- Preserve and verify evidence integrity.
- Examine FAT16, NTFS, and ext4 filesystems.
- Recover and validate selected files.
- Examine metadata and browser artifacts.
- Analyze available process and network snapshots.
- Construct and evaluate forensic timelines.
- Assess hypotheses and evidence reliability.
- Prepare incident response and SOC handoff documentation.
- Develop and test a basic DFIR automation tool.

All laboratory datasets were synthetic or controlled training evidence.

## 3. Methodology

The investigation followed these principles:

1. Preserve source evidence and use working copies for examination.
2. Calculate SHA256 hashes where applicable.
3. Record evidence sources and examination procedures.
4. Distinguish observations from interpretations.
5. Preserve unknown timestamps rather than estimating them.
6. Evaluate findings using confidence and documented limitations.
7. Avoid claiming compromise without sufficient corroborating evidence.

Tools used across the project included:

- SHA256 utilities
- The Sleuth Kit
- TestDisk and PhotoRec
- Foremost
- FAT and ext filesystem utilities
- NTFS examination utilities
- ExifTool
- SQLite
- Python
- Volatility 3

## 4. Evidence Acquisition and Integrity

The project included controlled acquisition and working-copy validation.

A FAT16 image was examined using a separate working copy. A later comparison confirmed that the source and working image had identical SHA256 values:

`5e1bdc964fc6ec43e955c67a07b01df76e2cec234e16f648b1d676c2fe4ceeef`

The project also documented a historical hash discrepancy involving host-events.log.

The current original and working-copy files match each other, but their hashes differ from the historical manifest because of documented publication redaction.

Therefore, historical integrity verification for the current redacted files cannot be claimed as successful.

## 5. Disk Forensics Findings

### FAT16

The FAT16 image was examined for filesystem structure, directory entries, file allocation, and deleted-file recovery.

TestDisk successfully recovered the controlled events.log sample.

The recovered content matched the original sample by SHA256 and byte comparison.

### NTFS

The NTFS image was examined using filesystem metadata and file extraction tools.

Three sample files were identified and examined.

A timestamp inconsistency was observed between examined MFT timestamp fields. Its cause was not established.

The extracted LogFile content did not provide interpretable transaction details.

### ext4

The ext4 image was examined using filesystem metadata and inode extraction.

Three sample files were extracted and matched their source samples.

The journal was extracted, but transaction-level details were not successfully interpreted.

### File Carving

Foremost recovered a PDF sample from the controlled disk image.

The recovered file matched the original PDF by SHA256.

The sample contained zero pages, and fragmentation recovery was not tested.

## 6. Metadata and Browser Artifacts

A synthetic browser-history database was examined.

It contained three URL records and one download record.

The database working copy matched the source database.

A timeline was created from browser records and a synthetic activity log.

These records demonstrate artifact examination and timeline construction, but they do not independently establish the identity or actions of a real user.

## 7. Memory and Process Analysis

Volatility 3 was installed and validated.

However, no forensic RAM image was available, and LiME was not successfully loaded for memory acquisition.

Consequently, no memory-image analysis was performed.

Available live-triage process records were examined.

The process snapshot contained 288 process records.

Firefox PID 5603 was examined in its process-tree context. Its executable context was consistent with Firefox activity.

No clearly malicious process was identified in the examined snapshot.

This is a point-in-time assessment, not proof that the host was free from compromise.

## 8. Network Analysis

The available network snapshot contained:

- 5 established TCP connections.
- 7 TCP listening sockets.
- 1 TCP TIME-WAIT connection.
- 1 established UDP connection.

Five established TCP connections were associated with Firefox PID 5389.

The remote connections used HTTPS ports, but their payloads and remote ownership were not independently verified.

No packet capture was available.

No confirmed malicious network activity was established.

## 9. Timeline Reconstruction

The master timeline contains 20 records:

- 10 records from the earlier host investigation timeline.
- 9 records from browser and activity artifacts.
- 1 live-triage capture event.

Three records have unknown timestamps.

The timeline combines independent synthetic datasets. Their temporal proximity does not establish a common incident or causal relationship.

The live-triage timestamp represents collection time, not necessarily the occurrence time of every recorded process or network event.

## 10. Hypothesis Assessment

The investigation assessed five principal hypotheses:

- Failed login indicates unauthorized access: inconclusive.
- Firefox PID 5603 is malicious: not supported by available evidence.
- events.log deletion was malicious: rejected in the controlled laboratory context.
- Network connections indicate compromise: not supported by available evidence.
- The examined host was compromised: not established.

These conclusions reflect the available evidence and its limitations.

## 11. IOC and Detection Handoff

The IOC list contains six contextual observations.

They include process context, executable paths, network observations, a historical hash discrepancy, and an NTFS timestamp inconsistency.

No confirmed malicious IOC was identified.

The SOC handoff is informational. The observations should not be treated as blocking indicators without additional validation.

## 12. Evidence Reliability and Limitations

Important limitations include:

- No forensic RAM image.
- No packet capture.
- Three unknown timeline timestamps.
- Limited FAT16 timestamp precision.
- An unresolved NTFS timestamp inconsistency.
- Uninterpreted NTFS LogFile and ext4 journal transaction details.
- No fragmentation recovery test.
- Independent synthetic datasets.
- Historical hash discrepancy caused by documented redaction.

A matching SHA256 hash establishes content equality at comparison time, not evidence authenticity or provenance.

## 13. Incident Response Recommendations

For a future authorized investigation:

1. Preserve original evidence and document every transfer.
2. Acquire volatile evidence when appropriate and authorized.
3. Collect network telemetry and packet evidence where available.
4. Correlate process, network, filesystem, and authentication records.
5. Preserve timestamps with timezone and source information.
6. Maintain separate manifests for original and modified evidence.
7. Escalate findings only when corroborating evidence supports the assessment.
8. Document uncertainty and investigative limitations.

## 14. Automation and Validation

A Python DFIR integrity validator was developed.

It supports:

- SHA256 calculation.
- Original and working-copy comparison.
- JSON report generation.
- Exit status indicating match or mismatch.

Four automated tests passed:

1. SHA256 calculation.
2. Identical-file comparison.
3. Modified-file detection.
4. Empty-file handling.

The tool also successfully compared the selected FAT16 source and working images.

## 15. Final Conclusion

The project successfully demonstrated multiple DFIR techniques across evidence integrity, filesystem analysis, file recovery, metadata examination, timeline construction, hypothesis assessment, and automation.

Several controlled recovery and integrity tests passed.

However, the available evidence does not establish a confirmed real-world security incident or host compromise.

The absence of a RAM image, packet capture, and independently corroborated incident evidence limits the investigation.

**Final assessment: No confirmed compromise based on the available evidence.**

This conclusion is limited to the evidence examined and should not be interpreted as proof that no compromise occurred.

## 16. Supporting Documentation

Supporting reports and artifacts are maintained in:

- `evidence-integrity/`
- `disk-forensics/`
- `memory-forensics/`
- `timeline-engineering/`
- `investigation/day20/`
- `investigation/day21/`
- `investigation/day22/`
- `investigation/day23/`
- `investigation/day24/`
- `investigation/day25/`
- `investigation/day26/`
- `week2-case/`

## 17. Reproducibility Statement

The investigation reports, scripts, test cases, evidence hashes, and analysis outputs are retained in the project repository.

Results should be interpreted together with their source files, documented limitations, and evidence-handling history.
