# Day 8 — FAT16 Filesystem Structure and Metadata Analysis

## 1. Objective

Examine the structure of a FAT16 filesystem image, identify
filesystem metadata, inspect directory entries, and document
file allocation information.

## 2. Evidence

- Source image: disk-forensics/day6/source/filesystem-lab.img
- Working image: disk-forensics/day8/working/filesystem-analysis.img
- Filesystem: FAT16
- Volume label: DFIR_LAB
- Image size: 32 MiB

## 3. Integrity Verification

The source and working image SHA-256 hashes were identical.

SHA-256:
5e1bdc964fc6ec43e955c67a07b01df76e2cec234e16f648b1d676c2fe4ceeef

Binary comparison using cmp: PASS.

## 4. Filesystem Structure

Observed properties:

- Logical sector size: 512 bytes
- Sectors per cluster: 4
- Cluster size: 2048 bytes
- Reserved sectors: 4
- Number of FAT tables: 2
- FAT size: 64 sectors per table
- Root directory entries: 512
- Total sectors: 65536
- Data clusters: 16343
- Used clusters: 3

The data area starts at sector 164.

## 5. Directory Contents

Three regular files were listed:

| Filename | Size |
|---|---:|
| case.txt | 26 bytes |
| events.log | 38 bytes |
| login.txt | 36 bytes |
| Total | 100 bytes |

The volume label is DFIR_LAB.

## 6. File Allocation

The mshowfat output identified:

- case.txt: cluster 2
- events.log: cluster 3
- login.txt: cluster 4

Each listed file occupies one cluster.

## 7. File Content Examination

The files contained:

- case.txt: Case reference: DFIR-DAY6
- events.log: Suspicious activity detected at 10:45
- login.txt: Employee login investigation sample

The text in events.log is a training observation and does
not independently establish malicious activity.

## 8. Boot Sector Observations

The first 128 bytes were examined using xxd.

The visible fields include:

- OEM identifier: mkfs.fat
- Bytes per sector: 512
- Sectors per cluster: 4
- Reserved sectors: 4
- FAT count: 2
- Root directory entries: 512
- Sectors per FAT: 64
- Total sectors: 65536

The boot code contains the message:
"This is not a bootable disk."

## 9. Limitations

- The image is synthetic training evidence.
- The analysis focused on FAT16 structure and allocated files.
- No conclusion about real-world malicious activity can be
  established from the sample text alone.
- The difference between the fsck.fat file count and mdir
  regular-file count requires further interpretation.

## 10. Conclusion

The FAT16 image was examined successfully.

Its filesystem geometry, directory contents, file allocation,
and selected boot-sector fields were documented.

The source image was preserved and analysis was performed
on a verified working copy.
