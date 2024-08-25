## OS Hardening

### Motivation

Operating Systems (OS) are often vulnerable by default when initially installed. Customizing and securing the settings is essential to enhance security.

**Concept of Least Functionality:**
- **Purpose:** Restrict and remove any functionality not required for operation to minimize attack surfaces.
- **Guidance:** Follow NIST CM-7 control procedures for implementing these restrictions.
- **Target Areas for Restriction:**
  - **Applications:** Uninstall or disable unnecessary software.
  - **Ports:** Close any unused network ports to reduce exposure.
  - **Services (Daemons):** Disable or remove services that are not essential.

**Additional Considerations:**
- **Backward Compatibility:** When removing obsolete applications, consider the impact on compatibility.
- **SCCM (System Center Configuration Manager):** Use for managing multiple machines and enforcing configuration standards.
- **Application Blacklisting/Whitelisting:** Control which applications can run on the system.
- **Service Configuration Commands:**
  - **Windows:** Use `services.msc`, `net stop`, and `sc stop` to manage services.
  - **Linux:** Use `/etc/init.d/<service> stop`, `service <service> stop`, etc., for service management.
  - **OSX:** Use the `kill` command to stop services.

---

### Updates, Patches, and Hotfixes

**Trusted Operating System (TOS):**
- **Definition:** An OS certified as secure according to government standards.

**Categories of Updates:**
1. **Security Update:** Addresses product-specific, security-related vulnerabilities.
2. **Critical Update:** Fixes critical, non-security-related bugs.
3. **Service Pack:** A cumulative set of updates (now discontinued).
4. **Windows Update:** Provides noncritical fixes, new features, and updates.
5. **Driver Update:** Be cautious of driver shimming and refactoring.

**Patches and Hotfixes:**
- **Terminology:** The terms "hotfix" and "patch" are often used interchangeably.
- **Update Strategy:** Disable automatic updates to synchronize versions and maintain control over the update process.

---

### Patch Management

Patch management involves a structured approach to planning, testing, implementing, and auditing patches.

1. **Planning:**
   - **Objective:** Decide which patches are required based on security needs and compatibility.
   - **Steps:**
     - Determine compatibility with existing systems.
     - Plan how the patch will be tested and deployed.

2. **Testing:**
   - **Objective:** Ensure the patch does not negatively affect the system.
   - **Steps:** Test the patch on a single machine or small system before wide deployment.

3. **Implementation:**
   - **Objective:** Deploy the patch across all machines.
   - **Steps:** Use SCCM or another centralized management system to distribute the patch.

4. **Auditing:**
   - **Objective:** Verify the patch is live and functioning correctly.
   - **Steps:** Check for failures or system changes post-deployment.

---

### Group Policies, Security Templates, and Configuration Baselines

**Group Policy:**
- **Function:** Used in Windows to set configurations across groups of users or computers.
- **Tool:** `gpedit.msc` is the primary tool for managing group policies.

---

### Hardening File Systems and Hard Drives

**a) Use a Secure File System:**
   - **Windows:** 
     - **NTFS:** Supports encryption, Access Control Lists (ACLs), and logging.
     - **Tools:** Use `chkdsk` and `convert` commands for maintenance.
   - **Linux:** 
     - **ext4:** A robust and secure file system.
     - **Tools:** Use `fdisk -l` or `df -T` to manage and check file systems.

**b) Hide Important Files:**
   - **Purpose:** Protect system and personal files from unauthorized access.

**c) Manage Hard Drives:**
   - **Tasks:**
     - **Delete Temp Files:** Regularly remove temporary files to free up space and reduce clutter.
     - **Verify System File Integrity:** Periodically check system files to ensure they have not been altered.
     - **Defrag Hard Drives:** Optimize disk performance by defragmenting.
     - **Backup Data:** Regularly back up important data to prevent data loss.
     - **Restore Points:** Create restore points to revert to a previous state in case of issues.
     - **Whole Disk Encryption:** Encrypt the entire disk to protect data at rest.
     - **Separate OS System and Personal Data:** Keep the OS and personal data on separate partitions or drives for better security and management.
