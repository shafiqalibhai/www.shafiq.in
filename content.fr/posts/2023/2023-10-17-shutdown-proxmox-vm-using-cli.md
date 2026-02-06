---
title: "Shutdown Proxmox VM using CLI"
date: 2023-10-17T01:30:03+00:00
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
categories:
    - Development
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
Si vous souhaitez éteindre une machine virtuelle en cours d'exécution sur un environnement virtuel Proxmox (PVE), vous pouvez utiliser l'interface en ligne de commande (CLI) de Proxmox pour accomplir cette tâche de manière efficace. La commande pour éteindre une machine virtuelle sous Proxmox est `qm shutdown`, suivie de l'identifiant de la machine virtuelle que vous souhaitez éteindre. Voici la procédure à suivre :

1. **Accéder au serveur** : Connectez-vous d'abord à votre serveur Proxmox via SSH.

   ```bash
   ssh username@your-proxmox-server-ip
   ```

2. **Trouver l'ID de la VM** : Si vous ne connaissez pas l'ID de la VM, vous pouvez lister toutes les machines virtuelles en exécutant la commande suivante :

   ```bash
   qm list
   ```

   Cette commande affiche une liste des machines virtuelles avec leurs identifiants et leurs états.

3. **Éteindre la VM** : Une fois que vous avez l'identifiant de la VM, utilisez la commande suivante pour éteindre la machine virtuelle de manière propre :

   ```bash
   qm shutdown VM_ID
   ```

   Remplacez `VM_ID` par l'identifiant de la machine virtuelle que vous souhaitez éteindre. Par exemple, si l'identifiant de votre VM est 101, la commande serait :

   ```bash
   qm shutdown 101
   ```

   Notez que `qm shutdown` tente d'éteindre la VM de manière propre, ce qui signifie qu'il envoie un signal de shutdown ACPI au système d'exploitation. Si la VM ne répond pas à ce signal, elle ne sera pas forcément éteinte. Si vous devez forcer l'extinction, vous pouvez utiliser `qm stop VM_ID`, bien que cette opération revienne à retirer la prise électrique et devrait être utilisée uniquement en dernier recours.
