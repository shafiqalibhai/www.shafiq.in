---
title: A Simple Guide to Installing Both Firefox 4 and Firefox 3 on Ubuntu
author: Shafiq Alibhai
date: 2011-02-07T07:03:39+00:00
categories:
  - Development
tags:
  - Advanced Packaging Tool
  - Browser
  - Firefox
  - Firefox 4.0
  - Mozilla Firefox 4
  - Ubuntu
  - Linux

disableHLJS: false
---
### Étape 1 : Ajouter le dépôt PPA Mozilla Daily

Ouvrez d'abord votre fenêtre de terminal. Une fois celle-ci ouverte, saisissez la commande ci-dessous pour ajouter le dépôt PPA Mozilla Daily Ubuntu à votre système :

```bash
sudo add-apt-repository ppa:ubuntu-mozilla-daily/ppa
```

Vous serez invité à entrer votre mot de passe. Procédez à cette opération, puis appuyez sur Entrée pour confirmer l’ajout du dépôt.

### Étape 2 : Mettre à jour la liste des paquets

Après avoir ajouté le dépôt, il est essentiel de mettre à jour la liste des paquets afin d’obtenir les dernières versions logicielles. Tapez la commande suivante :

```bash
sudo apt-get update
```

### Étape 3 : Installer Firefox 4

Passons maintenant à l’installation elle-même. Pour installer Firefox 4, exécutez la commande suivante dans votre terminal :

```bash
sudo apt-get install firefox-4.0
```

### Étape 4 : Installer Firefox 3

Si vous souhaitez également installer Firefox 3, vous pouvez le faire en exécutant cette commande :

```bash
sudo apt-get install firefox
```

### Étape 5 : Lancer la version de Firefox de votre choix

Une fois les installations terminées, vous pouvez lancer la version de Firefox de votre choix. Vous les trouverez dans votre menu d'applications, ou vous pouvez les lancer directement depuis le terminal en tapant `firefox-4.0` pour Firefox 4 ou `firefox` pour Firefox 3.
