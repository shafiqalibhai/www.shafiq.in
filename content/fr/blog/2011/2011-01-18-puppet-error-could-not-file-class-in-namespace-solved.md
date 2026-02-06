---
title: 'Puppet Error – Could not file class in namespace – [solved]'
author: Shafiq Alibhai
date: 2011-01-18T07:03:39+00:00
categories:
  - Development
tags:
  - puppet
  - troubleshooting
  - error
  - configuration

disableHLJS: false
---
## Comment résoudre l'erreur Puppet : Impossible de trouver la classe dans l'espace de noms

Parfois, en travaillant avec Puppet, vous pouvez rencontrer un message d'erreur qui ne reflète pas précisément le problème réel. Par exemple, si vous voyez cet erreur :

err : Impossible de récupérer le catalogue : Impossible de trouver la classe php dans les espaces de noms standardbuild à /etc/puppet/manifests/templates.pp:15 sur domain.internal.com

Une des causes possibles pourrait être un crochet manquant dans votre code. Cela peut être difficile à repérer et peut vous faire perdre beaucoup de temps. Pour éviter cela, assurez-vous de vérifier soigneusement la syntaxe de votre code et utilisez un éditeur de code qui peut vous signaler les erreurs automatiquement.
