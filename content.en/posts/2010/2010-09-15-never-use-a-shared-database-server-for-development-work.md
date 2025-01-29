---
title: Never use a shared database server for development work.
author: Shafiq Alibhai
date: 2010-09-15T08:39:58+00:00

reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1334973443";}'
categories:
  - Management
tags:
  - Cost
  - Database
  - database server
  - developer
  - shared database
  - Development

---
Like many conveniences in software development, a shared database is a tar pit waiting to fossilize a project. Developers overwrite each other's changes. The changes I make on the server break the code on your development machine. Remote development is slow and difficult. Avoid using a shared database at all costs, as they ultimately waste time and help produce bugs.
