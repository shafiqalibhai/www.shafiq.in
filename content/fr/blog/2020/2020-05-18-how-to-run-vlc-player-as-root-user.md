---
title: How to run VLC player as root user
author: Shafiq Alibhai
date: 2020-05-18T09:59:54+00:00
categories:
  - Development

disableHLJS: false
---
```bash
sed -i 's/geteuid/getppid/' /usr/bin/vlc
```

**Explication :** Le script d'initialisation vérifie si l'UID est égal à zéro. Zéro est réservé à l'utilisateur root. Utiliser `sed` pour remplacer `geteuid` par `getppid` trompe le script d'initialisation, car `getppid` est toujours `> 0`.

Bien que l'exécution de VLC en tant que root ne soit pas recommandée, cela fonctionne. Soyez conscient des risques et bien évidemment, ne le faites pas dans des environnements de production.
