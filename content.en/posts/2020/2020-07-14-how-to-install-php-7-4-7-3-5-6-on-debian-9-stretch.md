---
title: 'How To Install PHP (7.4, 7.3 & 5.6) on Debian 9 Stretch'
author: Shafiq Alibhai
date: 2020-07-14T09:11:45+00:00
categories:
  - Development

---
## Prerequisites

Login to your Debian 9 system using shell access. For remote systems connect with SSH. Windows users can use Putty or other alternatives applications for SSH connection.

```bash
ssh root@debian9
```

Run below commands to upgrade the current packages to the latest version.

```bash
sudo apt update 
sudo apt upgrade
```

Let's execute the following commands to install the required packages first on your system. Then import packages signing key. After that configure PPA for the PHP packages on your system.

```bash
sudo apt install ca-certificates apt-transport-https 
wget -q https://packages.sury.org/php/apt.gpg -O- | sudo apt-key add -
echo "deb https://packages.sury.org/php/ stretch main" | sudo tee /etc/apt/sources.list.d/php.list
```

Now use one of the below options to install PHP of your requirements.

## Installing PHP 7.4

You can also install the latest PHP version on your system. Run the following commands to install PHP 7.4 on Debian 9.

```bash
sudo apt update
sudo apt install php7.4
```

Also install required php modules.

```bash
sudo apt install php7.4-cli php7.4-common php7.4-curl php7.4-mbstring php7.4-mysql php7.4-xml
```

## Installing PHP 7.3

You can also install the latest PHP version on your system. Run the following commands to install PHP 7.3 on Debian 9.

```bash
sudo apt update
sudo apt install php7.3
```

Also install required php modules.

```bash
sudo apt install php7.3-cli php7.3-common php7.3-curl php7.3-mbstring php7.3-mysql php7.3-xml
```

## Installing PHP 7.2

You can also install the latest PHP version on your system. Run the following commands to install PHP 7.2 on Debian 9.

```bash
sudo apt update
sudo apt install php7.2
```

Also install required php modules.

```bash
sudo apt install php7.2-cli php7.2-common php7.2-curl php7.2-mbstring php7.2-mysql php7.2-xml
```

## Installing PHP 7.1

If your application has the specific requirement of PHP 7.1, You can use the following commands for installing PHP 7.1 on Debian 9 Stretch system.

```bash
sudo apt update
sudo apt install php7.1
```

Also, install the required PHP modules as per your requirements. Here is a list of some frequently used modules.

```bash
sudo apt install php7.1-cli php7.1-common php7.1-curl php7.1-mbstring php7.1-mysql php7.1-xml
```

## Installing PHP 5.6

Execute the following commands for installing PHP 5.6 on your Debian 9 Stretch system.

```bash
sudo apt update
sudo apt install php5.6
```

Also install required php modules.

```bash
sudo apt install php5.6-cli php5.6-common php5.6-curl php5.6-mbstring php5.6-mysql php5.6-xml
```
