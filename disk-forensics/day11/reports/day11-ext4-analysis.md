# Day 11 — Linux ext4 Filesystem Forensics

## 1. Objective

The objective was to examine a synthetic ext4 filesystem, inspect
its metadata and inodes, extract files, verify their integrity,
and examine the filesystem journal.

## 2. Evidence and Integrity

Source image:
`disk-forensics/day11/source/ext4-lab.img`

Working image:
`disk-forensics/day11/working/ext4-analysis.img`

Both images were verified using SHA-256 and binary comparison.

SHA-256:
`bc40e32e0d586460669b3265ba9b5887af10d01ae1ad8caf6463526cff0113a7`

Result:
- SHA-256 values matched.
- Binary comparison using `cmp` passed.
- The working image is identical to the source image.

## 3. Filesystem Structure

The image contains an ext4 filesystem.

Observed properties:
- Filesystem type: ext4
- Filesystem label: DFIR_EXT4
- Block size: 4096 bytes
- Inode size: 256 bytes
- Journal enabled: Yes
- Journal inode: 8
- Journal size: 4 MiB

The filesystem metadata was examined using `dumpe2fs`,
`debugfs`, and The Sleuth Kit tools.

## 4. Directory and Inode Analysis

The following entries were identified using `fls`:

| Entry | Inode |
|---|---:|
| users.txt | 14 |
| incident.txt | 13 |
| activity.log | 15 |
| lost+found | 11 |

The three sample files were allocated.

The `incident.txt` inode examination showed:
- Inode: 13
- Status: Allocated
- Size: 105 bytes
- Links: 1
- Data mapping: Extents
- Reported data block: 2097

The observed inode timestamps were:
2026-11-01 00:31:15 CET.

These are filesystem timestamps from the synthetic lab image,
not independently verified incident times.

## 5. File Extraction and Integrity

The files were extracted using `icat` and compared with
their original sample files.

| File | Result |
|---|---|
| incident.txt | SHA-256 match; cmp PASS |
| users.txt | SHA-256 match; cmp PASS |
| activity.log | SHA-256 match; cmp PASS |

The extracted files matched their corresponding samples.

No deleted-file recovery was performed during this exercise.

## 6. Journal Examination

The ext4 journal was identified as inode 8.

Its extracted binary size was 4 MiB.

The journal was examined using:

`debugfs -R "logdump" working/ext4-analysis.img`

Observed output:

`Journal starts at block 0, transaction 1`

No detailed transaction records or file-operation events
were displayed by this examination.

Therefore, no specific file activity or event timeline
can be reconstructed from the available journal output.

## 7. Tools Used

- mkfs.ext4
- dumpe2fs
- debugfs
- fls
- istat
- icat
- sha256sum
- cmp

## 8. Limitations

- The evidence is synthetic and created for training.
- The timestamps reflect the lab filesystem environment.
- The journal output did not expose detailed transactions.
- No deleted-file recovery was performed.
- Findings are limited to the examined image and available tool output.

## 9. Conclusion

The ext4 filesystem was successfully created and examined.

Three allocated files were identified and extracted.
Their extracted contents matched the original samples
through SHA-256 and binary comparison.

The filesystem journal was identified, but the available
logdump output did not provide detailed transaction records.

No conclusion about malicious activity can be established
from this exercise alone.
