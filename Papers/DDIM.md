---
title: DENOISING DIFFUSION IMPLICIT MODELS
time: 2010
author: Stanford University
link: https://arxiv.org/pdf/2010.02502.pdf
accepted: NeurIPS20
tags:
  - Image
  - Generation
  - Theory
  - Diffusion
todo: false
scanned: true
read: false
summary: "Use a non-Markovian\r diffusion processes that lead to the same training objective as DDPM"
---
# Summary
💡 Write a brief summary of this paper here
# Methodology
💡 Describe the methodology used in this paper

# Experiments
💡 List the experiments settings and results of this paper
By controling eta, we can obtain different results.
 - eta = 1 -> [[DDPM]]
 - eta = 0 -> [[DDIM]] (Deterministic, Same input noise will have same output image)
![[Pasted image 20240116205533.png]]
# Related Papers
💡 Include any related papers that are relevant to this one
- A improved model of [[DDPM]].
# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [DDIM 解讀](https://zhuanlan.zhihu.com/p/580106763)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
![[Pasted image 20240116205605.png]]
![[Pasted image 20240116205609.png]]
![[Pasted image 20240116205616.png]]