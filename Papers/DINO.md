---
title: Emerging Properties in Self-Supervised Vision Transformers
time: 2104
author: "Facebook AI Research; \rInria; Sorbonne University"
link: https://arxiv.org/pdf/2104.14294
accepted: ICCV21
tags:
  - Contrastive
  - Foundation
  - Image
todo: false
scanned: true
read: false
summary: A Self-supervised based vision model, strong and robust, can be used as backbone for multiple downstream tasks.
---
# Summary
💡 Write a brief summary of this paper here
Three main concepts that makes up DINO:
- Self-Supervised Learning (SSL)
- Teacher-Student
- Knowledge Distillation
![[Pasted image 20240523185407.png]]
# Methodology
💡 Describe the methodology used in this paper
- Align student output with teacher output
- Teacher model is updated by ema
- x1: Local views, x2: Global views
![[Pasted image 20240523185419.png]]

![[Pasted image 20240523185433.png]]
# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20240531144356.png]]

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [自監督DINO論文筆記](https://blog.csdn.net/hello_dear_you/article/details/133695006)
- [Meta发布的自监督ViT DINO的发展史：从DINO、DINOv2到通用视觉特征提取器DINOv3](https://blog.csdn.net/v_JULY_v/article/details/144622001)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
![[Pasted image 20240523185724.png]]
![[Pasted image 20240523185740.png]]