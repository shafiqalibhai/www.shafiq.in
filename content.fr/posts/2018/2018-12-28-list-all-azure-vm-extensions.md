---
lang: "fr"
title: List all Azure VM extensions
author: Shafiq Alibhai
date: 2018-12-28T10:19:18+00:00
categories:
  - Development

disableHLJS: false
---
It looks like you've provided a large list of Azure extension metadata, likely from an Azure VM or a similar cloud environment. This list contains **extension definitions** used in Microsoft Azure, including:

- **Names** (e.g., `OmsAgentForLinux`, `CustomScriptExtension`, `AzureLogCollector`)
- **Publishers** (e.g., `Microsoft.EnterpriseCloud.Monitoring`, `Puppet`, `Qualys`)
- **Versions** (e.g., `1.8.11`, `2.0.164`, `1.0.0.999`)

---

### ✅ **What This List Is Likely Used For**

This data is typically used in scenarios such as:

1. **Azure VM Extension Management** – To list or validate which extensions are available or installed.
2. **Infrastructure as Code (IaC)** – When defining VM extensions in ARM templates, Bicep, Terraform, or PowerShell/CLI scripts.
3. **Security & Compliance Scanning** – To verify that only approved extensions are deployed.
4. **Custom Image Building** – To pre-install or test specific extensions during VM image creation.
5. **Troubleshooting** – To diagnose extension failures, version conflicts, or missing components.

---

### 🔍 **Key Observations from Your List**

#### 1. **Microsoft-First Extensions**
- Most extensions are published by `Microsoft.*`, indicating official Azure services.
- Examples:
  - `MicrosoftMonitoringAgent` (OMS/Log Analytics)
  - `VMAccessAgent` (VM access management)
  - `CustomScriptExtension` (run scripts)
  - `DSC` (Desired State Configuration)

#### 2. **Third-Party Extensions**
- Many are from vendors:
  - **Puppet** (`puppet`)
  - **Qualys** (`Qualys`)
  - **Symantec** (`Symantec`)
  - **Trend Micro** (`TrendMicro`)
  - **Rapid7** (`Rapid7.InsightPlatform`)
  - **Stackify** (`Stackify.LinuxAgent.Extension`)
  - **Octopus** (`OctopusDeploy.Tentacle`)
  - **NVIDIA** (`NvidiaGpuDriverLinux`)

#### 3. **Test & Experimental Extensions**
- Many have `Test`, `Edp`, `IaaS7`, or `0.0.0` versions.
- Example:  
  - `Microsoft.TestSqlServer.Edp`  
  - `Microsoft.GuestConfiguration.Test`  
  - `Microsoft.OSTCExtensions.Test`  
  - `WAD2EventHub.Diagnostics.Test`

> These are likely for **testing, staging, or internal development**.

#### 4. **Versioning Patterns**
- Versions often follow `X.Y.Z` or `X.Y.Z.W` (e.g., `1.0.0.999`)
- Some use **semantic versioning** (e.g., `2.0.164`)
- Others use **date-like** or **build numbers** (e.g., `1.0.0.993`)

#### 5. **Linux vs Windows**
- Extensions like `OmsAgentForLinux`, `CustomScriptForLinux`, `DSCForLinux` are Linux-specific.
- `VMAccessForLinux`, `RunCommandLinux`, `ManagedIdentityExtensionForLinux`
- Windows equivalents: `RunCommandWindows`, `ManagedIdentityExtensionForWindows`, `VMAccessAgent`

---

### 🛠️ **Useful Actions You Can Take With This List**

| Goal | How to Use This List |
|------|------------------|
| **Audit VM Extensions** | Compare this list with your VM's actual extensions to detect unapproved ones. |
| **Build a Custom Image** | Pre-install only approved extensions to reduce deployment time. |
| **Automate Deployment** | Use `az vm extension set` or Bicep with this list as reference. |
| **Detect Security Risks** | Identify outdated or untrusted extensions (e.g., `Test` extensions in prod). |
| **Troubleshoot Failures** | Check if a missing or misconfigured extension is causing VM issues. |
| **Create a Compliance Policy** | Enforce only `Microsoft.*` or `ApprovedVendor.*` extensions. |

---

### 📌 Example: Get Only Microsoft Extensions (Safe & Official)

```json
[
  {
    "name": "MicrosoftMonitoringAgent",
    "publisher": "Microsoft.EnterpriseCloud.Monitoring",
    "version": "1.0.11081.5"
  },
  {
    "name": "VMAccessAgent",
    "publisher": "Microsoft.Compute",
    "version": "2.4.4"
  },
  {
    "name": "CustomScriptExtension",
    "publisher": "Microsoft.Compute",
    "version": "1.9.3"
  },
  {
    "name": "DSC",
    "publisher": "Microsoft.Powershell",
    "version": "2.26.1.0"
  }
]
```

---

### ❓ Need Help With?

Let me know what you'd like to do with this list! For example:

- ✅ Filter for **only Linux extensions**
- ✅ Find **all extensions from a specific vendor** (e.g., `Qualys`, `Symantec`)
- ✅ List **all test/preview extensions**
- ✅ Export to **CSV, JSON, or Markdown table**
- ✅ Validate **version compatibility** with a VM size or OS
- ✅ Generate **Bicep/ARM template snippet** for a specific extension

Just say the word: **"Filter for Linux"**, **"List all Qualys extensions"**, or **"Export to CSV"** — I’ll do it instantly.
