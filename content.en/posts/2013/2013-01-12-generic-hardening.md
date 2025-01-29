---
title: The Art of System Hardening - A Comprehensive Guide
author: Shafiq Alibhai
date: 2013-01-12
categories:
  - Development
tags:
  - System Hardening
  - Database
  - Security
  - Operating Systems
  - Virtual Machine
  - Network Security
---

# [Download the Complete Guide to System Hardening](https://www.shafiq.in/wp-content/uploads/2013/01/generic-hardening-doc.docx)

## Introduction to System Hardening 

System hardening is the art of strengthening your computing environment against potential threats. At its core, the philosophy is about implementing the principle of 'least privilege.' This involves:

- Knowing exactly what services and applications need to run on a system
- Creating documentation that outlines policy, standards, and guidelines
- Securely configuring operating systems, virtual servers, and software
- Managing application settings to enhance security
- Streamlining database setup and configuration
- Securing network devices and portable equipment

## Why Platform Hardening Matters

Platforms, such as servers or databases, are the foundation of your data infrastructure. Their integrity is crucial for the secure, reliable transfer and storage of information. As a best practice, ensure that your platforms are configured and maintained to repel unauthorized access and service interruptions.

## Key Definitions in System Hardening

- **Hardened System (H)**: This represents the secure state you aim to achieve for your system.
- **Baseline OS Hardening (Bos)**: Refers to the foundational security settings for the operating system.
- **Application/System Function Hardening (Af)**: Concerns the security configurations for applications like Apache, Oracle, and specific system functions like DNS or DHCP.
- **Base Hardening (B)**: It's the sum of Baseline OS Hardening and Application/System Function Hardening (B = Bos + Af).
- **Custom Hardening (C)**: This involves extra security layers, such as DMZ settings, specialized security settings, or custom OS-specific controls like TCP Wrappers.
- **Virtual System Hardening**: This pertains to hardening the virtual machines (VMs) themselves. 

## The Formula for a Hardened System

To put system hardening into simple math, you could say:

\[
H (Hardened System) = B (Base Hardening) + C (Custom Hardening)
\]

This equation illustrates how a hardened system is the result of combining basic security configurations with custom layers of protection.

## Hardening Virtual Systems

In a virtualized environment, you can adapt the hardening formula as follows:

\[
H (Hardened System) = Vos (Virtual OS Hardening) + B (Base Hardening) + C (Custom Hardening)
\]

The addition of Virtual OS Hardening reflects the need to secure the virtual machine itself, alongside the base and custom hardening procedures.

