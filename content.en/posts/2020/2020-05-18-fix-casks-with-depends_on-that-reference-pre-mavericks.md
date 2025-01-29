---
title: Fix casks with `depends_on` that reference pre-Mavericks
author: Shafiq Alibhai
date: 2020-05-18T10:01:16+00:00
categories:
  - Development

---
If you get an error of the type `Error: Cask 'hex-fiend-beta' definition is invalid: invalid 'depends_on macos' value: ":lion"`, where `hex-fiend-beta` can be any cask name, and `:lion` any macOS release name, run the following command:

```bash
/usr/bin/find "$(brew --prefix)/Caskroom/"*'/.metadata' -type f -name '*.rb' -print0 | /usr/bin/xargs -0 /usr/bin/perl -i -pe 's/depends_on macos: \[.*?\]//gsm;s/depends_on macos: .*//g'
```

This will remove all `depends_on macos` references of _installed_ casks.
