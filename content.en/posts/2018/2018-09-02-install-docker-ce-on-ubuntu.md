---
title: A Simple Guide to Installing Docker CE on Ubuntu
author: Shafiq Alibhai
date: 2018-09-02T09:09:10+00:00
categories:
  - Development
---

## What You Need Before You Begin

### Operating System Requirements

First things first, make sure you're running one of the following 64-bit Ubuntu versions to install Docker CE:

* Ubuntu 18.04 (Bionic) - LTS
* Ubuntu 17.10 (Artful)
* Ubuntu 16.04 (Xenial) - LTS
* Ubuntu 14.04 (Trusty) - LTS

Docker CE is compatible with these architectures: `x86_64`, `armhf`, `s390x` (IBM Z), and `ppc64le` (IBM Power).

> **Note**: For IBM Z and Power architectures, you'll need at least Ubuntu 16.04 (Xenial) or higher.

### Out with the Old

If you've had older versions of Docker installed, it’s a good idea to get rid of them first:

```bash
sudo apt-get remove docker docker-engine docker.io
```

Don't worry if `apt-get` says that none of these packages exist. It's fine. Your old files in `/var/lib/docker/`, such as images and containers, won't be deleted.

### Storage Driver Info

Docker CE supports `overlay2` and `aufs` storage drivers on Ubuntu.

* For Linux kernel version 4 or higher, `overlay2` is the recommended choice.
* If you’re on Linux kernel version 3, go with `aufs`.

If you need to use `aufs`, there's some additional setup, but we won't get into that here.

## Let's Install Docker CE

### Step-by-Step: Using a Repository

Before you can enjoy the perks of Docker CE, you have to set up its repository. Once that’s done, you can easily install or update Docker.

#### Setting Up the Docker Repository

1. Update your package list:

   ```bash
   sudo apt-get update
   ```

2. Install some required packages:

   ```bash
   sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
   ```
  
3. Add Docker's GPG key for secure downloads:

   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   ```

   Check if the key has the fingerprint `9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88`:

   ```bash
   sudo apt-key fingerprint 0EBFCD88
   ```

4. Finally, add the Docker repository:

   ```bash
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   ```

   > **Note**: If you’re adventurous and want to try the **edge** or **test** versions, you can add them to the repository command above.

#### Time to Install Docker CE

1. Refresh your package list again:

   ```bash
   sudo apt-get update
   ```
  
2. Install Docker CE:

   ```bash
   sudo apt-get install docker-ce
   ```

   If you want a specific version, first list the available ones:

   ```bash
   apt-cache madison docker-ce
   ```

   Then install the version you want:

   ```bash
   sudo apt-get install docker-ce=<VERSION>
   ```

3. Test your installation by running:

   ```bash
   sudo docker run hello-world
   ```

Docker CE should now be up and running on your machine. Initially, you'll need to use `sudo` for Docker commands. To enable non-root access, check out further [Linux post-install steps](https://docs.docker.com/install/linux/linux-postinstall/).
