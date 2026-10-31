# Day 6 — Filesystem Forensics Summary

## Activities

- Created a 32 MiB FAT16 filesystem image.
- Checked filesystem consistency using fsck.fat.
- Added three synthetic files using mtools.
- Listed filesystem contents using mdir.
- Examined Linux file metadata using stat.

## Findings

- Three files were present in the FAT16 image.
- Their combined size was 100 bytes.
- FAT16 displayed modification timestamps with limited precision.
- Linux stat exposed additional metadata fields.

## Limitations

The stat results describe the Linux source files,
not the complete metadata stored inside the FAT16 image.

## Conclusion

The exercise demonstrated basic FAT16 inspection
and the importance of understanding filesystem
metadata and timestamp limitations.

All files were synthetic training data.
