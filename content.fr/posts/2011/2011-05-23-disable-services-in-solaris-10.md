---
title: Disable services in Solaris 10
author: Shafiq Alibhai
date: 2011-05-23T16:57:14+00:00
categories:
  - Development
tags:
  - bash
  - Grep
  - Hosts (file)
  - Network
  - Puppet
  - Solaris
  - Sun Microsystems
  - unix

disableHLJS: false
---
Pour désactiver un service, vous devez être root ou disposer de privilèges sudo.

Par exemple, pour désactiver le service Puppet, vous exécuteriez la commande suivante :

```bash
svcadm disable network/cswpuppetd:default
```

Cela désactivera le service Puppet et empêchera son exécution.

Pour vérifier que le service a bien été désactivé, vous pouvez exécuter la commande suivante :

```bash
svcs | grep puppet
```

Cela affichera tous les services en cours d'exécution, et si le service Puppet est désactivé, il n'apparaîtra pas dans la liste.

Voici quelques conseils supplémentaires pour désactiver des services :

- Vous pouvez utiliser l'option `-s` avec la commande `svcadm disable` pour désactiver le service de manière synchrone. Cela signifie que la commande ne retournera pas avant que le service n'ait été entièrement désactivé.
- Vous pouvez utiliser l'option `-T` avec la commande `svcadm disable` pour spécifier un délai d'attente en secondes. Cela signifie que la commande ne retournera pas avant que le service n'ait été désactivé ou que le délai d'attente n'ait été atteint.
- Si vous souhaitez désactiver un service temporairement, vous pouvez utiliser la commande `svcadm disable -t`. Cela désactivera le service, mais il pourra être redémarré en exécutant la commande `svcadm enable`.
