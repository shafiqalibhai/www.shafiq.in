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

disableHLJS: false
---
**Comment installer les fichiers de développement PHP**

Si vous souhaitez exécuter `phpize` sur votre système, vous devez d'abord installer les fichiers de développement de PHP. Sinon, vous risquez d'obtenir un message d'erreur comme celui-ci :

```bash
sh: phpize: not found
ERROR: `phpize' failed
```

Pour installer les fichiers de développement PHP sur Ubuntu/Debian, vous pouvez utiliser la commande suivante dans le terminal :

```bash
apt-get install php5-dev
```

Cela devrait résoudre le problème. 🙂
