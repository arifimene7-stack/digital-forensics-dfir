# Day 8 — Memory Forensics Summary

## Completed
- Performed live memory and process triage.
- Examined process PID 5603 and its network sockets.
- Installed Volatility 3 (version 2.28.2).
- Installed and built LiME for the current kernel.
- Inspected LiME module signature and Secure Boot configuration.
- Documented the training-image reference and analysis limitations.

## Not Completed
- No RAM image was acquired.
- No Volatility analysis was performed on a memory image.
- LiME was not loaded because its signing key is not enrolled.

## Conclusion
Live triage identified a Firefox Socket Process consistent with normal
Firefox operation. No confirmed malicious activity was established.

Memory-image analysis remains an outstanding limitation. The live
triage findings must not be presented as a forensic RAM-image analysis.
