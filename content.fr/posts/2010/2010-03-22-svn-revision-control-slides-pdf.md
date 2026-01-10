---
lang: "fr"
title: SVN – revision control – slides – pdf
author: Shafiq Alibhai
draft: true
date: 2010-03-22T06:54:55+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1269438320";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1269524195";}'
tagazine-media:
  - 'a:6:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:7:"4390143";s:7:"blog_id";s:7:"4153392";}'
categories:
  - Development
tags:
  - copy
  - Database
  - developer
  - email
  - History
  - IP
  - Management
  - shafiq
  - URL

disableHLJS: false
---
### SVN - contrôle de révision

Coordination de projets

●

Problème : Comment coordonner et synchroniser le code



entre plusieurs développeurs sur un projet ?

– Travailler sur le même ordinateur, alterner les périodes de codage



Non...



– Envoyer les fichiers par e-mail ou les mettre en ligne. Beaucoup



de travail manuel.

– Mettre les fichiers sur un disque partagé. Les fichiers sont écrasés ou



supprimés. Beaucoup de coordination directe.

– En bref : sujet aux erreurs et inefficace.



Qu'est-ce qu'un système de contrôle de version ?

Un dépôt de fichiers avec un accès surveillé pour suivre qui et quoi



les modifications ont été apportées aux fichiers

Suivi des versions



Collaboration et partage de fichiers



Informations historiques



Récupération de versions passées



Gestion des branches



Pourquoi l'utiliser ?

Dans le développement logiciel, un système de contrôle de version est, à l'heure



actuelle, presque obligatoire

Avec plusieurs développeurs, impossible de suivre les versions sans



un tel système

Doit pouvoir revenir à une version antérieure si une suite de tests échoue



Doit pouvoir marquer les versions logicielles



Coordination de projets (solution)

Solution : Un outil de gestion du code source (scm).



– Dépôt : Le code stocké sur un serveur central.



– Copie de travail : Le développeur vérifie une copie du code du dépôt



sur son ordinateur.

– Historique des révisions : Chaque modification de chaque fichier est



enregistrée dans une base de données. Peut être annulée.

– Gestion des conflits : Que se passe-t-il quand deux développeurs modifient



le même fichier ? La même ligne ?

Cycle de travail de base

Vérifier une copie de travail



Mettre à jour une copie de travail



Apporter des modifications



Examiner vos modifications



Valider vos modifications



Quelques commandes

Commandes Subversion communiquant avec le serveur :



svn checkout ...



svn commit



Commandes Subversion hors ligne :



svn add



svn delete



svn status     (comparaison de haut niveau)



svn diff     (comparaison de bas niveau)



svn rename



svn move



...



Plus d'informations :



svn help [cmd]



Créer un dépôt

Création d'un dépôt :



/home/shafiqAlibhai> svnadmin create assignment1



...crée un répertoire dépôt :

/home/shafiqAlibhai/assignment1

Qu'y a-t-il à l'intérieur du dépôt ?



/conf/...



/dav/...



/db/...



/format



/hooks/...



/locks/...



/README.txt



Commandes de base

svn checkout <source>

$ svn checkout <http://url/repos/projectA>

A projectA/file1

A projectA/file2

A projectA/file3

Révision vérifiée 28.

$

svn status

$ svn status

M projectA/file1

?       projectA/file4

$

Commandes de base

svn add/delete/copy/move <filename>

$ svn add file4

A file4

$

svn commit <message>

$ svn commit –m "fix another bugs"

Sending         file1

Adding         file4

Transmission des données du fichier.

Révision validée 29.

$

Commandes de base

svn log

$ svn log

---------------------------

r29 | shafiq | Tue, 26 Dec 2006 18:03:46 +0900 | 1 line

fix another bugs

---------------------------

r28 | shafiq | Mon, 25 Dec 2006 13:01:24 +0900 | 1 line

Fixed some bugs.

---------------------------

r27 | jAlibhai | Mon, 25 Dec 2006 12:58:24 +0900 | 1 line

Some works.

Commandes de base

svn update

$ svn update

U file1

A file4

Mis à jour à la révision 29

$ svn update –r28

U file1

D file4

Mis à jour à la révision 28

$

Trunk, Branches, Tags

Les répertoires d'un projet SVN sont structurés par convention en trois répertoires de niveau supérieur :

trunk/



Représente la « ligne principale » du développement avec une copie complète du projet.

branches/



Contient des sous-répertoires, chacun contenant une copie complète du projet



Chaque branche représente une amélioration significative du projet qui



peut être développée indépendamment.

tags/



Contient des sous-répertoires, chacun contenant une capture instantanée du projet.



Chaque instantané représente une « version publique » ou autre configuration archivée du projet.

Trunk vs. Branch

Le trunk représente la version stable du



système. Elle doit toujours fonctionner, bien sûr.

Les branches représentent des flux de développement temporaires pour implémenter des fonctionnalités importantes.

Cela permet de valider des modifications dans le dépôt sans casser



la version stable (trunk).

Les branches peuvent contenir des erreurs/avertissements, etc.



Questions / Commentaires
