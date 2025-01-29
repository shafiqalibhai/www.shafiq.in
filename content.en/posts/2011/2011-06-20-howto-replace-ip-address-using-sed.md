---
title: '[HowTo] Replace ip address using sed'
author: Shafiq Alibhai
date: 2011-06-20T11:38:01+00:00
categories:
  - Development
tags:
  - IP
  - IP address
  - ipad
  - regular expression
  - sed
  - unix

---
Following one-liner will search for a ip address pattern in the specified file and replace it with the one provided :

```bash
sed 's/[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}/**IPADDRESS-COMES-HERE**/g' /SourceFilename > /DestinationFilename
```
