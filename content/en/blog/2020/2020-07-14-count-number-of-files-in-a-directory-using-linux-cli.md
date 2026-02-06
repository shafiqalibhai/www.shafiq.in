---
title: Count number of files in a directory using Linux cli
author: Shafiq Alibhai
date: 2020-07-14T09:15:31+00:00
categories:
  - Development
tags:
  - linux
  - cli
  - bash
  - how-to

disableHLJS: false
---
```bash
ls -l . | egrep -c '^-'
```