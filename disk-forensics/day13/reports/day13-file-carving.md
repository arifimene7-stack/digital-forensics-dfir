# Day 13 — File Carving and Recovery

## 1. Objective

Perform file carving on a synthetic raw disk image using Foremost.
Validate the recovered file through file-type identification,
size comparison, and SHA-256 verification.

## 2. Evidence

Source files:
- training-report.pdf
- training-note.txt

Disk image:
- source/carving-lab.img
- Size: 8 MiB

Working image:
- working/carving-analysis.img

The PDF was placed at offset 1,048,576 bytes inside the raw image.

## 3. Image Integrity

SHA-256:
58983403041042123994e0098823d566d1b447f889f48ae020e46ccbf03e1515

The source and working images had identical SHA-256 values.
Binary comparison using cmp passed.

## 4. File Carving

Tool: Foremost 1.5.7

Command:
foremost -t pdf -i carving-analysis.img -o recovered

Result:
- Files extracted: 1
- File type: PDF
- Recovered name: 00002048.pdf
- Size: 142 bytes
- Offset: 1,048,576 bytes

## 5. Recovery Validation

Original SHA-256:
554f5147984d75fe7e43c6f15d08e3d52097907a122299c06613e84b3b4c8749

Recovered SHA-256:
554f5147984d75fe7e43c6f15d08e3d52097907a122299c06613e84b3b4c8749

The hashes matched.

The recovered file was identified as PDF version 1.4.
The original and recovered sizes were identical.

## 6. Tools Used

- Foremost 1.5.7
- SHA-256
- cmp
- file

## 7. Limitations

- The disk image and files are synthetic.
- The PDF is a minimal zero-page test document.
- The exercise tests signature-based carving, not recovery
  from a real deleted filesystem entry.
- The TXT file was not carved because ordinary text has
  no unique file signature.
- No claim is made about recovering fragmented files.

## 8. Conclusion

Foremost successfully identified and extracted one PDF file
from the raw image.

The recovered file matched the original byte-for-byte,
as demonstrated by identical SHA-256 hashes and file sizes.

The exercise demonstrates basic signature-based file carving
and recovery validation.
