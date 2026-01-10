---
lang: "fr"
title: Never use a shared database server for development work.
author: Shafiq Alibhai
date: 2010-09-15T08:39:58+00:00

reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1334973443";}'
categories:
  - Management
tags:
  - Cost
  - Database
  - database server
  - developer
  - shared database
  - Development

disableHLJS: false
---
Comme beaucoup de commodités en développement logiciel, une base de données partagée est un piège à sable attendant de fossiliser un projet. Les développeurs écrasent les modifications les uns des autres. Les modifications que je fais sur le serveur cassent le code sur votre machine de développement. Le développement à distance est lent et difficile. Évitez absolument d'utiliser une base de données partagée, car elles finissent par gaspiller du temps et contribuent à produire des bogues.
