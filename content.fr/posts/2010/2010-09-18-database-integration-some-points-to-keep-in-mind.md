---
title: Database Integration – some points to keep in mind
author: Shafiq Alibhai
date: 2010-09-18T07:19:26+00:00

reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1334973443";}'
categories:
  - Development
tags:
  - Build Management
  - Database
  - Goa
  - IOS
  - IP

disableHLJS: false
---
**Disposez toujours d'une seule source officielle pour votre schéma**  
Tout le monde devrait savoir où se trouve le schéma officiel, et pouvoir obtenir une configuration de base de données fraîche sans aucun obstacle. Une personne devrait pouvoir s’approcher d’un ordinateur, récupérer la dernière version depuis le contrôle de version, construire, puis exécuter un outil simple pour initialiser la base de données (dans de nombreux cas, le processus de construction peut même initialiser la base de données si elle n’existe pas, ce qui raccourcit le processus à une seule étape).

**Toujours versionner votre base de données**  
L’objectif principal est de propager les modifications du développement, vers le test, puis vers la production de manière contrôlée et cohérente. Un deuxième objectif est de pouvoir recréer une base de données à tout moment. Ce deuxième objectif est particulièrement important si vous distribuez des logiciels à des clients. Si quelqu’un découvre un bug dans la version 20100612.1 de votre application, vous devez être en mesure de recréer l’application exactement comme elle était à ce moment-là — base de données comprise.
