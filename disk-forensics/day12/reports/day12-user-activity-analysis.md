# Day 12 — Metadata, User Activity and Browser Artifacts

## 1. Objective

Examine synthetic file metadata, browser history, download records,
and user activity logs. Construct a normalized timeline while
preserving the source of each event.

## 2. Evidence

The training evidence consists of:

- browser-history.db
- document.txt
- activity.log

All evidence is synthetic and was created specifically for this lab.

## 3. Metadata Examination

ExifTool 13.50 was used to examine document.txt.

Observed properties:
- File type: TXT
- File size: 99 bytes
- MIME type: text/plain
- Encoding: us-ascii
- Line count: 3
- Word count: 12

The filesystem modification, access, and inode-change
timestamps were reported as 2026-11-01 00:50:12 +01:00.

These timestamps describe the lab file metadata and are not
independent proof of user activity.

## 4. Browser History Analysis

SQLite was used to examine the synthetic browser database.

Three URL records were identified:

| URL | Title | Visit Count | Last Visit |
|---|---|---:|---|
| https://example.org/ | Example Domain | 3 | 09:10 |
| https://example.org/security | Security Training | 2 | 09:25 |
| https://example.net/report.pdf | Training Report | 1 | 09:40 |

One download record was identified:

- Target: /home/analyst/Downloads/report.pdf
- Source URL: https://example.net/report.pdf
- Recorded start time: 09:41
- Received bytes: 204800

These records represent synthetic browser data, not activity
from a real browser profile.

## 5. User Activity Log

The synthetic activity log contains:

- 09:00 — User session started.
- 09:10 — Browser opened.
- 09:25 — Security training page visited.
- 09:41 — Training report downloaded.
- 10:00 — User session ended.

## 6. Timeline Reconstruction

A normalized CSV timeline was generated at:

`analysis/day12-timeline.csv`

It combines browser history, download records, and activity log
entries while preserving the source of each event.

The browser and activity-log timestamps are synthetic
timestamps recorded in the training data.

The document filesystem timestamps belong to a different
metadata source and were not treated as equivalent event times.

## 7. Integrity Verification

The source and working browser databases were compared.

SHA-256:
`50997f1509b4e739e9585a97abd7cb2852a9f25b88787e8f0e5632fee32110e0`

Result:
- Hashes matched.
- Binary comparison passed.

## 8. Tools Used

- ExifTool
- SQLite
- Python 3
- sha256sum
- cmp

## 9. Limitations

- All evidence is synthetic.
- Browser records do not establish the identity of a real user.
- Visit counts and timestamps are database values, not independent
  proof that a person viewed or interacted with a page.
- No real browser profile was examined.
- Filesystem timestamps may be affected by file creation,
  copying, or later access.
- Timeline conclusions are limited to the supplied records.

## 10. Conclusion

The synthetic browser database and activity log were examined
successfully. Three URL records and one download record were
identified.

A normalized timeline was generated, and the source and working
browser databases passed integrity verification.

The exercise demonstrates metadata examination, browser artifact
analysis, and basic timeline reconstruction. It does not establish
real-world user attribution or malicious activity.
