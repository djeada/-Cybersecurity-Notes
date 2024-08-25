## PKI and Encryption Protocols

### PKI (Public Key Infrastructure)

PKI is a system of trust that uses public key cryptography to bind a certificate to an identity.

**Certificates:**
- **Definition:** Digitally signed electronic documents that bind a public key with an entity.
- **Format:** Mostly based on the X.509 format to facilitate Single Sign-On (SSO).
- **Contents:**
  - **User Information and Public Key**
  - **Certificate Authority Information:** Includes the name, digital signature, serial number, and issue/expiration date.
- **Usage:** Primarily used for HTTPS connections but can also be utilized for local encryption.

**Types of SSL Certificates:**
- **Domain Validation (DV):** Validates domain ownership.
- **Organizational Validation (OV):** Validates the organization behind the domain.
- **Extended Validation (EV):** Provides the highest level of validation, including the organization's legal identity.
- **Wildcard Certificates:** Secure an unlimited number of subdomains under a single domain.

**Single-Sided vs. Double-Sided Certificates:**
- **Single-Sided:** Validates the server to its users/clients.
- **Double-Sided:** Both the server and the user validate each other.

---

### Certificate Chain of Trust

The Certificate Chain of Trust is used to validate different pieces of hardware and software, providing scalability and flexibility in managing certificates.

**Certificate Formats:**
- **Identifying Formats by Extension and Encoding:**
  - **X.609 Encoding Rules:**
    - **BER (Basic Encoding Rule)**
    - **CER (Canonical Encoding Rule)**
    - **DER (Distinguished Encoding Rule)**

**Common Certificate Formats and Extensions:**
1. **PEM:**
   - **Encoding:** ASCII encoded, contains "Begin/End Certificate" statements.
   - **Extensions:** .pem, .crt, .cer, .key
   - **Details:** Uses DER encoding, with .der in pure binary.

2. **P12/PFX:**
   - **Encoding:** Pure binary.
   - **Extensions:** .pfx, .p12
   - **Usage:** Used to import/export certificates and private keys.

---

### Certificate Authorities (CA)

A Certificate Authority (CA) is an entity, typically a server, that issues certificates to users, acting as a trusted third party often used in HTTPS connections.

- **Certificate Details:** Clicking on the HTTPS padlock in a browser allows viewing of certificate details.
- **Certification Revocation List (CRL):** Invalid certificates are placed on this list.
- **SSL Pinning:** Attempts to prevent Man-in-the-Middle (MitM) attacks by ensuring the certificate used is the one expected.
- **Online Certificate Status Protocol (OCSP):** Used to verify certificate status in real-time.
- **Key Escrow:** A service that stores private keys securely.
- **Key Recovery Agent:** A trusted entity that can recover lost keys.
- **CA Hierarchy:** Often involves an offline root CA for added security.

**Web of Trust:**
- **Definition:** A decentralized system where certificates are self-signed and published.
- **Usage:** Commonly used by PGP (Pretty Good Privacy).

---

### Security Protocols

**Overview of Common Security Protocols:**
- **Email:** S/MIME, PGP
- **Web Login:** SSL, TLS
- **Direct Connections:** SSH
- **Virtual Connections:** PPTP, L2TP

---

### S/MIME (Secure/Multipurpose Internet Mail Extensions)

S/MIME is used for email security, providing authentication, message integrity, and non-repudiation. It requires a digital ID certificate in applications like MS Outlook to function.

---

### SSL/TLS (Secure Sockets Layer / Transport Layer Security)

SSL/TLS are protocols used for secure internet communication, such as web browsing, VoIP, and email. They rely on PKI for obtaining and validating certificates.

- **Encryption:** Uses asymmetric encryption (public key) for establishing a session and symmetric encryption (session key) for data transmission.
- **Accelerators:** SSL/TLS accelerators can be used to offload the encryption/decryption process.
- **Usage:** Widely used in e-commerce through HTTPS.
- **Vulnerabilities:** Susceptible to downgrade attacks, such as FREAK and DROWN.

---

### SSH (Secure Shell)

SSH uses public key cryptography to establish remote authenticated connections. It also serves as the basis for secure file transfer protocols like SFTP and SCP.

---

### PPTP, L2TP, and IPSec

**PPTP (Point-to-Point Tunneling Protocol):**
- **Usage:** Primarily used for VPNs.
- **Security:** Supports PPP packets but is considered insecure in most cases due to lack of encryption.

**L2TP (Layer 2 Tunneling Protocol):**
- **Security:** By default, L2TP does not include encryption but becomes powerful when combined with IPSec.
- **PKI:** Uses PKI when installed on Windows servers.

**IPSec (Internet Protocol Security):**
- **Function:** Authenticates and encrypts IP packets, operating at the Network layer of the OSI model.
- **Components:**
  1. **Security Association (SA)**
  2. **Authentication Header (AH)**
  3. **Encapsulating Security Payload (ESP)**
- **Modes of Implementation:**
  1. **Transport Mode:** Encrypts the packet payload, typically used within a LAN or private network.
  2. **Tunnel Mode:** Encrypts the entire packet, facilitating secure VPN connections through the internet.
