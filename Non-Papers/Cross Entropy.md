---
tags:
  - Metric
  - Loss
todo: false
summary: A classic loss for classification.
---
# Summary
💡 Write a brief summary of this paper here
Actually it's just a special case of [[KL Divergence]] when P,Q = P, P*, so it means Cross Entropy can be used to calculated the distance of two distributions. 
P* is real data distribution while P is predicted data distribution.
Binary Cross Entropy is just Cross Entropy with only two classes.

![[Pasted image 20240405191824.png]]
# Resources
💡 Include some useful links or related papers for better understanding of this concept
- [Cross Entropy 介紹](https://hackmd.io/PjUEbxbeSA2qNbRupRzYMw)
- [何謂 Cross-Entropy](https://r23456999.medium.com/%E4%BD%95%E8%AC%82-cross-entropy-%E4%BA%A4%E5%8F%89%E7%86%B5-b6d4cef9189d)
- [nn.CrossEntropyLoss](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)
- [nn.BCELoss](https://pytorch.org/docs/stable/generated/torch.nn.BCELoss.html)