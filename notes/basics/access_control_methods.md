## Access Control Methods and Models

### Access Control Models

Access control models define how access to physical areas and computer systems is managed. Here are the key models:

1. **Discretionary Access Control (DAC)**
   - Determined by the owner of the file or folder.
   - The owner decides how each user or group accesses their file.

2. **Mandatory Access Control (MAC)**
   - The strictest form of access control, typically used on a need-to-know basis.
   - Each user is given a clearance level and can only access files within that level (e.g., FOUO, Confidential, Secret, Top Secret).
   - **Rule-Based Access Control:** Access is determined by comparing labels to clearance levels.
   - **Lattice-Based Access Control:** More complex, involving set mathematics to determine access.

3. **Role-Based Access Control (RBAC)**
   - Access is controlled by a central authority.
   - Various roles with overlapping privileges are assigned to users.

4. **Attribute-Based Access Control (ABAC)**
   - A dynamic and context-aware access control method.

### Basic Access Control Practices

1. **Implicit Deny**
2. **Least Privilege**
3. **Separation of Duties**
4. **Job Rotation**

### Rights, Permissions, and Policies

### Users, Groups, and Permissions

**Windows Active Directory:**
- Users can be added to specific Organizational Units (OUs) or the Users folder.
- Logon times and valid login dates can also be configured.
- Consolidate multiple accounts with Federated Identity Management/Single Sign-On (SSO).
- Group users with similar permissions together.

**NTFS Permissions:**
1. Full Control
2. Modify
3. Read & Execute
4. List Folder Contents
5. Read
6. Write

### Permission Inheritance and Propagation

- The default behavior is that a child folder inherits the permissions of its parent folder.
- This behavior cannot be changed without disabling permission inheritance.
- **Moving vs Copying Data:**
  - **Copy:** Inherits the permissions of the destination folder.
  - **Move:** Retains the original permissions.

### Username and Passwords

- Weak and old passwords are common avenues for data exfiltration.
- Never use default usernames and passwords, especially for administrative accounts.
- Disable guest and unnecessary accounts.
- Use `Ctrl + Alt + Delete` to log in, ensuring users are using a keyboard rather than a network connection.
- Implement policy management to enforce security.

### Policies

Policies are enforced rules configured either on individual machines or across a network.

**Password Policies:**
1. Enforce password history.
2. Minimum and maximum password age.
3. Minimum password length.
4. Complexity requirements.

- Most policies are configured at the OS level with an Active Directory (AD) domain controller.

### UAC (User Account Control)

- By default, UAC keeps all non-admin users without full administrative rights.

