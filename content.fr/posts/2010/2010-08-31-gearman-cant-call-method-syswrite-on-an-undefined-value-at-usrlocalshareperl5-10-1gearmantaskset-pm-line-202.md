---
lang: "fr"
title: Gearman – Can't call method "syswrite" on an undefined value at /usr/local/share/perl/5.10.1/Gearman/Taskset.pm line 202.
author: Shafiq Alibhai
date: 2010-08-31T09:37:09+00:00

reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1334973445";}'
categories:
  - Development
tags:
  - gearman
  - gearman perl
  - Programming

disableHLJS: false
---
Si vous obtenez l'erreur suivante en exécutant le code client :

Impossible d'appeler la méthode « syswrite » sur une valeur non définie à /usr/local/share/perl/5.10.1/Gearman/Taskset.pm ligne 202.

... alors changez ceci

`$client->job_servers('127.0.0.1');`

en

`$client->job_servers('127.0.0.1:4730');`

c'est tout !

🙂
