---
title: 'ERROR: phpize failed [solved]'
author: Shafiq Alibhai
date: 2011-01-17T06:51:05+00:00
categories:
  - Development
tags:
  - FAQs Help and Tutorials
  - PHP
  - Programming
  - Ubuntu

---

**How to install PHP development files**

If you want to run `phpize` on your system, you need to install the development files of PHP first. Otherwise, you might get an error message like this:

```bash
sh: phpize: not found
ERROR: `phpize' failed
```

To install the PHP development files on Ubuntu/Debian, you can use the following command in the terminal:

```bash
apt-get install php5-dev
```

That should solve the problem. 🙂
