---
lang: "fr"
title: Fix casks with `depends_on` that reference pre-Mavericks
author: Shafiq Alibhai
date: 2020-05-18T10:01:16+00:00
categories:
  - Development

disableHLJS: false
---
Si vous obtenez une erreur du type `Error: Cask 'hex-fiend-beta' definition is invalid: invalid 'depends_on macos' value: ":lion"`, où `hex-fiend-beta` peut être n'importe quel nom de cask, et `:lion` n'importe quel nom de version de macOS, exécutez la commande suivante :

```bash
/usr/bin/find "$(brew --prefix)/Caskroom/"*'/.metadata' -type f -name '*.rb' -print0 | /usr/bin/xargs -0 /usr/bin/perl -i -pe 's/depends_on macos: \[.*?\]//gsm;s/depends_on macos: .*//g'
```

Cela supprimera toutes les références `depends_on macos` des casks _installés_.
