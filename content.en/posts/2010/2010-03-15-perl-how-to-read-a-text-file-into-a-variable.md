---
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

---


6 Ways to Read a Text File into a Variable

If you are working with large file(s) you might consider using File::Slurp.
 It is much fast than the conventional:

```perl
{
  local $/=undef;
  open FILE, "myfile" or die "Couldn't open file: $!";
  binmode FILE;
  $string = &lt;FILE>;
  close FILE;
}

{
  local $/=undef;
  open FILE, "myfile" or die "Couldn't open file: $!";
  $string = &lt;FILE>;
  close FILE;
}

open FILE, "myfile" or die "Couldn't open file: $!";
$string = join("", &lt;FILE>);
close FILE;
  
open FILE, "myfile" or die "Couldn't open file: $!";
while (&lt;FILE>){
 $string .= $_;
}
close FILE;

open( FH, "sample.txt") || die("Error: $!\n");
read(FH, $data, 2000);
close FH;
```

The format for the read function is:

`read(filehandle, destination, size/length);`

The example above will read 2000 bytes into the scalar variable $data.

```perl
  my $file = 'sample.txt';
  {
    local *FH;
    -f FH and sysread FH, my $file, -s FH;
  }
```
