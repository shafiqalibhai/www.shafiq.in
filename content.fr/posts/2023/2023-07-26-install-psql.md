---
lang: "fr"
title: "How to install Postgresql Client using Homebrew"
date: 2023-07-26T11:30:03+00:00
# weight: 1
# aliases: ["/first"]
# tags: ["first"]
author: "Me"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
# description: "Desc Text."
# canonicalURL: "https://canonical.url/to/page"
disableShare: false
disableHLJS: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
categories:
    - Development
# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
# editPost:
#     URL: "https://github.com/<path_to_repo>/content"
#     Text: "Suggest Changes" # edit text
#     appendFilePath: true # to append file path to Edit link
---
Psql est une interface en ligne de commande pour interagir avec PostgreSQL, un système de base de données relationnelle puissant et open source. Brew est un gestionnaire de paquets pour macOS qui facilite l'installation et la gestion des logiciels. Voici les étapes à suivre pour installer psql avec brew :

- Tout d’abord, installez le gestionnaire de paquets brew si vous ne l’avez pas déjà. Vous pouvez le faire en exécutant la commande suivante dans votre terminal :

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Ensuite, mettez à jour brew en exécutant les commandes suivantes :

```bash
brew doctor
brew update
```

- Troisièmement, installez libpq en exécutant la commande suivante :

```bash
brew install libpq
```

Libpq est une bibliothèque qui contient psql et d'autres utilitaires clients PostgreSQL.

- Quatrièmement, créez un lien symbolique de psql (et des autres outils libpq) dans /usr/local/bin en exécutant la commande :

```bash
brew link --force libpq
```

Cela rendra psql accessible depuis n’importe quel répertoire dans votre terminal.

- Cinquièmement, vérifiez la version de PostgreSQL en utilisant la commande psql :

```bash
psql --version
```

Vous devriez voir quelque chose comme ceci :

```bash
psql (PostgreSQL) 13.4
```

Félicitations, vous avez réussi à installer psql avec brew ! Vous pouvez maintenant utiliser psql pour vous connecter aux bases de données PostgreSQL et exécuter des requêtes SQL.
