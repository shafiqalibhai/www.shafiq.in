---
title: A Simple Guide to Using Ansible with Packer
author: Shafiq Alibhai
date: 2018-09-04T11:08:49+00:00
categories:
  - Development

disableHLJS: false
---
# Qu'est-ce que le provisionneur Ansible dans Packer ?

Si vous vous êtes aventuré dans le monde du DevOps, il est fort probable que vous ayez déjà croisé Ansible et Packer. Mais comment combiner les deux ? Le provisionneur Ansible dans Packer vous permet d'exécuter des playbooks Ansible tout en créant vos images machine. Autrement dit, il vous aide à configurer votre environnement serveur automatiquement, exactement comme vous le souhaitez, pendant que Packer s'occupe de créer l'image machine.

> **Attention** : Si vous spécifiez un `remote_user` dans vos tâches Ansible, sachez que Packer va l'ignorer. Packer se connecte en utilisant le nom d'utilisateur fourni dans sa configuration JSON pour ce provisionneur.

## Un exemple fonctionnel pour bien commencer

Plongeons directement dans un exemple simple qui utilise DigitalOcean comme fournisseur cloud. N'oubliez pas de remplacer le jeton API en tant que placeholder par votre jeton API DigitalOcean réel.

Voici la configuration JSON :

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

Pour plus de détails, n'hésitez pas à consulter la [documentation officielle de Packer sur les provisionneurs Ansible](https://www.packer.io/docs/provisioners/ansible.html#basic-example).
