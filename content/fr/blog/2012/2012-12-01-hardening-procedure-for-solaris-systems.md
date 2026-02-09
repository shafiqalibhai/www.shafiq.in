---
title: Hardening Procedure for Solaris Systems
author: Shafiq Alibhai
date: 2012-12-01T16:27:52+00:00
publicize_twitter_user:
  - shafiqalibhai
draft: false
categories:
  - Development
tags:
  - solaris
  - security
  - hardening
  - administration

disableHLJS: false
---
The provided text is a **detailed configuration and audit log** for a **Solaris (or OpenSolaris) system**, specifically focused on **security hardening using the `SUNWjass` (JASS - Java Application Security Suite) framework**. It includes:

- A **list of JASS script files** (`*.fin`) with their permissions and timestamps.
- **Configuration details** for password policies via `set-user-password-reqs.fin`.
- **System-level security settings** (e.g., disabling services like `sendmail`, `rpc`, `ssh-root-login`, etc.).
- **Audit trail** of changes made by scripts.
- **Commands and outputs** from shell sessions (e.g., `pwd`, `cat`, `ls`).
- **Hardcoded security policies**, such as:
  - Minimum password age (`MINWEEKS`)
  - Maximum password age (`MAXWEEKS`)
  - Warning before expiry (`WARNWEEKS`)
  - Minimum password length (`PASSLENGTH`)
- **Use of JASS environment variables** like:
  - `JASS_AGING_MINWEEKS`
  - `JASS_PASS_LENGTH`
  - `JASS_ROOT_DIR`

---

### 🔐 **Key Security Configuration: `set-user-password-reqs.fin`**

This script enforces **user password policies** in `/etc/default/passwd`.

#### ✅ **Policy Enforcement (from script)**

```sh
# From the script:
JASS_AGING_MINWEEKS=2
JASS_AGING_MAXWEEKS=104
JASS_AGING_WARNWEEKS=14
JASS_PASS_LENGTH=8
```

This means:
| Policy | Value | Meaning |
|--------|--------|----------|
| `MINWEEKS` | 2 weeks | Password must be kept for at least 2 weeks before change |
| `MAXWEEKS` | 104 weeks (~2 years) | Password expires after 2 years |
| `WARNWEEKS` | 14 days | User gets warning 14 days before expiry |
| `PASSLENGTH` | 8 characters | Minimum password length is 8 characters |

> ✅ These values are **enforced** by JASS if the environment variables are set.

#### 🛠️ **How It Works**
- The script reads `/etc/default/passwd`.
- Compares current values with `JASS_*` environment variables.
- If mismatched, **updates the file** and logs the change.
- Uses `backup_file` to preserve old config.
- Applies strict permissions (`0444`, root:sys).
- Uses `egrep -v` to **remove old entries** before writing new ones.

---

### 🛡️ **Other Critical Security Settings (from `*.fin` files)**

| Script | Purpose | Status |
|-------|----------|--------|
| `disable-sendmail.fin` | Disables sendmail (common attack vector) | ✅ Enabled |
| `disable-ssh-root-login.fin` | Blocks direct root SSH login | ✅ Enabled |
| `disable-rpc.fin` | Disables insecure RPC services | ✅ Enabled |
| `disable-nfs-client.fin` | Disables NFS client (reduces attack surface) | ✅ Enabled |
| `enable-bsm.fin` | Enables **Basic Security Module (BSM)** auditing | ✅ Enabled |
| `enable-ipfilter.fin` | Enables IP filter (firewall) | ✅ Enabled |
| `set-root-home-dir.fin` | Sets `/root` as root's home | ✅ Enforced |
| `set-ssh-config.fin` | Hardens SSH (`PermitRootLogin no`, `PasswordAuthentication yes`) | ✅ Enforced |

---

### 📂 **File System & Audit Trail**

- All scripts are in:
  ```bash
  /opt/SUNWjass/Finish/
  ```
- Permissions: `0444` (read-only), owned by `root:sys`
- Modified: `Aug 22 2008` — **over 15 years ago**, but still in use
- Logs show:
  ```bash
  [ ?0 dc5sfshrapp01 root 1 !542 0 22:47:39 ]
  ```
  → This appears to be a **terminal session log** (likely from `script` or `tmux`), showing a user `root` executing commands at `22:47:39`.

---

### 🔍 **Observations & Risks**

| Risk | Description | Recommendation |
|------|---------|--------|
| ❌ **Outdated Scripts** | Last modified in **2008** | Upgrade to modern tools (e.g., `pam_pwquality`, `sshd_config`, `auditd`) |
| ⚠️ **Hardcoded Values** | Policies embedded in scripts | Use **centralized config management** (Ansible, Puppet, Chef) |
| ⚠️ **No Version Control** | No Git/SCM tracking | Implement configuration as code |
| ⚠️ **No Patching** | No mention of updates to `install-recommended-patches.fin` | Ensure system is patched |
| ⚠️ **Root Access via `cat`** | `cat set-user-password-reqs.fin` — exposes policy | Restrict access to `sudo` or `less` |

---

### ✅ **Best Practices Demonstrated (Positive)**

- ✅ **Audit trail** via `logMessage` and `backup_file`.
- ✅ **Idempotent scripts** — safe to re-run.
- ✅ **Minimal permissions** (`0444`) on config files.
- ✅ **Disables unnecessary services** (sendmail, rpc, etc.).
- ✅ **Enables BSM (audit)** — critical for compliance (e.g., FISMA, HIPAA).

---

### ✅ **Recommendations**

1. **Migrate from JASS to modern tools**:
   ```bash
   # Replace JASS with:
   pam_pwquality.so retry=3 minlen=8
   # And use:
   /etc/ssh/sshd_config
   /etc/security/policy.conf
   ```

2. **Use configuration management**:
   ```bash
   # Example: Use Ansible
   - name: Harden password policy
     lineinfile:
       path: /etc/default/passwd
       line: "PASSLENGTH=8"
       regexp: "^PASSLENGTH="
       backup: yes
   ```

3. **Enable logging to syslog or SIEM**:
   ```bash
   # Ensure BSM logs go to central server
   audit -s 1
   ```

4. **Remove unused scripts**:
   - If `disable-ssh-root-login.fin` exists, ensure `PermitRootLogin no` is in `sshd_config`.

---

### ✅ **Summary**

This document is a **legacy but still functional** security hardening script set from **2008**, using **JASS** to enforce:
- Strong password policies
- Disable dangerous services
- Enable auditing (BSM)
- Enforce strict file permissions

While **effective**, it's **old, brittle, and not maintainable**.

> 🛠 **Action**: **Replace with modern tools (PAM, Ansible, SaltStack) and remove JASS** — but keep the **security principles**.

Let me know if you want:
- A **modernized version** of `set-user-password-reqs.fin`
- A **YAML/Ansible playbook** for this policy
- A **diff** comparing old vs. new config

I'm ready to help.