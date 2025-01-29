---
title: How to Hide a Column in jQuery DataTables Without Removing It From the DOM
author: Shafiq Alibhai
date: 2013-04-23T10:11:33+00:00
updated: 2023-10-06
categories:
  - Development
tags:
  - DataTables
  - JavaScript
  - jQuery
  - CSS

---

There are times when you may want to hide a column from view without actually removing it from the DOM. This can be useful if you want to keep the data accessible for other operations but don't want it visible on the front end.

## Quick Solution: Use CSS

One straightforward way to achieve this is by using CSS. This allows you to keep the column data in the DOM, but just not display it in the table.

### Step 1: Add a Class to the Column

You can add a class to the column you want to hide using the `sClass` attribute in DataTables.

```javascript
"sClass": "hide_column"
```

### Step 2: Define the Class in CSS

After assigning the class, you'll need to define it in your stylesheet. You can set the `display` property to `none` to hide the column.

```css
.hide_column {
    display: none;
}
```

And that's it! This way, the column will remain in the DOM, but it will be hidden from view in the DataTable.

## Why Would You Want to Do This?

You might be wondering why you'd want to hide a column but not remove it from the DOM. Here are a few scenarios where this can be handy:

1. **Data Processing**: You may want to keep the column accessible for data processing tasks without displaying it to users.

2. **Conditional Display**: Sometimes you might want to display the column based on certain conditions. Since the column is still in the DOM, it can be easily shown or hidden via JavaScript.

3. **Consistency**: Keeping the column in the DOM ensures that the table structure remains consistent, even when columns are toggled on or off.

4. **User Preferences**: You might want to allow users to customize which columns they can see, without affecting the data integrity or table structure.
