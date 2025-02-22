---
tags:
  - Metric
  - Loss
todo: false
summary: A improved metric / loss to evaluate distance between two distributions (symmetric).
---
# Summary
💡 Write a brief summary of this paper here
Based on [[KL Divergence]], JS divergence is a symmetric metric to calculate the distance between two distribution.
![[Pasted image 20240405191520.png]]

Problem:
When P and Q do not have any overlap, JS divergence always equals log 2, hence not able to learn. ([[WGAN]])
# Resources
💡 Include some useful links or related papers for better understanding of this concept
- [JS Divergence 介紹](https://hackmd.io/@kk6333/B1MwuGLei)