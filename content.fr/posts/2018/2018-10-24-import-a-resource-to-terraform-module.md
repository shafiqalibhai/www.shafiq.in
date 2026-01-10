---
lang: "fr"
title: Import a Resource to Terraform Module
author: Shafiq Alibhai
date: 2018-10-24T15:57:34+00:00
categories:
  - Development

disableHLJS: false
---
L'exemple ci-dessous va importer une instance AWS dans un module Terraform :

```
terraform import module.foo.aws_instance.bar i-abcd1234
```
