---
title: OpenSSL – Public Certificate and Private key
author: Shafiq Alibhai
date: 2010-06-10T12:19:12+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1280983797";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1299623065";}'
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:7:"4390143";s:7:"blog_id";s:7:"4153392";s:9:"mod_stamp";s:19:"2010-06-10 12:19:12";}'
categories:
  - Development
tags:
  - openssl
  - private key
  - public certificate

---
`privatekey -> openssl genrsa \[-out filename\] \[-passout arg\] \[-des\] \[-des3\] \[-idea\] \[-f4\] \[-3\] \[-rand file(s)\] [numbits]`

`public certificate -> $ openssl req -new -x509 -nodes -sha1 -days 365 -key host.key > host.cert`
