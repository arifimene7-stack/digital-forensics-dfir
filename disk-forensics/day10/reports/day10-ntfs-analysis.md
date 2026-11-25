# Day 10 — NTFS Forensic Analysis Report

## 1. Objective

The objective of this lab was to examine a synthetic NTFS disk image, identify filesystem metadata, inspect Master File Table (MFT) records, extract file contents, and examine the NTFS `$LogFile` and USN Journal availability.

## 2. Evidence and Integrity

Source image: `disk-forensics/day10/source/ntfs-lab.img`

Working image: `disk-forensics/day10/working/ntfs-analysis.img`

Image size: 67,108,864 bytes (64 MiB).

SHA256:
`49aaff8da51100dc45b4c4f60c271b64d1c889b9a5c962f98ad4a397fead542d`

The source and working image hashes were identical. A binary comparison using `cmp` also returned PASS.

The working image was used for analysis.

## 3. NTFS Filesystem Structure

The image was identified as NTFS 3.1.

Observed filesystem properties:

- Volume label: DFIR_NTFS
- Sector size: 512 bytes
- Cluster size: 4096 bytes
- MFT starting cluster: 4
- MFT mirror cluster: 8191
- MFT record size: 1024 bytes
- Index record size: 4096 bytes
- Root directory MFT entry: 5

The `fsstat`, `ntfsinfo`, and `ntfsls` tools were used to examine filesystem metadata and directory contents.

## 4. File and MFT Analysis

Three regular files were identified:

| File | MFT Entry | DATA Size | Storage |
|---|---:|---:|---|
| incident.txt | 64 | 88 bytes | Resident |
| users.txt | 65 | 35 bytes | Resident |
| activity.log | 66 | 158 bytes | Resident |

All three records were allocated and had one link.

The `$DATA` attributes were resident, meaning the file contents were stored directly within their MFT records.

The files were successfully read using `ntfscat`. Their contents matched the synthetic sample files used to create the image.

The MFT timestamps for these files were close to their creation time during the lab.

## 5. NTFS Metadata Files

The analysis identified standard NTFS metadata entries, including:

- `$MFT`
- `$MFTMirr`
- `$LogFile`
- `$Bitmap`
- `$Boot`
- `$Secure`
- `$UpCase`
- `$Extend`

The `$MFT` record showed an unusual timestamp of 2076-11-29 in its `$STANDARD_INFORMATION` attribute, while its `$FILE_NAME` timestamps showed 2026-10-31.

This discrepancy was documented without assuming malicious activity. Its cause was not established during this lab.

## 6. $LogFile Examination

The `$LogFile` stream was extracted using `icat` from MFT entry 2.

Extracted file:
`disk-forensics/day10/analysis/LogFile.bin`

Size: 2,097,152 bytes.

SHA256:
`4bda3a28f4ffe603c0ec1258c0034d65a1a0d35ab7bd523a834608adabf03cc5`

A byte-level inspection found:

- Total bytes: 2,097,152
- Bytes with value FF: 2,097,152
- Zero bytes: 0
- First non-FF byte: None

The `strings` command did not return readable strings.

Therefore, no transaction records or recoverable event details were established from this extracted stream. The reason for the all-FF content was not determined.

## 7. USN Journal Examination

A recursive `fls` search for `UsnJrnl` and `journal` returned no matching entries.

The `$Extend` directory listing also did not show a `$UsnJrnl` entry.

The journal was therefore not observed in the examined directory listings. This does not establish why it was absent or whether another examination method could identify related metadata.

## 8. Tools Used

- `mkntfs`
- `ntfsinfo`
- `ntfsls`
- `ntfscat`
- `ntfscp`
- `fls`
- `istat`
- `icat`
- `fsstat`
- `sha256sum`
- `cmp`
- `xxd`
- `strings`

## 9. Limitations

- The image is a synthetic training image, not a live system acquisition.
- No USN Journal entry was observed in the examined listings.
- The extracted `$LogFile` contained only FF bytes, so transaction-level analysis was not possible.
- The unusual `$MFT` timestamp discrepancy remains unexplained.
- No malicious activity can be concluded from these observations.

## 10. Conclusion

The lab successfully demonstrated NTFS filesystem identification, metadata examination, MFT record analysis, file-content extraction, and integrity verification.

Three regular files were identified and examined. Their resident data attributes and MFT metadata were documented.

The `$LogFile` was extracted and examined at the byte level, while the USN Journal was not observed in the examined listings.

All findings are limited to the synthetic training image and the tools and methods used during this exercise.
