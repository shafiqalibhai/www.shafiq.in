---
title: "Kubernetes Tolerations"
date: 2023-07-11T01:30:03+00:00
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
---

Kubernetes tolerations are a way of allowing pods to be scheduled on nodes that have taints, which are markers that repel pods by default. Tolerations let you control which pods can run on which nodes, based on the pod's requirements and the node's characteristics.

## What are Kubernetes tolerations?

Kubernetes tolerations are a pod property that allow a pod to be scheduled on a node with a matching taint. Taints are the opposite of node affinity, which is a way of attracting pods to a set of nodes. Taints are applied to nodes and act as a repelling barrier against new pods. Tainted nodes will only accept pods that have been marked with a corresponding toleration.

Tolerations are specified in the pod spec, under the `tolerations` field. A toleration consists of three components: a key, an operator, and an effect. The key and the operator are used to match the toleration with the taint. The effect determines how the scheduler behaves when it encounters the taint.

There are three possible effects for taints and tolerations:

- `NoSchedule`: Pods that do not tolerate the taint will not be scheduled on the node. Pods that are already running on the node are not affected.
- `PreferNoSchedule`: Pods that do not tolerate the taint will be avoided by the scheduler, but they may still be scheduled on the node if there are no other options.
- `NoExecute`: Pods that do not tolerate the taint will be evicted from the node if they are already running, and they will not be scheduled on the node in the future.

The operator can be either `Equal` or `Exists`. The `Equal` operator requires that the key and the value of the taint match exactly with the key and the value of the toleration. The `Exists` operator only requires that the key of the taint matches with the key of the toleration, regardless of the value.

Here is an example of a pod spec with a toleration:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  tolerations:
  - key: "example-key"
    operator: "Exists"
    effect: "NoSchedule"
```

This pod has a toleration for any taint with the key `example-key` and the effect `NoSchedule`. This means that it can be scheduled on any node that has such a taint, but it will not tolerate any other taints.

## How to use Kubernetes tolerations?

To use Kubernetes tolerations, you need to apply taints to your nodes first. You can do this using the `kubectl taint` command. For example, to apply a taint with the key `example-key`, the value `example-value`, and the effect `NoSchedule` to a node named `node1`, you can run:

```bash
kubectl taint nodes node1 example-key=example-value:NoSchedule
```

To remove a taint from a node, you can add a `-` at the end of the command:

```bash
kubectl taint nodes node1 example-key=example-value:NoSchedule-
```

You can also apply multiple taints to a node at once, or remove multiple taints at once, by separating them with spaces:

```bash
kubectl taint nodes node1 example-key=example-value:NoSchedule another-key=another-value:PreferNoSchedule
kubectl taint nodes node1 example-key=example-value:NoSchedule- another-key=another-value:PreferNoSchedule-
```

To view the taints on your nodes, you can use the `kubectl describe` command:

```bash
kubectl describe nodes node1
```

You should see something like this in the output:

```text
Name:               node1
Roles:              <none>
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/hostname=node1
Annotations:        <none>
Taints:             example-key=example-value:NoSchedule
                    another-key=another-value:PreferNoSchedule
...
```

Once you have applied taints to your nodes, you can create pods with tolerations that match them. You can do this by adding the `tolerations` field to your pod spec, as shown in the previous example. You can also use a pod template to create multiple pods with the same tolerations, such as in a deployment or a daemonset.

## Use cases for Kubernetes tolerations

Kubernetes tolerations can be used for various scenarios where you want to control which pods can run on which nodes, based on the pod's requirements and the node's characteristics. Here are some common use cases for tolerations:

- Isolating nodes for specific workloads: You may have some nodes that are dedicated for certain types of workloads, such as GPU-intensive applications, or sensitive data processing. You can taint these nodes with a unique key and value, and only allow pods that have a matching toleration to run on them. This way, you can ensure that these nodes are not used by other pods that do not need them, and that your special workloads have access to the resources they need.
- Reserving nodes for high-priority pods: You may have some pods that are more critical than others, such as system components, or pods that handle user requests. You can taint some nodes with a high-priority key and value, and only allow pods that have a matching toleration to run on them. This way, you can ensure that these nodes are not occupied by low-priority pods that could interfere with the performance or availability of your high-priority pods.
- Avoiding nodes with performance issues: You may have some nodes that are experiencing performance issues, such as high CPU load, memory pressure, or network congestion. You can taint these nodes with a key and value that indicate the problem, and use the `PreferNoSchedule` effect to discourage pods from being scheduled on them. This way, you can avoid placing more load on these nodes, and give them a chance to recover. You can also use the `NoExecute` effect to evict pods that are already running on these nodes, if you want to free up the resources more quickly.
