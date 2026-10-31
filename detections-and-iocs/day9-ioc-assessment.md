# Day 9 — IOC Assessment

| Indicator | Source | Classification | Assessment |
|---|---|---|---|
| Failed login for testuser | host-events.log | Security event | Requires additional investigation |
| Firefox PID 5603 | Live triage | Process observation | No confirmed malicious indicator |
| Firefox executable SHA-256 | Live triage | File hash | No trusted reference for comparison |
| events.log deletion | Day 7 report | Lab activity | Authorized test action |

## Conclusion

No confirmed malicious IOC was identified in the available evidence.

A failed login is an event requiring context, not automatically an IOC.
A process hash without a trusted comparison source cannot establish
whether a file is malicious.
