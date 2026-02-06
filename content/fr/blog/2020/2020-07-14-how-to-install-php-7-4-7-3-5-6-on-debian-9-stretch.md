---
title: 'How To Install PHP (7.4, 7.3 & 5.6) on Debian 9 Stretch'
author: Shafiq Alibhai
date: 2020-07-14T09:11:45+00:00
categories:
  - Development
tags:
  - php
  - tutorial
  - debian

disableHLJS: false
---
## Prérequis

Connectez-vous à votre système Debian 9 en utilisant un accès shell. Pour les systèmes distants, connectez-vous via SSH. Les utilisateurs Windows peuvent utiliser Putty ou d'autres applications alternatives pour établir une connexion SSH.

```bash
ssh root@debian9
```

Exécutez les commandes suivantes pour mettre à jour les paquets actuels vers la dernière version.

```bash
sudo apt update 
sudo apt upgrade
```

Exécutons maintenant les commandes suivantes pour installer les paquets requis sur votre système. Ensuite, importez la clé de signature des paquets. Après cela, configurez le PPA pour les paquets PHP sur votre système.

```bash
sudo apt install ca-certificates apt-transport-https 
wget -q https://packages.sury.org/php/apt.gpg -O- | sudo apt-key add -
echo "deb https://packages.sury.org/php/ stretch main" | sudo tee /etc/apt/sources.list.d/php.list
```

Maintenant, utilisez l'une des options ci-dessous pour installer PHP selon vos besoins.

## Installation de PHP 7.4

Vous pouvez également installer la dernière version de PHP sur votre système. Exécutez les commandes suivantes pour installer PHP 7.4 sur Debian 9.

```bash
sudo apt update
sudo apt install php7.4
```

Installez également les modules PHP requis.

```bash
sudo apt install php7.4-cli php7.4-common php7.4-curl php7.4-mbstring php7.4-mysql php7.4-xml
```

## Installation de PHP 7.3

Vous pouvez également installer la dernière version de PHP sur votre système. Exécutez les commandes suivantes pour installer PHP 7.3 sur Debian 9.

```bash
sudo apt update
sudo apt install php7.3
```

Installez également les modules PHP requis.

```bash
sudo apt install php7.3-cli php7.3-common php7.3-curl php7.3-mbstring php7.3-mysql php7.3-xml
```

## Installation de PHP 7.2

Vous pouvez également installer la dernière version de PHP sur votre système. Exécutez les commandes suivantes pour installer PHP 7.2 sur Debian 9.

```bash
sudo apt update
sudo apt install php7.2
```

Installez également les modules PHP requis.

```bash
sudo apt install php7.2-cli php7.2-common php7.2-curl php7.2-mbstring php7.2-mysql php7.2-xml
```

## Installation de PHP 7.1

Si votre application a un besoin spécifique pour PHP 7.1, vous pouvez utiliser les commandes suivantes pour installer PHP 7.1 sur un système Debian 9 Stretch.

```bash
sudo apt update
sudo apt install php7.1
```

Installez également les modules PHP requis selon vos besoins. Voici une liste des modules fréquemment utilisés.

```bash
sudo apt install php7.1-cli php7.1-common php7.1-curl php7.1-mbstring php7.1-mysql php7.1-xml
```

## Installation de PHP 5.6

Exécutez les commandes suivantes pour installer PHP 5.6 sur votre système Debian 9 Stretch.

```bash
sudo apt update
sudo apt install php5.6
```

Installez également les modules PHP requis.

```bash
sudo apt install php5.6-cli php5.6-common php5.6-curl php5.6-mbstring php5.6-mysql php5.6-xml
```
