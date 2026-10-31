# Day 8 — Live Memory Triage Report

## 1. Objective
Perform preliminary live-system triage and inspect running processes,
memory usage, and network connections.

## 2. System Memory
- Total RAM: 7.0 GiB
- Used RAM: 3.1 GiB
- Available RAM: 3.9 GiB
- Swap used: 616 KiB

## 3. Process Investigation

Investigated PID: 5603

- Process name: Socket Process
- Parent PID: 5600
- User: training-user (UID 1000)
- State: Sleeping
- Threads: 6
- Executable:
  /snap/firefox/8995/usr/lib/firefox/firefox

Process tree showed:
Firefox (PID 5389)
  -> forkserver (PID 5600)
     -> Socket Process (PID 5603)

The command line and executable path are consistent with
a Firefox content process.

## 4. Executable SHA-256

e4cb6178d7b335df55c307bdec103e7c98ef7eef9f57cf2f2936750c3ded0c67

This hash identifies the executable observed during the examination.
It does not independently establish that the executable is trusted.

## 5. Network Findings

Two UDP sockets were associated with PID 5603:
- REDACTED_LOCAL_IP:39122
- REDACTED_LOCAL_IP:49884

lsof displayed warnings about inaccessible FUSE filesystems.
Therefore, its output may be incomplete.

## 6. Assessment

The process tree, executable path, command line, and cgroup
are consistent with a Firefox Socket Process.

No evidence collected in this examination confirms malicious activity.

## 7. Limitations

- This was live-system triage, not a full RAM dump analysis.
- Process and network information represents a point in time.
- No memory image was analyzed with Volatility.
- The executable hash was not compared with an independently
  trusted reference.
- Findings should not be interpreted as proof that the entire
  system is free of compromise.

## 8. Conclusion

Preliminary live triage was completed.
The examined process appears consistent with normal Firefox activity.
Full memory-image analysis remains outstanding.
