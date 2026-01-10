---
lang: "fr"
title: The Art of System Hardening - A Comprehensive Guide
author: Shafiq Alibhai
date: 2013-01-12
categories:
  - Development
tags:
  - System Hardening
  - Database
  - Security
  - Operating Systems
  - Virtual Machine
  - Network Security
disableHLJS: false
---
# [Téléchargez le guide complet sur le renforcement des systèmes](https://www.shafiq.in/wp-content/uploads/2013/01/generic-hardening-doc.docx)

## Introduction au renforcement des systèmes

Le renforcement des systèmes est l'art de renforcer votre environnement informatique contre les menaces potentielles. Au cœur de cette philosophie se trouve l'application du principe du « privilège minimal ». Cela implique :

- De savoir exactement quels services et applications doivent fonctionner sur un système
- De créer une documentation qui décrit les politiques, les normes et les directives
- De configurer en toute sécurité les systèmes d'exploitation, les serveurs virtuels et les logiciels
- De gérer les paramètres des applications afin d'améliorer la sécurité
- De simplifier la configuration et l'installation des bases de données
- De sécuriser les équipements réseau et les périphériques portables

## Pourquoi le renforcement des plates-formes est-il important

Les plates-formes, telles que les serveurs ou les bases de données, constituent la fondation de votre infrastructure de données. Leur intégrité est cruciale pour le transfert sécurisé et fiable de l'information. En tant que bonne pratique, veillez à ce que vos plates-formes soient configurées et entretenues pour repousser les accès non autorisés et les interruptions de service.

## Définitions clés en renforcement des systèmes

- **Système renforcé (H)** : Représente l’état sécurisé que vous visez pour votre système.
- **Renforcement de base du système d'exploitation (Bos)** : Désigne les paramètres de sécurité fondamentaux pour le système d'exploitation.
- **Renforcement des fonctions applicatives/système (Af)** : Concerne les configurations de sécurité pour des applications comme Apache, Oracle, ou des fonctions système spécifiques comme DNS ou DHCP.
- **Renforcement de base (B)** : Il s'agit de la somme du renforcement de base du système d'exploitation et du renforcement des fonctions applicatives/système (B = Bos + Af).
- **Renforcement personnalisé (C)** : Implique des couches de sécurité supplémentaires, telles que les paramètres DMZ, des réglages de sécurité spécifiques, ou des contrôles propres au système d'exploitation comme les TCP Wrappers.
- **Renforcement des systèmes virtuels** : Cela concerne le renforcement des machines virtuelles (VM) elles-mêmes.

## La formule d’un système renforcé

Pour résumer le renforcement des systèmes en termes mathématiques simples, on pourrait dire :

\[
H (Système renforcé) = B (Renforcement de base) + C (Renforcement personnalisé)
\]

Cette équation illustre comment un système renforcé résulte de la combinaison de configurations de sécurité de base avec des couches personnalisées de protection.

## Renforcement des systèmes virtuels

Dans un environnement virtualisé, vous pouvez adapter la formule de renforcement comme suit :

\[
H (Système renforcé) = Vos (Renforcement du système d'exploitation virtuel) + B (Renforcement de base) + C (Renforcement personnalisé)
\]

L’ajout du renforcement du système d'exploitation virtuel reflète la nécessité de sécuriser la machine virtuelle elle-même, en plus des procédures de renforcement de base et personnalisé.
