---
title: 'Decoding the Error: StatusCode=0 "ReferencedResourceNotProvisioned" in Azure'
author: Shafiq Alibhai
date: 2018-12-22T09:38:39+00:00
categories:
  - Development
---

## Introduction

If you're working with Azure, you might have encountered an error that looks something like this:

> "Failure sending request: StatusCode=0 — Original Error: Code='ReferencedResourceNotProvisioned' Message='Cannot proceed with operation because resource used by resource is not in Succeeded state. Resource is in Updating state and the last operation that updated/is updating the resource is PutSubnetOperation.'"

Though the error message can seem intimidating and cryptic at first, don't worry. In this post, we'll delve into what this error means and how you can resolve it.

## Why Does This Error Occur?

The error message tells us that the operation you're trying to perform can't proceed because a related resource is in an 'Updating' state rather than a 'Succeeded' state. This usually happens when there's an ongoing operation on the same or a related resource, preventing Azure from executing the operation you've requested.

## A Practical Solution

While it may be tempting to start troubleshooting immediately, there is a relatively simple fix for this. You can adjust the number of simultaneous operations with Azure's API by setting the `-parallelism` flag. Setting it to 1 can often resolve this issue:

```bash
terraform apply -parallelism=1
```

## How Does This Work?

When you limit the number of parallel operations to 1, you're essentially telling Azure to focus on completing one operation at a time. This usually allows ongoing operations to complete, freeing up the resource to reach a 'Succeeded' state, and thus resolving the error.

While encountering errors during development can be frustrating, understanding what's behind them and how to fix them is part of the journey. The next time you find yourself up against a `StatusCode=0 "ReferencedResourceNotProvisioned"` error, remember to try adjusting the `-parallelism` flag. It's a simple yet effective way to clear the roadblocks in your Azure adventures.
