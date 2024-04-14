---
title: "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"
time: 2003
author: UC Berkeley; Google Research; UC San Diego
link: https://arxiv.org/pdf/2003.08934.pdf
accepted: None
tags:
  - 3D
  - Theory
  - Generation
  - Foundation
  - Image
todo: false
scanned: true
read: false
summary: Use 2d images of a scene, NeRF learns a model to perform novel view synthesis.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20240414101437.png]]
NeRF learns a model (MLP) that takes spatial locations and view directions and output the predicted colors and densities of a scene. NeRF model will then use a technique called 'volume rendering’ to render 2d image by projecting predicted color and density into it, hence makes it possible to render 2d image in any viewpoints.

Since volume rendering is a differentiable process, by computing losses between the rendered images and the corresponding real images, NeRF model can update its weights by stochastic gradient descent and learns a good representation for the given scene.
# Methodology
💡 Describe the methodology used in this paper

# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [NeRF 論文筆記](https://zhuanlan.zhihu.com/p/360365941)
- [Novel View Synthesis 介紹](https://zhuanlan.zhihu.com/p/486710656)
![[Pasted image 20240414101313.png]]
![[Pasted image 20240414101404.png]]
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper