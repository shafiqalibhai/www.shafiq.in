---
title: A Simple Guide to Installing Both Firefox 4 and Firefox 3 on Ubuntu
author: Shafiq Alibhai
date: 2011-02-07T07:03:39+00:00
categories:
  - Development
tags:
  - Advanced Packaging Tool
  - Browser
  - Firefox
  - Firefox 4.0
  - Mozilla Firefox 4
  - Ubuntu
  - Linux

---

### Step 1: Add the Mozilla Daily PPA Repository

First, open up your terminal window. Once it's up, type in the command below to add the Ubuntu Mozilla Daily PPA repository to your system:

```bash
sudo add-apt-repository ppa:ubuntu-mozilla-daily/ppa
```

You'll be prompted to enter your password. Go ahead and do that, then hit Enter to confirm the addition of the repository.

### Step 2: Update Your Package List

After adding the repository, it's crucial to update the package list to ensure you get the latest software. Type the following command:

```bash
sudo apt-get update
```

### Step 3: Install Firefox 4

Now, let's move on to the actual installation. To install Firefox 4, run the following command in your terminal:

```bash
sudo apt-get install firefox-4.0
```

### Step 4: Install Firefox 3

If you also want to install Firefox 3, you can do so by executing this command:

```bash
sudo apt-get install firefox
```

### Step 5: Launch Your Preferred Firefox Version

Once the installations are complete, you can launch either version of Firefox. You'll find them in your applications menu, or you can simply launch them from the terminal by typing `firefox-4.0` for Firefox 4 or `firefox` for Firefox 3.
