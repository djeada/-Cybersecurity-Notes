## Hashing Basics

### What are Hashes?
- **Definition:** A hash is a way of taking a piece of data of any length and representing it in a fixed-length form. This masks the original value of the data by running it through a hashing algorithm.
- **Example:** 
  - For "polo" (4 characters) using MD5: `b53759f3ce692de7aff1b5779d3964da`
  - For "polomints" (9 characters) using MD5: `584b6e4f4586e136bc280f27f9c64f3b`

### Purpose of Hashing
- **Integrity:** Ensures message integrity by producing a fixed-size hash value from variable-sized data.
- **Security:** Hashing functions are designed as one-way functions, making it computationally infeasible to reverse the process (i.e., finding the original input from the hash).

### Cryptographic Hash Functions
- **MD5 (Message Digest 5):**
  - Commonly used for file integrity verification.
  - Vulnerable to hash collision attacks.
  
- **SHA (Secure Hash Algorithm):**
  - **Current Standard:** SHA-2 (256/512 bits).
  - **Purpose:** Provides enhanced security over MD5.

- **RIPEMD & HMAC:**
  - **RIPEMD:** A family of cryptographic hash functions.
  - **HMAC (Hash-based Message Authentication Code):** Combines a hash function with a secret key for added security.

### Windows Hashing Mechanisms
- **LANMAN:**
  - An older Windows password hash based on DES, now deprecated and a security liability.
  - **Recommendation:** Disable via registry or local security policy.
  
- **NTLM (New Technology LAN Manager):**
  - Based on RC4, now considered insecure.
  
- **NTLMv2:**
  - Utilizes HMAC-MD5; however, Kerberos is preferred for most Windows environments.

## Hashing Attacks

### Pass the Hash
- **Method:** Uses a stored hash value to initiate an authenticated session without needing the plaintext password.
- **Target:** Often used against Windows/Kerberos in Single Sign-On (SSO) environments.
- **Mitigation:** Use unique session tokens, multifactor authentication, and least privilege principles.

### Birthday Attack
- **Description:** Attempts to produce a hash collision with the original message.
- **Target:** Hash functions with weak collision resistance.

### Additional Hashing Concepts
- **Key Stretching / Salting:** 
  - **Purpose:** Enhances the security of stored passwords by adding random data (salt) or stretching the hash computation.
  - **Effect:** Makes brute-force attacks more difficult by increasing the computational work required to generate a hash.

