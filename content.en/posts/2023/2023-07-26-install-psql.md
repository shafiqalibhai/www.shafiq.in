---
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
disableHLJS: true # to disable highlightjs
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

Psql is a command-line interface for interacting with PostgreSQL, a powerful and open source relational database system. Brew is a package manager for macOS that makes it easy to install and manage software. Here are the steps to install psql with brew:

- First, install the brew package manager if you don't have it already. You can do this by running the following command in your terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Second, update brew by running the following commands:

```bash
brew doctor
brew update
```

- Third, install libpq by running the command:

```bash
brew install libpq
```

Libpq is a library that contains psql and other PostgreSQL client utilities.

- Fourth, symlink psql (and other libpq tools) into /usr/local/bin by running the command:

```bash
brew link --force libpq
```

This will make psql accessible from any directory in your terminal.

- Fifth, check the version of PostgreSQL using the psql command:

```bash
psql --version
```

You should see something like this:

```bash
psql (PostgreSQL) 13.4
```

Congratulations, you have successfully installed psql with brew! You can now use psql to connect to PostgreSQL databases and run SQL queries.
