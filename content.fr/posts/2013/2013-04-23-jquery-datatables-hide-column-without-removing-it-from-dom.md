---
title: How to Hide a Column in jQuery DataTables Without Removing It From the DOM
author: Shafiq Alibhai
date: 2013-04-23T10:11:33+00:00
updated: 2023-10-06
categories:
  - Development
tags:
  - DataTables
  - JavaScript
  - jQuery
  - CSS

disableHLJS: false
---
Il arrive parfois que vous souhaitiez masquer une colonne sans pour autant la supprimer du DOM. Cela peut être utile si vous voulez garder les données accessibles pour d'autres opérations, tout en ne les affichant pas sur l'interface.

## Solution rapide : Utiliser le CSS

Une manière simple d’y parvenir consiste à utiliser le CSS. Cela vous permet de conserver les données de la colonne dans le DOM, tout en ne pas les afficher dans le tableau.

### Étape 1 : Ajouter une classe à la colonne

Vous pouvez ajouter une classe à la colonne que vous souhaitez masquer en utilisant l’attribut `sClass` dans DataTables.

```javascript
"sClass": "hide_column"
```

### Étape 2 : Définir la classe en CSS

Une fois la classe attribuée, vous devrez la définir dans votre feuille de style. Vous pouvez définir la propriété `display` à `none` pour masquer la colonne.

```css
.hide_column {
    display: none;
}
```

Et voilà ! Ainsi, la colonne restera présente dans le DOM, mais ne sera pas visible dans le DataTable.

## Pourquoi voudriez-vous faire cela ?

Vous vous demandez peut-être pourquoi masquer une colonne sans la supprimer du DOM. Voici quelques scénarios où cela peut être utile :

1. **Traitement des données** : Vous pourriez vouloir garder la colonne accessible pour des tâches de traitement des données, sans la montrer aux utilisateurs.

2. **Affichage conditionnel** : Parfois, vous souhaiterez afficher la colonne selon certaines conditions. Puisque la colonne reste dans le DOM, il est facile de la faire apparaître ou disparaître via JavaScript.

3. **Consistance** : Garder la colonne dans le DOM assure une structure de tableau cohérente, même lorsque les colonnes sont activées ou désactivées.

4. **Préférences utilisateur** : Vous pourriez vouloir permettre aux utilisateurs de personnaliser les colonnes visibles, sans affecter l’intégrité des données ni la structure du tableau.
