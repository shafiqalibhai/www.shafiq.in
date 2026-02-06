---
title: 'How to Fix the "RPC failed; HTTP 413 curl 22" Error in Nginx'
author: Shafiq Alibhai
date: 2018-10-12T09:49:17+00:00
categories:
  - Development

disableHLJS: false
---
## Comprendre le problème : « RPC failed ; HTTP 413 curl 22 »

Si vous avez rencontré le message d'erreur « RPC failed ; HTTP 413 curl 22 La URL demandée a renvoyé une erreur : 413 Request Entity Too Large », vous essayez probablement de pousser un commit important via HTTP vers votre serveur exécutant Nginx. Cet erreur signifie que la taille de la requête que vous tentez d'envoyer dépasse la limite que le serveur est prêt à accepter. Alors, comment la corriger ?

## Solution Nginx : Mise à jour du fichier de configuration

Ne vous inquiétez pas ; la solution est plus simple qu'elle n'en a l'air. Suivez ces étapes pour éliminer cette erreur :

### Étape 1 : Localiser votre fichier de configuration Nginx

La première chose à faire est de trouver votre fichier `nginx.conf`. Son emplacement peut varier selon votre configuration, mais il se trouve généralement dans `/etc/nginx/nginx.conf`.

### Étape 2 : Modifier le fichier de configuration

Ouvrez le fichier de configuration dans un éditeur de texte de votre choix. Faites défiler jusqu'à trouver l'un des blocs suivants : `http`, `server` ou `location`.

### Étape 3 : Ajouter ou mettre à jour « client_max_body_size »

Insérez la ligne `client_max_body_size 50m;` dans le bloc que vous avez sélectionné. N'hésitez pas à modifier `50m` par la taille maximale qui correspond à vos besoins.

### Étape 4 : Enregistrer et fermer le fichier

Une fois la modification effectuée, enregistrez le fichier et quittez l'éditeur de texte.

### Étape 5 : Recharger la configuration Nginx

Pour vous assurer que Nginx prend en compte votre nouvelle configuration, rechargez le service en exécutant la commande suivante dans votre terminal :

```bash
sudo service nginx reload
```

### Étape 6 : Tester la nouvelle configuration

Passez à nouveau à la poussée de votre commit via HTTP. Si tout s'est bien passé, l'erreur ne devrait plus apparaître.

## Conclusion

Et voilà ! Vous avez augmenté avec succès la limite de taille du corps, résolvant ainsi l'erreur « RPC failed ; HTTP 413 curl 22 ». Bonne programmation !
