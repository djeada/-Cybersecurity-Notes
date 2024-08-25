Network Design Elements
Network Design
OSI Model
- Goals
1. Explain network connection between hosts on LAN/WAN
2. Present a categorization system for communication protocols
3. Shows how different protocol suits communicate
- Overview
Layer Name Usage Units
1 Physical Physical and Electrical medium Bits
2 Data link Establishes, maintains and decides
how data transfer is accomplished
over the physical layer
Frames
3 Network Routing and Switching Packets
4 Transport Manages/ensures error free
transmission between hosts through
logical addressing/port assignment
Segments(TCP)
Datagrams(UDP)
5 Session Establishment, termination and
synchronization of sessions within
the OS over the network and between
hosts
Messages
6 Presentation Sender to receiver data translation,
Code conversion, data compression
and file encryption
Messages
7 Application FTP, HTTP and SMTP end user
protocols
Messages
Network Devices
- Switch
> Central connection device, replaces hubs and bridges
> Translates MAC and MAC+IP into physical ports to route messages
> Attacks
1. MAC Flooding : Uses up the CAM to force switch into broadcast
2. MAC Spoofing : Masks network adapter MAC with different value
3. Physical Tampering : Vulnerable management ports, Looping
* Use hierarchial router structure or spanning tree
protocol to prevent looping
- Bridges
> Used to separate physical LAN into two logical networks
> Works on layer 2 (Data link), now obsolete
- Router
> Used to connect two or more networks
> Works on network 3 (Network)
> Various forms : SOHO, servers configures as routers, Cisco black box
> Attacks : DOS, malware intrusions etc
> Defenses
1. Secure configurations
2. Firewalls
3. IPS
4. Secure VPN Connectivity
5. Content filtering
6. ACL (Access Control Lists)
NAT (Network Address Translation), Private vs Public Addresses
- NAT : Process of changing IP in transit
- Motivation
> Allow a large private address space mapped to a smaller public one
> Firewall effect (hides internal IPs)
* Static NAT : Only one machine uses the router that does NAT
- Private IP
> Invisible to public(internet)
> Assigned automatically by SOHO router or DHCP server
> Within predetermined range
- Public IP
> Visible to public, anyone can attempt connection
> Assigned by ISP DHCP servers
* IPv6 Vulnerability
> By default attempts to automatically connect to other IPv6 addresses
> Make sure to secure both IPv4 and IPv6
Network Zones and Interconnections
- LAN (Local Area Network)
> Group of interconnected computers contained in a small space
> Usually uses private IPs behind a firewall
> By default does not have internet access, but may connect to an
Internet proxy to do so
- WAN (Wide Area Network)
> Network of two or more interconnected LANS
> Covers a larger geographical area
> Requires telecomm/datacomm service company
- Internet
> Worldwide interconnected network
> Must secure all transmission that happens over the internet
- DMZ (Demilitarized Zone)
> Special subnetwork designed for external client access
> Common web/FTP/email/database etc services reside in DMZ
> Can also be accessed by LAN clients
> Often placed in a separate LAN network from the rest of system
> Common 3-leg perimeter configuration
- Intranets & Extranets
> Used to share company data securely through the internet
> One company = intranet, multiple companies involved = extranet
> Never store confidential+ data in these networks
> Crucial to properly implement firewall
NAC (Network Access Control)
- Denies network access until client obtains proper security measures
- Antivirus, system updates etc
- Preinstalled clientside software (agent) or remote scan (agentless)
- Persistent vs Dissolvable agents
> Persistent : Designed for multiple use
> Dissolvable : Designed for one time authentication
- Agentless offers less control for more flexibility
- Cisco offers hardware solutions
Subnetting
- Process of creating logical subnetworks through IP manipulation
- Benefits
1. Compartmentalizes network, increasing security
2. Efficient use of IP address
3. Reduces IP collision and broadcast signals
- Overview
1. Class A : Large network, 255.0.0.0
2. Class B : Medium network, 255.255.0.0
3. Class C : Small network, 255.255.255.0
Example : 192.168.1.0/28  28 is total number of bits used
Class C Network
255.255.255.240  1111 1111 . 1111 1111 . 1111 1111 . 1111 0000
First 3 octets are Class C mask
First 4 bits of last octet is subnet mask, 2^4 = 16 subnets
Last 4 bits of last octet is host ID, 2^4-2 = 14 hosts
VLAN(Virtual LAN)
- Segments various networks sharing the same switch, reduce collision,
Organize network, boost performance and security
- Works on Layer 2 (Data link frames)
- Allows admins to group hosts connected on different switches together
- VLAN Hopping : Methods of gaining access to other VLANs on switch
1. Switch Spoofing
2. Double Tagging
Telephony
- Provides voice communications, fax etc
- Now computers are involved in telephony as CTI
- Modems
> Still often used to connect to networking equip. via dial up
> Very insecure (War dialing)
> Protections : Callback, username/pw, hide modem number
PBX(Private Branch Exchange)
- Makes internal phone connections, connects to PSTN
- New added features now make them less secure
VoIP
- Broad term for voice data over IP networks
- IP phones exploited the same way as regular computers
- Home VoIP solutions use SIP(Session Initiation Protocol) vulnerable to MiTM
Cloud Security and Server Defense
Definition of Cloud : Any network between two organization borders
Cloud Computing
- A method of offering on demand services normal users don’t have
- SaaS (Software as a Service)
> Allows user to have access to software they don’t have on host
- IaaS (Infrastructure as a Service)
> Offers networking, routing, VM hosting and other networking
- PaaS (Platform as a Service)
> Offers virtual development of application
- SECaaS (Security as a Service)
> Offers security services to be integrated into existing infra.
Different Types of Cloud
- Public Cloud : Full public access, low security
- Private Cloud : Full private access, high security
- Hybrid Cloud : Utilize both private and public depending on handled data
- Community Cloud : Private to specific group, good for collab projects
Cloud Security
- Depends on the amount of security control the admin has
- Defenses for sending data to cloud
1. Passwords : 10 char general case, 15 for confidential data
2. Multifactor authentication
3. Strong data access policy : passwords, multifactor, group policy
4. Encryption : strong PKI encryption on all files
5. Programming standardization
6. Data protection
* Unconventional data channels : Social media, P2P, dark net
Server Defenses
- Servers are most important part of network to secure
- Contains all data and services
1. File Servers
> Stores, transfer, migrate, synchronize and archive files
> Identical vulnerability to malware that target desktop PCs
> Hardening, updates, AV, SW/HW firewall, HIDS, encryption, monitoring
2. Network Controllers
> Central repo of all user and computer accounts
> LDAP injection, Kerberos vulnerabilities  privilege escalation
> Updates, hot fixes
3. Email Servers
> Deals with email, texting, fax, chat etc
> May run multiple services and ports, POP3, SMTP, IMAP, Outlook
> XSS, DDOS, SMTP memory exploits, directory traversal etc
> Updates, quarantine, HW/SW spam filter, DLP, encryption (TLS/SSL)
4. Web Servers
> Provide web and website services to users
Ex) Microsoft IIS, Apache HTTP, lighthttp, Oracle iPlanet
> DDOS, overflow attacks, XSS, XSRF, remote code exec., backdoors
> Secure programming, updates, HW firewall, HTTPS
* Darkleech : Apache based attack using malicious Apache modules
5. FTP Servers
> Basic file access (public/private)
> Web shells, weak authentication, bounce attacks, buffer overflow
> Strong password, secure encrypted FTP, dynamic port assignment
