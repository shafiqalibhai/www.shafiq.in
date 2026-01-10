---
lang: "fr"
title: '[HowTo] Replace ip address using sed'
author: Shafiq Alibhai
date: 2011-06-20T11:38:01+00:00
categories:
  - Development
tags:
  - IP
  - IP address
  - ipad
  - regular expression
  - sed
  - unix

disableHLJS: false
---
La commande suivante recherchera un motif d'adresse IP dans le fichier spécifié et le remplacera par celle fournie :

```bash
sed 's/[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}/**IPADDRESS-COMES-HERE**/g' /SourceFilename > /DestinationFilename
```
