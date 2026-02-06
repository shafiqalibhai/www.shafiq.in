---
title: Perl – How to Read a Text File into a Variable – 6 ways to do it
author: Shafiq Alibhai
date: 2010-03-15T09:04:20+00:00
categories:
  - Development
tags:
  - perl
  - file-handling
  - tutorial
  - code-snippet

disableHLJS: false
---
6 façons de lire un fichier texte dans une variable

Si vous travaillez avec des fichiers volumineux, vous pourriez envisager d'utiliser File::Slurp.  
Il est bien plus rapide que la méthode conventionnelle :

```perl
{
  local $/=undef;
  open FILE, "myfile" or die "Couldn't open file: $!";
  binmode FILE;
  $string = <FILE>;
  close FILE;
}

{
  local $/=undef;
  open FILE, "myfile" or die "Couldn't open file: $!";
  $string = <FILE>;
  close FILE;
}

open FILE, "myfile" or die "Couldn't open file: $!";
$string = join("", <FILE>);
close FILE;
  
open FILE, "myfile" or die "Couldn't open file: $!";
while (<FILE>) {
 $string .= $_;
}
close FILE;

open( FH, "sample.txt") || die("Error: $!\n");
read(FH, $data, 2000);
close FH;
```

Le format de la fonction read est :

`read(filehandle, destination, size/length);`

L'exemple ci-dessus lit 2000 octets dans la variable scalaire $data.

```perl
  my $file = 'sample.txt';
  {
    local *FH;
    -f FH and sysread FH, my $file, -s FH;
  }
```
