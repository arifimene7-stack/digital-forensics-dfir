# Day 6 — Filesystem Metadata Analysis

## Filesystem Information
- Filesystem: FAT16
- Volume label: DFIR_LAB
- Logical sector size: 512 bytes
- Cluster size: 2048 bytes

## Files Found
 Volume in drive : is DFIR_LAB   
 Volume Serial Number is 30FA-1872
Directory for ::/

case     txt        26 2026-10-31  14:58 
events   log        38 2026-10-31  14:58 
login    txt        36 2026-10-31  14:58 
        3 files                 100 bytes
                         33 464 320 bytes free


## Linux Source File Metadata
  File: disk-forensics/day6/analysis/sample-files/case.txt
  size: 26        	Blocks: 8          IO Block: 4096   regular file
Device: 259,2	Inode: 2910892     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/training-user)   Gid: ( 1000/training-user)
Access: 2026-10-31 14:56:14.457237771 +0100
Modify: 2026-10-31 14:56:13.710239485 +0100
Change: 2026-10-31 14:56:13.710239485 +0100
 Birth: 2026-10-31 14:56:13.710239485 +0100
  File: disk-forensics/day6/analysis/sample-files/events.log
  size: 38        	Blocks: 8          IO Block: 4096   regular file
Device: 259,2	Inode: 2910880     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/training-user)   Gid: ( 1000/training-user)
Access: 2026-10-31 14:58:45.146926462 +0100
Modify: 2026-10-31 14:56:13.710239485 +0100
Change: 2026-10-31 14:56:13.710239485 +0100
 Birth: 2026-10-31 14:56:13.710239485 +0100
  File: disk-forensics/day6/analysis/sample-files/login.txt
  size: 36        	Blocks: 8          IO Block: 4096   regular file
Device: 259,2	Inode: 2907095     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/training-user)   Gid: ( 1000/training-user)
Access: 2026-10-31 14:56:14.469237744 +0100
Modify: 2026-10-31 14:56:13.709239487 +0100
Change: 2026-10-31 14:56:13.709239487 +0100
 Birth: 2026-10-31 14:56:13.709239487 +0100
