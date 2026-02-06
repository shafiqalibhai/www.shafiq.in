---
title: Perl – system load
author: Shafiq Alibhai
date: 2010-09-07T08:45:06+00:00

reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1334973449";}'
categories:
  - Development
tags:
  - AWK
  - Command-line interface
  - IP
  - Load (computing)
  - Programming
  - Uptime

disableHLJS: false
---
Pour trouver la charge système, utilisez le snippet Perl suivant :

1) <a class="zem_slink" title="Charge (informatique)" rel="wikipedia" href="http://en.wikipedia.org/wiki/Load_%28computing%29">Charge système</a> des dernières minutes :

```perl
my $system_load = exec('<a class="zem_slink" title="Uptime" rel="wikipedia" href="http://en.wikipedia.org/wiki/Uptime">uptime</a> | awk -F "load average: " \'{ print $2 }\' | cut -d, -f1');
my $system_load = qx('uptime | awk -F "load average: " \'{ print $2 }\' | cut -d, -f1');
``
2) Charge système des dernières 5 minutes :

```perl
my $system_load = exec('uptime | awk -F "load average: " \'{ print $2 }\' | cut -d, -f2');
my $system_load = qx('uptime | awk -F "load average: " \'{ print $2 }\' | cut -d, -f2');
``
3) Charge système des dernières 15 minutes :

```perl
my $system_load = exec('uptime | awk -F "load average: " \'{ print $2 }\' | cut -d, -f3');
my $system_load = qx('uptime | awk -F "load average: " \'{ print $2 }\' | cut -d, -f3');
```
