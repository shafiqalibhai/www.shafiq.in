---
title: "Shutdown Proxmox VM using CLI"
date: 2023-10-17T01:30:03+00:00
author: "Me"
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
categories:
    - Development
tags:
  - proxmox
  - vm
  - cli
  - how-to
disableShare: false
disableHLJS: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
---

If you're looking to shut down a virtual machine running on a Proxmox Virtual Environment (PVE), you can use the Proxmox command-line interface (CLI) to accomplish this task quite effectively. The command for shutting down a VM in Proxmox is `qm shutdown`, followed by the ID of the virtual machine you'd like to shut down. Here's how to do it:

1. **Access the Server**: First, log in to your Proxmox server via SSH.

   ```bash
   ssh username@your-proxmox-server-ip
   ```

2. **Locate the VM ID**: If you're unsure of the VM ID, you can list all VMs by running:

   ```bash
   qm list
   ```

   This will display a list of VMs along with their IDs and statuses.

3. **Shutdown the VM**: Once you have the VM ID, use the following command to shut down the VM gracefully:

   ```bash
   qm shutdown VM_ID
   ```

   Replace `VM_ID` with the ID of the virtual machine you want to shut down. For example, if your VM ID is 101, the command would be:

   ```bash
   qm shutdown 101
   ```

Note that `qm shutdown` will attempt to shut down the VM gracefully, meaning it will send an ACPI shutdown signal to the OS. If the VM does not respond to this signal, it will not be forcibly powered off. If you need to force the shutdown, you can use `qm stop VM_ID`, although this is akin to pulling the plug and should be used as a last resort.