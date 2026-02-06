---
title: How to get a remote server SSL certificate
author: Shafiq Alibhai
date: 2021-06-15T08:21:21+00:00
categories:
  - Development
tags:
  - openssl
  - ssl
  - how-to
  - security

disableHLJS: false
---
```bash
openssl s_client -connect {HOSTNAME}:{PORT} -showcerts
```