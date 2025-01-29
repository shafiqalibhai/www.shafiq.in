---
title: CSS Browser Compatibility Improvement Tip
author: Shafiq Alibhai
date: 2009-06-06T10:09:09+00:00
reddit:
  - 'a:2:{s:5:"count";s:1:"0";s:4:"time";s:10:"1276059878";}'
delicious:
  - 'a:3:{s:5:"count";s:1:"0";s:9:"post_tags";s:0:"";s:4:"time";s:10:"1276389029";}'
categories:
  - Development
tags:
  - Browser
  - Browser Compatibility
  - HTML
  - IP
  - Padding

---
To avoid inconsistencies across different browsers, always use the following CSS code unless you specify a different value for padding and margin. Some browsers do not set these properties to zero by default.

```css
html {  
padding: 0px;  
margin: 0px;  
}  
body {  
padding: 0px;  
margin: 0px;  
}
```
