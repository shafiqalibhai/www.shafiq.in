---
title: Navigating Terraform Modules Stored in Package Subdirectories
author: Shafiq Alibhai
date: 2018-10-24T13:16:15+00:00
categories:
  - Development
---

In the realm of Infrastructure as Code, Terraform modules can play a significant role in making your life easier. Sometimes, however, these modules don't live at the root directory of their source package. Instead, they reside in sub-directories. Thankfully, Terraform has a smart way to help you access these nested modules.

Terraform employs a unique double-slash (`//`) syntax to help pinpoint the exact sub-directory where the module is located. The path that follows this double-slash syntax is considered to be a sub-directory within the package or repository.

Here are some examples to illustrate this concept:

* Using the Consul module in AWS: `hashicorp/consul/aws//modules/consul-cluster`
* Pointing to a VPC module in a Git repository: `git::https://example.com/network.git//modules/vpc`
* Accessing a VPC module from a zip file: `https://example.com/network-module.zip//modules/vpc`
* Retrieving a VPC module from an S3 bucket: `s3::https://s3-eu-west-1.amazonaws.com/examplecorp-terraform-modules/network.zip//modules/vpc`

Now, if you're working with version control sources and you need to include arguments like `ref` for specifying a particular version, make sure the sub-directory path comes before these arguments. For instance:

* `git::https://example.com/network.git//modules/vpc?ref=v1.2.0`

Another thing to note is that when you use this feature, Terraform will download the entire package to your local machine. However, it will only utilize the module present in the specified sub-directory. This also means that if you have modules interacting with each other within the same package, they can safely refer to each other using local paths.

For more information, you can check the official Terraform documentation on [Modules in Package Subdirectories](https://www.terraform.io/docs/modules/sources.html#modules-in-package-sub-directories).

Navigating subdirectories might seem like a minor feature, but it’s a powerful tool that helps you keep your codebase organized while leveraging external modules effectively. Happy coding!
