# Week 1 — DFIR Summary

## Completed Activities

1. Case intake and evidence registration.
2. SHA-256 hashing and integrity verification.
3. Comparison of logical, physical, and live acquisition.
4. Creation of a synthetic disk image and forensic copy.
5. Chain-of-custody documentation.
6. Basic forensic tool validation.

## Validation Results

- Three synthetic evidence files were registered.
- Original and working-copy hashes matched.
- A modification test successfully detected an integrity mismatch.
- The synthetic disk image and its copy had identical SHA-256 hashes.
- The cmp comparison returned PASS.

## Tools Used

- dd
- sha256sum
- cmp
- Python verification script

## Limitations

All evidence used in the exercises was synthetic.
No real workstation or physical disk was acquired.

## Conclusion

Week 1 introduced evidence preservation, integrity
verification, acquisition planning, and documentation.
