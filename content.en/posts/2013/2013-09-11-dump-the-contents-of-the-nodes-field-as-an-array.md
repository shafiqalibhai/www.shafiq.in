---
title: How to Display the Contents of a Node's Field as an Array in Drupal 6
author: Shafiq Alibhai
date: 2013-09-11T09:32:05+00:00
categories:
  - Development
tags:
  - Drupal 6
  - Debugging
  - PHP
  - Web Development
---

When you're working with Drupal 6, it's sometimes necessary to inspect the data stored in a node's field. This is especially useful for debugging or when you're trying to understand the structure of the content better. One quick way to achieve this is by dumping the field contents as an array. In PHP, the `var_export()` function comes in handy for this purpose.

Here's how to do it:

```php
var_export(content_fields('field_name_of_the_field', 'name_of_the_content_type'));
```

In this snippet, replace `'field_name_of_the_field'` with the actual name of the field you're interested in and `'name_of_the_content_type'` with the specific content type containing that field.

This simple line of code will output the field's content as an array, making it easier for you to analyze its structure and content.
