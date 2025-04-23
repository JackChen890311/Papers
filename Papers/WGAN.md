---
title: Wasserstein GAN
time: 1701
author: "Courant Institute of Mathematical Sciences\r; Facebook AI Research"
link: https://arxiv.org/pdf/1701.07875
accepted: ICML17
tags:
  - Generation
  - Image
  - Loss
todo: false
scanned: true
read: false
summary: A improved GAN for solving the cold-start learning problem of JS divergence.
---
# Summary
💡 Write a brief summary of this paper here
The original [[JS Divergence]] will have some problem: When two distribution have no overlap, [[JS Divergence]] always equals log2. 
This paper propose to use [[Wasserstein Distance]] as loss for GAN training, and use gradient clipping as a simple and working method.
# Methodology
💡 Describe the methodology used in this paper
Earth Mover's Distance (or [[Wasserstein Distance]])
![[Pasted image 20250218175712.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [深度學習Paper系列(07)：Wasserstein GAN](https://tomohiroliu22.medium.com/%E6%B7%B1%E5%BA%A6%E5%AD%B8%E7%BF%92paper%E7%B3%BB%E5%88%97-07-wasserstein-gan-715d84f58545)
- [GAN Lecture 6 (2018): WGAN, EBGAN](https://www.youtube.com/watch?v=3JP-xuBJsyc)
![[Pasted image 20250218180609.png]]
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper