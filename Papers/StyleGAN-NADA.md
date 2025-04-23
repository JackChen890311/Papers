---
title: "StyleGAN-NADA: CLIP-Guided Domain Adaptation of Image Generators"
time: 2108
author: Tel-Aviv University; NVIDIA
link: https://arxiv.org/pdf/2108.00946
accepted: ACM22
tags:
  - Generation
  - Image
  - DomainAdaptation
todo: false
scanned: true
read: false
summary: A framework that can perform domain adaptation using only text guidance with CLIP.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20241229174048.png]]
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20241229181819.png]]
But this will cause some problems
![[Pasted image 20241229181912.png]]
So they use Directional CLIP Loss
![[Pasted image 20241229181656.png]]
With adaptive layer freezing (only train some layers)
![[Pasted image 20241229182205.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [StyleGAN-NADA: CLIP-Guided Domain Adaptation of Image Generators](https://stylegan-nada.github.io/)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper