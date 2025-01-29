---
title: How to run VLC player as root user
author: Shafiq Alibhai
date: 2020-05-18T09:59:54+00:00
categories:
  - Development

---
```bash
sed -i 's/geteuid/getppid/' /usr/bin/vlc

```

**Explanation:** The initialization script check if the UID is equals to zero. Zero is reserved for the root user. Using `sed` to replace `geteuid` for `getppid` fools the initialization script because it is always `> 0`.

While running the VLC as root is not recommended, it works. Be aware of the risks and obviously do not do it for production environments.
