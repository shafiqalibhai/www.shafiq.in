---
title: Navigating Terraform Modules Stored in Package Subdirectories
author: Shafiq Alibhai
date: 2018-10-24T13:16:15+00:00
categories:
  - Development
disableHLJS: false
---
Dans le domaine du Infrastructure as Code, les modules Terraform peuvent jouer un rôle important pour simplifier votre travail. Parfois, toutefois, ces modules ne se trouvent pas au niveau du répertoire racine de leur package source. Au contraire, ils sont situés dans des sous-répertoires. Heureusement, Terraform dispose d'une méthode intelligente pour vous aider à accéder à ces modules imbriqués.

Terraform utilise une syntaxe particulière avec deux barres obliques (`//`) pour indiquer précisément le sous-répertoire où se trouve le module. Le chemin qui suit cette syntaxe est considéré comme un sous-répertoire au sein du package ou du dépôt.

Voici quelques exemples pour illustrer ce concept :

* Utilisation du module Consul sur AWS : `hashicorp/consul/aws//modules/consul-cluster`
* Pointage vers un module VPC dans un dépôt Git : `git::https://example.com/network.git//modules/vpc`
* Accès à un module VPC à partir d'un fichier zip : `https://example.com/network-module.zip//modules/vpc`
* Récupération d'un module VPC depuis un bucket S3 : `s3::https://s3-eu-west-1.amazonaws.com/examplecorp-terraform-modules/network.zip//modules/vpc`

Si vous travaillez avec des sources contrôlées par version et que vous devez inclure des arguments comme `ref` pour spécifier une version précise, assurez-vous que le chemin du sous-répertoire précède ces arguments. Par exemple :

* `git::https://example.com/network.git//modules/vpc?ref=v1.2.0`

Une autre chose à noter est que, lorsque vous utilisez cette fonctionnalité, Terraform télécharge l’intégralité du package sur votre machine locale. Toutefois, il n’utilise que le module situé dans le sous-répertoire spécifié. Cela signifie également que si vous avez des modules qui interagissent entre eux au sein du même package, ils peuvent se référencer mutuellement en utilisant des chemins locaux.

Pour plus d'informations, consultez la documentation officielle Terraform sur les [Modules dans des sous-répertoires de package](https://www.terraform.io/docs/modules/sources.html#modules-in-package-sub-directories).

Naviguer dans les sous-répertoires peut sembler une fonctionnalité mineure, mais c’est un outil puissant qui vous aide à maintenir votre code bien organisé tout en tirant pleinement parti des modules externes. Bonne programmation !
