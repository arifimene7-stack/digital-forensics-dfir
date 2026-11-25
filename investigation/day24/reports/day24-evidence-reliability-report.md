# Day 24 — Evidence Reliability and Contradiction Analysis

## 1. Objective

Evaluate the reliability, integrity, limitations, and consistency of the evidence examined during the DFIR project.

The analysis distinguishes content integrity from source authenticity and separates observed discrepancies from proven manipulation.

## 2. Evidence Reliability Methodology

Evidence was evaluated using the following criteria:

- Integrity: whether available hash comparisons support unchanged content.
- Source reliability: whether the origin and context are sufficiently established.
- Completeness: whether relevant evidence is available.
- Accuracy: whether timestamps and recorded information can be interpreted reliably.
- Corroboration: whether independent evidence supports the same finding.
- Limitations: whether technical or contextual gaps affect conclusions.

Reliability ratings are qualitative and apply only within the documented laboratory scope.

A matching SHA256 hash supports content equality. It does not independently prove authenticity, provenance, or accuracy.

## 3. Reliability Assessment

The accompanying evidence-reliability-matrix.csv evaluates twelve evidence sources.

### Higher reliability within laboratory scope

- FAT16 recovered sample: recovered content matched the original sample.
- Browser database: source and working copies matched.
- File carving: recovered PDF matched the source PDF.
- ext4 extracted files: extracted samples matched their source files.

These results demonstrate successful technical validation within controlled exercises. They do not independently establish a real-world incident.

### Limited reliability

- FAT16 metadata: timestamp precision is limited.
- NTFS metadata: a timestamp inconsistency was observed.
- Process and network snapshots: represent a single point in time.
- Process-network correlation: depends on the accuracy and timing of source snapshots.
- Master timeline: combines independent datasets and contains unknown timestamps.

### Insufficient evidence

No forensic RAM image was available. Therefore, memory-image analysis was not performed.

No packet capture was available to verify network payloads or communication content.

## 4. Contradiction Analysis

The accompanying contradiction-register.csv records six discrepancies or interpretation limitations.

### C-01: Historical Hash Discrepancy

The historical manifest records:

`ee5bd815b5a848eb6b1fdc9f0cc2c00cc25122a464a6937066a6c250d180f3f1`

The current original and working-copy files both produce:

`d859f943e32986ef0286a189646059d5a547641b087eafb37a12b05b3324d0e0`

The integrity report documents publication redaction.

Assessment:
The current copies match each other but do not match the historical hash. The historical PASS result cannot be applied to the current redacted files.

### C-02: NTFS Timestamp Inconsistency

Different timestamp values were observed in the examined MFT timestamp fields.

Assessment:
The discrepancy is documented, but intentional timestamp manipulation has not been established.

### C-03: Timeline and Capture Time

The live-triage capture timestamp represents the collection time.

Assessment:
It must not be interpreted as the occurrence time of every process or network event in the snapshot.

### C-04: Unknown Timeline Events

Three events have unknown timestamps.

Assessment:
Their exact chronological positions remain unresolved.

### C-05: FAT16 Timestamp Precision

FAT16 timestamps have limited precision.

Assessment:
Small timing differences cannot automatically be interpreted as evidence of manipulation.

### C-06: Independent Datasets

The consolidated timeline combines separate synthetic training datasets.

Assessment:
Their proximity in the timeline does not establish a common incident or causal relationship.

## 5. Impact on Investigation Conclusions

The identified limitations affect the strength of conclusions:

- Historical integrity of the current redacted host-events.log cannot be verified against its old manifest.
- Exact chronology cannot be established for three events.
- NTFS timestamp interpretation remains uncertain.
- Network communication content remains unavailable.
- Memory-resident evidence remains unexamined.
- Independent synthetic datasets cannot establish a unified real incident.

These limitations reduce investigative completeness but do not independently demonstrate compromise.

## 6. Recommended Evidence Handling Improvements

1. Preserve original evidence separately from redacted publication copies.
2. Generate a new hash manifest for every authorized modified version.
3. Retain historical manifests unchanged.
4. Record timestamps with their source and timezone.
5. Preserve unknown timestamps instead of estimating them.
6. Document the limitations of each forensic tool.
7. Corroborate important findings using independent sources.
8. Avoid treating temporal proximity as proof of causation.
9. Clearly distinguish synthetic laboratory evidence from real incident evidence.

## 7. Final Assessment

The project demonstrates successful integrity comparisons and recovery validation for several controlled laboratory samples.

However, some evidence has limited completeness or unresolved interpretation issues.

The historical hash discrepancy is explained by documented redaction. The NTFS timestamp inconsistency remains unexplained. Three timeline events lack exact timestamps.

No confirmed malicious anti-forensic activity or real-world compromise was established by the examined evidence.

The overall conclusion remains:

**No confirmed compromise based on the available evidence. The assessment is limited by evidence completeness, source context, and unresolved interpretation issues.**

## 8. Reproducibility

Supporting files:

- `analysis/evidence-reliability-matrix.csv`
- `analysis/contradiction-register.csv`
- `investigation/day23/analysis/uncertainty-register.csv`
- `investigation/day21/reports/day21-integrated-investigation.md`
- `investigation/day23/reports/day23-anti-forensics-analysis.md`
- `evidence-integrity/reports/integrity-report.md`
- `timeline-engineering/day19/reports/day19-timeline-report.md`
