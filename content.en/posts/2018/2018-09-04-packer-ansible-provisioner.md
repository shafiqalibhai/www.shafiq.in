---
title: A Simple Guide to Using Ansible with Packer
author: Shafiq Alibhai
date: 2018-09-04T11:08:49+00:00
categories:
  - Development

---

# What is the Ansible Provisioner in Packer?

If you're dabbling in the DevOps world, chances are you've come across Ansible and Packer. But how about combining them? The Ansible provisioner in Packer lets you run Ansible playbooks while creating your machine images. In simpler terms, it helps you set up your server environment automatically, just the way you like it, while Packer goes about its business creating a machine image.

> **Heads Up**: If you're specifying a `remote_user` in your Ansible tasks, know that Packer will bypass it. Packer connects using the username provided in its JSON configuration for this provisioner.

## A Working Example to Get You Started

Let's jump right in with a straightforward example that uses DigitalOcean as our cloud provider. Make sure to replace the placeholder API token with your actual DigitalOcean API token.

Here's the JSON configuration:

```json
{
  "provisioners": [
    {
      "type": "ansible",
      "playbook_file": "./playbook.yml"
    }
  ],

  "builders": [
    {
      "type": "digitalocean",
      "api_token": "YOUR_API_TOKEN_GOES_HERE",
      "image": "ubuntu-14-04-x64",
      "region": "sfo1"
    }
  ]
}
```

For more details, you can always check out the [official Packer documentation on Ansible provisioners](https://www.packer.io/docs/provisioners/ansible.html#basic-example).
