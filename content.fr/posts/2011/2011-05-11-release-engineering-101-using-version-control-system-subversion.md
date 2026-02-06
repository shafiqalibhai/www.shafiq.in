---
title: A Practical Guide to Release Engineering - Mastering Version Control with Subversion
author: Shafiq Alibhai
date: 2011-05-11T16:38:57+00:00
categories:
  - Development
tags:
  - Apache Subversion
  - Version Control
  - Configuration Management
  - Git
  - Quality Assurance
  - Release Engineering
  - Release Management
  - DevOps Tools

disableHLJS: false
---
Subversion est bien plus qu'un simple outil pour suivre les modifications de votre code. Il peut devenir un pilier d'une stratégie efficace de génie logiciel, en offrant des fonctionnalités qui facilitent la transition fluide du code du développement à la production. Dans cet article, nous allons explorer deux techniques que vous pouvez utiliser : l'utilisation des numéros de révision et la création de balises (*tags*).

La plupart des personnes ayant déjà expérimenté Subversion connaissent les numéros de révision. Imaginons que vous effectuiez un commit et que votre code devienne « révision 1234 ». Vous pouvez alors exporter cette révision spécifique dans votre environnement de développement pour le tester. Une fois qu’elle a passé vos vérifications rigoureuses, elle est envoyée vers l’environnement de qualification (QA) pour une analyse plus approfondie.

Mais que faire si vous souhaitez une méthode plus fiable pour gérer votre base de code ? Voici l’intérêt des « balises » (*tags*).

Les numéros de révision comme « 1234 » sont un peu difficiles à retenir et ne disent pas grand-chose sur le code. Les balises, en revanche, offrent une manière plus humaine d’identifier des versions spécifiques de votre code. Pour créer une balise, vous copiez simplement votre code — par exemple, depuis le répertoire « /trunk/ » vers un nouveau répertoire comme « /tags/release-Jan11_3PM ». Ce qui est génial avec les balises dans Subversion, c’est qu’elles sont faciles à gérer. Vous pouvez en créer autant que nécessaire, par exemple « /tags/build-Jan11_4PM » ou « /tags/version-1.2.3 ».

L’avantage des balises réside dans leurs noms explicites, qui simplifient le processus d’exportation de versions spécifiques vers différents environnements comme Développement, QA ou Production. Cela ajoute non seulement une couche supplémentaire de clarté, mais rend aussi la vie des testeurs et des professionnels de la qualité beaucoup plus facile.

Que vous choisissiez les numéros de révision simples ou la méthode plus descriptive basée sur les balises, Subversion propose des options solides pour gérer votre base de code, du développement à la production. Choisissez la stratégie qui convient le mieux à votre projet et à votre équipe, et éliminez les tracas liés à la gestion des versions.
