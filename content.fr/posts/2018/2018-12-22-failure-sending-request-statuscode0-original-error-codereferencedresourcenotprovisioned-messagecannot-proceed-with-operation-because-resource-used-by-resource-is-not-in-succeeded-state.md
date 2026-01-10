---
lang: "fr"
title: 'Decoding the Error: StatusCode=0 "ReferencedResourceNotProvisioned" in Azure'
author: Shafiq Alibhai
date: 2018-12-22T09:38:39+00:00
categories:
  - Development
disableHLJS: false
---
## Introduction

Si vous travaillez avec Azure, vous avez peut-être rencontré une erreur qui ressemble à ceci :

> « Échec de l’envoi de la requête : StatusCode=0 — Erreur d’origine : Code='ReferencedResourceNotProvisioned' Message='Impossible de poursuivre l’opération car la ressource utilisée n’est pas dans l’état Succeeded. La ressource est en état de Mise à jour et la dernière opération qui a mis à jour ou met à jour la ressource est PutSubnetOperation.' »

Bien que le message d’erreur puisse sembler intimidant et cryptique au premier abord, ne vous inquiétez pas. Dans ce billet, nous allons explorer ce que signifie cette erreur et comment la résoudre.

## Pourquoi cette erreur se produit-elle ?

Le message d’erreur nous indique que l’opération que vous tentez d’exécuter ne peut pas se poursuivre parce qu’une ressource associée est dans l’état « Mise à jour » au lieu de « Réussie ». Cela se produit généralement lorsqu’une opération en cours est en cours sur la même ressource ou une ressource liée, empêchant Azure d’exécuter l’opération que vous avez demandée.

## Une solution concrète

Bien qu’il soit tentant de commencer à déboguer immédiatement, il existe une solution relativement simple à cette erreur. Vous pouvez ajuster le nombre d’opérations simultanées avec l’API Azure en définissant le drapeau `-parallelism`. En le fixant à 1, vous résolvez souvent ce problème :

```bash
terraform apply -parallelism=1
```

## Comment cela fonctionne-t-il ?

En limitant le nombre d’opérations parallèles à 1, vous demandez essentiellement à Azure de se concentrer sur la complétion d’une opération à la fois. Cela permet généralement aux opérations en cours de se terminer, libérant ainsi la ressource pour atteindre un état « Réussi », ce qui résout l’erreur.

Bien que rencontrer des erreurs pendant le développement puisse être frustrant, comprendre ce qui se cache derrière elles et savoir comment les corriger fait partie du parcours. La prochaine fois que vous vous retrouverez face à une erreur `StatusCode=0 "ReferencedResourceNotProvisioned"`, n’oubliez pas d’essayer d’ajuster le drapeau `-parallelism`. C’est une méthode simple mais efficace pour éliminer les obstacles dans vos aventures Azure.
