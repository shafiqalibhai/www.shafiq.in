---
title: Flash z-order — always on top?
author: Shafiq Alibhai
date: 2009-07-01T07:41:55+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1247977801";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1247977802";}'
categories:
  - Development
tags:
  - embed tag
  - flash movie
  - flash portion
  - IP
  - java
  - JavaScript
  - object tag
  - param name
  - Parameters

disableHLJS: false
---
J'ai eu un problème avec un menu déroulant JavaScript qui se superposait à une vidéo flash. Le menu apparaissait toujours derrière la vidéo flash, quelle que soit l'ordre z. J'ai résolu le problème en :

* Ajoutant le paramètre `<param name="wmode" value="transparent">` dans l'élément OBJECT.
* Ajoutant le paramètre `wmode="transparent"` dans l'élément EMBED.

Ces paramètres ont permis au menu d'afficher correctement au-dessus de la vidéo flash.
