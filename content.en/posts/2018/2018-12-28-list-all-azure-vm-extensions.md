---
title: List all Azure VM extensions
author: Shafiq Alibhai
date: 2018-12-28T10:19:18+00:00
categories:
  - Development

---

```bash
az vm extension image list
```

```json
[

  {

    "name": "AcronisBackup",

    "publisher": "Acronis.Backup",

    "version": "1.0.33"

  },

  {

    "name": "AcronisBackupLinux",

    "publisher": "Acronis.Backup",

    "version": "1.0.33"

  },

  {

    "name": "AlertLogicLM",

    "publisher": "alertlogic",

    "version": "1.3.0.1"

  },

  {

    "name": "AlertLogicLM",

    "publisher": "AlertLogic.Extension",

    "version": "1.3.0.0"

  },

  {

    "name": "AlertLogicLM",

    "publisher": "AlertLogic.Extension",

    "version": "1.4.0.0"

  },

  {

    "name": "AlertLogicLM",

    "publisher": "AlertLogic.Extension",

    "version": "1.9.0.0"

  },

  {

    "name": "AlertLogicLM",

    "publisher": "AlertLogic.Extension",

    "version": "1.9.1.0"

  },

  {

    "name": "AgentWinExt",

    "publisher": "bmc.ctm",

    "version": "9.0.0.1"

  },

  {

    "name": "ChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "11.18.6.2"

  },

  {

    "name": "ChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "1207.12.3.0"

  },

  {

    "name": "ChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "1210.12.109.1004"

  },

  {

    "name": "ChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "1210.12.109.1005"

  },

  {

    "name": "ChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "1210.12.110.1000"

  },

  {

    "name": "ChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "1210.12.110.1001"

  },

  {

    "name": "LinuxChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "11.18.6.2"

  },

  {

    "name": "LinuxChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "1207.12.3.0"

  },

  {

    "name": "LinuxChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "1210.12.109.1004"

  },

  {

    "name": "LinuxChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "1210.12.110.1000"

  },

  {

    "name": "LinuxChefClient",

    "publisher": "Chef.Bootstrap.WindowsAzure",

    "version": "1210.12.110.1001"

  },

  {

    "name": "CloudLinkSecureVMLinuxAgent",

    "publisher": "CloudLinkEMC.SecureVM",

    "version": "5.0.22503.21808"

  },

  {

    "name": "CloudLinkSecureVMLinuxAgent",

    "publisher": "CloudLinkEMC.SecureVM",

    "version": "5.5.23389.23430"

  },

  {

    "name": "CloudLinkSecureVMLinuxAgent",

    "publisher": "CloudLinkEMC.SecureVM",

    "version": "6.0.62.0"

  },

  {

    "name": "CloudLinkSecureVMWindowsAgent",

    "publisher": "CloudLinkEMC.SecureVM",

    "version": "5.5.6.23416"

  },

  {

    "name": "CloudLinkSecureVMWindowsAgent",

    "publisher": "CloudLinkEMC.SecureVM",

    "version": "6.0.66.0"

  },

  {

    "name": "CloudLinkSecureVMWindowsAgent",

    "publisher": "CloudLinkEMC.SecureVM",

    "version": "6.5.69.0"

  },

  {

    "name": "ConferForAzure",

    "publisher": "Confer",

    "version": "1.0.5.38"

  },

  {

    "name": "ConferForAzure",

    "publisher": "Confer",

    "version": "1.0.5.39"

  },

  {

    "name": "ConferForAzure",

    "publisher": "Confer",

    "version": "1.0.5.40"

  },

  {

    "name": "BmcCtmAgentLinux",

    "publisher": "ctm.bmc.com",

    "version": "9.0.0.1"

  },

  {

    "name": "DatadogLinuxAgent",

    "publisher": "Datadog.Agent",

    "version": "0.4"

  },

  {

    "name": "DatadogLinuxAgent",

    "publisher": "Datadog.Agent",

    "version": "0.6.1"

  },

  {

    "name": "DatadogLinuxAgent",

    "publisher": "Datadog.Agent",

    "version": "0.6.2"

  },

  {

    "name": "DatadogWindowsAgent",

    "publisher": "Datadog.Agent",

    "version": "0.4.1"

  },

  {

    "name": "DatadogWindowsAgent",

    "publisher": "Datadog.Agent",

    "version": "0.5"

  },

  {

    "name": "DatadogWindowsAgent",

    "publisher": "Datadog.Agent",

    "version": "0.5.2"

  },

  {

    "name": "DatadogWindowsAgent",

    "publisher": "Datadog.Agent",

    "version": "0.6.0"

  },

  {

    "name": "dtmanaged",

    "publisher": "dynatrace.ruxit",

    "version": "1.4.0.11"

  },

  {

    "name": "dtmanaged",

    "publisher": "dynatrace.ruxit",

    "version": "1.4.0.13"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "1.150.0.0"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "1.151.0.1"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "1.151.0.2"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "1.99.1.2"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "1.99.2.0"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "1.99.2.1"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "2.2.0.0"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "2.2.0.1"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "2.2.0.2"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "2.3.0.0"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "2.3.0.1"

  },

  {

    "name": "oneAgentLinux",

    "publisher": "dynatrace.ruxit",

    "version": "2.3.0.2"

  },

  {

    "name": "oneAgentManagedWindows",

    "publisher": "dynatrace.ruxit",

    "version": "1.0.0.4"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "1.150.0.0"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "1.150.0.1"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "1.151.0.2"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "1.99.1.1"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "1.99.1.2"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "1.99.1.3"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "2.2.0.0"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "2.2.0.1"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "2.2.0.2"

  },

  {

    "name": "oneAgentWindows",

    "publisher": "dynatrace.ruxit",

    "version": "2.3.0.2"

  },

  {

    "name": "FileSecurity",

    "publisher": "ESET",

    "version": "6.5.12010.1000"

  },

  {

    "name": "FileSecurity",

    "publisher": "ESET",

    "version": "6.5.12014.1002"

  },

  {

    "name": "FileSecurity",

    "publisher": "ESET",

    "version": "7.0.12014.1002"

  },

  {

    "name": "ProtectVClientLinuxExtension",

    "publisher": "Gemalto.SafeNet.ProtectV",

    "version": "3.0.0.205"

  },

  {

    "name": "ProtectVClientWindowsExtension",

    "publisher": "Gemalto.SafeNet.ProtectV",

    "version": "3.0.0.318"

  },

  {

    "name": "DotnetAgent",

    "publisher": "HPE.Security.ApplicationDefender",

    "version": "1.0.0.2"

  },

  {

    "name": "DotnetAgent",

    "publisher": "HPE.Security.ApplicationDefender",

    "version": "1.0.0.4"

  },

  {

    "name": "DotnetAgent",

    "publisher": "HPE.Security.ApplicationDefender",

    "version": "1.6.13.0"

  },

  {

    "name": "DotnetAgent",

    "publisher": "HPE.Security.ApplicationDefender",

    "version": "1.6.14.0"

  },

  {

    "name": "DotnetAgent",

    "publisher": "HPE.Security.ApplicationDefender",

    "version": "1.6.9.0"

  },

  {

    "name": "KESL",

    "publisher": "KasperskyLab.SecurityAgent",

    "version": "1.0.0.0"

  },

  {

    "name": "KSWS",

    "publisher": "KasperskyLab.SecurityAgent",

    "version": "1.0.0.0"

  },

  {

    "name": "McAfeeEndpointSecurity",

    "publisher": "McAfee.EndpointSecurity",

    "version": "6.0"

  },

  {

    "name": "Compute.AKS-Engine.Linux.Billing",

    "publisher": "Microsoft.AKS",

    "version": "1.0.0"

  },

  {

    "name": "AADLoginForWindows",

    "publisher": "Microsoft.Azure.ActiveDirectory",

    "version": "0.3.0.0"

  },

  {

    "name": "AADLoginForWindows",

    "publisher": "Microsoft.Azure.ActiveDirectory",

    "version": "0.3.1.0"

  },

  {

    "name": "AADLoginForLinux",

    "publisher": "Microsoft.Azure.ActiveDirectory.LinuxSSH",

    "version": "1.0.4870001"

  },

  {

    "name": "AADLoginForLinux",

    "publisher": "Microsoft.Azure.ActiveDirectory.LinuxSSH",

    "version": "1.0.4890001"

  },

  {

    "name": "AADLoginForLinux",

    "publisher": "Microsoft.Azure.ActiveDirectory.LinuxSSH",

    "version": "1.0.5160001"

  },

  {

    "name": "AADLoginForLinux",

    "publisher": "Microsoft.Azure.ActiveDirectory.LinuxSSH",

    "version": "1.0.5920001"

  },

  {

    "name": "AADLoginForLinux",

    "publisher": "Microsoft.Azure.ActiveDirectory.LinuxSSH",

    "version": "1.0.6350001"

  },

  {

    "name": "AADLoginForLinux",

    "publisher": "Microsoft.Azure.ActiveDirectory.LinuxSSH",

    "version": "1.0.6430001"

  },

  {

    "name": "IaaS47C6E03DTest",

    "publisher": "Microsoft.Azure.Applications",

    "version": "1.0.0.3"

  },

  {

    "name": "MyBackupTest",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.116.0"

  },

  {

    "name": "MyBackupTest",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.117.0"

  },

  {

    "name": "MyBackupTest",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.118.0"

  },

  {

    "name": "MyBackupTest",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.121.0"

  },

  {

    "name": "MyBackupTest",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.124.0"

  },

  {

    "name": "MyBackupTest",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.125.0"

  },

  {

    "name": "Compute.AKS-Engine.Windows.Billing",

    "publisher": "Microsoft.AKS",

    "version": "1.0.0"

  },

  {

    "name": "MyBackupTestLinuxInt",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.9142.0"

  },

  {

    "name": "MyBackupTestLinuxInt",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.9143.0"

  },

  {

    "name": "MyBackupTestLinuxInt",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.9144.0"

  },

  {

    "name": "MyBackupTestLinuxInt",

    "publisher": "Microsoft.Azure.Backup.Test",

    "version": "1.0.9147.0"

  },

  {

    "name": "Compute.AKS.Linux.Billing",

    "publisher": "Microsoft.AKS",

    "version": "1.0.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.1.0.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.10.0.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.10.0.1"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.10.1.1"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.0.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.1.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.2.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.3.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.3.1"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.3.10"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.3.12"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.3.5"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.3.7"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.11.3.9"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.12.0.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.12.1.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.2.0.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.3.1.6"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.4.2.1"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.5.9.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.6.2.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.6.3.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.6.4.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.7.1.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.7.3.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.7.4.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.8.0.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.8.1.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "1.9.0.0"

  },

  {

    "name": "Compute.AKS.Windows.Billing",

    "publisher": "Microsoft.AKS",

    "version": "1.0.0"

  },

  {

    "name": "CustomScript",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.0.0"

  },

  {

    "name": "CustomScript",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.0.1"

  },

  {

    "name": "CustomScript",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.0.2"

  },

  {

    "name": "CustomScript",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.0.3"

  },

  {

    "name": "CustomScript",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.0.4"

  },

  {

    "name": "CustomScript",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.0.5"

  },

  {

    "name": "CustomScript",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.0.6"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "3.0.101"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "3.0.103"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "3.0.107"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "3.0.109"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "3.0.111"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "3.0.113"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "3.0.115"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.Azure.Diagnostics",

    "version": "3.0.117"

  },

  {

    "name": "GenevaMonitoring",

    "publisher": "Microsoft.Azure.Geneva",

    "version": "1.0.0.3"

  },

  {

    "name": "GenevaMonitoring",

    "publisher": "Microsoft.Azure.Geneva",

    "version": "1.0.0.6"

  },

  {

    "name": "GenevaMonitoring",

    "publisher": "Microsoft.Azure.Geneva",

    "version": "1.0.0.8"

  },

  {

    "name": "GenevaMonitoring",

    "publisher": "Microsoft.Azure.Geneva",

    "version": "1.8.0.2"

  },

  {

    "name": "GenevaMonitoring",

    "publisher": "Microsoft.Azure.Geneva",

    "version": "1.8.0.3"

  },

  {

    "name": "KeyVaultForWindows",

    "publisher": "Microsoft.Azure.KeyVault",

    "version": "0.1.0.717"

  },

  {

    "name": "KeyVaultForWindows",

    "publisher": "Microsoft.Azure.KeyVault",

    "version": "0.2.0.898"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.0.1512030601"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.1.1512090359"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.1.1512180541"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.1.1601070410"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.1.1601140348"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.1.1602270800"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.1.1604142300"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.1.1606092330"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.2.0"

  },

  {

    "name": "DockerExtension",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.2.2"

  },

  {

    "name": "KeyVaultForWindows",

    "publisher": "Microsoft.Azure.KeyVault.Edp",

    "version": "0.0.0.705"

  },

  {

    "name": "KeyVaultForWindows",

    "publisher": "Microsoft.Azure.KeyVault.Edp",

    "version": "0.0.0.867"

  },

  {

    "name": "KeyVaultForWindows",

    "publisher": "Microsoft.Azure.KeyVault.Edp",

    "version": "0.0.0.887"

  },

  {

    "name": "FixEmulatedIO",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.0.0"

  },

  {

    "name": "AquariusLinux",

    "publisher": "Microsoft.Azure.Networking.SDN",

    "version": "1.4.0.0"

  },

  {

    "name": "AquariusLinux",

    "publisher": "Microsoft.Azure.Networking.SDN",

    "version": "1.5.0.0"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.1.0.886"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.2.0.1001"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.2.1.1014"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.3.0.1058"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.4.0.1112"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.4.1.1134"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.4.2.1150"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.5.0.1174"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.5.1.1204"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.6.2.1366"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.7.1.1416"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.7.3.1475"

  },

  {

    "name": "DependencyAgentLinux",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.7.4.3150"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.105.0"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.306.5"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.411.1"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.466.1"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.493.1"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.518.1"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.526.2"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.585.2"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.861.1"

  },

  {

    "name": "NetworkWatcherAgentLinux",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.861.2"

  },

  {

    "name": "FixLinuxDiagnostic",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "1.0.0"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.1.0.886"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.2.0.1001"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.2.1.1014"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.3.0.1058"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.4.0.1112"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.4.1.1134"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.5.0.1174"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.6.2.1366"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.7.1.1416"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.7.3.1475"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.7.4.3150"

  },

  {

    "name": "DependencyAgentWindows",

    "publisher": "Microsoft.Azure.Monitoring.DependencyAgent",

    "version": "9.7.5.3590"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.104.0"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.306.5"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.411.1"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.466.1"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.493.1"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.518.1"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.526.2"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.585.2"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.861.1"

  },

  {

    "name": "NetworkWatcherAgentWindows",

    "publisher": "Microsoft.Azure.NetworkWatcher",

    "version": "1.4.861.2"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.1"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.10"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.11"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.12"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.2"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.5"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.6"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.7"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.8"

  },

  {

    "name": "AzurePerformanceDiagnostics",

    "publisher": "Microsoft.Azure.Performance.Diagnostics",

    "version": "1.0.9"

  },

  {

    "name": "LinuxAsm",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.0.1"

  },

  {

    "name": "LinuxAsm",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.1.0"

  },

  {

    "name": "LinuxAsm",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.1.1"

  },

  {

    "name": "LinuxAsm",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.2.0"

  },

  {

    "name": "LinuxAsm",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.2.1"

  },

  {

    "name": "LinuxAsm",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.2.2"

  },

  {

    "name": "LinuxAsm",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.2.3"

  },

  {

    "name": "LinuxAsm",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.2.4"

  },

  {

    "name": "LinuxAsm",

    "publisher": "Microsoft.Azure.Extensions",

    "version": "2.2.5"

  },

  {

    "name": "VMSnapshot",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.40.0"

  },

  {

    "name": "VMSnapshot",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.42.0"

  },

  {

    "name": "VMSnapshot",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.43.0"

  },

  {

    "name": "VMSnapshot",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.46.0"

  },

  {

    "name": "VMSnapshot",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.47.0"

  },

  {

    "name": "VMSnapshot",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.49.0"

  },

  {

    "name": "VMSnapshot",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.53.0"

  },

  {

    "name": "VMSnapshot",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.54.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9124.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9125.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9126.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9127.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9128.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9131.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9133.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9134.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9135.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9136.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9137.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9140.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9141.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9142.0"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices",

    "version": "1.0.9143.0"

  },

  {

    "name": "VMSnapshot",

    "publisher": "Microsoft.Azure.RecoveryServices.Edp",

    "version": "1.0.39.0"

  },

  {

    "name": "Linux",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9102"

  },

  {

    "name": "Linux",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9103"

  },

  {

    "name": "Linux",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9104"

  },

  {

    "name": "Linux",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "Linux",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9107"

  },

  {

    "name": "LinuxDEBIAN7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9102"

  },

  {

    "name": "LinuxDEBIAN7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxDEBIAN7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxDEBIAN7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9106"

  },

  {

    "name": "AzureBackupLinuxWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.1"

  },

  {

    "name": "AzureBackupLinuxWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.10"

  },

  {

    "name": "AzureBackupLinuxWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.12"

  },

  {

    "name": "AzureBackupLinuxWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.4"

  },

  {

    "name": "AzureBackupLinuxWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.5"

  },

  {

    "name": "AzureBackupLinuxWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.6"

  },

  {

    "name": "AzureBackupLinuxWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.9"

  },

  {

    "name": "VMSnapshotLinux",

    "publisher": "Microsoft.Azure.RecoveryServices.Edp",

    "version": "1.0.9125.0"

  },

  {

    "name": "LinuxOL6",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9101"

  },

  {

    "name": "LinuxOL6",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxOL6",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxOL6",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "LinuxDEBIAN8",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9102"

  },

  {

    "name": "LinuxDEBIAN8",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxDEBIAN8",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxDEBIAN8",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9106"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.0"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.2"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.4"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.0.0.5"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.1.0.1"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.1.0.2"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.1.0.3"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.1.0.4"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.1.0.5"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.1.0.6"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.1.0.7"

  },

  {

    "name": "AzureBackupWindowsWorkload",

    "publisher": "Microsoft.Azure.RecoveryServices.WorkloadBackup",

    "version": "1.1.0.8"

  },

  {

    "name": "ADETest",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.4.0.8"

  },

  {

    "name": "ADETest",

    "publisher": "Microsoft.Azure.Security",

    "version": "2.0.0.4"

  },

  {

    "name": "ADETest",

    "publisher": "Microsoft.Azure.Security",

    "version": "2.2.0.4"

  },

  {

    "name": "LinuxOL7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "LinuxSLES12",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxSLES12",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxSLES12",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9105"

  },

  {

    "name": "LinuxSLES12",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9106"

  },

  {

    "name": "LinuxSLES12",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery2",

    "version": "1.0.0.9107"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.0.0.0"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.0"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.1"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.2"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.4"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "2.0.0.0"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "2.1.0.0"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "2.2.0.1"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "2.2.0.2"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "2.2.0.3"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "2.2.0.4"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security",

    "version": "2.2.0.5"

  },

  {

    "name": "DSMSForWindows",

    "publisher": "Microsoft.Azure.Security.Dsms",

    "version": "2.15.794.0"

  },

  {

    "name": "DSMSForWindows",

    "publisher": "Microsoft.Azure.Security.Dsms",

    "version": "2.17.869.0"

  },

  {

    "name": "LinuxRHEL6",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9102"

  },

  {

    "name": "LinuxRHEL6",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxRHEL6",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxRHEL6",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "ADETest",

    "publisher": "Microsoft.Azure.Security.Edp",

    "version": "2.2.0.4"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999302"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999304"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999305"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999306"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999307"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999308"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999309"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999313"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999315"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999316"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999319"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999321"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999322"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999326"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.999327"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.0.0.0"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.0"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.14"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.15"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.17"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.20"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.21"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.5"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.6"

  },

  {

    "name": "LinuxRHEL7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9101"

  },

  {

    "name": "LinuxRHEL7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9102"

  },

  {

    "name": "LinuxRHEL7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxRHEL7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxRHEL7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "LinuxRHEL7",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9107"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security.Test",

    "version": "1.5.2.0"

  },

  {

    "name": "AzureDiskEncryption",

    "publisher": "Microsoft.Azure.Security.Edp",

    "version": "2.2.0.4"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.0.0.0"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.1.0.0"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.2.0.0"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.3.0.2"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.3.0.3"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.4.0.0"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.4.0.1"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.5.0.0"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.5.2.0"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.5.4.2"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.5.4.3"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.5.4.4"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.5.5.0"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.5.5.1"

  },

  {

    "name": "IaaSAntimalware",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.5.5.9"

  },

  {

    "name": "Linux",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.2.0.250"

  },

  {

    "name": "Linux",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.2.0.252"

  },

  {

    "name": "LinuxSLES11SP3",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9101"

  },

  {

    "name": "LinuxSLES11SP3",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxSLES11SP3",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxSLES11SP3",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security.Edp",

    "version": "0.1.0.999327"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.Azure.Security.Edp",

    "version": "1.1.0.20"

  },

  {

    "name": "TestGenevaMonitoringExtension",

    "publisher": "Microsoft.Azure.Security",

    "version": "1.7.0.6"

  },

  {

    "name": "LinuxOL6",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.3.0.339"

  },

  {

    "name": "LinuxOL6",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.3.0.341"

  },

  {

    "name": "LinuxSLES11SP4",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9101"

  },

  {

    "name": "LinuxSLES11SP4",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9102"

  },

  {

    "name": "LinuxSLES11SP4",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxSLES11SP4",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxSLES11SP4",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "LinuxDEBIAN7",

    "publisher": "Microsoft.Azure.SiteRecovery2.Test",

    "version": "1.0.0.247"

  },

  {

    "name": "LinuxDEBIAN7",

    "publisher": "Microsoft.Azure.SiteRecovery2.Test",

    "version": "1.0.0.249"

  },

  {

    "name": "VMBackupForLinuxExtension",

    "publisher": "Microsoft.Azure.Security",

    "version": "0.1.0.995"

  },

  {

    "name": "LinuxOL7",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.0.0.63"

  },

  {

    "name": "LinuxOL7",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.0.0.65"

  },

  {

    "name": "LinuxUBUNTU1404",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9101"

  },

  {

    "name": "LinuxUBUNTU1404",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9102"

  },

  {

    "name": "LinuxUBUNTU1404",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxUBUNTU1404",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxUBUNTU1404",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "LinuxUBUNTU1404",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9107"

  },

  {

    "name": "LinuxDEBIAN8",

    "publisher": "Microsoft.Azure.SiteRecovery2.Test",

    "version": "1.0.0.247"

  },

  {

    "name": "LinuxDEBIAN8",

    "publisher": "Microsoft.Azure.SiteRecovery2.Test",

    "version": "1.0.0.249"

  },

  {

    "name": "TestMSILinuxExtension",

    "publisher": "Microsoft.Azure.Test.Identity",

    "version": "1.0.0.7"

  },

  {

    "name": "LinuxRHEL6",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.5.0.342"

  },

  {

    "name": "LinuxRHEL6",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.5.0.344"

  },

  {

    "name": "LinuxUBUNTU1604",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9"

  },

  {

    "name": "LinuxUBUNTU1604",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9101"

  },

  {

    "name": "LinuxUBUNTU1604",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9102"

  },

  {

    "name": "LinuxUBUNTU1604",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9103"

  },

  {

    "name": "LinuxUBUNTU1604",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9104"

  },

  {

    "name": "LinuxUBUNTU1604",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "LinuxUBUNTU1604",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9107"

  },

  {

    "name": "LinuxOL7",

    "publisher": "Microsoft.Azure.SiteRecovery2.Test",

    "version": "1.0.0.28"

  },

  {

    "name": "LinuxOL7",

    "publisher": "Microsoft.Azure.SiteRecovery2.Test",

    "version": "1.0.0.29"

  },

  {

    "name": "TestMSIWindowsExtension",

    "publisher": "Microsoft.Azure.Test.Identity",

    "version": "1.0.0.11"

  },

  {

    "name": "LinuxRHEL7",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.3.0.339"

  },

  {

    "name": "LinuxRHEL7",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.3.0.341"

  },

  {

    "name": "SiteRecovery",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "0.0.0.0"

  },

  {

    "name": "AzureCATExtensionHandler",

    "publisher": "Microsoft.AzureCAT.AzureEnhancedMonitoring",

    "version": "2.2.0.48"

  },

  {

    "name": "AzureCATExtensionHandler",

    "publisher": "Microsoft.AzureCAT.AzureEnhancedMonitoring",

    "version": "2.2.0.68"

  },

  {

    "name": "LinuxSLES11SP3",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.3.0.335"

  },

  {

    "name": "LinuxSLES11SP3",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.3.0.337"

  },

  {

    "name": "SiteRecoveryLinux",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "0.0.0.1"

  },

  {

    "name": "VMJITAccessExtension",

    "publisher": "Microsoft.AzureSecurity.JITAccess",

    "version": "1.0.0.0"

  },

  {

    "name": "VMJITAccessExtension",

    "publisher": "Microsoft.AzureSecurity.JITAccess",

    "version": "1.0.1.0"

  },

  {

    "name": "LinuxSLES11SP4",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.3.0.335"

  },

  {

    "name": "LinuxSLES11SP4",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.3.0.337"

  },

  {

    "name": "Windows",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9102"

  },

  {

    "name": "Windows",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9103"

  },

  {

    "name": "Windows",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9104"

  },

  {

    "name": "Windows",

    "publisher": "Microsoft.Azure.RecoveryServices.SiteRecovery",

    "version": "1.0.0.9106"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.1338.47"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.1338.48"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.1.0.0"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.1.0.2"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.1.0.3"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.1.0.4"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.1.0.5"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.1.0.6"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.1.0.7"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.1.0.8"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension.Edp",

    "version": "1.0.1338.47"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension.Edp",

    "version": "1.0.1338.48"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension.Edp",

    "version": "1.0.1338.49"

  },

  {

    "name": "WorkloadBackup",

    "publisher": "Microsoft.CloudBackup.Workload.Extension.Edp",

    "version": "1.0.1338.50"

  },

  {

    "name": "LinuxUBUNTU1404",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.0.0.340"

  },

  {

    "name": "LinuxUBUNTU1404",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.0.0.342"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.1"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.11"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.12"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.14"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.15"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.16"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.17"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.18"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.19"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.2"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.3"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.5"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.6"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.7"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.8"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension",

    "version": "1.0.0.9"

  },

  {

    "name": "BGInfo",

    "publisher": "Microsoft.Compute",

    "version": "2.1"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension.Edp",

    "version": "1.0.0.14"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension.Edp",

    "version": "1.0.0.15"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension.Edp",

    "version": "1.0.0.16"

  },

  {

    "name": "WorkloadBackupLinux",

    "publisher": "Microsoft.CloudBackup.Workload.Extension.Edp",

    "version": "1.0.0.17"

  },

  {

    "name": "LinuxUBUNTU1604",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.0.0.253"

  },

  {

    "name": "LinuxUBUNTU1604",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.0.0.255"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.1"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.2"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.3"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.1.0"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.2.0"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.3.0"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.0.0"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.1.0"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.3.0"

  },

  {

    "name": "NullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "4.0.1"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.0.1"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.0.3"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.1"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.2"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.3"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.4"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.7"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.8"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.9"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.9.1"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.9.2"

  },

  {

    "name": "CustomScriptExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.9.3"

  },

  {

    "name": "WindowsTest",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.4.0.257"

  },

  {

    "name": "WindowsTest",

    "publisher": "Microsoft.Azure.SiteRecovery.Test",

    "version": "1.4.0.261"

  },

  {

    "name": "NullSeqA",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.1"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.0.11049.5"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.0.11049.7"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.0.11072.0"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.0.11072.1"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.0.11081.1"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.0.11081.2"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.0.11081.4"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.0.11081.5"

  },

  {

    "name": "JsonADDomainExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.0"

  },

  {

    "name": "JsonADDomainExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.3"

  },

  {

    "name": "JsonADDomainExtension",

    "publisher": "Microsoft.Compute",

    "version": "1.3.2"

  },

  {

    "name": "NullSeqB",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.1"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.0.217.0"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.2.148.0"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.3.127.5"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.3.127.7"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.3.18.7"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.4.45.2"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.4.45.3"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.4.55.4"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.4.56.5"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.4.58.7"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.4.59.1"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.4.60.2"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.6.42.0"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.7.3"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.7.7"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.7.9"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.8.11"

  },

  {

    "name": "OmsAgentForLinux",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring",

    "version": "1.8.9"

  },

  {

    "name": "VMAccessAgent",

    "publisher": "Microsoft.Compute",

    "version": "2.0"

  },

  {

    "name": "VMAccessAgent",

    "publisher": "Microsoft.Compute",

    "version": "2.0.1"

  },

  {

    "name": "VMAccessAgent",

    "publisher": "Microsoft.Compute",

    "version": "2.0.2"

  },

  {

    "name": "VMAccessAgent",

    "publisher": "Microsoft.Compute",

    "version": "2.3"

  },

  {

    "name": "VMAccessAgent",

    "publisher": "Microsoft.Compute",

    "version": "2.4"

  },

  {

    "name": "VMAccessAgent",

    "publisher": "Microsoft.Compute",

    "version": "2.4.1"

  },

  {

    "name": "VMAccessAgent",

    "publisher": "Microsoft.Compute",

    "version": "2.4.2"

  },

  {

    "name": "VMAccessAgent",

    "publisher": "Microsoft.Compute",

    "version": "2.4.3"

  },

  {

    "name": "VMAccessAgent",

    "publisher": "Microsoft.Compute",

    "version": "2.4.4"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.1"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.2"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.3"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.1.0"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.2.0"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.3.0"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.0.0"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.1.0"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.2.0"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.4.0"

  },

  {

    "name": "NullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "4.0.0"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring.Test",

    "version": "1.0.11030.0"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring.Test",

    "version": "1.0.11049.0"

  },

  {

    "name": "MicrosoftMonitoringAgent",

    "publisher": "Microsoft.EnterpriseCloud.Monitoring.Test",

    "version": "1.0.11049.1"

  },

  {

    "name": "OtherNullLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.0.1"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.GuestConfig.Test",

    "version": "2.2.0.0"

  },

  {

    "name": "ConfigurationforWindows",

    "publisher": "Microsoft.GuestConfiguration.Test",

    "version": "1.0.0.0"

  },

  {

    "name": "ConfigurationforWindows",

    "publisher": "Microsoft.GuestConfiguration.Test",

    "version": "1.1.0.0"

  },

  {

    "name": "ConfigurationforWindows",

    "publisher": "Microsoft.GuestConfiguration.Test",

    "version": "1.2.0.0"

  },

  {

    "name": "ConfigurationForLinux",

    "publisher": "Microsoft.GuestConfiguration",

    "version": "0.2.0"

  },

  {

    "name": "ConfigurationForLinux",

    "publisher": "Microsoft.GuestConfiguration",

    "version": "1.0.0"

  },

  {

    "name": "ConfigurationForLinux",

    "publisher": "Microsoft.GuestConfiguration",

    "version": "1.1.0"

  },

  {

    "name": "ConfigurationForLinux",

    "publisher": "Microsoft.GuestConfiguration",

    "version": "1.2.1"

  },

  {

    "name": "OtherNullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.1"

  },

  {

    "name": "OtherNullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.2"

  },

  {

    "name": "OtherNullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.0.3"

  },

  {

    "name": "OtherNullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.1.0"

  },

  {

    "name": "OtherNullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.2.0"

  },

  {

    "name": "OtherNullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "2.3.0"

  },

  {

    "name": "OtherNullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.0.0"

  },

  {

    "name": "OtherNullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "3.2.0"

  },

  {

    "name": "OtherNullWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "4.0.0"

  },

  {

    "name": "HpcVmDrivers",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.1.0.0"

  },

  {

    "name": "HpcVmDrivers",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.1.1.1"

  },

  {

    "name": "HpcVmDrivers",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.1.2.0"

  },

  {

    "name": "HpcVmDrivers",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.1.3.0"

  },

  {

    "name": "ConfigurationforWindows",

    "publisher": "Microsoft.GuestConfiguration",

    "version": "1.2.0.0"

  },

  {

    "name": "ConfigurationforWindows",

    "publisher": "Microsoft.GuestConfiguration",

    "version": "1.3.0.0"

  },

  {

    "name": "ConfigurationforWindows",

    "publisher": "Microsoft.GuestConfiguration",

    "version": "1.4.0.0"

  },

  {

    "name": "ConfigurationforWindows",

    "publisher": "Microsoft.GuestConfiguration",

    "version": "1.5.1.0"

  },

  {

    "name": "RunCommandLinux",

    "publisher": "Microsoft.CPlat.Core",

    "version": "1.0.0"

  },

  {

    "name": "NvidiaGpuDriverLinux",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.0.0.0"

  },

  {

    "name": "NvidiaGpuDriverLinux",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.1.0.0"

  },

  {

    "name": "NvidiaGpuDriverLinux",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.1.1.0"

  },

  {

    "name": "NvidiaGpuDriverLinux",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.1.2.0"

  },

  {

    "name": "NvidiaGpuDriverLinux",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.1.3.0"

  },

  {

    "name": "NvidiaGpuDriverLinux",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.2.0.0"

  },

  {

    "name": "HPCAcmAgent",

    "publisher": "Microsoft.HpcPack",

    "version": "1.0.30.0"

  },

  {

    "name": "HPCAcmAgent",

    "publisher": "Microsoft.HpcPack",

    "version": "1.0.31.0"

  },

  {

    "name": "ManagedIdentityExtensionForLinux",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.1"

  },

  {

    "name": "ManagedIdentityExtensionForLinux",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.10"

  },

  {

    "name": "ManagedIdentityExtensionForLinux",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.11"

  },

  {

    "name": "ManagedIdentityExtensionForLinux",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.12"

  },

  {

    "name": "ManagedIdentityExtensionForLinux",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.13"

  },

  {

    "name": "ManagedIdentityExtensionForLinux",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.3"

  },

  {

    "name": "ManagedIdentityExtensionForLinux",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.8"

  },

  {

    "name": "RunCommandWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "1.0.0"

  },

  {

    "name": "RunCommandWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "1.0.1"

  },

  {

    "name": "RunCommandWindows",

    "publisher": "Microsoft.CPlat.Core",

    "version": "1.1.0"

  },

  {

    "name": "NvidiaGpuDriverWindows",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.0.0.0"

  },

  {

    "name": "NvidiaGpuDriverWindows",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.1.0.0"

  },

  {

    "name": "NvidiaGpuDriverWindows",

    "publisher": "Microsoft.HpcCompute",

    "version": "1.2.0.0"

  },

  {

    "name": "LinuxNodeAgent",

    "publisher": "Microsoft.HpcPack",

    "version": "1.5.1.0"

  },

  {

    "name": "LinuxNodeAgent",

    "publisher": "Microsoft.HpcPack",

    "version": "1.6.18.3"

  },

  {

    "name": "LinuxNodeAgent",

    "publisher": "Microsoft.HpcPack",

    "version": "1.7.11.2"

  },

  {

    "name": "LinuxNodeAgent",

    "publisher": "Microsoft.HpcPack",

    "version": "2.1.5.0"

  },

  {

    "name": "ManagedIdentityExtensionForWindows",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.1"

  },

  {

    "name": "ManagedIdentityExtensionForWindows",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.10"

  },

  {

    "name": "ManagedIdentityExtensionForWindows",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.11"

  },

  {

    "name": "ManagedIdentityExtensionForWindows",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.12"

  },

  {

    "name": "ManagedIdentityExtensionForWindows",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.13"

  },

  {

    "name": "ManagedIdentityExtensionForWindows",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.3"

  },

  {

    "name": "ManagedIdentityExtensionForWindows",

    "publisher": "Microsoft.ManagedIdentity",

    "version": "1.0.0.8"

  },

  {

    "name": "ApplicationHealthLinux",

    "publisher": "Microsoft.ManagedServices",

    "version": "1.0.0"

  },

  {

    "name": "LinuxNodeAgent2016",

    "publisher": "Microsoft.HpcPack",

    "version": "2.1.6.0"

  },

  {

    "name": "ApplicationHealthWindows",

    "publisher": "Microsoft.ManagedServices",

    "version": "1.0.4"

  },

  {

    "name": "AzureDiskEncryptionForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "0.1.0.999105"

  },

  {

    "name": "LinuxNodeAgent2016U1",

    "publisher": "Microsoft.HpcPack",

    "version": "2.3.4.0"

  },

  {

    "name": "LinuxNodeAgent2016U1",

    "publisher": "Microsoft.HpcPack",

    "version": "2.3.4.1"

  },

  {

    "name": "LinuxNodeAgent2016U1",

    "publisher": "Microsoft.HpcPack",

    "version": "2.3.6.0"

  },

  {

    "name": "AzureDiagnosticsLinuxExtIaaS7.Test",

    "publisher": "Microsoft.OSTCExtensions.Test",

    "version": "1.0.0.0"

  },

  {

    "name": "AzureEnhancedMonitorForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.0.0.2"

  },

  {

    "name": "AzureEnhancedMonitorForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "3.0.0.1"

  },

  {

    "name": "AzureEnhancedMonitorForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "3.0.0.5"

  },

  {

    "name": "AzureEnhancedMonitorForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "3.0.0.97"

  },

  {

    "name": "AzureEnhancedMonitorForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "3.0.0.98"

  },

  {

    "name": "AzureEnhancedMonitorForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "3.0.0.99"

  },

  {

    "name": "AzureEnhancedMonitorForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "3.0.1.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.10.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.13.2.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.14.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.15.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.16.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.17.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.18.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.19.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.20.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.21.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.22.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.23.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.24.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.25.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.26.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.26.1.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.4.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.5.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.6.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.7.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.70.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.71.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.71.1.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.72.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.73.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.74.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.75.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.76.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.77.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.8.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell",

    "version": "2.9.1.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell.Test",

    "version": "2.76.0.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell.Test",

    "version": "2.76.1.0"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell.Test",

    "version": "2.76.2.0"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0.1"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.1"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.1.1"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.2.2.0"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.3.0.0"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.3.0.1"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.3.0.2"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.0.0"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.1.0"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.5.2.0"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.5.2.1"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.5.2.2"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.5.3"

  },

  {

    "name": "CustomScriptForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.5.4"

  },

  {

    "name": "DSC",

    "publisher": "Microsoft.Powershell.Test01",

    "version": "1.0.0.0"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0.0.0"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.0.0.0"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.1.0.0"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.2.0.0"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.3.0.0"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.4.0.0"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.5.0.0"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.6.0.0"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.70.0.10"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.70.0.2"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.70.0.3"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.70.0.4"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.70.0.7"

  },

  {

    "name": "DSCForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.70.0.8"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.10.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.11.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.12.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.13.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.14.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.15.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.16.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.17.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.18.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.19.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.20.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.22.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.24.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.29.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.30.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.2.9.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "2.0.1.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "2.0.3.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "2.0.4.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "2.0.5.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "2.0.6.0"

  },

  {

    "name": "SqlIaaSAgent",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "2.0.7.0"

  },

  {

    "name": "MSEnterpriseApplication",

    "publisher": "Microsoft.SystemCenter",

    "version": "1.0.5.0"

  },

  {

    "name": "TestSqlIaaSAgent",

    "publisher": "Microsoft.TestSqlServer.Edp",

    "version": "1.4.0.0"

  },

  {

    "name": "TestSqlIaaSAgent",

    "publisher": "Microsoft.TestSqlServer.Edp",

    "version": "2.0.0.1"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.0.9023"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.1.9023"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.2.9023"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.3.9023"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.3.9025"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.3.9027"

  },

  {

    "name": "LinuxDiagnostic",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.3.9029"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.1.0.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.1.0.1"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.2.0.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.3.0.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.4.0.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.5.0.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.6.0.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.7.0.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.7.1.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.7.2.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.7.3.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "0.8.0.0"

  },

  {

    "name": "VSETWTraceListenerService",

    "publisher": "Microsoft.VisualStudio.Azure.ETWTraceListenerService",

    "version": "1.0.0.0"

  },

  {

    "name": "TestSqlIaaSAgentLinux",

    "publisher": "Microsoft.TestSqlServer.Edp",

    "version": "1.0.16"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0.0.0"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0.0.3"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0.1.0"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0.2.0"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0.3.0"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.1.0.0"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.2.0.0"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.3.0.0"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.0.0.0"

  },

  {

    "name": "Null",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.1.0.0"

  },

  {

    "name": "VSRemoteDebugger",

    "publisher": "Microsoft.VisualStudio.Azure.RemoteDebug",

    "version": "1.1.1.0"

  },

  {

    "name": "VSRemoteDebugger",

    "publisher": "Microsoft.VisualStudio.Azure.RemoteDebug",

    "version": "1.1.2.0"

  },

  {

    "name": "VSRemoteDebugger",

    "publisher": "Microsoft.VisualStudio.Azure.RemoteDebug",

    "version": "1.1.3.0"

  },

  {

    "name": "SqlIaaSAgentLinux",

    "publisher": "Microsoft.SqlServer.Management",

    "version": "1.0.0.0"

  },

  {

    "name": "OSPatchingForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0"

  },

  {

    "name": "OSPatchingForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0.1.1"

  },

  {

    "name": "OSPatchingForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.0.0.0"

  },

  {

    "name": "OSPatchingForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.0.0.1"

  },

  {

    "name": "OSPatchingForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.0.0.2"

  },

  {

    "name": "OSPatchingForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.0.0.5"

  },

  {

    "name": "OSPatchingForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.1.0.0"

  },

  {

    "name": "OSPatchingForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.2.0.0"

  },

  {

    "name": "OSPatchingForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "2.3.0.1"

  },

  {

    "name": "ServiceProfilerAgent",

    "publisher": "Microsoft.VisualStudio.ServiceProfiler",

    "version": "0.1.0.24"

  },

  {

    "name": "ServiceProfilerAgent",

    "publisher": "Microsoft.VisualStudio.ServiceProfiler",

    "version": "0.1.0.25"

  },

  {

    "name": "RDMAUpdateForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "0.1.0.9"

  },

  {

    "name": "TeamServicesAgent",

    "publisher": "Microsoft.VisualStudio.Services",

    "version": "1.20.0.0"

  },

  {

    "name": "TeamServicesAgent",

    "publisher": "Microsoft.VisualStudio.Services",

    "version": "1.21.0.0"

  },

  {

    "name": "TeamServicesAgent",

    "publisher": "Microsoft.VisualStudio.Services",

    "version": "1.22.0.0"

  },

  {

    "name": "TeamServicesAgent",

    "publisher": "Microsoft.VisualStudio.Services",

    "version": "1.23.0.0"

  },

  {

    "name": "AzureRemoteAppTestAgentV2",

    "publisher": "Microsoft.Windows.AzureRemoteApp.Test",

    "version": "1.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.1"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.2"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.3.0.1"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.0.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.1.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.2.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.3.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.4.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.5.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.6.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.7.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.4.7.1"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.5.0"

  },

  {

    "name": "VMAccessForLinux",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "1.5.1"

  },

  {

    "name": "TeamServicesAgentLinux",

    "publisher": "Microsoft.VisualStudio.Services",

    "version": "1.15.0.0"

  },

  {

    "name": "TeamServicesAgentLinux",

    "publisher": "Microsoft.VisualStudio.Services",

    "version": "1.16.0.0"

  },

  {

    "name": "TeamServicesAgentLinux",

    "publisher": "Microsoft.VisualStudio.Services",

    "version": "1.17.0.0"

  },

  {

    "name": "TeamServicesAgentLinux",

    "publisher": "Microsoft.VisualStudio.Services",

    "version": "1.18.0.0"

  },

  {

    "name": "TeamServicesAgentLinux",

    "publisher": "Microsoft.VisualStudio.Services",

    "version": "1.19.0.0"

  },

  {

    "name": "AzureLogCollector",

    "publisher": "Microsoft.WindowsAzure.Compute",

    "version": "1.0.0.7"

  },

  {

    "name": "AzureLogCollector",

    "publisher": "Microsoft.WindowsAzure.Compute",

    "version": "1.0.0.8"

  },

  {

    "name": "AzureLogCollector",

    "publisher": "Microsoft.WindowsAzure.Compute",

    "version": "1.0.0.9"

  },

  {

    "name": "VMBackupForLinuxExtension",

    "publisher": "Microsoft.OSTCExtensions",

    "version": "0.1.0.993"

  },

  {

    "name": "OctopusDeployWindowsTentacle",

    "publisher": "OctopusDeploy.Tentacle",

    "version": "2.0.104"

  },

  {

    "name": "OctopusDeployWindowsTentacle",

    "publisher": "OctopusDeploy.Tentacle",

    "version": "2.0.108"

  },

  {

    "name": "OctopusDeployWindowsTentacle",

    "publisher": "OctopusDeploy.Tentacle",

    "version": "2.0.113"

  },

  {

    "name": "OctopusDeployWindowsTentacle",

    "publisher": "OctopusDeploy.Tentacle",

    "version": "2.0.135"

  },

  {

    "name": "OctopusDeployWindowsTentacle",

    "publisher": "OctopusDeploy.Tentacle",

    "version": "2.0.156"

  },

  {

    "name": "OctopusDeployWindowsTentacle",

    "publisher": "OctopusDeploy.Tentacle",

    "version": "2.0.164"

  },

  {

    "name": "PuppetAgent",

    "publisher": "puppet",

    "version": "1.4.2"

  },

  {

    "name": "PuppetAgent",

    "publisher": "puppet",

    "version": "1.5.2"

  },

  {

    "name": "PuppetEnterpriseAgent",

    "publisher": "PuppetLabs",

    "version": "2015.2.3"

  },

  {

    "name": "PuppetEnterpriseAgent",

    "publisher": "PuppetLabs",

    "version": "2015.3.3"

  },

  {

    "name": "PuppetEnterpriseAgent",

    "publisher": "PuppetLabs",

    "version": "3.2.1"

  },

  {

    "name": "PuppetEnterpriseAgent",

    "publisher": "PuppetLabs",

    "version": "3.2.2"

  },

  {

    "name": "PuppetEnterpriseAgent",

    "publisher": "PuppetLabs",

    "version": "3.2.3"

  },

  {

    "name": "PuppetEnterpriseAgent",

    "publisher": "PuppetLabs",

    "version": "3.7.2"

  },

  {

    "name": "PuppetEnterpriseAgent",

    "publisher": "PuppetLabs",

    "version": "3.8.4"

  },

  {

    "name": "PuppetEnterpriseAgent",

    "publisher": "PuppetLabs.Test",

    "version": "3.8.4"

  },

  {

    "name": "QualysAgent",

    "publisher": "Qualys",

    "version": "0.0.0.1"

  },

  {

    "name": "QualysAgent",

    "publisher": "Qualys",

    "version": "0.0.0.3"

  },

  {

    "name": "QualysAgent",

    "publisher": "Qualys",

    "version": "0.0.0.4"

  },

  {

    "name": "QualysAgent",

    "publisher": "Qualys",

    "version": "0.0.0.5"

  },

  {

    "name": "QualysAgent",

    "publisher": "Qualys",

    "version": "0.0.0.7"

  },

  {

    "name": "QualysAgent",

    "publisher": "Qualys",

    "version": "0.0.0.8"

  },

  {

    "name": "QualysAgent",

    "publisher": "Qualys",

    "version": "0.0.0.9"

  },

  {

    "name": "QualysAgent",

    "publisher": "Qualys",

    "version": "1.6.4.9"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.5.0.72"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.5.0.73"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.5.0.82"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.6.0.1"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.6.0.100"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.6.0.3"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.6.0.90"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.6.0.91"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.6.0.93"

  },

  {

    "name": "QualysAgentLinux",

    "publisher": "Qualys",

    "version": "1.6.0.96"

  },

  {

    "name": "InsightAgentLinux",

    "publisher": "Rapid7.InsightPlatform",

    "version": "2.0.0.2"

  },

  {

    "name": "InsightAgentWindows",

    "publisher": "Rapid7.InsightPlatform",

    "version": "2.0.0.2"

  },

  {

    "name": "Site24x7ApmInsightExtn",

    "publisher": "Site24x7",

    "version": "1.9.0.0"

  },

  {

    "name": "Site24x7LinuxServerExtn",

    "publisher": "Site24x7",

    "version": "1.5.0.0"

  },

  {

    "name": "Site24x7LinuxServerExtn",

    "publisher": "Site24x7",

    "version": "1.6.0.0"

  },

  {

    "name": "Site24x7WindowsServerExtn",

    "publisher": "Site24x7",

    "version": "1.6.0.0"

  },

  {

    "name": "Site24x7WindowsServerExtn",

    "publisher": "Site24x7",

    "version": "1.8.0.0"

  },

  {

    "name": "StackifyLinuxAgentExtension",

    "publisher": "Stackify.LinuxAgent.Extension",

    "version": "1.0.0.21"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "StatusReport.Diagnostics.Test",

    "version": "0.27.0.0"

  },

  {

    "name": "SymantecEndpointProtection",

    "publisher": "Symantec",

    "version": "12.1.4100.2"

  },

  {

    "name": "SymantecEndpointProtection",

    "publisher": "Symantec",

    "version": "12.1.7007.6505"

  },

  {

    "name": "SCWPAgentForLinux",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "1.7.0.0"

  },

  {

    "name": "SCWPAgentForLinux",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "1.8.0.0"

  },

  {

    "name": "SCWPAgentForLinux",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "1.9.0.0"

  },

  {

    "name": "SCWPAgentForLinux",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "2.0.0.0"

  },

  {

    "name": "SCWPAgentForLinux",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "2.1.0.0"

  },

  {

    "name": "SCWPAgentForLinux",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "2.2.0.0"

  },

  {

    "name": "SCWPAgentForLinuxTest",

    "publisher": "Symantec.CloudWorkloadProtection.Test",

    "version": "2.0.0.0"

  },

  {

    "name": "SCWPAgentForLinuxTest",

    "publisher": "Symantec.CloudWorkloadProtection.Test",

    "version": "2.1.0.0"

  },

  {

    "name": "SCWPAgentForLinuxTest",

    "publisher": "Symantec.CloudWorkloadProtection.Test",

    "version": "2.2.0.0"

  },

  {

    "name": "SCWPAgentForLinuxTestOnStage",

    "publisher": "Symantec.CloudWorkloadProtection.TestOnStage",

    "version": "1.5.0.0"

  },

  {

    "name": "SCWPAgentForLinuxTestOnStage",

    "publisher": "Symantec.CloudWorkloadProtection.TestOnStage",

    "version": "1.6.0.0"

  },

  {

    "name": "SCWPAgentForLinuxTestOnStage",

    "publisher": "Symantec.CloudWorkloadProtection.TestOnStage",

    "version": "1.8.0.0"

  },

  {

    "name": "SCWPAgentForLinuxTestOnStage",

    "publisher": "Symantec.CloudWorkloadProtection.TestOnStage",

    "version": "1.9.0.0"

  },

  {

    "name": "SCWPAgentForWindows",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "1.4.0.0"

  },

  {

    "name": "SCWPAgentForWindows",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "1.5.0.0"

  },

  {

    "name": "SCWPAgentForWindows",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "1.6.0.0"

  },

  {

    "name": "SCWPAgentForWindows",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "1.7.0.0"

  },

  {

    "name": "SCWPAgentForWindows",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "1.8.0.0"

  },

  {

    "name": "SCWPAgentForWindows",

    "publisher": "Symantec.CloudWorkloadProtection",

    "version": "1.9.0.0"

  },

  {

    "name": "SCWPAgentForWindowsTest",

    "publisher": "Symantec.CloudWorkloadProtection.Test",

    "version": "1.8.0.0"

  },

  {

    "name": "SCWPAgentForWindowsTest",

    "publisher": "Symantec.CloudWorkloadProtection.Test",

    "version": "1.9.0.0"

  },

  {

    "name": "TrendMicroDSA",

    "publisher": "Test.TrendMicro.DeepSecurity",

    "version": "10.0.0.10705"

  },

  {

    "name": "TrendMicroDSA",

    "publisher": "Test.TrendMicro.DeepSecurity",

    "version": "9.6.2.11301"

  },

  {

    "name": "TrendMicroDSALinux",

    "publisher": "Test.TrendMicro.DeepSecurity",

    "version": "10.0.0.10601"

  },

  {

    "name": "TrendMicroDSALinux",

    "publisher": "Test.TrendMicro.DeepSecurity",

    "version": "9.6.2.11401"

  },

  {

    "name": "TrendMicroDSA",

    "publisher": "TrendMicro.DeepSecurity",

    "version": "10.0.0.107"

  },

  {

    "name": "TrendMicroDSA",

    "publisher": "TrendMicro.DeepSecurity",

    "version": "9.6.2.113"

  },

  {

    "name": "TrendMicroDSALinux",

    "publisher": "TrendMicro.DeepSecurity",

    "version": "10.0.0.106"

  },

  {

    "name": "TrendMicroDSALinux",

    "publisher": "TrendMicro.DeepSecurity",

    "version": "9.6.2.114"

  },

  {

    "name": "PortalProtectExtension",

    "publisher": "TrendMicro.PortalProtect",

    "version": "2.1"

  },

  {

    "name": "VormetricTransparentEncryptionAgent",

    "publisher": "Vormetric",

    "version": "5.2.339.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "WAD2AI.Diagnostics.Test",

    "version": "0.23.0.0"

  },

  {

    "name": "IaaSDiagnostics",

    "publisher": "WAD2EventHub.Diagnostics.Test",

    "version": "0.1.0.0"

  }

]
```
