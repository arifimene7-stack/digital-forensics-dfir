# Day 7 — Deleted File Recovery Report

## 1. Objective
Demonstrate deleted-file recovery from a FAT16 forensic disk image.

## 2. Lab Environment
- Operating system: Ubuntu
- Recovery tool: TestDisk 7.2
- Filesystem: FAT16
- Volume label: DFIR_LAB
- Image: disk-forensics/day7/working/deletion-lab.img
- Recovered file: _VENTS.LOG

## 3. Procedure
1. Created an independent working copy of the Day 6 FAT16 image.
2. Deleted events.log from the working image using mdel.
3. Confirmed that events.log no longer appeared in the active directory listing.
4. Opened the image using TestDisk.
5. Selected the non-partitioned media option.
6. Selected the FAT16 filesystem and used Undelete.
7. Located the deleted entry displayed as _VENTS.LOG.
8. Recovered the file into the recovery directory.

## 4. Recovery Results
- Recovery status: SUCCESS
- Recovered filename: _VENTS.LOG
- Recovered file size: 38 bytes
- Original filename: events.log

## 5. Integrity Verification

Original SHA-256:
834afab7318b30d35a5e9df11196d3a3c0cff641b0beb0182fac1e79b2e62b9c

Recovered SHA-256:
834afab7318b30d35a5e9df11196d3a3c0cff641b0beb0182fac1e79b2e62b9c

- SHA-256 comparison: PASS
- Binary comparison using cmp: PASS
- Content verification: PASS

Recovered content:
Suspicious activity detected at 10:45

## 6. Forensic Interpretation
TestDisk successfully located and recovered the deleted file.
The recovered content was identical to the original file, as confirmed
by matching SHA-256 hashes and binary comparison.

The filename appeared as _VENTS.LOG because FAT deletion changes
the first character of the directory entry.

## 7. Limitations
- This was a controlled experiment using synthetic data.
- The original file was available for comparison.
- Results do not guarantee recovery in cases where file data
  has been overwritten or filesystem metadata is damaged.
- The experiment does not represent acquisition from a real device.

## 8. Conclusion
The deleted file was successfully recovered from the FAT16 image.
All integrity verification checks passed.
The experiment demonstrates the importance of preserving forensic
images and verifying recovered evidence cryptographically.
