---
title: Import a Resource to Terraform Module
author: Shafiq Alibhai
date: 2018-10-24T15:57:34+00:00
categories:
  - Development

---
The example below will import an AWS instance into a terraform module:

```
terraform import module.foo.aws_instance.bar i-abcd1234
```
