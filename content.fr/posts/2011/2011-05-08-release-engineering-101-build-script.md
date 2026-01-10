---
lang: "fr"
title: Demystifying Release Engineering - A Guide to Build Scripts
author: Shafiq Alibhai
date: 2011-05-07T20:37:16+00:00
categories:
  - Development

disableHLJS: false
---
Lorsqu'il s'agit du développement logiciel, l'une des étapes clés pour s'assurer que votre code se transforme en une application fonctionnelle est le « processus de construction ». Chaque plateforme logicielle, qu'il s'agisse de Unix, de Windows ou d'une autre, propose sa propre manière de scripter ce processus. Vous avez peut-être déjà entendu parler des scripts shell Unix, des fichiers batch Windows ou des fichiers make qui servent de scripts de construction. Ces scripts sont essentiellement une liste de contrôle que l'ordinateur suit pour compiler votre code en un programme exécutable.

Vous vous demandez peut-être : « N'existe-t-il pas une méthode plus universelle pour cela ? » C’est là qu'interviennent des outils comme Apache Ant. Ant permet d’abstraire votre script de construction des détails spécifiques à la plateforme en utilisant un simple fichier XML. Ce fichier XML définit les étapes que doit suivre votre processus de construction. N'allez pas croire qu'Ant est une entité magique. Il s'agit en réalité d'un ensemble de notations XML qui définissent l'ordre des tâches à exécuter. Ces tâches dépendent toujours du code réel, du framework et des binaires SDK pour effectuer le travail lourd.

En bref, peu importe le langage ou la syntaxe que vous choisissez, l'objectif reste le même : automatiser la séquence d'actions nécessaires pour compiler votre code en un logiciel fonctionnel. Que vous soyez un développeur expérimenté ou simplement en train de découvrir le monde de l'ingénierie logicielle, savoir rédiger un script de construction efficace est une compétence que vous ne devriez pas négliger.
