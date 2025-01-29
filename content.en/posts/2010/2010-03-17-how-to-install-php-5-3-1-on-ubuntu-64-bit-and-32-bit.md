---
title: How to Install PHP 5.3.1 on Ubuntu 64 bit and 32 bit
author: Shafiq Alibhai
date: 2010-03-17T07:33:06+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1269438039";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1269438049";}'
categories:
  - Development
tags:
  - PHP
  - Ubuntu

---
## ...yes just 2 lines

### For Ubuntu x64

1) sudo su

2) cd /tmp && mkdir php53 && cd php53 && wget && wget && dpkg -i *.deb && echo "deb <http://php53.dotdeb.org> stable all" >> /etc/apt/sources.list && aptitude update && aptitude install libapache2-mod-php5=5.3.1 apache2

### For Ubuntu 32 bit i386

1) sudo su

2) cd /tmp && mkdir php53 && cd php53 && wget && wget && dpkg -i *.deb && echo "deb <http://php53.dotdeb.org> stable all" >> /etc/apt/sources.list && aptitude update && aptitude install libapache2-mod-php5=5.3.1 apache2
