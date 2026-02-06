---
title: Merging Unrelated Git Histories - A Simple Guide
author: Shafiq Alibhai
date: 2018-09-04T13:48:55+00:00
categories:
  - Development

disableHLJS: false
---
Vous êtes bloqué avec deux dépôts Git ou deux branches ayant des historiques complètement différents, mais vous devez les fusionner ? Vous pouvez rencontrer un obstacle car Git est conçu pour empêcher ce type d'opération par défaut. Cependant, il existe une solution de contournement, et elle est plus simple que vous ne le pensez.

### Le Problème : Historiques Git non liés

Imaginez que vous travaillez sur un projet avec une branche `main`, et qu'une autre personne a un projet complètement indépendant, avec son propre historique. Maintenant, vous souhaitez combiner les deux projets dans un seul dépôt. Si vous tentez d'exécuter une fusion `git merge` classique ou un `git rebase`, Git vous empêchera probablement avec un message d'erreur, par exemple :

```
fatal: refusing to merge unrelated histories
```

### La Solution : Autoriser les historiques non liés

La clé pour résoudre ce problème réside dans l'option `--allow-unrelated-histories`. Cette option indique à Git de négliger le fait que les deux branches n'ont pas de base commune et de procéder à la fusion.

Voici un guide étape par étape simple :

1. **Récupérer l'autre dépôt** : Si vous travaillez avec un dépôt séparé, vous devez d'abord le récupérer dans votre dépôt actuel. Vous pouvez le faire avec :

    ```bash
    git remote add other_repo [URL_of_other_repo]
    git fetch other_repo
    ```

2. **Passer à la branche cible** : Assurez-vous d’être sur la branche vers laquelle vous souhaitez fusionner l’historique non lié. Habituellement, il s’agit de votre branche `main` :

    ```bash
    git checkout main
    ```

3. **Effectuer la fusion** : Procédez maintenant à la fusion réelle en utilisant l’option `--allow-unrelated-histories` :

    ```bash
    git merge other_repo/other_branch --allow-unrelated-histories
    ```

4. **Résoudre les conflits** : Si des conflits de fichiers apparaissent, résolvez-les comme d’habitude.

5. **Valider et pousser** : Enfin, validez les modifications et poussez-les vers votre dépôt :

    ```bash
    git commit -m "Merged unrelated histories"
    git push origin main
    ```

Et voilà ! Vous avez fusionné avec succès deux historiques Git non liés.

Bien que ce cas soit rare, il est bon de savoir que vous disposez des outils nécessaires pour accomplir cette tâche quand c’est nécessaire. N’oubliez pas d’utiliser l’option `--allow-unrelated-histories` avec prudence et attention, car elle peut entraîner des modifications importantes dans votre historique Git.
