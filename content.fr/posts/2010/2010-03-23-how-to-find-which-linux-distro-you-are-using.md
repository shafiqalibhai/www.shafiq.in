---
lang: "fr"
title: How to Identify Your Linux Distribution and Version with Simple Commands
author: Shafiq Alibhai
date: 2010-03-23T05:10:33+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1269968925";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1269968930";}'
categories:
  - Development
tags:

disableHLJS: false
---
Si vous utilisez un système d'exploitation basé sur Linux et que vous souhaitez connaître la distribution et la version spécifiques que vous avez installées, il existe une commande simple qui peut vous aider. Ouvrez simplement une fenêtre de terminal et saisissez la commande suivante :

```bash
cat /etc/issue
```

Cela affichera le nom et le numéro de version de votre distribution Linux. Par exemple, si vous utilisez Debian 4.0, la sortie ressemblera à ceci :

```bash
Debian GNU/Linux 4.0 \n \l
```

Les caractères spéciaux `\n` et `\l` représentent respectivement la date actuelle et le nom de l'appareil terminal. Ils ne font pas partie du nom de la distribution.

Cette commande fonctionne pour la plupart des distributions Linux, mais certaines peuvent avoir des méthodes différentes ou supplémentaires pour afficher leurs informations. Par exemple, Debian dispose également d'un fichier appelé `/etc/os-release` qui contient des détails plus complets sur la distribution. Vous pouvez afficher son contenu avec cette commande :

```bash
cat /etc/os-release
```

La sortie ressemblera à quelque chose comme ceci :

```bash
PRETTY_NAME="Debian GNU/Linux 4.0 (etch)"
NAME="Debian GNU/Linux"
VERSION_ID="4.0"
VERSION="4.0 (etch)"
ID=debian
```

Vous pouvez également utiliser la commande `hostnamectl` pour obtenir certaines informations sur votre système, telles que la version du noyau, l'architecture ou l'identifiant de machine. Par exemple, pour n'obtenir que la version du noyau, vous pouvez utiliser cette commande :

```bash
hostnamectl | grep Kernel
```

La sortie sera la suivante :

```bash
Kernel: Linux 2.6.18-6-686
```

Pour voir toutes les informations disponibles avec `hostnamectl`, vous pouvez l'utiliser sans arguments, ou lire sa page de manuel avec `man hostnamectl`.
