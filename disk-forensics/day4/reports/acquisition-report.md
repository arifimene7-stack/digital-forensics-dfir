# Day 4 — Forensic Disk Acquisition Report

## 1. Objective

Create a forensic copy of a synthetic training disk image
and verify its integrity.

## 2. Source Evidence

- File: training-disk.img
- Location: disk-forensics/day4/source/
- Size: 10 MiB
- Type: Raw binary data
- Origin: Analyst-generated synthetic training data

## 3. Acquisition Method

A bit-for-bit copy was created using the Linux dd utility.

- Source: training-disk.img
- Destination: training-disk-copy.img
- Block size: 1 MiB

## 4. Integrity Verification

SHA-256 source:
74bdf9d5b168ce9a5d8fd7f23624adee755a93d0b7653f6ed9a4eba6fab56b5f

SHA-256 copy:
74bdf9d5b168ce9a5d8fd7f23624adee755a93d0b7653f6ed9a4eba6fab56b5f

Comparison using cmp:
PASS — Images are identical.

## 5. Conclusion

The forensic copy matches the synthetic source image.

The SHA-256 hashes are identical, and byte-level comparison
confirmed that no differences were detected.

This exercise demonstrates basic image copying and
integrity verification. It does not represent acquisition
from a physical storage device.
