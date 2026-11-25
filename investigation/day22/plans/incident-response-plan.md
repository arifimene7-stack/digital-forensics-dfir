# Day 22 — Incident Response Plan

## 1. Purpose

This plan defines a structured response process for a suspected cybersecurity incident.

It is designed for authorized investigations and evidence-based decision-making.

The current training investigation did not establish a confirmed security compromise. This plan therefore provides procedures for a hypothetical incident.

## 2. Incident Response Objectives

- Protect systems and users.
- Preserve digital evidence.
- Establish the scope and impact of an incident.
- Identify the root cause where evidence permits.
- Contain and recover from confirmed incidents.
- Document decisions and lessons learned.

## 3. Incident Response Phases

### Phase 1 — Preparation

Actions:
- Maintain an inventory of systems and critical assets.
- Verify forensic tools and evidence storage.
- Define authorized investigation personnel.
- Prepare evidence registers and chain-of-custody records.
- Maintain secure backups and recovery procedures.

Expected output:
- Prepared investigation environment.
- Available response procedures and documentation.

### Phase 2 — Identification and Analysis

Actions:
- Review alerts and reported suspicious activity.
- Collect relevant logs and system information.
- Validate timestamps and evidence integrity.
- Examine processes, network activity and persistence indicators.
- Correlate evidence from independent sources.
- Evaluate hypotheses and confidence levels.

Decision:
- If evidence is insufficient, continue investigation.
- If suspicious activity is confirmed, assess its scope and severity.
- Do not classify an event as a confirmed compromise without supporting evidence.

### Phase 3 — Containment

Actions:
- Obtain authorization before containment.
- Identify affected systems and accounts.
- Isolate affected systems when justified.
- Preserve volatile evidence when feasible and authorized.
- Document every containment action and its impact.

Important:
Containment must not unnecessarily destroy or modify evidence.

### Phase 4 — Eradication

Actions:
- Identify and remove confirmed malicious artifacts.
- Address exploited vulnerabilities.
- Review affected accounts and permissions.
- Validate system integrity.
- Document the evidence supporting each remediation action.

Do not remove suspected artifacts before appropriate evidence preservation.

### Phase 5 — Recovery

Actions:
- Restore systems from trusted backups.
- Apply required security updates.
- Verify system functionality and security controls.
- Monitor systems for recurring suspicious activity.
- Obtain approval before returning systems to normal operation.

### Phase 6 — Post-Incident Review

Actions:
- Prepare the final incident report.
- Record the timeline and decisions.
- Identify control weaknesses.
- Document lessons learned.
- Recommend preventive improvements.

Expected output:
- Final report and improvement plan.

## 4. Evidence Handling Requirements

For every collected item:
1. Assign a unique evidence ID.
2. Record its source and acquisition time.
3. Record the collector and acquisition method.
4. Calculate a SHA256 hash where applicable.
5. Preserve the original evidence.
6. Perform analysis on a working copy when possible.
7. Record every transfer or access.
8. Document limitations and integrity discrepancies.

## 5. Severity and Escalation

| Level | Description | Response |
|---|---|---|
| Low | Unusual activity without confirmed impact | Document and investigate |
| Medium | Credible suspicious activity requiring further analysis | Escalate and increase monitoring |
| High | Confirmed compromise with significant impact | Activate incident response and containment |
| Critical | Widespread or severe impact on critical systems | Immediate escalation and coordinated response |

Severity must be based on evidence, impact, and business context.

## 6. Communication

- Notify the authorized incident response lead.
- Escalate significant findings to the responsible security team.
- Share evidence only with authorized personnel.
- Keep communications factual and time-stamped.
- Avoid unsupported conclusions.

## 7. Closure Criteria

An incident may be closed when:
- The investigation scope is documented.
- Available evidence has been reviewed.
- Findings and limitations are recorded.
- Required containment and recovery actions are verified.
- Evidence records are complete.
- The final report is approved.

An inconclusive investigation must be documented as inconclusive, not automatically classified as clean.

## 8. Application to This Training Investigation

Current assessment:
- No confirmed real-world compromise was established.
- No RAM image was available for memory-image analysis.
- No packet capture was available.
- Process and network findings came from point-in-time live-triage snapshots.
- Most disk and browser datasets were synthetic laboratory evidence.

Therefore:
- No real-system containment or eradication action is justified by the current findings.
- The appropriate action is to preserve the evidence, document limitations, and retain the investigation as an inconclusive training assessment.

## 9. Final Principle

All incident response actions must be authorized, proportionate, documented, and supported by evidence.
