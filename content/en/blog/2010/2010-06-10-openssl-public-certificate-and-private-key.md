---
title: OpenSSL – Public Certificate and Private key
author: Shafiq Alibhai
date: 2010-06-10T12:19:12+00:00
categories:
  - Development
tags:
  - openssl
  - ssl
  - security
  - reference

disableHLJS: false
---
---
`privatekey -> openssl genrsa \[-out filename\] \[-passout arg\] \[-des\] \[-des3\] \[-idea\] \[-f4\] \[-3\] \[-rand file(s)\] [numbits]`

`public certificate -> $ openssl req -new -x509 -nodes -sha1 -days 365 -key host.key > host.cert`