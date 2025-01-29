---
title: "How to avoid other pods from being scheduled on your node in Kubernetes"
date: 2023-07-13T11:30:03+00:00
# weight: 1
# aliases: ["/first"]
# tags: ["first"]
author: "Me"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
# description: "Desc Text."
# canonicalURL: "https://canonical.url/to/page"
disableHLJS: true # to disable highlightjs
disableShare: false
disableHLJS: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
categories:
    - Development
# cover:
#     image: "<image path/url>" # image path/url
#     alt: "<alt text>" # alt text
#     caption: "<text>" # display caption under cover
#     relative: false # when using page bundles set this to true
#     hidden: true # only hide on current single page
# editPost:
#     URL: "https://github.com/<path_to_repo>/content"
#     Text: "Suggest Changes" # edit text
#     appendFilePath: true # to append file path to Edit link
---

Kubernetes is a powerful platform for managing containerized applications across a cluster of nodes. However, sometimes you may want to have more control over which pods are scheduled on which nodes, for various reasons such as performance, security, or cost.

## What are taints and tolerations?

Taints and tolerations are a feature of Kubernetes that allow you to mark nodes with certain attributes or conditions, and then specify which pods can or cannot be scheduled on those nodes based on those attributes or conditions. Taints are applied to nodes, and tolerations are applied to pods.

A taint consists of three components: a key, a value, and an effect. The key and the value are arbitrary strings that you can choose to identify the taint. The effect determines what happens to pods that do not tolerate the taint. There are three possible effects:

- `NoSchedule`: Pods that do not tolerate the taint are not scheduled on the node.
- `PreferNoSchedule`: Pods that do not tolerate the taint are preferably not scheduled on the node, but it is not guaranteed.
- `NoExecute`: Pods that do not tolerate the taint are not scheduled on the node, and any existing pods on the node that do not tolerate the taint are evicted.

A toleration consists of four components: a key, a value, an operator, and an effect. The key and the value must match the key and the value of the taint. The operator can be either `Equal` or `Exists`. The effect can be either `NoSchedule`, `PreferNoSchedule`, or `NoExecute`, or left empty (which means any effect).

A pod can tolerate a taint if one of its tolerations matches the taint according to the following rules:

- The keys must be equal.
- The values must be equal if the operator is `Equal`, or any value if the operator is `Exists`.
- The effects must match, or the toleration's effect must be empty.

## How to use taints and tolerations?

To use taints and tolerations, you need to apply them to your nodes and pods using kubectl commands or YAML manifests. Here are some examples of how to do that.

### Apply a taint to a node

To apply a taint to a node, you can use the following command:

`kubectl taint nodes <node-name> <key>=<value>:<effect>`

For example, if you want to mark a node as dedicated for database pods only, you can apply a taint with the key `type`, the value `db`, and the effect `NoSchedule`:

`kubectl taint nodes node1 type=db:NoSchedule`

This will prevent any pod from being scheduled on node1 unless it has a matching toleration.

### Apply a toleration to a pod

To apply a toleration to a pod, you can add it to the pod spec under the `tolerations` field. For example, if you want to allow a database pod to be scheduled on node1, you can add a toleration with the key `type`, the value `db`, and the operator `Equal`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db-pod
spec:
  containers:
  - name: db-container
    image: db-image
  tolerations:
  - key: type
    operator: Equal
    value: db
    effect: NoSchedule
```

This will allow the pod to tolerate the taint on node1 and be scheduled there.

### Remove a taint from a node

To remove a taint from a node, you can use the following command:

`kubectl taint nodes <node-name> <key>:<effect>-`

For example, if you want to remove the taint with the key `type` and the effect `NoSchedule` from node1, you can use:

`kubectl taint nodes node1 type:NoSchedule-`

This will allow any pod to be scheduled on node1 again.




Taints and tolerations are a useful feature of Kubernetes that allow you to control which pods are scheduled on which nodes. You can use them to isolate certain nodes for specific purposes, such as performance, security, or cost. You can also use them to avoid conflicts or interference between different types of pods. To use them effectively, you need to understand how they work and how to apply them correctly.