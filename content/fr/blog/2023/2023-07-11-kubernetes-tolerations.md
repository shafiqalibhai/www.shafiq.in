---
title: "Kubernetes Tolerations"
date: 2023-07-11T01:30:03+00:00
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
---
Les tolérances Kubernetes sont une manière de permettre à des pods d’être planifiés sur des nœuds possédant des *taints*, qui sont des marqueurs repoussant les pods par défaut. Les tolérances vous permettent de contrôler quels pods peuvent s’exécuter sur quels nœuds, en fonction des besoins du pod et des caractéristiques du nœud.

## Qu’est-ce que les tolérances Kubernetes ?

Les tolérances Kubernetes sont une propriété d’un pod qui permet à ce pod d’être planifié sur un nœud ayant un *taint* correspondant. Les *taints* sont l’inverse de l’affinité de nœud, qui est une manière d’attirer les pods vers un ensemble de nœuds. Les *taints* sont appliqués aux nœuds et agissent comme une barrière répulsive contre les nouveaux pods. Les nœuds *taintés* n’accepteront que les pods marqués d’une tolérance correspondante.

Les tolérances sont spécifiées dans la spécification du pod, sous le champ `tolerations`. Une tolérance se compose de trois composants : une clé, un opérateur et un effet. La clé et l’opérateur sont utilisés pour faire correspondre la tolérance au *taint*. L’effet détermine le comportement du planificateur lorsqu’il rencontre le *taint*.

Il existe trois effets possibles pour les *taints* et les tolérances :

- `NoSchedule` : les pods qui ne tolèrent pas le *taint* ne seront pas planifiés sur le nœud. Les pods déjà en cours d’exécution sur le nœud ne sont pas affectés.
- `PreferNoSchedule` : les pods qui ne tolèrent pas le *taint* seront évités par le planificateur, mais ils pourraient quand même être planifiés sur le nœud s’il n’y a pas d’autre option.
- `NoExecute` : les pods qui ne tolèrent pas le *taint* seront évacués du nœud s’ils sont déjà en cours d’exécution, et ils ne seront pas planifiés sur le nœud à l’avenir.

L’opérateur peut être soit `Equal` soit `Exists`. L’opérateur `Equal` exige que la clé et la valeur du *taint* correspondent exactement à la clé et à la valeur de la tolérance. L’opérateur `Exists` ne requiert que la clé du *taint* corresponde à la clé de la tolérance, indépendamment de la valeur.

Voici un exemple de spécification de pod avec une tolérance :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  tolerations:
  - key: "example-key"
    operator: "Exists"
    effect: "NoSchedule"
```

Ce pod possède une tolérance pour tout *taint* ayant la clé `example-key` et l’effet `NoSchedule`. Cela signifie qu’il peut être planifié sur n’importe quel nœud ayant un tel *taint*, mais il ne tolérera pas d’autres *taints*.

## Comment utiliser les tolérances Kubernetes ?

Pour utiliser les tolérances Kubernetes, vous devez d’abord appliquer des *taints* à vos nœuds. Vous pouvez le faire en utilisant la commande `kubectl taint`. Par exemple, pour appliquer un *taint* ayant la clé `example-key`, la valeur `example-value`, et l’effet `NoSchedule` à un nœud nommé `node1`, vous pouvez exécuter :

```bash
kubectl taint nodes node1 example-key=example-value:NoSchedule
```

Pour supprimer un *taint* d’un nœud, vous pouvez ajouter un `-` à la fin de la commande :

```bash
kubectl taint nodes node1 example-key=example-value:NoSchedule-
```

Vous pouvez également appliquer plusieurs *taints* à un nœud en même temps, ou supprimer plusieurs *taints* à la fois, en les séparant par des espaces :

```bash
kubectl taint nodes node1 example-key=example-value:NoSchedule another-key=another-value:PreferNoSchedule
kubectl taint nodes node1 example-key=example-value:NoSchedule- another-key=another-value:PreferNoSchedule-
```

Pour afficher les *taints* sur vos nœuds, vous pouvez utiliser la commande `kubectl describe` :

```bash
kubectl describe nodes node1
```

Vous devriez voir quelque chose comme ceci dans la sortie :

```text
Name:               node1
Roles:              <none>
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/hostname=node1
Annotations:        <none>
Taints:             example-key=example-value:NoSchedule
                    another-key=another-value:PreferNoSchedule
...
```

Une fois que vous avez appliqué des *taints* à vos nœuds, vous pouvez créer des pods avec des tolérances correspondantes. Vous pouvez le faire en ajoutant le champ `tolerations` à votre spécification de pod, comme montré dans l’exemple précédent. Vous pouvez également utiliser un modèle de pod pour créer plusieurs pods ayant les mêmes tolérances, par exemple dans un déploiement ou un daemonset.

## Cas d’usage des tolérances Kubernetes

Les tolérances Kubernetes peuvent être utilisées dans divers scénarios où vous souhaitez contrôler quels pods peuvent s’exécuter sur quels nœuds, en fonction des besoins du pod et des caractéristiques du nœud. Voici quelques cas d’usage courants pour les tolérances :

- **Isoler des nœuds pour des charges spécifiques** : Vous pouvez avoir certains nœuds dédiés à des types particuliers de charges, comme des applications intensives en GPU, ou du traitement de données sensibles. Vous pouvez *taint* ces nœuds avec une clé et une valeur uniques, et autoriser uniquement les pods ayant une tolérance correspondante à s’exécuter dessus. Ainsi, vous assurez que ces nœuds ne sont pas utilisés par d’autres pods qui n’en ont pas besoin, et que vos charges spéciales ont accès aux ressources dont elles ont besoin.

- **Réserver des nœuds pour des pods à haute priorité** : Vous pouvez avoir certains pods plus critiques que d’autres, comme des composants système ou des pods traitant les requêtes utilisateurs. Vous pouvez *taint* certains nœuds avec une clé et une valeur de haute priorité, et autoriser uniquement les pods ayant une tolérance correspondante à s’exécuter dessus. Ainsi, vous assurez que ces nœuds ne sont pas occupés par des pods à faible priorité pouvant interférer avec les performances ou la disponibilité de vos pods à haute priorité.

- **Éviter les nœuds ayant des problèmes de performance** : Vous pouvez avoir certains nœuds en proie à des problèmes de performance, comme une charge CPU élevée, une pression mémoire ou une congestion réseau. Vous pouvez *taint* ces nœuds avec une clé et une valeur indiquant le problème, et utiliser l’effet `PreferNoSchedule` pour décourager les pods d’être planifiés dessus. Ainsi, vous évitez de surcharger davantage ces nœuds, leur laissant une chance de se rétablir. Vous pouvez également utiliser l’effet `NoExecute` pour évacuer les pods déjà en cours d’exécution sur ces nœuds, si vous souhaitez libérer les ressources plus rapidement.
