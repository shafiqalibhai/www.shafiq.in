---
lang: "fr"
title: A Simple Guide to Installing Docker CE on Ubuntu
author: Shafiq Alibhai
date: 2018-09-02T09:09:10+00:00
categories:
  - Development
disableHLJS: false
---
## Ce dont vous avez besoin avant de commencer

### Conditions système requises

Tout d’abord, assurez-vous d’exécuter l’une des versions 64 bits suivantes d’Ubuntu pour installer Docker CE :

* Ubuntu 18.04 (Bionic) - LTS
* Ubuntu 17.10 (Artful)
* Ubuntu 16.04 (Xenial) - LTS
* Ubuntu 14.04 (Trusty) - LTS

Docker CE est compatible avec ces architectures : `x86_64`, `armhf`, `s390x` (IBM Z) et `ppc64le` (IBM Power).

> **Remarque** : Pour les architectures IBM Z et Power, vous devez disposer d’Ubuntu 16.04 (Xenial) ou d’une version ultérieure.

### Adieu le vieux

Si vous avez installé des versions anciennes de Docker, il est préférable de les supprimer d’abord :

```bash
sudo apt-get remove docker docker-engine docker.io
```

Ne vous inquiétez pas si `apt-get` indique que ces paquets n'existent pas. C’est normal. Vos anciens fichiers dans `/var/lib/docker/`, tels que les images et les conteneurs, ne seront pas supprimés.

### Informations sur le pilote de stockage

Docker CE prend en charge les pilotes de stockage `overlay2` et `aufs` sur Ubuntu.

* Pour les versions du noyau Linux 4 ou supérieures, `overlay2` est le choix recommandé.
* Si vous êtes sur une version du noyau Linux 3, choisissez `aufs`.

Si vous devez utiliser `aufs`, une configuration supplémentaire est nécessaire, mais nous n’entrerons pas dans les détails ici.

## Installons Docker CE

### Étapes : Utilisation d’un dépôt

Avant de pouvoir profiter des avantages de Docker CE, vous devez configurer son dépôt. Une fois cela fait, vous pouvez installer ou mettre à jour Docker facilement.

#### Configuration du dépôt Docker

1. Mettez à jour votre liste de paquets :

   ```bash
   sudo apt-get update
   ```

2. Installez les paquets requis :

   ```bash
   sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
   ```

3. Ajoutez la clé GPG de Docker pour les téléchargements sécurisés :

   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   ```

   Vérifiez que la clé possède l’empreinte `9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88` :

   ```bash
   sudo apt-key fingerprint 0EBFCD88
   ```

4. Enfin, ajoutez le dépôt Docker :

   ```bash
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   ```

   > **Remarque** : Si vous êtes aventurier et souhaitez essayer les versions **edge** ou **test**, vous pouvez les ajouter à la commande du dépôt ci-dessus.

#### Installation de Docker CE

1. Mettez à jour votre liste de paquets :

   ```bash
   sudo apt-get update
   ```

2. Installez Docker CE :

   ```bash
   sudo apt-get install docker-ce
   ```

   Si vous souhaitez une version spécifique, listez d’abord les versions disponibles :

   ```bash
   apt-cache madison docker-ce
   ```

   Ensuite, installez la version souhaitée :

   ```bash
   sudo apt-get install docker-ce=<VERSION>
   ```

3. Testez votre installation en exécutant :

   ```bash
   sudo docker run hello-world
   ```

Docker CE devrait maintenant être en cours d’exécution sur votre machine. Au départ, vous devrez utiliser `sudo` pour les commandes Docker. Pour permettre l’accès sans privilèges root, consultez les étapes supplémentaires [dans le guide post-installation Linux](https://docs.docker.com/install/linux/linux-postinstall/).
