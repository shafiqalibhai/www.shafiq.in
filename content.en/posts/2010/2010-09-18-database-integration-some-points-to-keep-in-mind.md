---
title: Database Integration – some points to keep in mind
author: Shafiq Alibhai
date: 2010-09-18T07:19:26+00:00

reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1334973443";}'
categories:
  - Development
tags:
  - Build Management
  - Database
  - Goa
  - IOS
  - IP

---
**Always Have a Single, Authoritative Source For Your Schema  
** Everyone should know where the official schema resides, and have a frictionless experience in getting a fresh database setup. One should be able to walk up to a computer, get the latest from source control, build, and run a simple tool to setup the database (in many scenarios, the build process can even setup a database if none exists, so the process is one step shorter).

**Always Version Your Database  
** The common goal is to propagate changes from development, to test, and ultimately to production in a controlled and consistent manner. A second goal is to have the ability to recreate a database at any point in time. This second goal is particularly important if you are shipping software to clients. If someone finds a bug in build 20100612.1 of your application, you must be able to recreate the application as it appeared in that build - database and all.
