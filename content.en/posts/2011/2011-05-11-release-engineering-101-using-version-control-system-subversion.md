---
title: A Practical Guide to Release Engineering - Mastering Version Control with Subversion
author: Shafiq Alibhai
date: 2011-05-11T16:38:57+00:00
categories:
  - Development
tags:
  - Apache Subversion
  - Version Control
  - Configuration Management
  - Git
  - Quality Assurance
  - Release Engineering
  - Release Management
  - DevOps Tools

---

Subversion is more than just a tool for tracking changes in your code. It can be a cornerstone of an effective release engineering strategy, offering features that facilitate a smooth transition of code from development to production. Here, we'll explore two techniques you can employ: utilizing revision numbers and creating tags.

Most people who have dabbled in Subversion are familiar with revision numbers. Let's say you make a commit and your code becomes "revision 1234." You can then export this specific revision to your development environment for testing. Once it passes your rigorous checks, it's off to the QA environment for further scrutiny.

But what if you want a more foolproof way to manage your codebase? Enter "tags."

Revision numbers like "1234" are a bit hard to remember and don't say much about the code. Tags, on the other hand, provide a more human-friendly way to identify specific versions of your code. To create a tag, you'll copy your code—say, from the "/trunk/" directory to a new directory like "/tags/release-Jan11_3PM." The great thing about tags in Subversion is that they're easy to manage. You can create tags as often as you'd like, for instance, "/tags/build-Jan11_4PM" or "/tags/version-1.2.3."

The advantage of using tags is their easy-to-understand naming conventions, which simplify the process of exporting specific versions to various environments like Development, QA, and Production. This not only adds an extra layer of clarity but also makes the lives of testers and quality assurance professionals a lot easier.

Whether you opt for the straightforward revision numbers or the more descriptive tagging method, Subversion offers robust options for managing your codebase from development through to production. Choose the strategy that best suits your project and team's needs, and take the hassle out of release engineering.
