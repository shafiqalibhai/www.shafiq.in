---
title: '[solved] xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist'
author: Shafiq Alibhai
date: 2018-09-06T09:43:25+00:00
categories:
  - Development

---
Error:

xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist  
Use `sudo xcode-select --switch path/to/Xcode.app` to specify the Xcode that you wish to use for command line developer tools, or use `xcode-select --install` to install the standalone command line developer tools.  
See `man xcode-select` for more details.  
xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist  
Use `sudo xcode-select --switch path/to/Xcode.app` to specify the Xcode that you wish to use for command line developer tools, or use `xcode-select --install` to install the standalone command line developer tools.  
See `man xcode-select` for more details.

Solution:

**sudo xcode-select -reset**
