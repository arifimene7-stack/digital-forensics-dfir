# Day 17 — Network Artifacts Analysis

## 1. Objective
Analyze recorded network connections, listening services,
remote peers, and process associations.

## 2. Evidence
Source: Linux live network-connection snapshot.
The source contains 25 lines, including its header.

Specific host identifiers and network addresses are
excluded from this public report.

## 3. Connection States

| Protocol / State | Count |
|---|---:|
| TCP ESTAB | 5 |
| TCP LISTEN | 7 |
| TCP TIME-WAIT | 1 |
| UDP ESTAB | 1 |

## 4. Established TCP Connections

Five established TCP connections were associated with
a browser process. All observed remote connections
used port 443.

The use of port 443 is consistent with HTTPS traffic.
The captured data does not reveal the encrypted content
or establish the identity of the remote services.

Remote addresses and process identifiers are omitted
from this public version.

## 5. Listening Services

The snapshot showed local listening services associated
with DNS resolution, database services, and printing.

Virtualization-related network services were also observed.

Specific local addresses and host identifiers are omitted.

## 6. DHCP Observation

A UDP connection was consistent with DHCP client/server
communication.

Specific network addresses and interface identifiers
are omitted from this public version.

## 7. Process Associations

The captured output associated a browser process with
established TCP connections.

A separate process association was observed for UDP sockets.

Process identifiers are omitted.

## 8. Assessment

The observed connections were consistent with browser
HTTPS traffic and expected local services.

No confirmed malicious network connection was identified.

IP addresses, port numbers, and process associations
alone are insufficient to establish malicious activity
or remote service identity.

## 9. Limitations

- This is a point-in-time network snapshot.
- Encrypted traffic content was unavailable.
- No packet capture or DNS history was analyzed.
- Remote peer ownership was not independently verified.
- The evidence does not establish user intent.
- Host-specific identifiers were omitted from this
  public report.

## 10. Conclusion

The available network telemetry did not reveal a
confirmed malicious connection.

This conclusion is limited to the captured snapshot
and does not establish that all network activity
was benign.

---

End of Day 17 Report
