---
title: 'One liner: To get available virtual memory'
author: Shafiq Alibhai
date: 2011-12-10T12:43:02+00:00
categories:
  - development
tags:
  - linux
  - cli
  - bash
  - code-snippet

disableHLJS: false
---
```bash
vmstat -s -SM | grep "free memory" | awk -F" " '{print$1}'
```