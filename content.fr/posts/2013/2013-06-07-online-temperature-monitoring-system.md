---
lang: "fr"
title: Online Temperature Monitoring System
author: Shafiq Alibhai
date: 2013-06-07T09:52:57+00:00
categories:
  - Development

disableHLJS: false
---
# Téléchargement : [PROJ\_FORMAT\_][1]

1. Introduction

2. Environnement de travail

2.1 Spécifications des exigences matérielles

i. Microcontrôleur AT89c52  
ii. ADC ADC0808  
iii. <a class="zem_slink" title="Horloge temps réel" href="http://en.wikipedia.org/wiki/Real-time_clock" target="_blank" rel="wikipedia">Horloge temps réel</a> DS1307  
iv. EEPROM sériel AT24c08  
v. Transmetteur-récepteur sériel MAX232  
vi. LCD 16&#215;2

2.2 <a class="zem_slink" title="Exigence" href="http://en.wikipedia.org/wiki/Requirement" target="_blank" rel="wikipedia">Spécifications logicielles</a>

i. Langage de programmation ANSI C  
ii. Compilateur KEIL

2.3 À propos du matériel

2.3.1 Microcontrôleur (89C52)  
Fonctionnalités principales  
 Compatible avec les produits MCS-51™  
 8 Ko de mémoire Flash réprogrammable en système  
 Durée de vie : 1 000 cycles d'écriture/effacement  
 256 octets de RAM interne 8 bits  
 32 lignes d'entrée/sortie programmables  
 Trois compteurs/timers 16 bits  
 Huit sources d'interruption  
 Canal série programmable

Description  
L'AT89C52 est un microcontrôleur CMOS 8 bits à faible consommation et à haute performance, doté de 8 Ko de mémoire Flash programmable et effaçable en lecture seule (PEROM). L'appareil est fabriqué à l'aide de la technologie de mémoire non volatile à haute densité d'<a class="zem_slink" title="NASDAQ: ATML" href="http://www.google.com/finance?q=NASDAQ:ATML" target="_blank" rel="googlefinance">Atmel</a>. La mémoire Flash intégrée permet la reprogrammation de la mémoire de programme en système ou à l'aide d'un programmeur classique de mémoire non volatile. En combinant un CPU 8 bits polyvalent avec une mémoire Flash sur une seule puce, l'AT89C52 d'Atmel constitue un microordinateur puissant qui offre une solution flexible et rentable pour de nombreuses applications embarquées.

Schéma des broches

Description des broches  
• RST  
Entrée de réinitialisation. Un niveau haut sur cette broche pendant deux cycles machine, tandis que l'oscillateur fonctionne, réinitialise l'appareil.  
• ALE/PROG  
Signal d'activation de verrouillage d'adresse : émet un signal d'impulsion pour verrouiller le bas de l'adresse lors des accès à la mémoire externe. Cette broche est également l'entrée d'impulsion de programmation (PROG) pendant la <a class="zem_slink" title="Adobe Flash" href="http://www.adobe.com/flashplatform/" target="_blank" rel="homepage">programmation Flash</a>.  
• PSEN  
Signal d'activation de mémoire programme : impulsion de lecture pour la mémoire programme externe. Lorsque l'AT89C52 exécute du code depuis une mémoire programme externe, PSEN est activé deux fois par cycle machine, sauf que deux activations PSEN sont sautées lors de chaque accès à la mémoire donnée externe.  
• EA/VPP  
Activation de l'accès externe. EA doit être relié à GND afin d'activer l'appareil pour lire le code depuis les adresses mémoire externes allant de 0000H à FFFFH.

Programmation de la mémoire Flash

Pour programmer l'89c52, suivez les étapes suivantes.

1. Entrez l'emplacement mémoire souhaité sur les lignes d'adresse.  
2. Entrez les données appropriées sur les lignes de données  
3. Activez la combinaison correcte des signaux de contrôle  
4. Activez EA/Vpp  
5. Pulsez ALE/PROG une fois pour programmer un octet dans le tableau Flash ou verrouiller les bits. Le cycle d'écriture d'octet est auto-chronométré et dure généralement au plus 1,5 ms. Répétez les étapes 1 à 5, en changeant l'adresse et les données pour toute la mémoire ou jusqu'à la fin du fichier objet.

2.3.2 ADC 0808  
Fonctionnalités principales :

2.3.3 Horloge temps réel (DS1307)  
Fonctionnalités  
 Horloge temps réel (RTC) qui compte les secondes, les minutes, les heures, la date du mois, le mois, le jour de la semaine, et l'année avec compensation de l'année bissextile, valable jusqu'en 2100  
 56 octets de mémoire vive (NV) alimentée par batterie  
 <a class="zem_slink" title="I²C" href="http://en.wikipedia.org/wiki/I%C2%B2C" target="_blank" rel="wikipedia">Interface série à deux fils</a>  
 Détection automatique des coupures d'alimentation et commutation du circuit

Schéma des broches

Description des broches  
 SCL (entrée horloge série) – SCL est utilisée pour synchroniser le transfert de données sur l'interface série.  
 SDA (entrée/sortie données série) – SDA est la broche d'entrée/sortie pour l'interface série à deux fils.  
 SQW/OUT (conducteur de sortie d'onde carrée) – Lorsqu'elle est activée, le bit SQWE défini à 1, la broche SQW/OUT produit l'une des quatre fréquences d'onde carrée (1 Hz, 4 kHz, 8 kHz, 32 kHz).  
 X1, X2 – Connexions pour un cristal standard de 32,768 kHz. Le circuit d'oscillateur interne est conçu pour fonctionner avec un cristal ayant une capacité de charge (CL) de 12,5 pF.

Description  
Le DS1307 est une horloge/chronomètre en série à faible consommation, avec un calendrier complet en BCD (code binaire décimal) et 56 octets de mémoire vive (NV) SRAM. Les adresses et les données sont transférées en série via un bus bidirectionnel à deux fils. L'horloge/calendrier fournit des informations sur les secondes, les minutes, les heures, les jours, les dates, les mois et les années. La fin du mois est automatiquement ajustée pour les mois comportant moins de 31 jours, y compris les corrections pour les années bissextiles. L'horloge fonctionne en mode 24 heures ou en mode 12 heures avec indicateur AM/PM. Le DS1307 dispose d'un circuit intégré de détection de coupure d'alimentation qui détecte les coupures d'alimentation et bascule automatiquement sur l'alimentation de la batterie.

Fonctionnement  
Le DS1307 fonctionne comme un périphérique esclave sur le bus série. L'accès est obtenu en implémentant une condition de départ (START) et en fournissant un code d'identification du périphérique, suivi d'une adresse de registre. Les registres suivants peuvent être accessibles séquentiellement jusqu'à ce qu'une condition d'arrêt (STOP) soit exécutée. Lorsque VCC tombe en dessous de 1,25 x VBAT, l'appareil interrompt l'accès en cours et réinitialise le compteur d'adresse du périphérique. Les entrées vers le périphérique ne seront pas reconnues à ce moment-là pour éviter l'écriture de données erronées provenant d'un système hors tolérance. Lorsque VCC tombe en dessous de VBAT, l'appareil bascule en mode de sauvegarde à faible courant alimenté par la batterie. Lors du démarrage, l'appareil bascule de la batterie vers VCC lorsque VCC est supérieur à VBAT + 0,2 V, et reconnaît les entrées lorsque VCC est supérieur à 1,25 x VBAT.

2.3.4 Transmetteur-récepteur série (MAX232)

Fonctionnalités  
 Débit de données élevé – 250 <a class="zem_slink" title="Unités de débit de données" href="http://en.wikipedia.org/wiki/Data_rate_units" target="_blank" rel="wikipedia">kbits/s</a> sous charge  
 Fonctionnement à partir d'une alimentation unique +5 V  
 Utilisation de condensateurs petits : 0,1 µF

Schéma des broches

Description

Le DS232A est une paire double de conducteurs/récepteurs RS-232 qui génère des niveaux de tension RS-232 à partir d'une alimentation unique +5 V. Aucune alimentation supplémentaire ±12 V n'est nécessaire car le DS232A utilise des pompes de charge intégrées pour convertir l'alimentation +5 V en ±10 V. Les taux de montée des conducteurs et les débits de données sont garantis jusqu'à 250 kbits/s. Le DS232A fonctionne avec seulement des condensateurs de pompe de charge de 0,1 µF.

2.3.4 EEPROM série  
Fonctionnalités  
 Mémoire organisée en interne 1024 x 8 (8 Ko)  
 Interface série à deux fils  
 Protocole de transfert de données bidirectionnel  
 Broche de protection contre l'écriture pour une protection matérielle des données  
 Mode d'écriture par page : 8 octets (1K, 2K), 16 octets (4K, 8K, 16K)  
 Écriture partielle de page autorisée

Schéma des broches

Description  
L'AT24C08 fournit 8192 bits de mémoire EEPROM sérielle effaçable et programmable, organisée en 1024 mots de 8 bits chacun. L'appareil est optimisé pour une utilisation dans de nombreuses applications industrielles et commerciales où l'opération à faible puissance et à faible tension est essentielle. L'AT24C08 est accessible via une interface série à deux fils.

2.3.5 Écran à cristaux liquides  
Le système en ligne de surveillance de température utilise un écran à cristaux liquides comme affichage final du système, avec un affichage de 16 x 2. Il peut afficher 16 caractères de données ASCII sur 2 lignes, soit un total de 32 caractères.

2.4 À propos du logiciel

2.4.1 Langage de programmation (ANSI C)  
Le logiciel du projet a été écrit dans le langage "C" de haut niveau, en utilisant le compilateur KEIL.  
Pourquoi le "C" ?  
Le C est devenu le langage de prédilection pour les programmeurs embarqués, car il offre l'avantage de l'indépendance du processeur. Cette indépendance permet au programmeur de se concentrer sur les algorithmes et les applications plutôt que sur les détails de l'architecture du processeur. Cependant, de nombreuses de ses fonctionnalités s'appliquent également aux autres langages de haut niveau. Peut-être la force du C réside dans le fait qu'il donne aux programmeurs embarqués un degré exceptionnel de contrôle direct sur le matériel sans sacrifier les avantages des langages de haut niveau.  
Des compilateurs et des crois-compilateurs sont disponibles pour presque tous les processeurs avec le C. Tout code source en C, C++ ou langage assembleur doit être converti en une image exécutable pouvant être chargée dans une puce ROM.

2.4.2 Compilateur KEIL  
Environnement de développement Raisonance  
À propos des kits de développement Raisonance  
Les kits de développement Raisonance 8051, XA et ST6 constituent une solution complète pour créer des logiciels pour la famille 8051, la famille XA et la famille ST6. Les kits de développement comprennent de nombreux outils différents qui permettent de développer des projets allant de simples à très complexes avec une relative facilité. KEIL développe des outils embarqués depuis 1988 et a accumulé de nombreuses années d'expérience.

Outils de développement  
• Compilateur C ANSI  
Le compilateur C est un compilateur conforme à ANSI qui prend des fichiers sources et génère des fichiers objets. Des extensions au langage C sont utilisées pour activer des fonctionnalités du microcontrôleur.  
• Assembleur  
L'assembleur prend des fichiers sources écrits en assembleur et génère des fichiers objets.  
• Lien/Localisation  
Le lien combine les fichiers objets générés par le compilateur et le lien et produit un autre type de fichier objet. Le lien décide également de l'emplacement de certains types de données et de code en mémoire.  
• Convertisseur objet-HEX  
Le convertisseur transforme un fichier objet généré par le lien et génère un fichier HEX Intel, compatible avec la plupart des programmeurs de périphériques.  
• KEIL  
L'Environnement de développement intégré KEIL. KEIL est un programme Windows qui permet à l'utilisateur de créer des projets, d'appeler facilement le compilateur, l'assembleur et le lien pour construire le projet, et de le simuler ou de le déboguer.  
• Gestionnaire de bibliothèques  
Le gestionnaire de bibliothèques peut prendre des fichiers objets générés par le compilateur ou l'assembleur et créer une bibliothèque incluse dans d'autres projets.  
• Moniteur  
Le moniteur est un programme qui s'exécute sur le matériel et transmet des informations de débogage à KEIL pendant l'exécution du programme. Il fournit également un moyen de contrôler l'exécution du programme et de déboguer le programme pendant son exécution sur le matériel.

Étapes du développement

1. RIDE fournit un éditeur qui permet à l'utilisateur de générer des fichiers sources C (.c) et des fichiers sources assembleur (.a51 pour 8051, .axa pour XA et .st6 pour ST6).  
2. Chaque fichier source est traduit en utilisant l'outil approprié. Le compilateur traduit les fichiers sources C. L'assembleur traduit les fichiers sources assembleur. Chaque outil génère un fichier objet rélocalisable (.obj). Si un projet comporte plus d'un fichier source C ou plus d'un fichier source assembleur, alors le compilateur et l'assembleur sont exécutés autant de fois que nécessaire.  
3. Si un fichier bibliothèque est généré, le gestionnaire de bibliothèques prend tous les fichiers objets rélocalisables et les combine en un fichier bibliothèque (.lib). Le fichier bibliothèque peut ensuite être lié à d'autres projets.  
4. Le lien/localisation prend les fichiers objets rélocalisables et les fichiers bibliothèques et les lie ensemble, résolvant les références externes. Le lien/localisation décide également de l'emplacement de certaines variables et de code à des adresses spécifiques dans la carte mémoire. Le lien/localisation génère un fichier objet absolu unique (.aof) et un fichier avec extension vide.  
5. Le fichier objet absolu peut être utilisé par le simulateur ou le débogueur dans KEIL, car le fichier peut contenir des informations de débogage. Alternativement, le fichier objet absolu peut être utilisé avec des émulateurs en circuit.  
6. L'outil convertisseur objet-HEX convertit un fichier objet absolu en un fichier HEX Intel (.hex), qui représente le code binaire pur généré, sans informations de débogage. Le fichier HEX Intel est accepté par presque tous les programmeurs de périphériques. En plus d'être un éditeur, un simulateur et un débogueur, KEIL contrôle également et automatise l'ensemble du processus de construction. En sélectionnant un seul élément de menu, KEIL exécutera les outils appropriés pour générer soit un fichier bibliothèque, soit un fichier objet absolu et un fichier HEX Intel.

Spécifications minimales du système

• Windows 9x/NT/2000  
• Processeur Pentium  
• 20 Mo d'espace disque dur  
• 32 Mo de RAM

2.4.3 Outil d'interface  
2.4.4 Plateforme

3. Conception et description matérielle

Figure 1 Diagramme bloc du système de surveillance de température en ligne

Description du système

. Ce bus I2C fournit une communication fiable et rapide entre le périphérique maître (microcontrôleur) et les autres périphériques esclaves (horloge temps réel, EEPROM série).

4. Analyse du système

La tâche d'analyse du système comprend deux sous-tâches.  
Elles sont  

1. Diagramme de flux de données  
2. Diagramme de flux de contrôle

1. Diagramme de flux de données

Un diagramme de flux de données est une représentation graphique qui illustre le flux d'informations et les transformations appliquées aux données lorsqu'elles passent de l'entrée à la sortie. Le DFD peut être utilisé pour représenter un système ou un logiciel à n'importe quel niveau d'abstraction.

Notations clés utilisées dans DFD et CFD

Diagramme de flux de données de niveau contexte pour OTMS

Un DFD de niveau 0, également appelé modèle fondamental du système ou modèle contexte, représente l'ensemble du logiciel comme une seule bulle avec les données d'entrée et de sortie indiquées par des flèches entrantes et sortantes respectivement.  
À mesure que le DFD est affiné en niveaux plus détaillés, l'analyste effectue une décomposition fonctionnelle implicite du système, accomplissant ainsi l'analyse fonctionnelle requise. En même temps, l'affinement du DFD résulte en un affinement correspondant des données lors de leur passage à travers les processus qui incarnent l'application.

Figure 2 Diagramme de flux de données de niveau contexte

Diagramme de flux de données de niveau 1 pour OTMS

Figure 3 Diagramme de flux de données de niveau 1

Informations sur le flux de données

1) Commandes utilisateur et données  
2) Demande de configuration  
3) Données de configuration  
4) Démarrer/Arrêter  
5) Statut du capteur  
6) Données de configuration  
7) Message A/D  
8) Données de configuration  
9) Informations du capteur  
10) Informations à afficher  
11) Type d'alarme

Diagramme de flux de données de niveau 2 pour OTMS

Diagramme de flux de données de niveau 2 affinant le processus de surveillance des capteurs

Figure 1 Diagramme de flux de données de niveau 2

Informations sur le flux de données

1. Statut du capteur  
2. ID du capteur, type  
3. Données d'alarme  
4. Données de configuration  
5. ID du capteur, type, emplacement  
6. Informations du capteur  
7. Type d'alarme

Diagramme de flux de contrôle

Les grandes applications sont souvent « pilotées » par des événements plutôt que par des données ; elles produisent des informations de contrôle plutôt que des rapports ou des affichages, et traitent les informations avec une forte préoccupation pour le temps et les performances.

Figure 1 Diagramme de flux de contrôle  
Informations sur le flux de données

1. Commandes utilisateur et données  
2. Demande de configuration  
3. Données de configuration  
4. Démarrer/Arrêter  
5. Statut du capteur  
6. Données de configuration  
7. Message A/D  
8. Données de configuration  
9. Informations du capteur  
10. Informations à afficher  
11. Type d'alarme  
5. Conception logicielle  
La conception logicielle inclura deux parties  
• Conception du programme C (source)  
5.1 Conception du programme C  
Il s'agit du programme principal du système de surveillance de température en ligne. Il est compilé avec le compilateur RIDE (Raisonance Integrated Development Environment) et l'image exécutable générée sera déversée dans la puce du microcontrôleur (AT 89c52). Les diagrammes de flux complets pour le programme sont donnés ci-dessous  
Le routine principale du programme

Diagramme de flux pour la routine « Contrôle »

Diagramme de flux pour la routine « Écrire l'heure »

1. Protocole I2C  
2. Protocole de communication série  
6.2 Communication par protocole I2C  
Aperçu  
Dans les équipements électroniques grand public, les télécommunications et l'électronique industrielle, il existe souvent des similitudes entre des conceptions apparemment sans lien. Par exemple, presque tous les systèmes incluent : • Un contrôle intelligent, généralement un microcontrôleur à puce unique • Des circuits généraux comme les pilotes LCD, les ports d'entrée/sortie à distance, la RAM, l'EEPROM ou les convertisseurs de données • Des circuits orientés application comme les circuits de réglage numérique et de traitement de signal pour les systèmes radio et vidéo, ou les générateurs DTMF pour les téléphones à tonalité. Pour tirer parti de ces similitudes afin de bénéficier à la fois aux concepteurs de systèmes et aux fabricants d'équipements, ainsi qu'à maximiser l'efficacité du matériel et la simplicité du circuit, Philips a développé une simple bus bidirectionnel à deux fils pour un contrôle efficace entre les IC. Ce bus est appelé le bus IC ou I2C-bus. Actuellement, la gamme d'IC de Philips comprend plus de 150 types CMOS et bipolaires compatibles avec le bus I2C pour effectuer des fonctions dans les trois catégories mentionnées précédemment. Tous les périphériques compatibles avec le bus I2C intègrent une interface sur puce qui leur permet de communiquer directement entre eux via le bus I2C. Ce concept de conception résout les nombreux problèmes d'interfaçage rencontrés lors de la conception de circuits de contrôle numérique.  
Fonctionnalités du bus I2C  
• Seulement deux lignes de bus sont nécessaires ; une ligne de données série (SDA) et une ligne d'horloge série (SCL)  
• Chaque périphérique connecté au bus est logiquement adressable par une adresse unique et des relations maître/esclave simples existent à tout moment ; les maîtres peuvent fonctionner comme émetteurs ou récepteurs maîtres  
• C'est un bus véritable multi-maître incluant une détection de collision et une arbitrage pour éviter la corruption des données si deux ou plusieurs maîtres initient simultanément un transfert de données  
• Des transferts de données série, orientés sur 8 bits, peuvent être effectués à une vitesse maximale de 100 kbit/s en mode standard, jusqu'à 400 kbit/s en mode rapide, ou jusqu'à 3,4 Mbit/s en mode haute vitesse  
• Une filtration intégrée rejette les pics sur la ligne de données du bus afin de préserver l'intégrité des données  
• Le nombre d'ICs qui peuvent être connectés au même bus est limité uniquement par une capacité maximale du bus de 400 pF.

Avantages pour les concepteurs

• Les blocs fonctionnels du schéma-bloc correspondent aux ICs réels ; les conceptions progressent rapidement du schéma-bloc à la schéma final.  
• Il n'est pas nécessaire de concevoir les interfaces de bus car l'interface du bus I2C est déjà intégrée sur puce.  
• Le protocole d'adressage et de transfert de données intégrés permet aux systèmes d'être entièrement définis logiciellement  
• Les mêmes types d'IC peuvent souvent être utilisés dans de nombreuses applications différentes  
• Le temps de conception est réduit car les concepteurs deviennent rapidement familiers avec les blocs fonctionnels fréquemment utilisés représentés par les ICs compatibles avec le bus I2C  
• Les ICs peuvent être ajoutés ou retirés d'un système sans affecter les autres circuits du bus  
• Le diagnostic des pannes et le débogage sont simples ; les défaillances peuvent être immédiatement localisées

Concept du bus I2C  
Le bus I2C contient deux fils, les données série (SDA) et l'horloge série (SCL), qui transmettent des informations entre les périphériques connectés au bus. Chaque périphérique est reconnu par une adresse unique (qu'il s'agisse d'un microcontrôleur, d'un pilote LCD, d'une mémoire ou d'une interface clavier) et peut fonctionner soit comme émetteur soit comme récepteur, selon la fonction du périphérique. Évidemment, un pilote LCD n'est qu'un récepteur, tandis qu'une mémoire peut à la fois recevoir et transmettre des données. En plus des émetteurs et récepteurs, les périphériques peuvent également être considérés comme maîtres ou esclaves lors du transfert de données.

Définition de la terminologie du bus I2C

Format des octets  
Chaque octet transmis sur la ligne SDA doit être de 8 bits. Le nombre d'octets pouvant être transmis par transfert est illimité. Chaque octet doit être suivi d'un bit d'acquittement. Les données sont transmises avec le bit le plus significatif (MSB) en premier (voir Figure a). Si un esclave ne peut pas recevoir ou transmettre un autre octet complet de données avant d'avoir effectué une autre fonction, par exemple le service d'une interruption interne, il peut maintenir la ligne d'horloge SCL à un niveau bas pour forcer le maître en état d'attente. Le transfert de données reprend lorsque l'esclave est prêt pour un autre octet de données et relâche la ligne d'horloge SCL.

Figure a. Transfert de données sur le bus I2C

Accusé de réception  
Le transfert de données avec accusé de réception est obligatoire. L'impulsion d'horloge liée à l'accusé de réception est générée par le maître. Le transmetteur libère la ligne SDA (haut) pendant l'impulsion d'horloge d'accusé de réception. Le récepteur doit abaisser la ligne SDA pendant l'impulsion d'horloge d'accusé de réception pour que celle-ci reste stable à bas pendant la période haute de cette impulsion d'horloge (voir Figure).

Figure b. Accusé de réception sur le bus I2C

Formats avec adresses de 7 bits  
Les transferts de données suivent le format indiqué dans la Figure a. Après la condition de départ (S), une adresse esclave est envoyée. Cette adresse est de 7 bits, suivie d'un huitième bit qui est un bit de direction de données (R/W) – un « zéro » indique une transmission (ÉCRITURE), un « un » indique une demande de données (LECTURE). Un transfert de données est toujours terminé par une condition d'arrêt (P) générée par le maître. Toutefois, si le maître souhaite toujours communiquer sur le bus, il peut générer une condition de départ répétée (Sr) et adresser un autre esclave sans d'abord générer une condition d'arrêt. Des combinaisons de formats lecture/écriture sont alors possibles dans un tel transfert.

Figure a. Transfert de données complet.

Format complet de transfert de données

S - Condition de départ  
P - Condition d'arrêt  
A - Accusé de réception

3. Protocole de communication série  
La mise en place du RS 232 et de l'ASCII a été liée au développement des organisations informatiques multi-utilisateurs où un certain nombre d'utilisateurs étaient reliés à une machine hôte via des liens de données série, et les données série étaient encodées en ASCII. Les périphériques périphériques, tels que les imprimantes, ont adopté les mêmes normes afin d'accéder au marché croissant des périphériques série.  
La transmission de données série utilisant l'ASCII est devenue si universelle que des circuits intégrés spécialisés, les récepteurs émetteurs asynchrones universels (UART), ont été développés pour effectuer les tâches de conversion d'un octet parallèle de 8 bits en un flux série de 10 bits et de conversion d'un flux série de 10 bits en un octet parallèle de 8 bits.  
L'89c52 contient une circuit de transmission/réception de données série qui peut être programmée pour utiliser quatre modes de communication asynchrone numérotés de 0 à 3.

• Mode 0 : Haute vitesse, registre à décalage de 8 bits ; un débit de baud de f/12  
• Mode 1 : UART standard 8 bits ; débits de bauds variables  
• Mode 2 et Mode 3 : UART multiprocesseur 9 bits

Caractère asynchrone 8 bits (Mode 1)

7. Spécifications opérationnelles

8. Application temps réel

9. Conclusion  
9.1 Perspectives futures

9.2 Limitations  
.

10. Bibliographie

 [1]:https://www.shafiq.in/wp-content/uploads/2013/06/proj_format_.doc
