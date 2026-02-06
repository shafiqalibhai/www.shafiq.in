---
title: A Beginner's Guide to Perl Expect Bindings - A Simple Walkthrough
author: Shafiq Alibhai
date: 2012-02-21T07:18:05+00:00
categories:
  - Development
tags:
  - Expect
  - Perl
  - Automation
  - Beginners Guide
disableHLJS: false
---
## Script Perl basique "Hello World" (hello.pl)

Commençons par le commencement. Voici un script simple "Hello World" rédigé en Perl. Créez un nouveau fichier et nommez-le `hello.pl`.

```perl
#!/usr/bin/perl
use strict;
use warnings;
use diagnostics;

print "-----------\n",
      "Hello World\n",
      "-----------\n";
```

Dans ce script, nous utilisons les modules intégrés de Perl pour la gestion des erreurs (`use strict; use warnings; use diagnostics;`) afin de garantir que le code est robuste.

## Présentation des liaisons Expect avec Perl (test.pl)

Passons maintenant au sujet principal : comment utiliser les liaisons Expect dans un script Perl. Créez un autre fichier, `test.pl`, et ajoutez le code suivant :

```perl
#!/usr/bin/perl
use strict;
use warnings;
use diagnostics;
use Expect;

my $timeout = 5;  # définir le délai d'attente à 5 secondes
for my $i (1..20) {  # boucle 20 fois
    my $exp = Expect->spawn("./hello.pl")  # exécuter le script hello.pl
        or die "Impossible de lancer le processus : $!\n";
    $exp->expect($timeout);  # attendre que le processus se termine
}
```

Dans cet exemple, la ligne `Expect->spawn("./hello.pl")` exécute le script `hello.pl`, et nous utilisons la méthode `expect` pour attendre la fin de son exécution. Nous avons également défini un délai d'attente pour le script, afin d'éviter qu'il ne reste bloqué indéfiniment.
