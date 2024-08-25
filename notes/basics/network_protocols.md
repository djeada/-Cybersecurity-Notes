## Networking Protocols and Threats

### Ports and Protocols

#### Port Ranges, Inbound vs. Outbound, Common Ports
- **Ports:** Logical communication endpoints that are essential for network protocols.
- **TCP vs. UDP:**
  - **TCP (Transmission Control Protocol):** Ensures ordered, reliable communication, making it connection-oriented.
  - **UDP (User Datagram Protocol):** Provides faster, connectionless communication, suitable for real-time data like streaming.
- **Port Ranges:**
  - **0 – 1023:** Well-known ports (e.g., HTTP, FTP).
  - **1024 – 49151:** Registered ports for proprietary applications.
  - **49152 – 65535:** Dynamic and private ports, used for temporary or custom communications.

#### Inbound vs. Outbound Ports
- **Inbound Ports:** Usually involve well-known ports that need to be secured by an administrator.
- **Outbound Ports:** Used to initiate connections from a client to a server; dynamic port assignment can enhance security.

#### Well-Known Ports
| Port  | Protocol | TCP/UDP | Secure Version | Usage                                             |
|-------|----------|---------|----------------|---------------------------------------------------|
| 21    | FTP      | TCP     | FTPS, 989/990  | File transfer between hosts                        |
| 22    | SSH      | TCP/UDP | N/A            | Secure shell connection                           |
| 23    | Telnet   | TCP/UDP | N/A            | Remote administration (deprecated)                |
| 25    | SMTP     | TCP     | SMTP w/ TLS, 465/587 | Sends email                                 |
| 53    | DNS      | TCP/UDP | DNSSEC         | Hostname to IP resolution                         |
| 80    | HTTP     | TCP     | HTTPS, 443     | Transmit web page data                            |
| 110   | POP3     | TCP     | POP3 w/ TLS, 995 | Receives email                                  |
| 143   | IMAP     | TCP     | IMAP4 w/ TLS, 993 | Email retrieval                              |
| 389   | LDAP     | TCP/UDP | LDAP w/ TLS, 636 | Directory services                             |
| 445   | SMB      | TCP     | N/A            | Shared access to files and resources              |
| 514   | Syslog   | UDP     | Syslog w/ TLS, 6514 | Computer message logging                      |
| 3389  | RDP      | TCP/UDP | N/A            | Remote Desktop Protocol for Windows               |

### Malicious Attacks

#### Denial of Service (DOS) – Resource Depletion Attacks
- **Flood Attack:** 
  - **Ping Floods:** Utilizes ICMP packets (disable ICMP to protect servers).
  - **Smurf Attack:** Redirects ICMP echoes to a spoofed IP address.
  - **SYN Flood:** Sends excessive TCP SYN packets to overwhelm a target.
  - **Xmas Flood:** Aims to reboot routers by sending packets with all flags set.
- **Ping of Death:** Sends oversized or malformed packets to crash services (mostly mitigated by modern OSes).
- **Teardrop Attack:** Mangled IP fragments crash IP reassembly code.
- **Permanent DOS:** Flashes custom images onto routers or devices, rendering them unusable.
- **Fork Bomb:** Forces numerous processes, saturating the processor.

#### Distributed Denial of Service (DDOS)
- Utilizes botnets to overwhelm and DOS a target.
- Common defenses: ACL routers, firewalls, IPS, simulated servers.

#### Spoofing Attacks
- **Spoofing:** Impersonation of various identifiers like IP, MAC addresses, or session tokens.
- **Session Hijacking:** 
  - **Session Theft:** Hijacking browser sessions through cookies.
  - **TCP/IP Hijacking:** Predicts the next sequence number in TCP to inject data.
  - **Blind Hijacking:** Injects data without knowing the session state.
- **Man-in-the-Middle (MitM):** Intercepts and possibly alters communication between two parties.

#### Replay Attacks
- Attacker saves and reuses valid packets later.
- **Defenses:** Use session tokens, timestamps, synchronization, cryptography, and nonces.

#### Null Session
- Uses ports 139 and 445 (NetBIOS and SMB) to establish unauthenticated connections, often on older Windows systems.

#### Transitive Access and Client-side Attacks
- Compromising a trusted user to indirectly compromise a server.
- **Defenses:** Only establish temporary, necessary trust relationships.

#### DNS Poisoning
- Improper modification of DNS information, redirecting users to malicious sites.
- **Defenses:** TLS, DNSSEC, TSIG, and regular server patches.

#### ARP Poisoning
- ARP resolves IP addresses to MAC addresses.
- **Defense:** VLAN segmentation and separation to limit the scope of damage.
