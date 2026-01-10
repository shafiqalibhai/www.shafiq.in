---
lang: "fr"
title: A Simple Guide to Installing SSHPass on Ubuntu and macOS
author: Shafiq Alibhai
date: 2018-09-02T10:33:49+00:00
categories:
  - Development
disableHLJS: false
---
# Introduction

SSHPass est un petit outil pratique qui permet d'automatiser la connexion SSH en contournant la demande de mot de passe habituelle. Bien qu'il soit très pratique pour la création de scripts, il convient de noter qu'il n'est pas idéal pour un environnement multi-utilisateurs en raison de préoccupations liées à la sécurité. Toutefois, si vous l'utilisez sur votre machine de développement personnelle, il est relativement sans danger.

## Comment installer SSHPass sur Ubuntu

L'installation de SSHPass sur Ubuntu est aussi simple que possible. Il vous suffit d'ouvrir votre terminal et d'exécuter la commande suivante :

```bash
sudo apt-get install sshpass
```

## Installation de SSHPass sur macOS

Configurer SSHPass sur un Mac nécessite un peu plus d'efforts car il n'existe pas de version officielle pour macOS. Mais ne vous inquiétez pas, cela n'est pas trop compliqué. Tout d'abord, vous devez avoir Xcode et les outils en ligne de commande installés sur votre système.

### Comment installer avec Homebrew

Malheureusement, le dépôt standard de Homebrew ne propose pas `sshpass`. Toutefois, il existe une formule alternative que vous pouvez utiliser. Ouvrez votre terminal et exécutez la commande suivante :

```bash
brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
```

C'est tout ! Vous avez installé avec succès SSHPass sur votre machine, qu'elle soit Ubuntu ou macOS. Bonne chance avec vos scripts !

Pour plus d'informations, vous pouvez consulter ces ressources utiles :

- [Documentation officielle de SSHPass](http://www.cyberciti.biz/faq/noninteractive-shell-script-ssh-password-provider/)
- [Site officiel de Homebrew](http://brew.sh/)

N'oubliez pas qu' bien que SSHPass soit un outil pratique, il n'est pas le choix le plus sécurisé disponible. Soyez donc vigilant quant à l'endroit et à la manière dont vous l'utilisez.
