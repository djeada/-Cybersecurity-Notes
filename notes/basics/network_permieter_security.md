## Network Perimeter Security

### Firewalls and Network Security

**Firewalls:**
Firewalls are essential for preventing unwanted access to networks by blocking specific ports and IP addresses.

- **ACL (Access Control List):** Determines which packets are allowed or denied access.
- **Packet Filtering:** Inspects and filters unwanted packets.
  - **Stateless:** Does not keep track of previous packets.
  - **Stateful:** Keeps a record of previous packets for cumulative filtering.
- **NAT Filtering:** Filters according to matching inbound and outbound ports.
- **Application Level Gateway:** Security measures applied to a specific application.
- **Circuit Level Gateway:** Only checks if a connection is valid, ignoring the validity of individual packets.
- **Firewall Logging:** Logs all connections and blocked packets.

**Types of Firewalls:**
1. **Packet Filtering Firewalls:**
   - **Description:** The most basic form, observes packet headers to see if they violate firewall rules.
2. **Stateful Firewalls:**
   - **Description:** Keeps track of established sessions and filters unwanted requests to open new connections.
3. **Application Firewalls:**
   - **Description:** Blocks or allows specific applications to communicate.
4. **Web Application Firewalls:**
   - **Description:** Specifically designed for HTTP sessions, focusing on web-based applications.

---

### Proxy Servers

**Function:**
Proxy servers act as intermediaries between LAN clients and outside servers, providing an additional layer of security.

**Types of Proxies:**
1. **IP Proxy:**
   - **Function:** Uses NAT to hide client IP addresses, a basic function of routers.
2. **Caching Proxy:**
   - **Function:** Saves remote server data for efficiency, commonly used in HTTP proxies.
   - **Note:** Disable PAC (Proxy Auto Configuration) files for better security.
3. **Reverse Proxy:**
   - **Function:** Protects LAN servers from outside clients by acting as an intermediary.
4. **Application Proxy:**
   - **Function:** Acts as a remote connection application, often modifying client requests for anonymity and security.

**Transparent Proxies:**
Proxies that do not modify client requests are called transparent proxies.

**Internet Content Filtering:**
- **Function:** Can be installed on each host, but more efficient when installed on a proxy.

**Web Security Gateways:**
- **Function:** Actively monitors and filters user data streams, often part of UTM (Unified Threat Management) systems.

---

### Honeypots / Honeynets

**Definition:**
Honeypots and honeynets are decoy systems or networks used to study and analyze attacker behavior. They can range from a single file or machine to an entire network.

---

### DLP (Data Loss Prevention)

**Function:**
DLP systems stop the leakage of confidential information through content inspection. They detect company-confidential information and prevent it from exiting the network.

- **Cloud-Based DLP:** More suitable if data is stored on the cloud or used in BYOD (Bring Your Own Device) scenarios.

---

### NIDS vs. NIPS

**NIDS (Network Intrusion Detection System):**
- **Function:** Attempts to detect malicious network activities such as port scans and DDoS attacks.
- **Common Solutions:** Snort (open source), Bro (open source).
- **Placement:** Often placed before a firewall but also in key network locations.
- **Promiscuous Mode:** Allows NIDS to examine all network packets.
- **Pros:** 
  - Effective detection of network intrusion.
  - Installed on only a few machines to cover the whole network.
- **Cons:** 
  - Cannot read encrypted traffic.
  - Cannot monitor individual machines.
  - Passive (does not prevent attacks).

**NIPS (Network Intrusion Prevention System):**
- **Function:** Inspects packets and removes or redirects malicious traffic. It is an application-aware device, able to associate packets with specific applications.
- **Pros:** 
  - Can protect non-computer-based network devices (routers, switches).
  - Prevents attackers from entering the network (active).
  - Able to read encrypted traffic.
- **Cons:** 
  - Single point of failure; can bring down the entire network if knocked out.
  - Prone to false positives/negatives.
  - Fail-open/close scenarios.
  - Uses more resources.

---

### Protocol Analyzer

**Function:**
Captures and analyzes packets, allowing for inspection of packet content, useful for deep packet analysis.

---

### UTM (Unified Threat Management)

**Definition:**
UTM systems represent a culmination of various network defenses in a single device, often referred to as an all-in-one device or NGFW (Next Generation Firewall).

- **Risk:** Can also serve as a single point of failure if not properly managed.
