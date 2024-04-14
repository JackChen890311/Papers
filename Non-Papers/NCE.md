---
tags:
  - Loss
  - Contrastive
todo: false
summary: A sampling based loss for contrastive learning
---
# Summary
💡 Write a brief summary of this paper here
NCE stands for Noise-Contrastive **Estimation**.
X- will be sampled from the negative set, thus improving computational efficiency.
This can be seen as Binary [[Cross Entropy]] between data pairs (Binary classification).

![[Pasted image 20240409123147.png]]
# Resources
💡 Include some useful links or related papers for better understanding of this concept
- [Original Paper](https://arxiv.org/pdf/1410.8251.pdf)
- [對比學習介紹](https://u9534056.medium.com/%E9%9D%A2%E8%A9%A6%E5%BF%85%E5%82%99-%E5%B0%8D%E6%AF%94%E5%AD%B8%E7%BF%92-contrastive-learning-%E4%B8%BB%E6%B5%81%E6%96%B9%E6%B3%95%E4%B8%80%E8%A6%BD-bddf2afc5e5f)
- [InfoNCE Loss 損失函數](https://blog.csdn.net/qq_46006468/article/details/126076039)
- [比較學習損失（InfoNCE loss）與交叉熵損失的聯繫，以及溫度係數的作用](https://zhuanlan.zhihu.com/p/506544456)