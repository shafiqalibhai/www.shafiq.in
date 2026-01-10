---
lang: "fr"
title: Perl – How to Read a Text File into a Variable – 6 ways to do it
author: Shafiq Alibhai
date: 2010-03-15T09:04:20+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1269438325";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1269438336";}'
categories:
  - Development
tags:
  - Git

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
