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
---

## Basic Perl "Hello World" Script (hello.pl)

Let's start with the basics. Here is a straightforward "Hello World" script written in Perl. Create a new file and name it `hello.pl`.

```perl
#!/usr/bin/perl
use strict;
use warnings;
use diagnostics;

print "-----------\n",
      "Hello World\n",
      "-----------\n";
```

In this script, we're using Perl's built-in modules for error handling (`use strict; use warnings; use diagnostics;`) to make sure the code is robust.

## Introducing Expect Bindings with Perl (test.pl)

Now, let's dive into the main topic: how to use Expect bindings in a Perl script. Create another file, `test.pl`, and add the following code:

```perl
#!/usr/bin/perl
use strict;
use warnings;
use diagnostics;
use Expect;

my $timeout = 5;  # set timeout to 5 seconds
for my $i (1..20) {  # loop 20 times
    my $exp = Expect->spawn("./hello.pl")  # execute the hello.pl script
        or die "Couldn't spawn the process: $!\n";
    $exp->expect($timeout);  # wait for the process to complete
}
```

In this example, the `Expect->spawn("./hello.pl")` line runs the `hello.pl` script, and we use the `expect` method to wait for it to finish. We've also set a timeout for the script, ensuring it doesn't hang indefinitely.
