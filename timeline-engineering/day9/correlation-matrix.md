# Day 9 — Evidence Correlation Matrix

| Evidence ID | Evidence | Related Hypothesis | Correlation | Assessment |
|---|---|---|---|---|
| EV-01 | Failed login for testuser | H1 | No successful login evidence available | Inconclusive |
| EV-02 | Firefox PID 5603 process tree | H2 | Consistent with Firefox parent process | No confirmed threat |
| EV-03 | Firefox executable path | H2 | Located in Firefox installation directory | Consistent with expected application |
| EV-04 | Deleted events.log | H3 | Deletion occurred during authorized lab exercise | Not malicious |
| EV-05 | Recovered events.log hash | H3 | Matches original SHA-256 | Integrity verified |
| EV-06 | Synthetic host event log | H1 | Contains one failed login event | Limited evidence |

## Correlation Limitations

- Evidence is synthetic or generated during laboratory exercises.
- No independent authentication logs were available.
- No full RAM image was acquired.
- No real endpoint compromise was investigated.
- Correlation does not independently prove causation.

## Conclusion

The available evidence does not establish a confirmed security incident.
The failed login requires additional context, while the examined Firefox
process is consistent with normal operation. The deleted file was part
of an authorized recovery exercise.
