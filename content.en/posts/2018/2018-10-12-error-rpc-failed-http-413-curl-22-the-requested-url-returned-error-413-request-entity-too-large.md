---
title: 'How to Fix the "RPC failed; HTTP 413 curl 22" Error in Nginx'
author: Shafiq Alibhai
date: 2018-10-12T09:49:17+00:00
categories:
  - Development

---

## Understanding the Issue: 'RPC failed; HTTP 413 curl 22'

If you've stumbled upon the error message "RPC failed; HTTP 413 curl 22 The requested URL returned error: 413 Request Entity Too Large," you're probably trying to push a rather hefty commit over HTTP to your server running Nginx. This error means that the size of the request you're trying to send exceeds the limit that the server is willing to accept. So, how do you fix it?

## Nginx Solution: Updating the Configuration File

Don't fret; the solution is simpler than it sounds. Follow these steps to rid yourself of this error:

### Step 1: Locate Your Nginx Configuration File

The first thing you need to do is find your `nginx.conf` file. The location may differ based on your setup, but generally, you'll find it in `/etc/nginx/nginx.conf`.

### Step 2: Edit the Configuration File

Open the configuration file in a text editor of your choice. Scroll until you find one of the following blocks: `http`, `server`, or `location`.

### Step 3: Add or Update 'client_max_body_size'

Insert the line `client_max_body_size 50m;` within the block you've chosen. Feel free to change the `50m` to whatever size limit fits your needs.

### Step 4: Save and Close the File

Once you've made the change, save the file and exit the text editor.

### Step 5: Reload the Nginx Configuration

To make sure Nginx takes into account your new setting, reload the service by running the following command in your terminal:

```bash
sudo service nginx reload
```

### Step 6: Test the New Configuration

Go ahead and try to push your commit over HTTP once more. If all has gone well, the error should no longer appear.

## Wrap-Up

And there you have it! You've successfully increased the body size limit, resolving the "RPC failed; HTTP 413 curl 22" error. Happy coding!
