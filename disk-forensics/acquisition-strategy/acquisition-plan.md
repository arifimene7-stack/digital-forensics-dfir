# Acquisition Plan — Day 3

## 1. Case Scenario

An organization reports suspicious activity on an employee's
workstation.

The investigator must identify relevant evidence while
preserving its integrity.

This is a synthetic educational scenario.

## 2. Investigation Objectives

- Identify relevant files.
- Understand the system's current running state.
- Preserve storage evidence for further examination.
- Maintain evidence integrity and documentation.

## 3. Selected Acquisition Methods

### A. Logical Acquisition

Purpose:
Collect relevant files and directories.

Reason:
The investigation requires examination of selected files.

### B. Live Response

Purpose:
Document volatile system information, such as running
processes and active network connections.

Reason:
This information may change or disappear when the system
is shut down.

### C. Physical Acquisition

Purpose:
Preserve a broader storage-level representation for
subsequent forensic examination.

Reason:
Further examination may require filesystem metadata
and unallocated-space analysis.

## 4. Acquisition Order and Considerations

1. Confirm authorization and investigation scope.
2. Document the system state and collection conditions.
3. Consider volatile evidence before shutdown.
4. Collect authorized logical evidence.
5. Acquire storage evidence using an approved forensic
   procedure, where technically and legally appropriate.
6. Calculate and record SHA-256 hashes.
7. Verify acquired copies.
8. Document tools, versions, timestamps, and handlers.

## 5. Evidence Preservation

- Do not analyze original evidence directly.
- Use verified forensic copies for examination.
- Record every evidence transfer.
- Maintain a chain-of-custody record.
- Document errors and limitations.

## 6. Risks and Limitations

- Live response can change system state.
- Encryption may limit acquisition.
- Physical acquisition requires suitable storage and tools.
- Acquisition must remain within authorized scope.
- No real workstation or disk was acquired in this exercise.

## 7. Conclusion

A combination of live response, logical acquisition,
and physical acquisition may provide complementary
evidence.

The final method depends on authorization, investigation
objectives, system state, and technical constraints.
