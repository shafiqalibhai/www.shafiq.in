---
lang: "fr"
title: Juniper Hardening Procedure
author: Shafiq Alibhai
date: 2012-12-03T08:23:05+00:00
draft: true
publicize_twitter_user:
  - shafiqalibhai
publicize_reach:
  - 'a:3:{s:7:"twitter";a:1:{i:1937780;i:137;}s:2:"fb";a:1:{i:1937778;i:171;}s:2:"wp";a:1:{i:0;i:9;}}'
categories:
  - Development
tags:
  - administrator
  - Browser
  - Business
  - cp
  - Harden
  - implementation
  - IP
  - IP address
  - logs
  - Management
  - Network
  - promise
  - Requirement
  - sed
  - URL

disableHLJS: false
---
<h1 class="western" style="margin-left:.95cm;text-indent:-.95cm;margin-top:.21cm;margin-bottom:0;page-break-before:auto;page-break-after:auto;">
  <a href="/wp-content/uploads/2012/12/juniper-device-hardening-1.pdf">TÉLÉCHARGER - Renforcement des dispositifs Juniper</a>

<h1 class="western" style="margin-left:.95cm;text-indent:-.95cm;margin-top:.21cm;margin-bottom:0;page-break-before:auto;page-break-after:auto;">
  <span style="colour:#17365d;"><span style="font-family:Verdana, sans-serif;"><span style="font-size:large;">Introduction

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Raisonnement

<p class="western" style="margin-top:.21cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Une implémentation de pare-feu « hors boîte » n’est pas entièrement sécurisée et doit être renforcée. Ce document détaille les différents aspects de sécurité des pare-feux Juniper et des normes mises en œuvre pour sécuriser les pare-feux Juniper.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Objectif

<p class="western" style="margin-top:.21cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Ce document a pour objectif de définir une norme de base de sécurité pour les implémentations de pare-feux Juniper par les administrateurs de pare-feux.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Portée

<p class="western" style="margin-top:.21cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Ces normes de sécurité couvrent l’implémentation Screen OS du pare-feu Juniper.

<p class="western" style="margin-top:.21cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Toutefois, pour certaines configurations, ces exigences minimales et certaines fonctionnalités de ces normes peuvent ne pas être pratiques à mettre en œuvre. Pour les exceptions, les administrateurs système doivent documenter les raisons pour lesquelles elles ne respectent pas pleinement ces normes et demander une exemption au département de sécurité.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Public cible

<p class="western" style="margin-top:.21cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Les administrateurs de pare-feux ont la responsabilité principale de mettre en œuvre ces normes. Lors de leurs revues et inspections, les auditeurs doivent utiliser ce document pour vérifier le respect des normes.

<p class="western" style="margin-top:.21cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Les gestionnaires commerciaux peuvent lire les raisons derrière chaque point des normes afin de mieux comprendre l’importance de les appliquer à leurs environnements.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Mise en œuvre

<p class="western" style="margin-top:.21cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Les administrateurs de pare-feux Juniper doivent utiliser ces normes pour établir les procédures d’installation et d’exploitation.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;page-break-before:always;">
  <span style="font-family:Verdana, sans-serif;">Aperçu de la sécurité des pare-feux Juniper

<p style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Cette section donne un bref aperçu des différents aspects de la sécurité des pare-feux Juniper. Les détails du renforcement pour chaque aspect sont présents dans les sections suivantes du document.

<p style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’environnement de sécurité opérationnel du pare-feu Juniper comprend divers aspects :

* <p style="margin-top:.21cm;">
      <span style="font-family:Verdana, sans-serif;">Configuration initiale du dispositif et de Screen OS

* <p style="margin-top:.21cm;">
      <span style="font-family:Verdana, sans-serif;">Configuration du dispositif

* <p style="margin-top:.21cm">
      <span style="font-family:Verdana, sans-serif;">Gestion du dispositif

* <p style="margin-top:.21cm">
      <span style="font-family:Verdana, sans-serif;">Gestion des utilisateurs

* <p style="margin-top:.21cm">
      <span style="font-family:Verdana, sans-serif;">Services

* <p style="margin-top:.21cm">
      <span style="font-family:Verdana, sans-serif;">Accès au système

* <p style="margin-top:.21cm">
      <span style="font-family:Verdana, sans-serif;">Journalisation et surveillance du système

* <p style="margin-top:.21cm">
      <span style="font-family:Verdana, sans-serif;">Journalisation et surveillance des politiques

<h1 class="western" style="margin-left:.95cm;text-indent:-.95cm;margin-top:.21cm;margin-bottom:0;page-break-before:auto;page-break-after:auto;">
  <span style="colour:#17365d;"><span style="font-family:Verdana, sans-serif;"><span style="font-size:large;">Configuration du dispositif et de Screen OS

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">La sécurité du pare-feu Juniper Screen OS débute par une configuration sécurisée. Les facteurs influant sur cela incluent l’utilisation de la version correcte de Screen OS.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:150%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Identifier correctement le dispositif pour prévenir les manipulations physiques

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’emballage extérieur ne doit pas présenter de dommages, ni de preuve que des personnes non autorisées l’ont ouvert. Si le carton présente des dommages qui permettraient au dispositif d’être déballé ou échangé, cela pourrait être une preuve de manipulation.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Chaque boîte emballée arrive avec un ruban personnalisé pour indiquer que Juniper ou un fabricant autorisé a emballé le dispositif. Le ruban est unique ; le mot « Juniper » est imprimé répétitivement tout au long du ruban. Si le ruban n’est pas présent, cela pourrait être une preuve de manipulation.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’emballage intérieur ne doit pas présenter de dommages ou de preuve de manipulation. Le sac en plastique ne doit pas avoir de grand trou et l’étiquette qui scelle le sac en plastique ne doit pas être détachée ou manquante. Tout dommage au sac ou à l’étiquette pourrait être une preuve de manipulation.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:150%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Vérifier la version correcte du matériel et du logiciel

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour vérifier que le produit reçu est la version correcte du matériel et du logiciel, exécutez la commande suivante depuis l’interface CLI :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><i><b>get system</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">La sortie de cette commande inclut deux éléments clés : la version du matériel et la version du logiciel. Les versions du matériel et du logiciel doivent correspondre à la cible de sécurité commune pour être pleinement conformes à la configuration évaluée selon les critères communs.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les pare-feux sont livrés avec le logiciel Screen OS pré-installé. Toutefois, les versions du logiciel Screen OS installées sur les dispositifs peuvent varier en fonction de l’époque de fabrication des appareils de sécurité.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:150%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Mise à jour d’un pare-feu Juniper

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Il faut charger l’image correcte du logiciel Screen OS sur l’appareil de sécurité.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Avant de pouvoir charger l’image du logiciel Screen OS, configurez l’interface de gestion par laquelle les images peuvent être téléchargées depuis le serveur FTP vers les appareils de sécurité. Les commandes suivantes permettent de configurer la zone et l’adresse IP pour l’interface de gestion.

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set interface </b><i>interface-name </i><b>zone </b><i>trust

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set interface </b><i>interface-name </i><b>ip </b><i>ip-address

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><i>Note : Le nom de l’interface doit être le nom de l’interface réelle connectée à l’ordinateur servant de pare-feu FTP ; à travers cette interface, les appareils de sécurité peuvent communiquer avec le pare-feu FTP. Pour les appareils de série 5, l’interface <b>trust – </b>liée par défaut à la zone de sécurité <b>trust </b>peut être utilisée. Pour les appareils Juniper NetScreen-204 et 208, vous pouvez utiliser l’interface <b>ethernet1</b>. Pour les appareils Juniper NetScreen-500, l’interface ethernet1/1 dans la zone de sécurité <b>trust </b>peut remplacer l’interface-name. Sur les appareils de sécurité haut de gamme, y compris Juniper NetScreen-ISG2000 et ISG1000, l’interface peut utiliser ethernet1/1. Juniper NetScreen-5200 et NetScreen 5400 peuvent utiliser l’interface ethernet2/1.</i>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’adresse <i>ip-address </i>doit être une adresse IP valide, qui peut être dans le même sous-réseau ou dans un sous-réseau différent du pare-feu TFTP.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Une fois configuré, utilisez les commandes suivantes pour télécharger l’image Screen OS depuis le pare-feu FTP vers l’appareil de sécurité :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>save software from tftp </b><i>tftp-firewall-ip Screen OS-image </i><b>to flash</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">où <i>tftp-firewall-ip </i>est l’adresse IP de l’ordinateur servant de pare-feu TFTP où se trouvent les images logicielles Screen OS et <i>Screen OS-image </i>est le chemin relatif vers le fichier d’image logicielle Screen OS et le nom du fichier lui-même.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Par exemple, si l’image Screen OS pour l’appareil Juniper NetScreen-5GT est « ns5gt.5.4.0r4.0 » et se trouve sur le pare-feu FTP (avec l’adresse IP 10.155.95.253), dans le répertoire /tftpboot/screen OS-image/5.4/, la commande doit être la suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>save software from tftp </b><i>10.155.95.253 /tftpboot/screen OS-image/5.4/ns5gt.5.4.0r4.0 </i><b>to flash</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Le processus de téléchargement prendra quelques minutes. Une fois le processus de téléchargement terminé, l’appareil de sécurité reviendra à l’invite CLI et nécessitera un redémarrage. Émettez la commande <b>reset </b>et fournissez les réponses aux questions ci-dessous pour charger complètement l’image sur l’appareil de sécurité et restaurer les configurations d’usine par défaut.

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>reset</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>Configuration modifiée, sauvegarder ? [y]/n n</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>Redémarrage du système, êtes-vous sûr ? y/[n] y</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’appareil de sécurité reviendra à l’invite de connexion. À ce stade, l’appareil de sécurité a été complètement chargé avec la version correcte du logiciel Screen OS.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:150%;page-break-inside:auto;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;">Mises à jour de Screen OS

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Mettez à jour les pare-feux Screen OS avec les mises à jour recommandées par le fournisseur, dans le cadre de chaque trimestre.

<h1 class="western" style="margin-left:.95cm;text-indent:-.95cm;margin-top:.21cm;margin-bottom:0;page-break-before:auto;page-break-after:auto;">
  <span style="colour:#17365d;"><span style="font-family:Verdana, sans-serif;"><span style="font-size:large;">Configuration du dispositif

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Restaurer les paramètres par défaut </b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Restaurez le pare-feu à son mode opérationnel et configurations d’usine par défaut avant de mettre l’appareil dans un mode opérationnel différent, y compris le mode authentifié transparent (aussi appelé mode VPN transparent) ou le mode NAT/Route authentifié (aussi appelé mode VPN NAT/Route) ou avant d’effectuer toute configuration pour un test spécifique.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Utilisez les commandes <b>unset all </b>et <b>reset </b>avec les réponses suivantes pour restaurer le mode opérationnel et les configurations par défaut pour l’appareil.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">unset all

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Erase all system config, are you sure y/ [n]? Y

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">reset

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configuration modified, save? [y]/n n

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">System reset, are you sure? y/[n] y

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">set clock mm/dd/yyyy hh:mm

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">get system

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">"System in NAT/Route mode" indique qu’il fonctionne en mode NAT/Route

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">"System in transparent mode" indique qu’il fonctionne en mode transparent

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Tous les appareils de sécurité sont, par défaut, configurés en mode NAT/Route sans VPN.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour garantir que l’appareil de sécurité est en mode conforme aux critères communs EAL4 évalués, suivez l’une des trois séquences suivantes selon la configuration souhaitée :

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Mode NAT/Route non authentifié

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Mode NAT/Route authentifié

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">VPN basé sur le routage

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">VPN basé sur la politique

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Mode transparent authentifié

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Mode NAT/Route authentifié

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configurez le pare-feu en mode NAT/Route authentifié en utilisant un VPN basé sur le routage ou un VPN basé sur la politique. Vous pouvez configurer les deux, un VPN basé sur le routage et un VPN basé sur la politique, en mode NAT/Route authentifié.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Seul la clé manuelle est prise en charge dans la configuration évaluée, c’est-à-dire que la clé automatique ne peut pas être utilisée. Faites attention à sélectionner les valeurs de clé manuelle de manière à ce qu’elles suivent les mêmes règles que les mots de passe administrateurs. Distribuez les clés manuelles en utilisant une méthode sécurisée afin de garantir qu’elles ne sont pas accessibles publiquement.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">VPN basé sur le routage

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configurez l’appareil de sécurité correspondant avec un VPN basé sur le routage en mode NAT/Route authentifié.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">VPN basé sur la politique

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configurez l’appareil de sécurité correspondant avec un VPN basé sur la politique en mode NAT/Route authentifié.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Convention de nommage du pare-feu

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pare-feux de branche : (Convention de nommage non définie)

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pare-feux du centre de données : (Convention de nommage non définie)

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configuration des options d’écran

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les appareils de sécurité doivent empêcher tous les types d’attaques de type déni de service (DoS) et de signatures d’attaques sur chaque zone de sécurité pour éviter que ces types d’attaques se produisent sur le réseau.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour afficher les options d’écran par défaut pour une zone de sécurité spécifique, exécutez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>get zone zone-name screen</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Par défaut, les options d’écran activées pour la zone de sécurité Untrust/V1-Untrust (et les interfaces dans la zone Untrust/V1-Untrust) dans Screen OS 5.0 :

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Protection contre les attaques de type Tear-drop : activée

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Protection contre les attaques de type SYN Flood (200) : activée

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Seuil d’alarme : alarm-threshold

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Taille de file d’attente : Q-size

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Valeur d’expiration : 20

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Seuil source : src-threshold

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Seuil de destination : dst-threshold

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Supprimer MAC inconnu (mode transparent uniquement) : désactivé

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Protection contre les attaques Ping-of-Death : activée

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Filtre des options IP de route source : activé

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Protection contre les attaques Land : activée

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les seuils d’alarme, Q-size, src-threshold et dst-threshold sont dépendants de la plateforme, comme indiqué dans le tableau ci-dessous.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour les zones de sécurité Trust/V1-Trust et DMZ/V1-DMZ (et les interfaces dans les zones Trust et DMZ), aucune option d’écran n’est activée par défaut.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Fonction d’écran ne générant que des alarmes sans supprimer les paquets : désactivée

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver toutes les options d’écran par défaut pour la zone Untrust/V1-Untrust, les commandes suivantes sont utilisées :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset zone untrust screen tear-drop</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset zone untrust screen syn-flood</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset zone untrust screen ping-death</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset zone untrust screen ip-filter-src</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Lorsque la zone de sécurité n’a pas d’options d’écran activées, le message suivant s’affiche :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>"Screen function only generate alarm without dropping packet: OFF"</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">La commande CLI suivante active tous les écrans par zone (et est appliquée à toutes les interfaces de cette zone) :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen block-frag</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen component-block</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen fin-no-ack</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen icmp-flood</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen icmp-fragment</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen icmp-large</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-bad-option</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-filter-src</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-loose-src-route</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-record-route</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-security-opt</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-spoofing</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-stream-opt</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-strict-src-route</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-sweep</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-timestamp-opt</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen land</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen limit-session</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen mal-url code-red</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ping-death</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen port-scan</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen syn-ack-ack-proxy</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen syn-fin</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen syn-flood</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen syn-frag</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen tcp-no-flag</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen tear-drop</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen udp-flood</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen unknown-protocol</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen winnuke</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les commandes ci-dessus doivent être exécutées pour les zones internes et externes (c’est-à-dire Trust et Untrust) afin de protéger les réseaux internes et externes. Lorsque l’appareil de sécurité fonctionne en mode NAT/Route, exécutez les commandes ci-dessus pour les zones de sécurité Trust et Untrust.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Lorsque l’appareil de sécurité fonctionne en mode « transparent », (y compris le mode transparent authentifié), exécutez les commandes ci-dessus pour les zones de sécurité V1-Trust et V1-Untrust.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Vous devez exécuter les mêmes commandes (comme indiqué ci-dessus) pour chaque zone de sécurité supplémentaire.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Lorsque l’appareil de sécurité fonctionne en mode NAT/Route (y compris le mode NAT/Route non authentifié et le mode NAT/Route authentifié), activez le rejet des paquets sans adresse IP source ou ayant une adresse IP source non routable en utilisant la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone zone-name screen ip-spoofing drop-no-rpf-route</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">« zone-name » est le nom de la zone de sécurité telle que Trust ou Untrust.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Par exemple, lorsque le pare-feu fonctionne en mode NAT/Route, pour activer la fonctionnalité de rejet des paquets pour la zone de sécurité trust et untrust, émettez les commandes suivantes :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone trust screen ip-spoofing drop-no-rpf-route</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set zone untrust screen ip-spoofing drop-no-rpf-route</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Assurez-vous d’exécuter la même commande (comme indiqué ci-dessus) pour toute zone de sécurité de couche 3 utilisée. Lorsque vous modifiez l’option de blocage HTTP, les modifications ne s’appliquent qu’aux sessions créées après la mise en œuvre de cette option de blocage.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configuration de la protection contre les falsifications IP

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configurez la protection contre les falsifications IP en utilisant l’option d’écran « ip-spoofing » comme indiqué ci-dessus dans la section « Configuration des options d’écran ». Cela inclut les configurations intrazone où le trafic VPN se trouve dans la même zone que le trafic déchiffré. Toutefois, selon la configuration mise en œuvre (en particulier les configurations interzone), les étapes suivantes sont nécessaires pour être adéquatement protégé contre les attaques de falsification IP.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les directives suivantes pour les modes Authentifié NAT/Route et Authentifié Transparent doivent compléter les directives fournies dans la section précédente « Définition d’une politique pour autoriser le trafic ».

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’option d’écran « IP-Spoofing » est ignorée – un ensemble d’adresses et de politiques doit être défini pour autoriser uniquement le trafic autorisé, en excluant les adresses IP falsifiées.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Lorsque le pare-feu fonctionne en mode Authentifié NAT/Route ou Authentifié Transparent, l’option d’écran « IP-Spoofing » est « ignorée ». Par conséquent, définissez un ensemble d’adresses et de politiques pour autoriser le trafic, en excluant les adresses IP falsifiées.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Gestion du dispositif

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Cette section fournit des détails sur la sécurisation des aspects de gestion du dispositif de pare-feu.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Sécurisation du trafic administrateur sur le dispositif

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Quatre étapes sont nécessaires pour sécuriser le trafic administrateur du dispositif :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">a) Définir l’adresse IP autorisée pour l’adresse IP du client administrateur

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">b) Définir les options spécifiques à l’interface

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">i) Définir l’adresse IP de gestion pour les interfaces

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">ii) Désactiver les services de gestion inutiles

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">c) Changer les numéros de port pour les services administrateurs

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Désactiver les commandes internes

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’administrateur du pare-feu doit désactiver les commandes internes. L’utilisation des commandes internes s’applique uniquement à des fins de dépannage et de débogage.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver les commandes internes, vous devez exécuter la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set common-criteria no-internal-commands</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour utiliser les commandes internes (par exemple, « debug flow basic » et « get dbuf stream », « debug ids sat ») à des fins de dépannage et de débogage, utilisez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset common-criteria no-internal-commands</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Note : Utilisez les commandes internes « debug ids sat » pour ISG-1000, ISG-2000, NS-5200 et NS-5400.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Désactiver Telnet pour la gestion du dispositif

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’utilisation de Telnet est déconseillée sur les pare-feux Juniper. Utilisez SSH, version 2.0, pour gérer le pare-feu Juniper :

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour ce faire :

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Désactiver Telnet sur l’interface de gestion

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Activer SSH

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Contrôle des réinitialisations matérielles non autorisées

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver la récupération via la connexion, utilisez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset admin device-reset</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver la récupération via le trou, utilisez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset admin hw-reset</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Lorsqu’elles sont désactivées, les administrateurs du pare-feu doivent activer la réinitialisation correspondante afin d’effectuer toute activité nécessitant un redémarrage du pare-feu.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Restriction de l’accès à distance

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’accès à la gestion doit être limité au port de console connecté localement, plutôt que aux paramètres par défaut d’usine.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour limiter l’accès à la gestion au port de console, l’interface qui est par défaut dans la zone de sécurité V1-Trust ou Trust doit avoir l’accès à la gestion désactivé.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Toutes les autres interfaces ont l’accès à la gestion désactivé par défaut.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver la gestion de l’interface, émettez la commande CLI suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset interface interface-name manage</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Gestion des utilisateurs

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les administrateurs des appareils de sécurité doivent choisir des noms d’utilisateur et des mots de passe qui non seulement ont une longueur d’au moins huit caractères et utilisent autant de types de caractères que possible. Il est nécessaire de mélanger les lettres minuscules et majuscules pour assurer une protection adéquate. En outre, les noms d’utilisateur et les mots de passe faciles à deviner ne sont pas sécurisés.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les appareils de sécurité sont livrés avec un nom d’utilisateur et un mot de passe par défaut de « netscreen ». Changez le mot de passe par défaut dès que possible pour empêcher l’accès non autorisé.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">La durée recommandée entre les changements de mot de passe est de 30 jours maximum pour atténuer les effets d’une identité d’administrateur compromise.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Définition/Changement des restrictions de longueur du mot de passe

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour garantir que les mots de passe de huit caractères ou plus sont toujours utilisés, vous devez d’abord définir la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin password restrict length password-length</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">où password-length est une valeur décimale égale ou supérieure à 8 et inférieure ou égale à 31. Elle doit également suivre la politique de mot de passe.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Définition/Changement du nom d’administrateur et du mot de passe

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les commandes CLI suivantes, dans l’ordre, sont nécessaires pour définir un nouveau nom d’administrateur et un mot de passe :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin name name-string</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin password password-string</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">où name-string et password-string doivent être remplacés par le nom d’utilisateur réel et le mot de passe de l’administrateur.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Gestion des politiques

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Supprimer la politique par défaut autorisant

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Le pare-feu pourrait avoir une politique par défaut autorisant le trafic traversant le dispositif depuis l’interface dans la zone Trust vers l’interface dans la zone Untrust. Supprimez cette politique par défaut pour éviter une autorisation involontaire de l’information traversant le dispositif. Utilisez la commande CLI :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset policy id 1</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Journalisation du trafic refusé

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Par défaut, l’appareil de sécurité rejette tout trafic qui ne correspond à aucune politique « autorisée ». Par conséquent, ajoutez une politique à la fin de la liste des politiques afin de journaliser le trafic refusé qui ne correspond à aucune politique :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from scr-zone to dst-zone any any any deny log</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">... où pol-id est l’ID de la politique, scr-zone et dst-zone sont respectivement la zone source d’où le trafic provient et la zone de destination vers laquelle le trafic arrive.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour chaque zone de sécurité qui a une interface réseau attribuée, ajoutez les politiques ci-dessus à la fin des tables de politique afin de garantir que le journal des paquets rejetés est conservé.

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from trust to untrust any any any deny log count</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from untrust to trust any any any deny log count</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from trust to dmz any any any deny log count</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from dmz to trust any any any deny log count</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">... 

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Définition d’une politique pour autoriser le trafic

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Deux étapes importantes à suivre lors de la création d’une politique de sécurité :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Activer le comptage et la journalisation pour maintenir les informations de journal d’audit pour le trafic passant à travers le dispositif.

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Doit être spécifique pour garantir que le trafic autorisé est intentionnel et non inclus dans une politique générale.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Utilisez une adresse IP source spécifique (src-addr), une adresse IP de destination (dst-addr), une zone source (src-zone), une zone de destination (dst-zone), un protocole et un service (servicename) si possible. Un exemple où il peut ne pas être pertinent d’être spécifique est pour le trafic destiné à un réseau externe pour un accès web général.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Après avoir créé et configuré les adresses source et de destination, configurez la politique avec le comptage et la journalisation en utilisant la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id id-num from src-zone to dst-zone src-addr dst-addr servicename</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">action log count

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">... où « id-num » est le nombre décimal représentant l’ID de la politique et « action » peut être « permit » pour autoriser un service spécifique à passer de l’adresse source à travers l’appareil de sécurité vers l’adresse de destination ; ou « deny » pour bloquer le service qui passe à travers l’appareil de sécurité.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Ordre des politiques

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’ordre des politiques est important, car les politiques correspondent dans l’ordre en commençant par la première dans la liste des politiques et en se déplaçant à travers la liste. La première politique correspondante s’applique au trafic réseau pour déterminer l’action à effectuer. Par défaut, une nouvelle politique créée apparaît à la fin de la liste des politiques.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Il existe une option qui permet de positionner une politique au sommet de la liste plutôt que de laisser la politique apparaître à la fin. Dans l’interface CLI, ajoutez le mot-clé « top » à la commande « set policy » :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>For example,</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id 6 top from trust to untrust trust-HostA untr-NetworkB http</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>permit log</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">La politique nouvellement créée peut également être positionnée à n’importe quel emplacement dans la liste des politiques en utilisant l’option de mot-clé « before » à la commande CLI « set policy » :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>For example:</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id 4 before 98 from untrust to trust untr-NetworkB trust-HostA ftp</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>permit log</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Si des politiques globales sont utilisées, remplacez la politique ci-dessus qui s’exécute avant toute politique globale. Une politique globale de refus peut être utilisée qui doit être ajoutée à la fin de la liste des politiques globales :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy global id pol-id any any any deny log count</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Journalisation et surveillance du système

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configurer Syslog

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Vous devez configurer un pare-feu Syslog comme sauvegarde pour les informations d’audit et le stockage à long terme des journaux d’audit. Cela aidera à prévenir la perte d’informations d’audit.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les commandes spécifiques nécessaires pour configurer un pare-feu Syslog sont :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog config ip-address facilities local0 local0</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog config ip-address port 514</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog config ip-address log traffic</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog enable</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set log module system level level-name destination syslog</b>

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">où ip-address est l’adresse IP réelle du pare-feu Syslog et level-name est le niveau de gravité du journal.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Note : Vous devez entrer la commande set log une fois pour chaque niveau de message.

<p class="western" style="margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les options pour level-name sont listées ci-dessous :

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>emergency</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>alert</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>critical</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>error</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>warning</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>notification</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>information</b>

<p class="western" style="margin-left:1.27cm;margin-top:.21cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>debugging</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.21cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Événements à journaliser

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les journaux du système contiennent les événements historiques du pare-feu et les informations d’utilisation, utilisées pour le débogage des dysfonctionnements du système et les enquêtes pénales. Par conséquent, journalisez toutes les informations critiques.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configurez Syslog pour journaliser les éléments suivants sur chaque pare-feu :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Chaque connexion et déconnexion

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Démarrage et arrêt du pare-feu

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Session complète

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Administration des comptes utilisateurs et groupes

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Défaillances matérielles

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Rétention et archivage des journaux

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Il arrive souvent qu’il soit nécessaire d’obtenir une traçabilité complète d’un processus pour des investigations de sécurité ou des buts de dépannage. Par conséquent, conservez localement les journaux du pare-feu pendant un nombre défini de jours. Il doit y avoir suffisamment d’espace de stockage alloué pour gérer cela. En outre, il doit y avoir un contrôle d’accès très strict mis en œuvre sur les journaux stockés.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les fichiers de journal doivent être archivés hors ligne. Protégez adéquatement les journaux archivés afin que les utilisateurs non autorisés n’y aient pas accès.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Protection des fichiers de journal

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Si un utilisateur malveillant parvient à modifier les fichiers de journal et à supprimer les traces d’attaque, aucune enquête ne pourra être concluante. En outre, le journal étendu pour la traçabilité d’audit. Par conséquent, protégez les fichiers de journal contre toute manipulation et stockez-les en toute sécurité.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Journaux d’activité des utilisateurs privilégiés

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les utilisateurs privilégiés ont un contrôle total sur le pare-feu. Journalisez chaque activité effectuée sur le pare-feu par ces utilisateurs.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Surveillance périodique

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour maintenir les niveaux de sécurité sur les pare-feux Juniper, surveillez les pare-feux régulièrement. Effectuez ces tâches de surveillance à intervalles régulières.

<h1 class="western" style="margin-left:.95cm;text-indent:-.95cm;margin-top:.22cm;margin-bottom:0;page-break-before:auto;page-break-after:auto;">
  <span style="colour:#17365d;"><span style="font-family:Verdana, sans-serif;"><span style="font-size:large;">Configuration de la mitigation des pertes d’audit

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Il existe des cas où plus d’événements auditables peuvent se produire que le dispositif de sécurité n’est pas capable d’écrire sur un pare-feu Syslog. Le dispositif de sécurité doit arrêter tout événement auditable supplémentaire jusqu’à ce que la traçabilité d’audit puisse gérer plus de trafic. Un administrateur autorisé doit activer la commande suivante :

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set log audit-loss-mitigation</b>

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Journalisation des paquets autorisés</b>

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Pour journaliser les paquets autorisés passant à travers le dispositif, activez l’option de journalisation sur toutes les politiques de trafic authentifiées et/ou non authentifiées.

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Dans ce document, toutes les politiques autorisisées incluent le mot-clé <b>log</b>, afin de créer des entrées de journalisation du trafic pour le trafic autorisé.

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">À la fin de la session d’application, les journaux du trafic autorisé sont créés.

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Vous pouvez utiliser la commande suivante pour visualiser les journaux de trafic globaux, ou les journaux de trafic spécifiques à une politique :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;"><b>get log traffic</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;"><b>get log traffic policy </b><i>id</i>

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Journalisation des paquets rejetés</b>

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Pour journaliser les paquets rejetés, définissez la commande suivante pour terminer sur l’une des interfaces du dispositif :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;"><b>set firewall log-self</b>

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Pour journaliser les paquets rejetés authentifiés ; vous devez ajouter le mot-clé <b>log</b> à la première politique associée à un tunnel VPN. Les paquets qui ne correspondent à aucune des politiques associées au tunnel sont « rejetés ». Les entrées de journal pour ces paquets rejetés sont liées à la politique de plus haut niveau (première dans la liste « get policy all ») associée au tunnel et à la direction du flux de trafic.

<p class="western" style="margin-top:.22cm;line-height:115%;page-break-before:always;">
  <span style="colour:#17365d;"><b>Temps d’expiration inactif de la gestion du pare-feu</b>

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Interface de ligne de commande</b>

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Protégez la gestion depuis le port console en définissant un délai d’inactivité. Par défaut, les sessions console et Telnet expireront après 10 minutes d’inactivité. Il est recommandé de ne jamais définir la valeur du délai d’expiration à zéro.

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour vérifier, exécutez la commande :

<p style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><i><b>get console</b></i>

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Interface utilisateur Web (WebUI)</b>

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Le délai d’expiration de l’interface utilisateur Web, tout comme celui de la console, est par défaut de 10 minutes. Lors du changement du délai d’expiration de l’interface utilisateur Web, précisez un nombre de minutes (entre 1 et 999) de temps d’inactivité avant la fermeture du navigateur. Activez l’option « Activer le délai d’expiration inactif de la gestion Web » et ne la désactivez pas.

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Gestionnaire de sécurité

<p style="margin-left:.95cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Modifier le dispositif > Administration du dispositif > Gestion Web

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Adresses IP autorisées</b>

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Configurez les dispositifs Juniper Networks pour accepter les demandes de gestion uniquement à partir de sources fiables. Définissez une liste d’adresses IP autorisées. Les adresses IP autorisées incluent un paramètre de masque spécifié sous forme de valeur décimale pointée. Les adresses IP autorisées peuvent être des hôtes / sous-réseaux. NOTE : Vous êtes limité à six entrées.

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">CLI

<p style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin manager-ip <span style="text-decoration:underline;">address [mask]</b>

<p style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">WebUI

<p style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Configuration > Admin > Adresses IP autorisées

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Gestionnaire de sécurité

<p style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Modifier le dispositif > Administration du dispositif > Adresses IP autorisées > Ajouter

<p class="western" style="margin-top:.22cm;line-height:100%;page-break-before:always;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches quotidiennes de surveillance</b>

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Trois tentatives de connexion échouées consécutives

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Événements Syslog avec niveaux – critique, alerte ou urgence

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Ajout ou suppression non autorisée aux comptes utilisateurs et groupes

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Modifications / modifications non autorisées effectuées

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Tentatives d’accès non autorisées

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches hebdomadaires de surveillance</b>

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Fonctionnement correct du démon Syslog

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Utilisation de toutes les ressources (CPU, mémoire) dépassant les seuils prédéfinis (basés sur les chiffres de planification de capacité)

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches mensuelles de surveillance</b>

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Niveau des correctifs du pare-feu

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Redémarrages du pare-feu

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Utilisation de l’espace disque

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Changements de membres du groupe de comptes

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Vérification des sauvegardes

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches biannuelles de surveillance</b>

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Effectuer une vérification physique

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Les administrateurs de pare-feux Juniper doivent effectuer ces tâches de surveillance. Signalez tout écart observé par rapport au fonctionnement normal au service concerné.

<h1 class="western" style="margin-left:.95cm;text-indent:-.95cm;margin-top:.22cm;margin-bottom:0;page-break-before:auto;page-break-after:auto;">
  <span style="colour:#17365d;"><span style="font-family:Verdana, sans-serif;"><span style="font-size:large;">Protection du pare-feu

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Plan de récupération après sinistre (DRP)

<p style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Afin de fournir une protection contre les pannes système, il doit y avoir un DRP testé et approuvé. Cela devrait inclure la politique de sauvegarde et les arrangements d’urgence.

<p style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Le DRP pour chaque pare-feu Juniper doit être prêt au moment où le pare-feu est mis en environnement de production.

<p style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Il doit y avoir un exercice de récupération après sinistre planifié et biannuel afin de garantir que le DRP est efficace.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Gestion du dispositif

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les administrateurs du dispositif doivent désactiver les commandes internes. L’utilisation des commandes internes s’applique uniquement à des fins de dépannage et de débogage.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver les commandes internes, vous devez exécuter la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set common-criteria no-internal-commands</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour utiliser les commandes internes (par exemple, « debug flow basic » et « get dbuf stream », « debug ids sat ») à des fins de dépannage et de débogage, utilisez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset common-criteria no-internal-commands</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Note : Utilisez les commandes internes « debug ids sat » pour ISG-1000, ISG-2000, NS-5200 et NS-5400.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Désactiver Telnet pour la gestion du dispositif

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’utilisation de Telnet est déconseillée sur les pare-feux Juniper. Utilisez SSH, version 2.0, pour gérer le pare-feu Juniper :

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour ce faire :

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Désactiver Telnet sur l’interface de gestion

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Activer SSH

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Contrôle des réinitialisations matérielles non autorisées

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver la récupération via la connexion, utilisez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset admin device-reset</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver la récupération via le trou, utilisez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset admin hw-reset</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Lorsqu’elles sont désactivées, les administrateurs du pare-feu doivent activer la réinitialisation correspondante afin d’effectuer toute activité nécessitant un redémarrage du pare-feu.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Restriction de l’accès à distance

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’accès à la gestion doit être limité au port de console connecté localement, plutôt que aux paramètres par défaut d’usine.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour limiter l’accès à la gestion au port de console, l’interface qui est par défaut dans la zone de sécurité V1-Trust ou Trust doit avoir l’accès à la gestion désactivé.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Toutes les autres interfaces ont l’accès à la gestion désactivé par défaut.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver la gestion de l’interface, émettez la commande CLI suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset interface interface-name manage</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Gestion des utilisateurs

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les administrateurs des appareils de sécurité doivent choisir des noms d’utilisateur et des mots de passe qui non seulement ont une longueur d’au moins huit caractères et utilisent autant de types de caractères que possible. Il est nécessaire de mélanger les lettres minuscules et majuscules pour assurer une protection adéquate. En outre, les noms d’utilisateur et les mots de passe faciles à deviner ne sont pas sécurisés.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les appareils de sécurité sont livrés avec un nom d’utilisateur et un mot de passe par défaut de « netscreen ». Changez le mot de passe par défaut dès que possible pour empêcher l’accès non autorisé.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">La durée recommandée entre les changements de mot de passe est de 30 jours maximum pour atténuer les effets d’une identité d’administrateur compromise.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Définition/Changement des restrictions de longueur du mot de passe

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour garantir que les mots de passe de huit caractères ou plus sont toujours utilisés, vous devez d’abord définir la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin password restrict length password-length</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">où password-length est une valeur décimale égale ou supérieure à 8 et inférieure ou égale à 31. Elle doit également suivre la politique de mot de passe.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Définition/Changement du nom d’administrateur et du mot de passe

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les commandes CLI suivantes, dans l’ordre, sont nécessaires pour définir un nouveau nom d’administrateur et un mot de passe :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin name name-string</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin password password-string</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">où name-string et password-string doivent être remplacés par le nom d’utilisateur réel et le mot de passe de l’administrateur.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Gestion des politiques

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Supprimer la politique par défaut autorisant

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Le pare-feu pourrait avoir une politique par défaut autorisant le trafic traversant le dispositif depuis l’interface dans la zone Trust vers l’interface dans la zone Untrust. Supprimez cette politique par défaut pour éviter une autorisation involontaire de l’information traversant le dispositif. Utilisez la commande CLI :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>unset policy id 1</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Journalisation du trafic refusé

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Par défaut, l’appareil de sécurité rejette tout trafic qui ne correspond à aucune politique « autorisée ». Par conséquent, ajoutez une politique à la fin de la liste des politiques afin de journaliser le trafic refusé qui ne correspond à aucune politique :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from scr-zone to dst-zone any any any deny log</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">... où pol-id est l’ID de la politique, scr-zone et dst-zone sont respectivement la zone source d’où le trafic provient et la zone de destination vers laquelle le trafic arrive.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour chaque zone de sécurité qui a une interface réseau attribuée, ajoutez les politiques ci-dessus à la fin des tables de politique afin de garantir que le journal des paquets rejetés est conservé.

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from trust to untrust any any any deny log count</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from untrust to trust any any any deny log count</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from trust to dmz any any any deny log count</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from dmz to trust any any any deny log count</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Définition d’une politique pour autoriser le trafic

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Deux étapes importantes à suivre lors de la création d’une politique de sécurité :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
    <span style="font-family:Verdana, sans-serif;">• Activer le comptage et la journalisation pour maintenir les informations de journal d’audit pour le trafic passant à travers le dispositif.

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
    <span style="font-family:Verdana, sans-serif;">• Doit être spécifique pour garantir que le trafic autorisé est intentionnel et non inclus dans une politique générale.

<p class="western" style="margin-top:.22cm;line-height:150%;">
    <span style="font-family:Verdana, sans-serif;">Utilisez une adresse IP source spécifique (src-addr), une adresse IP de destination (dst-addr), une zone source (src-zone), une zone de destination (dst-zone), un protocole et un service (servicename) si possible. Un exemple où il peut ne pas être pertinent d’être spécifique est pour le trafic destiné à un réseau externe pour un accès web général.

<p class="western" style="margin-top:.22cm;line-height:150%;">
    <span style="font-family:Verdana, sans-serif;">Après avoir créé et configuré les adresses source et de destination, configurez la politique avec le comptage et la journalisation en utilisant la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
    <span style="font-family:Verdana, sans-serif;"><b>set policy id id-num from src-zone to dst-zone src-addr dst-addr servicename</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
    <span style="font-family:Verdana, sans-serif;">action log count

<p class="western" style="margin-top:.22cm;line-height:150%;">
    <span style="font-family:Verdana, sans-serif;">... où « id-num » est le nombre décimal représentant l’ID de la politique et « action » peut être « permit » pour autoriser un service spécifique à passer de l’adresse source à travers l’appareil de sécurité vers l’adresse de destination ; ou « deny » pour bloquer le service qui passe à travers l’appareil de sécurité.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Ordre des politiques

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">L’ordre des politiques est important, car les politiques correspondent dans l’ordre en commençant par la première dans la liste des politiques et en se déplaçant à travers la liste. La première politique correspondante s’applique au trafic réseau pour déterminer l’action à effectuer. Par défaut, une nouvelle politique créée apparaît à la fin de la liste des politiques.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Il existe une option qui permet de positionner une politique au sommet de la liste plutôt que de laisser la politique apparaître à la fin. Dans l’interface CLI, ajoutez le mot-clé « top » à la commande « set policy » :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>For example,</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id 6 top from trust to untrust trust-HostA untr-NetworkB http</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>permit log</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">La politique nouvellement créée peut également être positionnée à n’importe quel emplacement dans la liste des politiques en utilisant l’option de mot-clé « before » à la commande CLI « set policy » :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>For example:</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id 4 before 98 from untrust to trust untr-NetworkB trust-HostA ftp</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>permit log</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Si des politiques globales sont utilisées, remplacez la politique ci-dessus qui s’exécute avant toute politique globale. Une politique globale de refus peut être utilisée qui doit être ajoutée à la fin de la liste des politiques globales :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy global id pol-id any any any deny log count</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Journalisation et surveillance du système

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configurer Syslog

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Vous devez configurer un pare-feu Syslog comme sauvegarde pour les informations d’audit et le stockage à long terme des journaux d’audit. Cela aidera à prévenir la perte d’informations d’audit.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les commandes spécifiques nécessaires pour configurer un pare-feu Syslog sont :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog config ip-address facilities local0 local0</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog config ip-address port 514</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog config ip-address log traffic</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog enable</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set log module system level level-name destination syslog</b>

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">où ip-address est l’adresse IP réelle du pare-feu Syslog et level-name est le niveau de gravité du journal.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Note : Vous devez entrer la commande set log une fois pour chaque niveau de message.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les options pour level-name sont les suivantes :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>emergency</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>alert</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>critical</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>error</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>warning</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>notification</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>information</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>debugging</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Événements à journaliser

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les journaux du système contiennent les événements historiques du pare-feu et les informations d’utilisation, utilisées pour le débogage des dysfonctionnements du système et les enquêtes pénales. Par conséquent, journalisez toutes les informations critiques.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Configurez Syslog pour journaliser les éléments suivants sur chaque pare-feu :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Chaque connexion et déconnexion

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Démarrage et arrêt du pare-feu

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Session complète

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Administration des comptes utilisateurs et groupes

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">• Défaillances matérielles

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Réserve et archivage des journaux

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Il arrive souvent qu’il soit nécessaire d’obtenir une traçabilité complète d’un processus pour des investigations de sécurité ou des buts de dépannage. Par conséquent, conservez localement les journaux du pare-feu pendant un nombre défini de jours. Il doit y avoir suffisamment d’espace de stockage alloué pour gérer cela. En outre, il doit y avoir un contrôle d’accès très strict mis en œuvre sur les journaux stockés.

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les fichiers de journal doivent être archivés hors ligne. Protégez adéquatement les journaux archivés afin que les utilisateurs non autorisés n’y aient pas accès.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Protection des fichiers de journal

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Si un utilisateur malveillant parvient à modifier les fichiers de journal et à supprimer les traces d’attaque, aucune enquête ne pourra être concluante. En outre, le journal étendu pour la traçabilité d’audit. Par conséquent, protégez les fichiers de journal contre toute manipulation et stockez-les en toute sécurité.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Journaux d’activité des utilisateurs privilégiés

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Les utilisateurs privilégiés ont un contrôle total sur le pare-feu. Journalisez chaque activité effectuée sur le pare-feu par ces utilisateurs.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Surveillance périodique

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;">Pour maintenir les niveaux de sécurité sur les pare-feux Juniper, surveillez les pare-feux régulièrement. Effectuez ces tâches de surveillance à intervalles réguliers.

<h1 class="western" style="margin-left:.95cm;text-indent:-.95cm;margin-top:.22cm;margin-bottom:0;page-break-before:auto;page-break-after:auto;">
  <span style="colour:#17365d;"><span style="font-family:Verdana, sans-serif;"><span style="font-size:large;">Configuration de la mitigation des pertes d’audit

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Il existe des cas où plus d’événements auditables peuvent se produire que le dispositif de sécurité n’est pas capable d’écrire sur un pare-feu Syslog. Le dispositif de sécurité doit arrêter tout événement auditable supplémentaire jusqu’à ce que la traçabilité d’audit puisse gérer plus de trafic. Un administrateur autorisé doit activer la commande suivante :

<p class="western" style="margin-top:.22cm;line-height:150%;">
  <span style="font-family:Verdana, sans-serif;"><b>set log audit-loss-mitigation</b>

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Journalisation des paquets autorisés</b>

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Pour journaliser les paquets autorisés passant à travers le dispositif, activez l’option de journalisation sur toutes les politiques de trafic authentifiées et/ou non authentifiées.

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Dans ce document, toutes les politiques autorisées incluent le mot-clé <b>log</b>, afin de créer des entrées de journalisation du trafic pour le trafic autorisé.

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">À la fin de la session d’application, les journaux du trafic autorisé sont créés.

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Vous pouvez utiliser la commande suivante pour visualiser les journaux de trafic globaux, ou les journaux de trafic spécifiques à une politique :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;"><b>get log traffic</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;"><b>get log traffic policy </b><i>id</i>

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Journalisation des paquets rejetés</b>

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Pour journaliser les paquets rejetés, définissez la commande suivante pour terminer sur l’une des interfaces du dispositif :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;"><b>set firewall log-self</b>

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Pour journaliser les paquets rejetés authentifiés ; vous devez ajouter le mot-clé <b>log</b> à la première politique associée à un tunnel VPN. Les paquets qui ne correspondent à aucune des politiques associées au tunnel sont « rejetés ». Les entrées de journal pour ces paquets rejetés sont liées à la politique de plus haut niveau (première dans la liste « get policy all ») associée au tunnel et à la direction du flux de trafic.

<p class="western" style="margin-top:.22cm;line-height:115%;page-break-before:always;">
  <span style="colour:#17365d;"><b>Temps d’expiration inactif de la gestion du pare-feu</b>

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Interface de ligne de commande</b>

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Protégez la gestion depuis le port console en définissant un délai d’inactivité. Par défaut, les sessions console et Telnet expireront après 10 minutes d’inactivité. Il est recommandé de ne jamais définir la valeur du délai d’expiration à zéro.

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour vérifier, exécutez la commande :

<p style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><i><b>get console</b></i>

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Interface utilisateur Web (WebUI)</b>

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Le délai d’expiration de l’interface utilisateur Web, tout comme celui de la console, est par défaut de 10 minutes. Lors du changement du délai d’expiration de l’interface utilisateur Web, précisez un nombre de minutes (entre 1 et 999) de temps d’inactivité avant la fermeture du navigateur. Activez l’option « Activer le délai d’expiration inactif de la gestion Web » et ne la désactivez pas.

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Gestionnaire de sécurité

<p style="margin-left:.95cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Modifier le dispositif > Administration du dispositif > Gestion Web

<p style="margin-top:.22cm;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Adresses IP autorisées</b>

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Configurez les dispositifs Juniper pour accepter les demandes de gestion uniquement à partir de sources fiables. Définissez une liste d’adresses IP autorisées. Les adresses IP autorisées incluent un paramètre de masque spécifié sous forme décimale. Les adresses IP autorisées peuvent être des hôtes / sous-réseaux. NOTE : Vous êtes limité à six entrées.

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">CLI

<p style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin manager-ip <span style="text-decoration:underline;">address [mask]</b>

<p style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Interface Web

<p style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>Configuration > Administration > Adresses IP autorisées</b>

<p style="margin-left:.64cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Gestionnaire de sécurité

<p style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>Modifier le dispositif > Administration du dispositif > Adresses IP autorisées > Ajouter</b>

<p class="western" style="margin-top:.22cm;line-height:100%;page-break-before:always;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches quotidiennes de surveillance</b>

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Trois tentatives de connexion échouées consécutives

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Événements Syslog avec niveaux – critique, alerte ou urgence

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Ajout ou suppression non autorisée aux comptes utilisateurs et groupes

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Modifications / modifications non autorisées effectuées

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Tentatives d’accès non autorisées

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches hebdomadaires de surveillance</b>

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Fonctionnement correct du démon Syslog

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Utilisation de toutes les ressources (CPU, mémoire) dépassant les seuils prédéfinis (basés sur les chiffres de planification de capacité)

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches mensuelles de surveillance</b>

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Niveau des correctifs du pare-feu

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Redémarrages du pare-feu

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Utilisation de l’espace disque

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Changements de membres du groupe de comptes

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Vérification des sauvegardes

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches biannuelles de surveillance</b>

* <p class="western" style="margin-top:.22cm;line-height:100%;">
      <span style="font-family:Verdana, sans-serif;">Effectuer une vérification physique

<p class="western" style="margin-top:.22cm;line-height:115%;">
  <span style="font-family:Verdana, sans-serif;">Les administrateurs du pare-feu Juniper doivent effectuer ces tâches de surveillance. Signalez tout écart observé par rapport au fonctionnement normal au service concerné.

<h1 class="western" style="margin-left:.95cm;text-indent:-.95cm;margin-top:.22cm;margin-bottom:0;page-break-before:auto;page-break-after:auto;">
  <span style="colour:#17365d;"><span style="font-family:Verdana, sans-serif;"><span style="font-size:large;">Protection du pare-feu

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Plan de récupération après sinistre (DRP)

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Afin de fournir une protection contre les pannes système, il doit y avoir un DRP testé et approuvé. Cela devrait inclure la politique de sauvegarde et les arrangements d’urgence.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Le DRP pour chaque pare-feu Juniper doit être prêt au moment où le pare-feu est mis en environnement de production.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Il doit y avoir un exercice de récupération après sinistre planifié et biannuel afin de garantir que le DRP est efficace.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Gestion du dispositif

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Les administrateurs du dispositif doivent désactiver les commandes internes. L’utilisation des commandes internes s’applique uniquement à des fins de dépannage et de débogage.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver les commandes internes, vous devez exécuter la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set common-criteria no-internal-commands</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour utiliser les commandes internes (par exemple, « debug flow basic » et « get dbuf stream », « debug ids sat ») à des fins de dépannage et de débogage, utilisez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>unset common-criteria no-internal-commands</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Note : Utilisez les commandes internes « debug ids sat » pour ISG-1000, ISG-2000, NS-5200 et NS-5400.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Désactiver Telnet pour la gestion du dispositif

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">L’utilisation de Telnet est déconseillée sur les pare-feux Juniper. Utilisez SSH, version 2.0, pour gérer le pare-feu Juniper :

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour ce faire :

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Désactiver Telnet sur l’interface de gestion

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Activer SSH

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Contrôle des réinitialisations matérielles non autorisées

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver la récupération via la connexion, utilisez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>unset admin device-reset</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver la récupération via le trou, utilisez la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>unset admin hw-reset</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Lorsqu’elles sont désactivées, les administrateurs du pare-feu doivent activer la réinitialisation correspondante afin d’effectuer toute activité nécessitant un redémarrage du pare-feu.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Restriction de l’accès à distance

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">L’accès à la gestion doit être limité au port de console connecté localement, plutôt que aux paramètres par défaut d’usine.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour limiter l’accès à la gestion au port de console, l’interface qui est par défaut dans la zone de sécurité V1-Trust ou Trust doit avoir l’accès à la gestion désactivé.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Toutes les autres interfaces ont l’accès à la gestion désactivé par défaut.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour désactiver la gestion de l’interface, émettez la commande CLI suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>unset interface interface-name manage</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Gestion des utilisateurs

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Les administrateurs des appareils de sécurité doivent choisir des noms d’utilisateur et des mots de passe qui non seulement ont une longueur d’au moins huit caractères et utilisent autant de types de caractères que possible. Il est nécessaire de mélanger les lettres minuscules et majuscules pour assurer une protection adéquate. En outre, les noms d’utilisateur et les mots de passe faciles à deviner ne sont pas sécurisés.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Les appareils de sécurité sont livrés avec un nom d’utilisateur et un mot de passe par défaut de « netscreen ». Changez le mot de passe par défaut dès que possible pour empêcher l’accès non autorisé.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">La durée recommandée entre les changements de mot de passe est de 30 jours maximum pour atténuer les effets d’une identité d’administrateur compromise.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Définition/Changement des restrictions de longueur du mot de passe

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour garantir que les mots de passe de huit caractères ou plus sont toujours utilisés, vous devez d’abord définir la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin password restrict length password-length</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">où password-length est une valeur décimale égale ou supérieure à 8 et inférieure ou égale à 31. Elle doit également suivre la politique de mot de passe.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Définition/Changement du nom d’administrateur et du mot de passe

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Les commandes CLI suivantes, dans l’ordre, sont nécessaires pour définir un nouveau nom d’administrateur et un mot de passe :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin name name-string</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set admin password password-string</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">où name-string et password-string doivent être remplacés par le nom d’utilisateur réel et le mot de passe de l’administrateur.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Gestion des politiques

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Supprimer la politique par défaut autorisant

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Le pare-feu pourrait avoir une politique par défaut autorisant le trafic traversant le dispositif depuis l’interface dans la zone Trust vers l’interface dans la zone Untrust. Supprimez cette politique par défaut pour éviter une autorisation involontaire de l’information traversant le dispositif. Utilisez la commande CLI :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>unset policy id 1</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Journalisation du trafic refusé

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Par défaut, l’appareil de sécurité rejette tout trafic qui ne correspond à aucune politique « autorisée ». Par conséquent, ajoutez une politique à la fin de la liste des politiques afin de journaliser le trafic refusé qui ne correspond à aucune politique :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from scr-zone to dst-zone any any any deny log</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">... où pol-id est l’ID de la politique, scr-zone et dst-zone sont respectivement la zone source d’où le trafic provient et la zone de destination vers laquelle le trafic arrive.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour chaque zone de sécurité qui a une interface réseau attribuée, ajoutez les politiques ci-dessus à la fin des tables de politique afin de garantir que le journal des paquets rejetés est conservé.

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from trust to untrust any any any deny log count</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from untrust to trust any any any deny log count</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from trust to dmz any any any deny log count</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id pol-id from dmz to trust any any any deny log count</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Définition d’une politique pour autoriser le trafic

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Deux étapes importantes à suivre lors de la création d’une politique de sécurité :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">• Activer le comptage et la journalisation pour maintenir les informations de journal d’audit pour le trafic passant à travers le dispositif.

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">• Doit être spécifique pour garantir que le trafic autorisé est intentionnel et non inclus dans une politique générale.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Utilisez une adresse IP source spécifique (src-addr), une adresse IP de destination (dst-addr), une zone source (src-zone), une zone de destination (dst-zone), un protocole et un service (servicename) si possible. Un exemple où il peut ne pas être pertinent d’être spécifique est pour le trafic destiné à un réseau externe pour un accès web général.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Après avoir créé et configuré les adresses source et de destination, configurez la politique avec le comptage et la journalisation en utilisant la commande suivante :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id id-num from src-zone to dst-zone src-addr dst-addr servicename</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">action log count

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">... où « id-num » est le nombre décimal représentant l’ID de la politique et « action » peut être « permit » pour autoriser un service spécifique à passer de l’adresse source à travers l’appareil de sécurité vers l’adresse de destination ; ou « deny » pour bloquer le service qui passe à travers l’appareil de sécurité.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Ordre des politiques

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">L’ordre des politiques est important, car les politiques correspondent dans l’ordre en commençant par la première dans la liste des politiques et en se déplaçant à travers la liste. La première politique correspondante s’applique au trafic réseau pour déterminer l’action à effectuer. Par défaut, une nouvelle politique créée apparaît à la fin de la liste des politiques.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Il existe une option qui permet de positionner une politique au sommet de la liste plutôt que de laisser la politique apparaître à la fin. Dans l’interface CLI, ajoutez le mot-clé « top » à la commande « set policy » :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>For example,</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id 6 top from trust to untrust trust-HostA untr-NetworkB http</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>permit log</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">La politique nouvellement créée peut également être positionnée à n’importe quel emplacement dans la liste des politiques en utilisant l’option de mot-clé « before » à la commande CLI « set policy » :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>For example:</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy id 4 before 98 from untrust to trust untr-NetworkB trust-HostA ftp</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>permit log</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Si des politiques globales sont utilisées, remplacez la politique ci-dessus qui s’exécute avant toute politique globale. Une politique globale de refus peut être utilisée qui doit être ajoutée à la fin de la liste des politiques globales :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set policy global id pol-id any any any deny log count</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Journalisation et surveillance du système

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Configurer Syslog

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Vous devez configurer un pare-feu Syslog comme sauvegarde pour les informations d’audit et le stockage à long terme des journaux d’audit. Cela aidera à prévenir la perte d’informations d’audit.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Les commandes spécifiques nécessaires pour configurer un pare-feu Syslog sont :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog config ip-address facilities local0 local0</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog config ip-address port 514</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog config ip-address log traffic</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set syslog enable</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>set log module system level level-name destination syslog</b>

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">où ip-address est l’adresse IP réelle du pare-feu Syslog et level-name est le niveau de gravité du journal.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Note : Vous devez entrer la commande set log une fois pour chaque niveau de message.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Les options pour level-name sont les suivantes :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>emergency</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>alert</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>critical</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>error</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>warning</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>notification</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>information</b>

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;"><b>debugging</b>

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Événements à journaliser

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Les journaux du système contiennent les événements historiques du pare-feu et les informations d’utilisation, utilisées pour le débogage des dysfonctionnements du système et les enquêtes pénales. Par cons conséquent, journalisez toutes les informations critiques.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Configurez Syslog pour journaliser les éléments suivants sur chaque pare-feu :

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">• Chaque connexion et déconnexion

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">• Démarrage et arrêt du pare-feu

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">• Session complète

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">• Administration des comptes utilisateurs et groupes

<p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">• Défaillances matérielles

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Réserve et archivage des journaux

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Il arrive souvent qu’il soit nécessaire d’obtenir une traçabilité complète d’un processus pour des investigations de sécurité ou des buts de dépannage. Par cons conséquent, conservez localement les journaux du pare-feu pendant un nombre défini de jours. Il doit y avoir suffisamment d’espace de stockage alloué pour gérer cela. En outre, il doit y avoir un contrôle d’accès très strict mis en œuvre sur les journaux stockés.

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Les fichiers de journal doivent être archivés hors ligne. Protégez adéquatement les journaux archivés afin que les utilisateurs non autorisés n’y aient pas accès.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Protection des fichiers de journal

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Si un utilisateur malveillant parvient à modifier les fichiers de journal et à supprimer les traces d’attaque, aucune enquête ne pourra être concluante. En outre, le journal étendu pour la traçabilité d’audit. Par cons conséquent, protégez les fichiers de journal contre toute manipulation et stockez-les en toute sécurité.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Journaux d’activité des utilisateurs privilégiés

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Les utilisateurs privilégiés ont un contrôle total sur le pare-feu. Journalisez chaque activité effectuée sur le pare-feu par ces utilisateurs.

<h2 class="western" style="margin-left:1.4cm;text-indent:-1.4cm;margin-top:.22cm;line-height:100%;page-break-inside:auto;">
  <span style="font-family:Verdana, sans-serif;">Surveillance périodique

<p class="western" style="margin-top:.22cm;">
  <span style="font-family:Verdana, sans-serif;">Pour maintenir les niveaux de sécurité sur les pare-feux Juniper, surveillez les pare-feux régulièrement. Effectuez ces tâches de surveillance à intervalles réguliers.

<h1 class="western" style="margin-left:.95cm;text-indent:-.95cm;margin-top:.22cm;margin-bottom:0;page-break-before:auto;page-break-after:auto;">
  <span style="colour:#17365d;"><span style="font-family:Verdana, sans-serif;"><span style="font-size:large;">Configuration de la mitigation des pertes d’audit</</h1>
  <span style="font-family:Verdana, sans-serif;">Il existe des cas où plus d’événements auditables peuvent se produire que le dispositif de sécurité n’est pas capable d’écrire sur un pare-feu Syslog. Le dispositif de sécurité doit arrêter tout événement auditable supplémentaire jusqu’à ce que la traçabilité d’audit puisse gérer plus de trafic. Un administrateur autorisé doit activer la commande suivante :

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;"><b>set log audit-loss-mitigation</b>

  <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Pour journaliser les paquets autorisés traversant le dispositif, activez l'option de journalisation sur toutes les politiques de trafic authentifiées et/ou non authentifiées.

  <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Dans ce document, toutes les politiques autorisées incluent le mot-clé <b>log</b>, afin de créer des entrées de journalisation du trafic pour le trafic autorisé.

  <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">À la fin de la session d'application, les journaux du trafic autorisé sont créés.

  <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Vous pouvez utiliser la commande suivante pour visualiser les journaux de trafic globaux, ou les journaux de trafic spécifiques à une politique :

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;"><b>get log traffic</b>

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;"><b>get log traffic policy </b><i>id</i>

  <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Pour journaliser les paquets rejetés, définissez la commande suivante pour terminer sur l'une des interfaces du dispositif :

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;"><b>set firewall log-self</b>

  <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Pour journaliser les paquets rejetés authentifiés ; vous devez ajouter le mot-clé <b>log</b> à la première politique associée à un tunnel VPN. Les paquets qui ne correspondent à aucune des politiques associées au tunnel sont « rejetés ». Les entrées de journal pour ces paquets rejetés sont liées à la politique de plus haut niveau (première dans la liste « get policy all ») associée au tunnel et à la direction du flux de trafic.

  <p class="western" style="margin-top:.22cm;page-break-before:always;">
    <span style="colour:#17365d;"><b>Délai d'expiration inactif de la gestion du pare-feu</b>

  <p class="western" style="margin-top:.22cm;">
    <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Interface de ligne de commande</b>

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Protégez la gestion depuis le port console en définissant un délai d'inactivité. Par défaut, les sessions console et Telnet expireront après 10 minutes d'inactivité. Il est recommandé de ne jamais définir la valeur du délai d'expiration à zéro.

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Pour vérifier, exécutez la commande :

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;"><i><b>get console</b></i>

  <p class="western" style="margin-top:.22cm;">
    <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Interface utilisateur Web (WebUI)</b>

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Le délai d'expiration de l'interface utilisateur Web, tout comme celui de la console, est par défaut de 10 minutes. Lors du changement du délai d'expiration de l'interface utilisateur Web, précisez un nombre de minutes (entre 1 et 999) de temps d'inactivité avant la fermeture du navigateur. Activez l'option « Activer le délai d'expiration inactif de la gestion Web » et ne la désactivez pas.

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;"><b>Administrateur de sécurité</b>

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;"><b>Modifier le dispositif > Administration du dispositif > Gestion Web</b>

  <p class="western" style="margin-top:.22cm;">
    <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Adresses IP autorisées</b>

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Configurez les dispositifs Juniper pour accepter les demandes de gestion uniquement à partir de sources fiables. Définissez une liste d'adresses IP autorisées. Les adresses IP autorisées incluent un paramètre de masque spécifié sous forme décimale. Les adresses IP autorisées peuvent être des hôtes / sous-réseaux. NOTE : Vous êtes limité à six entrées.

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;"><b>CLI</b>

  <p class="western" style="margin-left:1.27cm;margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;"><b>set admin manager-ip <span style="text-decoration:underline;">address [mask]</span></b>

  <p class="western" style="margin-top:.22cm;">
    <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches quotidiennes de surveillance</b>

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Trois tentatives de connexion échouées consécutives

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Événements Syslog avec niveaux – critique, alerte ou urgence

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Ajout ou suppression non autorisée aux comptes utilisateurs et groupes

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Modifications / modifications non autorisées effectuées

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Tentatives d'accès non autorisées

  <p class="western" style="margin-top:.22cm;">
    <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches hebdomadaires de surveillance</b>

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Fonctionnement correct du démon Syslog

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Utilisation de toutes les ressources (CPU, mémoire) dépassant les seuils prédéfinis (basés sur les chiffres de planification de capacité)

  <p class="western" style="margin-top:.22cm;">
    <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches mensuelles de surveillance</b>

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Niveau des correctifs du pare-feu

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Redémarrages du pare-feu

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Utilisation de l'espace disque

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Changements de membres du groupe de comptes

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Vérification des sauvegardes

  <p class="western" style="margin-top:.22cm;">
    <span style="colour:#548dd4;"><span style="font-family:Verdana, sans-serif;"><b>Tâches biannuelles de surveillance</b>

* <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Effectuer une vérification physique

  <p class="western" style="margin-top:.22cm;">
    <span style="font-family:Verdana, sans-serif;">Les administrateurs du pare-feu Juniper doivent effectuer ces tâches de surveillance. Signalez tout écart observé par rapport au fonctionnement normal au service concerné. 
  </p>
</body>
</html>
