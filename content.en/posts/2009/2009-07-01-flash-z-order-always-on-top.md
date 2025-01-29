---
title: Flash z-order — always on top?
author: Shafiq Alibhai
date: 2009-07-01T07:41:55+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1247977801";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1247977802";}'
categories:
  - Development
tags:
  - embed tag
  - flash movie
  - flash portion
  - IP
  - java
  - JavaScript
  - object tag
  - param name
  - Parameters

---

I had a problem with a javascript pull-down menu that overlapped with a flash movie. The menu always appeared BEHIND the flash movie, regardless of the z-order. I solved it by:

* Adding the parameter `<param name="wmode" value="transparent">` to the OBJECT tag.
* Adding the parameter `wmode="transparent"` to the EMBED tag.

These parameters made the menu display correctly over the flash movie.
