---
lang: "fr"
title: How to Display the Contents of a Node's Field as an Array in Drupal 6
author: Shafiq Alibhai
date: 2013-09-11T09:32:05+00:00
categories:
  - Development
tags:
  - Drupal 6
  - Debugging
  - PHP
  - Web Development
disableHLJS: false
---
Lorsque vous travaillez avec Drupal 6, il arrive parfois que vous deviez inspecter les données stockées dans un champ d'un nœud. Cela est particulièrement utile pour le débogage ou lorsque vous cherchez à mieux comprendre la structure du contenu. Une manière rapide d'y parvenir consiste à afficher le contenu du champ sous forme de tableau. En PHP, la fonction `var_export()` s'avère très pratique à cet effet.

Voici comment procéder :

```php
var_export(content_fields('field_name_of_the_field', 'name_of_the_content_type'));
```

Dans ce morceau de code, remplacez `'field_name_of_the_field'` par le nom réel du champ qui vous intéresse et `'name_of_the_content_type'` par le type de contenu spécifique contenant ce champ.

Cette ligne simple de code affichera le contenu du champ sous forme de tableau, ce qui facilite l'analyse de sa structure et de son contenu.
