# Day 25 — IOC Development and Detection Handoff

## 1. Purpose

Provide the detection and SOC team with validated observations, contextual indicators, confidence levels, and recommended follow-up actions.

## 2. Investigation Summary

The investigation did not establish a confirmed real-world compromise.

Process and network observations originated from a point-in-time live-triage snapshot. No forensic RAM image or packet capture was available.

The IOC list therefore includes contextual observations and evidence discrepancies, not confirmed malicious indicators.

## 3. Key Observations

### Process Context

Firefox PID 5603 was correlated with the process snapshot.

Its executable context and process relationship were consistent with Firefox activity.

No confirmed malicious behavior was established.

### Network Context

Five established TCP connections were associated with Firefox PID 5389 in the examined snapshot.

The connections used remote HTTPS endpoints, but their content and ownership were not independently verified.

No malicious network activity was confirmed.

### Evidence Integrity

The current host-events.log copies match each other but differ from the historical manifest because of documented publication redaction.

This discrepancy must not be treated as a confirmed compromise indicator.

### Filesystem Metadata

An NTFS timestamp inconsistency was observed.

The cause remains undetermined, and intentional timestamp manipulation was not established.

## 4. Recommended Detection and Monitoring

1. Monitor unexpected executable paths and unusual parent-child process relationships.
2. Correlate suspicious network connections with DNS, process, and endpoint telemetry.
3. Preserve process and network snapshots with accurate collection timestamps.
4. Maintain separate hashes for original and redacted evidence.
5. Investigate timestamp inconsistencies using additional independent metadata.
6. Escalate only when multiple independent indicators support suspicious activity.

## 5. Detection Limitations

- No RAM image was available for memory-based detection.
- No packet capture was available for network-content analysis.
- No confirmed malicious IOC was identified.
- Synthetic laboratory datasets do not establish a real incident.
- A process ID or IP address alone is not proof of malicious activity.

## 6. SOC Handoff Decision

**Status: Informational handoff — no confirmed incident.**

The listed observations may support future correlation and monitoring, but they should not be deployed as blocking rules or treated as confirmed malicious indicators without further validation.

## 7. Required Follow-up Evidence

If a real incident is later suspected, obtain authorized endpoint telemetry, memory acquisition where appropriate, DNS records, packet capture, and independently preserved filesystem evidence.

## 8. Conclusion

The investigation produced useful forensic observations and documented evidence limitations.

No confirmed compromise or malicious indicator was established.

The SOC team should retain the observations as contextual information and reassess them only if additional corroborating evidence becomes available.
