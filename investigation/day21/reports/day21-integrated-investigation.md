# Day 21 — Integrated Digital Forensics Investigation

## 1. Executive Summary

This report consolidates the findings from disk forensics, filesystem analysis, browser artifacts, file carving, live host triage, process analysis, network analysis, process-network correlation, timeline reconstruction, and hypothesis assessment.

The available evidence consists primarily of controlled synthetic datasets and a point-in-time live triage snapshot.

No confirmed real-world security compromise was established from the examined evidence.

This conclusion is limited by the absence of a physical memory image, packet capture, and independently verified incident context.

## 2. Scope and Methodology

The investigation consolidates work completed during Days 1–20.

The methodology included:
- Evidence integrity checks using SHA256 and comparison tools.
- FAT16, NTFS, and ext4 filesystem examination.
- File recovery and signature-based file carving.
- Browser database and activity-log examination.
- Process and network snapshot analysis.
- Process-to-network PID correlation.
- Timeline construction and hypothesis evaluation.

Original evidence was preserved where working copies were used. Findings are classified as observations, interpretations, or limitations.

## 3. Evidence Sources

| Evidence ID | Source | Description |
|---|---|---|
| E-01 | Day 7 FAT16 recovery | Controlled deletion and recovery of events.log |
| E-02 | Day 8 FAT16 analysis | Filesystem structure and file metadata |
| E-03 | Day 10 NTFS analysis | NTFS metadata, MFT and LogFile examination |
| E-04 | Day 11 ext4 analysis | Inodes, file extraction and journal examination |
| E-05 | Day 12 browser artifacts | Synthetic browser history, downloads and activity log |
| E-06 | Day 13 file carving | Foremost extraction of a PDF from a raw image |
| E-07 | Day 15 memory assessment | Assessment of available memory-related evidence |
| E-08 | Day 16 process analysis | Point-in-time process snapshot |
| E-09 | Day 17 network analysis | Point-in-time network connection snapshot |
| E-10 | Day 18 correlation | Process-to-network PID correlation |
| E-11 | Day 19 master timeline | Consolidated timeline from available sources |
| E-12 | Day 20 hypothesis matrix | Evaluation of five investigation hypotheses |

## 4. Disk and Filesystem Findings

### FAT16
A controlled deleted-file recovery exercise recovered the file `_VENTS.LOG`, corresponding to the deleted `events.log` sample.

The recovered file matched the original sample by SHA256 and binary comparison.

This demonstrates successful recovery in the laboratory scenario. It does not independently establish malicious deletion.

### NTFS
The NTFS image contained the examined files:
- incident.txt
- users.txt
- activity.log

The examined MFT records showed allocated files with resident data streams.

A timestamp discrepancy was observed in the examined MFT entry. It was documented as an inconsistency, not proof of timestamp manipulation.

The extracted LogFile data did not provide interpretable transaction details. The available examination therefore does not support claims about specific NTFS transaction events.

### ext4
The ext4 image contained the examined sample files, which were extracted and validated against their source copies.

The journal was extracted, but the available logdump output did not provide detailed transaction events. No unsupported journal conclusions are made.

### File Carving
Foremost recovered one PDF from the raw laboratory image.

The recovered file matched the source PDF by SHA256. It was a minimal synthetic PDF with zero pages.

This demonstrates signature-based carving, not recovery of a fragmented or deleted file from a real incident.

## 5. User Activity and Timeline Findings

The synthetic browser database contained three URL records and one download record.

The associated activity log recorded a session start, browser activity, a download, and a session end.

Day 12 produced nine timeline records. Day 19 consolidated these with ten records from the earlier timeline and one live-triage capture-time record, for twenty records total.

Three records with unknown timestamps were retained rather than assigned invented times.

The datasets originate from separate laboratory exercises. Their combination does not prove that all events occurred on one real host or formed one incident.

The recovered text `Suspicious activity detected at 10:45` is file content, not an independently verified event timestamp.

## 6. Process and Network Findings

### Process Analysis
The examined process snapshot contained 288 process records.

The examined process tree showed a Firefox process and its related content and socket processes.

PID 5603 was identified as a Firefox Socket Process and its executable context was consistent with the Firefox installation.

A command-line argument containing `/tmp/` was observed for the Firefox crash helper. This was an argument, not evidence that the executable itself was running from a temporary directory.

No clearly malicious process was identified in the examined snapshot.

### Network Analysis
The network snapshot contained:
- 5 established TCP connections.
- 7 TCP listening sockets.
- 1 TCP connection in TIME-WAIT.
- 1 established UDP entry.

The five established TCP connections were associated with Firefox PID 5389.

Local listening services included DNS, MySQL and CUPS-related ports. The snapshot also contained local virtual-network and DHCP-related entries.

HTTPS-like connections on port 443 do not reveal the encrypted application content or independently establish the identity or trustworthiness of remote systems.

No confirmed malicious network connection was identified from the available snapshot.

### Process-Network Correlation
The correlation script processed 288 process records and identified two unique network PIDs.

Both PIDs, 5389 and 5603, matched process records belonging to the user `imene`.

This supports the association between the observed network entries and the recorded processes. It does not establish what data was exchanged.

## 7. Memory Evidence Assessment

No RAM image was available in the examined project evidence.

LiME was not successfully loaded, and Volatility was not used to analyze a captured memory image.

The process and network findings in this report come from live-triage text snapshots. They must not be described as results from a Volatility memory-image analysis.

Consequently, memory-resident artifacts, historical process state, and other memory-only evidence remain unexamined.

## 8. Hypothesis Assessment

The Day 20 hypothesis matrix evaluated five hypotheses:

| Hypothesis | Assessment | Reason |
|---|---|---|
| H1: Failed login indicates unauthorized access | Inconclusive | One failed login does not establish successful unauthorized access |
| H2: Firefox PID 5603 is malicious | Not supported | Observed executable and process relationship were consistent with Firefox |
| H3: Deletion of events.log was malicious | Rejected in the lab context | The deletion was controlled and the file was successfully recovered and matched |
| H4: Observed network connections indicate compromise | Not supported | Available snapshot did not establish malicious communication |
| H5: The examined host was compromised | Not established | No confirmed malicious activity was identified, but evidence coverage is limited |

These assessments are based on the evidence available in the corresponding laboratory exercises. They are not proof that a real host is clean.

## 9. Limitations

The investigation has the following limitations:

1. Most evidence comes from synthetic or controlled laboratory exercises.
2. The different datasets are not independently established as one incident.
3. No RAM image was acquired for Volatility analysis.
4. No packet capture was available to inspect network communication.
5. The network snapshot represents only one point in time.
6. NTFS LogFile and ext4 journal transaction details were not successfully interpreted.
7. No independent evidence establishes the identity of a user behind every recorded action.
8. The file-carving exercise did not test fragmented-file recovery.
9. The available evidence cannot establish the complete historical state of a real endpoint.

## 10. Final Assessment

The examined laboratory evidence demonstrates practical use of forensic acquisition validation, filesystem examination, file recovery, metadata analysis, timeline construction, process inspection, network inspection, and hypothesis evaluation.

No confirmed real-world compromise was established.

The appropriate conclusion is:

**No confirmed compromise based on the available evidence; assessment remains limited and inconclusive beyond the examined laboratory datasets and point-in-time snapshots.**

Further investigation of a real incident would require authorized acquisition of relevant endpoint evidence, including a forensic memory image and network evidence where appropriate, together with independently verified incident context.

## 11. Reproducibility

Supporting reports and analysis files are retained in their respective Day 7–20 directories.

Key supporting artifacts include:
- `week2-case/reports/day14-integrated-disk-investigation.md`
- `memory-forensics/day15/reports/day15-memory-evidence-assessment.md`
- `memory-forensics/day16/reports/day16-process-analysis.md`
- `memory-forensics/day17/reports/day17-network-analysis.md`
- `memory-forensics/day18/reports/day18-correlation.md`
- `timeline-engineering/day19/analysis/master-timeline.csv`
- `timeline-engineering/day19/reports/day19-timeline-report.md`
- `investigation/day20/analysis/hypothesis-matrix.csv`
- `investigation/day20/reports/day20-hypothesis-matrix.md`
