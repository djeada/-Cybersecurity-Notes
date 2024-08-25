## Cracking Windows Hashes

Gaining access to authentication hashes on a Windows system can be a crucial step in penetration testing or red team activities. These hashes, particularly the **NTHash** or **NTLM** format, are used by modern Windows operating systems to store user and service passwords.

### NTLM Overview

- **NTLM (NT LAN Manager):** A suite of Microsoft security protocols that provide authentication, integrity, and confidentiality to users. NTLM is an evolution of the older LAN Manager (LM) hash and is the format in which modern Windows systems store passwords. The "NT" in NTLM refers to "New Technology," originating from Windows NT, the first version of Windows independent of MS-DOS.

### Acquiring NTLM Hashes

To crack NTLM hashes, you first need to obtain them, typically requiring elevated privileges on a Windows system. These hashes are stored in either the **Security Account Manager (SAM)** database on individual Windows machines or the **NTDS.dit** database within a domain environment.

#### Common Methods to Obtain NTLM Hashes:

1. **Dumping the SAM Database:**
   - **SAM (Security Account Manager):** Stores user passwords in a hashed format on Windows machines.
   - **Tools:** 
     - **Mimikatz:** A popular tool for extracting passwords and hashes.
     - **Metasploit's `hashdump` module:** Used within the Metasploit framework to dump SAM hashes.
     - **samdump2:** A tool that extracts SAM hashes from a Windows system.

2. **Extracting from NTDS.dit:**
   - **NTDS.dit:** The Active Directory database file that stores all information, including user credentials, within a domain environment.
   - **Tools:**
     - **ntdsutil:** A native Windows tool for interacting with the NTDS.dit file.
     - **secretsdump.py (Impacket):** A Python tool used for extracting hashes from NTDS.dit.
     - **Mimikatz (`lsadump::dcsync` command):** Allows for dumping credentials from NTDS.dit by simulating the behavior of a domain controller.

### Cracking NTLM Hashes

Once you have obtained the NTLM hashes, you can attempt to crack them using tools like **John the Ripper** or **Hashcat**. Although NTLM is a robust hashing algorithm, weak passwords can often be cracked, especially with the use of wordlists.

#### Example of Using John the Ripper:
```bash
john --format=NT --wordlist=/path/to/wordlist.txt ntlm_hashes.txt
```
- **Explanation:** This command instructs John the Ripper to use the NTLM hash format and a specified wordlist to attempt to crack the hashes.

### Pass-the-Hash Attacks

In some scenarios, cracking the hash may not be necessary. **Pass-the-Hash (PtH)** is a technique where an attacker uses the NTLM hash of a user's password instead of the plaintext password to authenticate to a network service. This method is particularly effective in Windows environments, allowing attackers to move laterally across a network without needing the actual passwords.

### Defensive Measures

1. **Enforce Strong Password Policies:**
   - **Purpose:** Ensure that complex passwords are required and changed regularly to reduce the likelihood of successful hash-based attacks.

2. **Enable SMB Signing:**
   - **Purpose:** Enabling SMB signing helps prevent Man-in-the-Middle attacks that capture NTLM hashes.

3. **Use Multi-Factor Authentication (MFA):**
   - **Purpose:** MFA adds an additional layer of security, making it harder for attackers to succeed even if they obtain password hashes.
