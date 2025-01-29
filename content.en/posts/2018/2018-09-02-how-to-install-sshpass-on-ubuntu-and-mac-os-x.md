---
title: A Simple Guide to Installing SSHPass on Ubuntu and macOS
author: Shafiq Alibhai
date: 2018-09-02T10:33:49+00:00
categories:
  - Development
---

# Introduction

SSHPass is a nifty little tool that lets you automate SSH login by bypassing the usual password prompt. While it's super convenient for scripting, bear in mind that it's not ideal for a multi-user setup due to security concerns. However, if you're using it on your personal development machine, it's pretty harmless.

## How to Install SSHPass on Ubuntu

Installing SSHPass on Ubuntu is as straightforward as it gets. All you need to do is open up your terminal and run the following command:

```bash
sudo apt-get install sshpass
```

## Installing SSHPass on macOS

Setting up SSHPass on a Mac requires a bit more legwork because there's no official macOS version. But don't fret; it's not too complicated. First off, you need to have Xcode and command-line tools installed on your system.

### How to Install Using Homebrew

Unfortunately, the standard Homebrew repository doesn't offer `sshpass`. However, there's an alternative formula that you can use. Open your terminal and execute the following command:

```bash
brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb
```

That's it! You've successfully installed SSHPass on your machine, be it Ubuntu or macOS. Happy scripting!

For more information, you can check out these useful resources:

- [SSHPass Official Documentation](http://www.cyberciti.biz/faq/noninteractive-shell-script-ssh-password-provider/)
- [Homebrew Official Site](http://brew.sh/)
  
Remember, while SSHPass is a handy tool, it's not the most secure option out there. So be cautious about where and how you use it.
