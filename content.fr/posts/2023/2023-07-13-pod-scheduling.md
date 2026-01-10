---
lang: "fr"
title: "How to avoid other pods from being scheduled on your node in Kubernetes"
date: 2023-07-13T11:30:03+00:00
# weight: 1
# aliases: ["/first"]
# tags: ["first"]
author: "Me"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
# description: "Desc Text."
# canonicalURL: "https://canonical.url/to/page"
disableShare: false
disableHLJS: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
categories:
    - Development
# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
# editPost:
#     URL: "https://github.com/<path_to_repo>/content"
#     Text: "Suggest Changes" # edit text
#     appendFilePath: true # to append file path to Edit link
---
Kubernetes est une plateforme puissante pour gérer des applications conteneurisées sur un cluster de nœuds. Cependant, il arrive parfois que vous souhaitiez avoir un contrôle plus fin sur lesquels pods sont planifiés sur quels nœuds, pour diverses raisons telles que les performances, la sécurité ou les coûts.

## Qu'est-ce que les taints et les tolerations ?

Les taints et les tolerations sont une fonctionnalité de Kubernetes qui vous permet de marquer des nœuds avec certains attributs ou conditions, puis de préciser quels pods peuvent ou ne peuvent pas être planifiés sur ces nœuds en fonction de ces attributs ou conditions. Les taints sont appliqués aux nœuds, et les tolerations sont appliquées aux pods.

Un taint se compose de trois composants : une clé, une valeur et un effet. La clé et la valeur sont des chaînes arbitraires que vous pouvez choisir pour identifier le taint. L'effet détermine ce qui se passe avec les pods qui ne tolèrent pas le taint. Il existe trois effets possibles :

- `NoSchedule` : les pods qui ne tolèrent pas le taint ne sont pas planifiés sur le nœud.
- `PreferNoSchedule` : les pods qui ne tolèrent pas le taint sont préférés mais pas garanties à ne pas être planifiés sur le nœud, mais cela n'est pas garanti.
- `NoExecute` : les pods qui ne tolèrent pas le taint ne sont pas planifiés sur le nœud, et tous les pods existants sur le nœud qui ne tolèrent pas le taint sont évacués.

Une toleration se compose de quatre composants : une clé, une valeur, un opérateur et un effet. La clé et la valeur doivent correspondre à celles du taint. L'opérateur peut être soit `Equal`, soit `Exists`. L'effet peut être soit `NoSchedule`, `PreferNoSchedule`, `NoExecute`, soit laisser vide (ce qui signifie tout effet).

Un pod peut tolérer un taint si l'une de ses tolerations correspond au taint selon les règles suivantes :

- Les clés doivent être égales.
- Les valeurs doivent être égales si l'opérateur est `Equal`, ou toute valeur si l'opérateur est `Exists`.
- Les effets doivent correspondre, ou l'effet de la toleration doit être vide.

## Comment utiliser les taints et les tolerations ?

Pour utiliser les taints et les tolerations, vous devez les appliquer à vos nœuds et vos pods à l'aide de commandes kubectl ou de manifestes YAML. Voici quelques exemples de leur utilisation.

### Appliquer un taint à un nœud

Pour appliquer un taint à un nœud, vous pouvez utiliser la commande suivante :

`kubectl taint nodes <nom-du-nœud> <clé>=<valeur>:<effet>`

Par exemple, si vous souhaitez marquer un nœud comme dédié uniquement aux pods de base de données, vous pouvez appliquer un taint avec la clé `type`, la valeur `db` et l'effet `NoSchedule` :

`kubectl taint nodes node1 type=db:NoSchedule`

Cela empêchera tout pod d’être planifié sur node1 à moins qu’il n’ait une toleration correspondante.

### Appliquer une toleration à un pod

Pour appliquer une toleration à un pod, vous pouvez l’ajouter à la spécification du pod sous le champ `tolerations`. Par exemple, si vous souhaitez autoriser un pod de base de données à être planifié sur node1, vous pouvez ajouter une toleration avec la clé `type`, la valeur `db` et l’opérateur `Equal` :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db-pod
spec:
  containers:
  - name: db-container
    image: db-image
  tolerations:
  - key: type
    operator: Equal
    value: db
    effect: NoSchedule
```

Cela permettra au pod de tolérer le taint sur node1 et d’être planifié là-bas.

### Supprimer un taint d’un nœud

Pour supprimer un taint d’un nœud, vous pouvez utiliser la commande suivante :

`kubectl taint nodes <nom-du-nœud> <clé>:<effet>-`

Par exemple, si vous souhaitez supprimer le taint avec la clé `type` et l'effet `NoSchedule` du nœud node1, vous pouvez utiliser :

`kubectl taint nodes node1 type:NoSchedule-`

Cela permettra à nouveau à tout pod d’être planifié sur node1. 

Les taints et les tolerations sont une fonctionnalité utile de Kubernetes qui vous permet de contrôler quels pods sont planifiés sur quels nœuds. Vous pouvez les utiliser pour isoler certains nœuds à des fins spécifiques, telles que les performances, la sécurité ou les coûts. Vous pouvez également les utiliser pour éviter les conflits ou les interférences entre différents types de pods. Pour les utiliser efficacement, vous devez comprendre leur fonctionnement et savoir les appliquer correctement.
