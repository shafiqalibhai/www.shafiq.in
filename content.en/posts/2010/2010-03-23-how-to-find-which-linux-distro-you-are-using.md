---
title: How to Identify Your Linux Distribution and Version with Simple Commands
author: Shafiq Alibhai
date: 2010-03-23T05:10:33+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1269968925";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1269968930";}'
categories:
  - Development
tags:

---
If you are using a Linux-based operating system and you want to know which specific distribution and version you have installed, there is a simple command that can help you with that. Just open a terminal window and type the following:

```bash
cat /etc/issue
```

This will display the name and the release number of your Linux distribution. For example, if you are using Debian 4.0, the output will look like this:

```bash
Debian GNU/Linux 4.0 \n \l
```

The `\n` and `\l` are special characters that represent the current date and the name of the terminal device, respectively. They are not part of the distribution name.

This command works for most Linux distributions, but some may have different or additional ways to show their information. For example, Debian also has a file called `/etc/os-release` that contains more details about the distribution. You can read its contents with this command:

```bash
cat /etc/os-release
```

The output will look something like this:

```bash
PRETTY_NAME="Debian GNU/Linux 4.0 (etch)"
NAME="Debian GNU/Linux"
VERSION_ID="4.0"
VERSION="4.0 (etch)"
ID=debian
```

You can also use the `hostnamectl` command to get some information about your system, such as the kernel version, the architecture, and the machine ID. For example, to get only the kernel version, you can use this:

```bash
hostnamectl | grep Kernel
```

The output will be:

```bash
Kernel: Linux 2.6.18-6-686
```

To see all the available information from `hostnamectl`, you can use it without any arguments or read its manual page with `man hostnamectl`.
