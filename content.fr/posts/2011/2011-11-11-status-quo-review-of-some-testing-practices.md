---
lang: "fr"
title: "Evaluating Modern Testing Practices: A Comprehensive Look"
author: Shafiq Alibhai
date: 2011-11-11T05:10:14+00:00
categories:
  - Development

disableHLJS: false
---
## Naviguer les méthodologies dans les projets SAP

Dans l'évolution du développement logiciel, particulièrement pour les systèmes d'entreprise comme SAP, comprendre la méthodologie qui pilote votre projet est essentiel. Des acteurs majeurs comme Deloitte Consulting et IBM proposent des cadres propriétaires comme Thread Manager et Ascendant™ pour vous guider. SAP elle-même offre sa méthodologie Roadmap via sa plateforme Solution Manager. Ces cadres sont également soutenus par des normes établies comme celles de l'IEEE et du Département de la Défense des États-Unis.

Les petites entreprises sans méthodologie définie peuvent également trouver des repères dans des modèles classiques du développement logiciel comme les approches en cascade, en spirale ou évolutive. Ces modèles sont assez souples pour s'adapter à différentes portées de projet et à divers niveaux de stabilité des exigences. Si votre organisation a déjà une expérience réussie dans d'autres projets logiciels à grande échelle, cette expérience peut s'avérer précieuse pour façonner votre mise en œuvre SAP.

## L'essentiel ? Assurez-vous que votre méthodologie choisie offre une orientation suffisante pour tester votre système ERP. Certains cadres conçus pour développer des logiciels de zéro peuvent ne pas convenir aux solutions « clés en main » comme SAP.

## Le test en phase avec les méthodologies projet

Quelle que soit la présence ou non d'une méthodologie formelle dans votre projet, une attention méticuleuse doit être portée à l'alignement de vos activités de test avec votre approche globale. Les responsables de test doivent se concentrer sur la création de plans de test complets qui respectent la méthodologie générale du projet afin de répondre efficacement aux critères de test.

## Les limites du test manuel

Bien que le test manuel soit une option courante pour de nombreux projets, il présente toutefois des inconvénients :

- **Temps consommateur** : La documentation et l'exécution de chaque test manuellement peuvent allonger les délais.
- **Complexité croissante** : La complexité croissante des environnements informatiques exige une couverture de test plus poussée, poussant les équipes vers le test automatisé.
- **Globalisation** : Les équipes réparties géographiquement exigent des processus standardisés que le test manuel peine à fournir.
- **Problèmes de documentation** : Sans automatisation, maintenir la documentation synchronisée avec le processus de test devient une tâche colossale.
- **Prone aux erreurs** : Les tests manuels sont plus sujets aux erreurs humaines que les tests automatisés.

## Enregistrement et lecture : pas une solution miracle

Les outils automatisés de test par enregistrement et lecture peuvent sembler être une solution rapide, mais ils déçoivent souvent à long terme. Ces scripts sont étroitement liés à des fonctionnalités ou éléments spécifiques de l'application, ce qui les rend fragiles et difficiles à maintenir à mesure de l'évolution du logiciel. L'effort initial nécessaire pour adapter et annoter ces scripts bruts dépasse souvent les bénéfices attendus, contredisant ainsi l'objectif même de l'automatisation.

## Trouver l'équilibre : des questions à se poser

Avant d'automatiser tout, demandez-vous :

- Vos tests manuels actuels sont-ils rentables ?
- Pourrait-on simplifier ou réviser certains tests pour les rendre plus gérables ?
- L'ajout de testeurs supplémentaires soulagerait-il la charge ?
- Les procédures de test sont-elles claires et bien comprises par l'équipe ?

## Utiliser des outils pour comparer les résultats de test

Des utilitaires de comparaison sont disponibles non seulement dans des outils dédiés au test, mais aussi dans la plupart des systèmes d'exploitation. Ces outils peuvent être d'une grande aide pour évaluer les résultats de test et constituent une étape intermédiaire vers une automatisation plus poussée.

## La documentation des tests : un aspect négligé

La tenue d'un registre détaillé est indispensable. La documentation des tests varie du plan de test de niveau management aux scripts de test très précis. Les outils automatisés peuvent offrir des solutions aux problèmes de documentation, mais l'élément essentiel reste d'avoir un processus bien défini dès le départ.

## Quand automatiser ?

- Aucune crise organisationnelle en cours
- Une personne dédiée chargée du choix et de la mise en œuvre des outils
- Une insatisfaction vis-à-vis des pratiques de test actuelles
- Un soutien clair de la direction pour l'investissement dans les outils et l'amélioration des processus

Si ces conditions ne sont pas réunies, cela ne signifie pas que l'automatisation est impossible. Cela indique simplement que vous devrez peut-être vous investir davantage pour la réussite de sa mise en œuvre.

Bien que les outils automatisés puissent grandement aider le processus de test, ils ne sont pas une panacée. Une approche équilibrée, alignée sur les besoins propres à votre organisation et les spécificités de votre mise en œuvre SAP, est essentielle pour une réussite à long terme.
