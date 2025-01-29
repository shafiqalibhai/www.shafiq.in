---
title: Disable services in Solaris 10
author: Shafiq Alibhai
date: 2011-05-23T16:57:14+00:00
categories:
  - Development
tags:
  - bash
  - Grep
  - Hosts (file)
  - Network
  - Puppet
  - Solaris
  - Sun Microsystems
  - unix

---
To disable a service, you must be root or have sudo privileges.

For example, to disable the Puppet service, you would run the following command:

```bash
svcadm disable network/cswpuppetd:default
```

This will disable the Puppet service and prevent it from running.

To verify that the service has been disabled, you can run the following command:

```bash
svcs | grep puppet
```

This will list all of the services that are currently running, and if the Puppet service is disabled, it will not be listed.

Here are some additional tips for disabling services:

You can use the -s option with the svcadm disable command to disable the service synchronously. This means that the command will not return until the service has been fully disabled.
You can use the -T option with the svcadm disable command to specify a timeout in seconds. This means that the command will not return until the service has been disabled or the timeout has been reached.
If you want to disable a service temporarily, you can use the svcadm disable -t command. This will disable the service, but it will be able to be restarted by running the svcadm enable command.
