# Day 14 — Integrated Disk Forensics Investigation

## 1. Executive Summary

This investigation consolidates the disk-forensics exercises
completed during Week 2.

The examined evidence consists of independent synthetic
training datasets and filesystem images.

The work covered FAT16, NTFS, ext4, deleted-file recovery,
browser artifacts, timeline construction, and file carving.

No real-world security incident or system compromise
was established.

## 2. Scope and Methodology

The investigation reviewed previously documented laboratory
results without modifying original evidence.

The methodology included:

- Filesystem identification and metadata examination.
- SHA-256 integrity verification.
- Binary comparison using cmp.
- File extraction and recovery.
- Browser database examination.
- Timeline review.
- Signature-based file carving.

The analysis was limited to the available synthetic evidence
and previously recorded tool outputs.

## 3. Evidence Summary

| Evidence ID | Source | Description |
|---|---|---|
| E-01 | Day 6 FAT16 image | Synthetic FAT16 filesystem |
| E-02 | Day 7 recovery | Recovered deleted events.log |
| E-03 | Day 8 working image | FAT16 structure and metadata |
| E-04 | Day 10 NTFS image | NTFS filesystem and MFT |
| E-05 | Day 11 ext4 image | ext4 filesystem and extracted files |
| E-06 | Day 12 browser database | Synthetic browser history and download |
| E-07 | Day 12 activity log | Synthetic activity records |
| E-08 | Day 13 raw image | Synthetic image used for file carving |
| E-09 | Day 13 recovered PDF | Carved PDF file |

## 4. Technical Findings

### 4.1 FAT16

The FAT16 filesystem structure was examined.

Three regular files were identified:
- case.txt
- events.log
- login.txt

The filesystem geometry and cluster allocation were documented.

A controlled deletion and recovery experiment was performed.
TestDisk recovered events.log as _VENTS.LOG.

The recovered file matched the original SHA-256 hash
and passed binary comparison.

### 4.2 NTFS

The NTFS 3.1 image was examined.

Three allocated files were identified:
- incident.txt
- users.txt
- activity.log

Their MFT records and resident DATA attributes were inspected.

The extracted $LogFile contained only FF bytes.
No transaction records could be established.

The USN Journal was not observed in the examined listings.
An unusual MFT timestamp discrepancy was documented
without assigning a cause.

### 4.3 ext4

The ext4 filesystem and its metadata were examined.

Three allocated files were extracted:
- incident.txt
- users.txt
- activity.log

All three extracted files matched their original samples
through SHA-256 and binary comparison.

The journal was identified, but the available logdump output
did not expose detailed transaction records.

### 4.4 Browser and User Activity Artifacts

The synthetic browser database contained three URL records
and one download record.

The activity log contained five events between 09:00 and 10:00.

A normalized timeline was generated while preserving
the source of each event.

These records do not independently establish the identity
or actions of a real user.

### 4.5 File Carving

Foremost extracted one PDF from the synthetic raw image.

The recovered file:
- Name: 00002048.pdf
- Size: 142 bytes
- Offset: 1,048,576 bytes

The recovered file's SHA-256 matched the original.
Binary comparison also passed.

This demonstrates signature-based extraction, not recovery
from a deleted filesystem entry.

## 5. Timeline and Correlation

The following timestamps belong to the synthetic Day 12
browser and activity-log dataset:

| Time | Event | Source |
|---|---|---|
| 09:00 | Session started | Activity log |
| 09:10 | Browser opened; example.org visited | Activity log / browser DB |
| 09:25 | Security training page visited | Activity log / browser DB |
| 09:40 | Training report URL recorded | Browser DB |
| 09:41 | Report download recorded | Activity log / browser DB |
| 10:00 | Session ended | Activity log |

The Day 7 recovered file contains the text
"Suspicious activity detected at 10:45".

This is file content, not an independently verified event
timestamp. It is not merged into the Day 12 timeline.

Filesystem timestamps from the NTFS, ext4, and document
metadata exercises belong to separate laboratory datasets
and are not treated as one chronological incident.

## 6. Hypothesis Assessment

| Hypothesis | Evidence | Assessment |
|---|---|---|
| A deleted file may be recoverable | Day 7 recovery and matching hash | Confirmed in the controlled lab |
| NTFS transaction history is available | Extracted $LogFile contains only FF bytes | Not established |
| ext4 journal reveals file operations | No detailed transactions in logdump output | Not established |
| Browser records demonstrate user activity | Synthetic browser and activity records | Demonstrated only within the dataset |
| A PDF can be recovered by signature | Day 13 Foremost extraction | Confirmed in the controlled lab |
| A real system was compromised | No real-system evidence | Not established |

## 7. Integrity and Validation

Documented validation results include:

- FAT16 recovered file SHA-256: PASS.
- FAT16 recovered file binary comparison: PASS.
- NTFS source and working image integrity: PASS.
- ext4 source and working image integrity: PASS.
- ext4 extracted sample-file comparisons: PASS.
- Browser database source and working copy: PASS.
- Day 13 source and working image comparison: PASS.
- Day 13 original and recovered PDF comparison: PASS.

These results apply to the specific files and comparisons
documented in the individual laboratory reports.

## 8. Limitations

- All examined datasets are synthetic training evidence.
- The filesystem images represent separate laboratory exercises.
- No real endpoint or physical disk was investigated.
- NTFS $LogFile transaction details were unavailable.
- No detailed ext4 journal transactions were recovered.
- The USN Journal was not observed in the examined listings.
- Browser records do not establish real-world user attribution.
- File carving was tested using a small, contiguous PDF.
- Fragmented-file recovery was not tested.
- No confirmed malicious activity was established.

## 9. Final Conclusion

The Week 2 exercises successfully demonstrated filesystem
analysis, metadata examination, file extraction, deleted-file
recovery, browser artifact analysis, timeline construction,
and signature-based file carving.

The documented integrity checks support the reliability
of the specific laboratory copies and recovered files tested.

Some journal-level analysis remained limited by the available
data and tool output.

The examined evidence does not establish a real security
incident or system compromise.

The results demonstrate practical forensic procedures
within controlled synthetic laboratory environments.

---
End of Day 14 Report
