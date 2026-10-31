# Evidence Integrity Report

## Case ID
DFIR-2026-001

## Hash Algorithm
SHA-256

## Objective
Verify the integrity of original evidence and forensic working copies.

## Method
1. Generate SHA-256 hashes for original evidence.
2. Create working copies.
3. Calculate hashes for working copies.
4. Compare original and working-copy hashes.

## Expected Result
All original and working-copy hashes must match.

## Limitations
A matching SHA-256 hash supports file-integrity verification.
It does not independently prove evidence authenticity or source reliability.

## Results

Three original evidence files were compared with their working copies.

| Evidence | Verification |
|---|---|
| analyst-notes.txt | PASS |
| file-inventory.csv | PASS |
| host-events.log | PASS |

## Tampering Detection Test

A separate temporary test file was created with different content.

The verification script returned:
- RESULT: FAIL - Integrity mismatch
- Exit code: 1

The test confirmed that content changes are detected.

## Conclusion

All three working copies matched their original evidence
during verification.

The modification test successfully detected a mismatch.

SHA-256 verifies content integrity but does not independently
establish evidence authenticity or source reliability.

## Publication Redaction Notice

Before public release, host-specific identifiers were redacted
from host-events.log in both the original and working-copy paths.

Consequently:
- The current files are identical to each other.
- Their current SHA-256 hashes do not match the previously recorded hashes.
- The historical hash verification for host-events.log is therefore FAILED.
- The original unredacted content is not represented by these published files.

The previous hash manifest has been preserved unchanged.
The original PASS result must not be interpreted as verification
of the currently published, redacted files.

The verification script compares the current original and working
copy directly; it does not validate either file against the
historical manifest.
