---
title: Replace all dots in filenames except the extension on Linux
author: Shafiq Alibhai
date: 2021-01-21T13:00:41+00:00
categories:
  - Development

---

```bash
for f in .; do pre="${f%.}"; suf="${f##.}"; mv -i -f -- "$f" "${pre//./_}.${suf}"; done
```
