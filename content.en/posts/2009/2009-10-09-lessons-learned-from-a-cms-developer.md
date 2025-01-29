---
title: Lessons Learned – from a cms developer
author: Shafiq Alibhai
date: 2009-10-09T07:32:57+00:00
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1275202511";}'
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1275202512";}'
categories:
  - Development
tags:
  - beta
  - cms
  - developer
  - hosting services
  - IP
  - lessons learned
  - root directory
  - Website

---

As a CMS developer, I have learned some valuable lessons over the years. Here are some of the most important ones that I want to share with you:

- **Never use the Root directory for your website; “forward” requests to a secondary directory.** This will make your website more secure and easier to manage. You can use .htaccess files or other methods to redirect requests from the root directory to a subdirectory where your CMS files are located.
- **Giving credit is nice; hackers will love you!** While it is good to acknowledge the developers and contributors of the CMS you are using, you should avoid displaying their names and links on your website. This will only attract hackers who can exploit the vulnerabilities of your CMS or plugins. You can still give credit in your source code or in a private page that only you can access.
- **“Everything isn’t always BETA.” STABLE works.** It is tempting to use the latest and greatest features of your CMS, but sometimes they are not fully tested or compatible with your existing setup. You should always backup your website before updating or installing new plugins, and stick to stable versions that have been proven to work well.
- **CMS do not equate to no web-editing or scripting—just less of it!** A CMS can make your life easier by providing you with a user-friendly interface and ready-made templates for creating and managing your website content. However, you still need some basic web-editing and scripting skills to customize your website according to your needs and preferences. You should also learn how to troubleshoot and fix any errors or issues that may arise with your CMS or plugins.
- **Commercial Hosting Services offer the Fantastico program for installing OS Applications. Why not?** Fantastico is a convenient tool that allows you to install various open source applications, including CMS, with just a few clicks. However, it may not always be the best option for your website. Some of the drawbacks of using Fantastico are: it may not install the latest version of the application, it may not allow you to choose your own database name or prefix, it may not update the application automatically, and it may not be compatible with some plugins or themes. You should always check the compatibility and requirements of the application before using Fantastico, and consider installing it manually if possible.
