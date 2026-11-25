# Day 26 — DFIR Automation and Validation

## Objective

Develop and validate a Python tool for forensic file integrity comparison.

## Implementation

The tool `dfir_validator.py` provides:

- SHA256 calculation using chunk-based file reading.
- Comparison of original and working-copy hashes.
- JSON output containing paths, hashes, comparison result, and generation time.
- Exit status 0 for matching files and 1 for mismatches.

## Automated Testing

Four unit tests were executed successfully:

1. SHA256 calculation.
2. Identical-file comparison.
3. Modified-file detection.
4. Empty-file handling.

Result: 4 tests passed.

## Practical Validation

The tool compared:

- Original: disk-forensics/day6/source/filesystem-lab.img
- Working copy: disk-forensics/day8/working/filesystem-analysis.img

Both SHA256 values were:

`5e1bdc964fc6ec43e955c67a07b01df76e2cec234e16f648b1d676c2fe4ceeef`

Result: MATCH.

The JSON report was saved to:

`investigation/day26/output/fat16-integrity-report.json`

## Limitations

The tool verifies content equality through SHA256.

It does not establish evidence authenticity, acquisition provenance, chain of custody, or historical integrity.

## Conclusion

The automation tool passed all four unit tests and successfully validated the selected forensic image pair.
