---
title: '[solved] xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist'
author: Shafiq Alibhai
date: 2018-09-06T09:43:25+00:00
categories:
  - Development

disableHLJS: false
---
Erreur :

xcrun : erreur : chemin du développeur actif ("/Applications/Xcode.app/Contents/Developer") n'existe pas  
Utilisez `sudo xcode-select --switch chemin/Vers/Xcode.app` pour spécifier l'Xcode que vous souhaitez utiliser pour les outils de développement en ligne de commande, ou utilisez `xcode-select --install` pour installer les outils de développement en ligne de commande autonomes.  
Voir `man xcode-select` pour plus de détails.  
xcrun : erreur : chemin du développeur actif ("/Applications/Xcode.app/Contents/Developer") n'existe pas  
Utilisez `sudo xcode-select --switch chemin/Vers/Xcode.app` pour spécifier l'Xcode que vous souhaitez utiliser pour les outils de développement en ligne de commande, ou utilisez `xcode-select --install` pour installer les outils de développement en ligne de commande autonomes.  
Voir `man xcode-select` pour plus de détails.

Solution :

**sudo xcode-select -reset**
