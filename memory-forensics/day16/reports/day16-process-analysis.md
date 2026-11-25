# Day 16 — Process Analysis

## 1. Objective
Analyze recorded Linux process telemetry, identify unusual
execution paths, review process ownership, and examine
parent-child relationships.

## 2. Evidence
Source:
memory-forensics/day8/live-triage/processes.txt

Additional source:
memory-forensics/day8/process-analysis/process-5603.txt

The process listing contains 288 process records.

## 3. Process Ownership
| User | Process Count |
|---|---:|
| root | 180 |
| imene | 94 |
| systemd+ | 2 |
| avahi | 2 |
| Other service accounts | 10 |

System services running as root or dedicated service accounts
are not inherently suspicious.

## 4. Process Tree Findings
- Firefox PID 5389 is the parent browser process.
- PID 5600 is a Firefox content process.
- PID 5603 is a child Socket Process of PID 5600.
- PID 5482 is Firefox crashhelper.
- MySQL PID 1745 runs under the mysql account.
- libvirtd PID 1884 runs under root.

## 5. Executable Path Review
Firefox-related executable paths resolve within the installed
Snap package under /snap/firefox/8995/.

The /tmp/ string in the crashhelper command line is an
argument and does not establish execution from /tmp.

The executable links for PIDs 1745 and 1884 were not resolved
by the recorded readlink command; their paths remain unverified
in this analysis.

## 6. Suspicious Path Search
A search for /tmp/, /var/tmp/, and /dev/shm/ found one
command-line match: Firefox crashhelper.

No evidence from this match alone establishes malicious
execution.

## 7. Assessment
No clearly malicious process was identified in the examined
process listing and process tree.

The reviewed processes are consistent with the observed
Linux desktop, Firefox, MySQL, and virtualization services.

## 8. Limitations
- Analysis uses a previously recorded process snapshot.
- No physical memory image was available.
- Process ancestry and executable paths are point-in-time data.
- No complete behavioral or historical process analysis
  was possible.

## 9. Conclusion
The available process telemetry did not reveal a confirmed
malicious process.

This is a limited finding and does not prove that the host
was free of compromise.

---
End of Day 16 Report
