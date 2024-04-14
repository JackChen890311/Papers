---
title: "DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation"
time: 2208
author: Google Research; Boston University
link: https://arxiv.org/pdf/2208.12242.pdf
accepted: CVPR23
tags:
  - Image
  - Generation
  - Diffusion
  - Personalization
  - Multimodal
  - Text
todo: false
scanned: true
read: false
summary: A method for personalization on diffusion models with a class preservation loss.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20240211155402.png]]

# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20240211155109.png]]
- Finetune the model and identifier \[V\] together
- Besides from the identifier reconstruction loss, they also add a class-specific prior preservation loss
	- To prevent the possibility of language drift and reduced output diversity
- They also propose a method to find rare word for identifier initialization
# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20240413181420.png]]
# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Demo Page](https://dreambooth.github.io/)
- [Official Dataset](https://github.com/google/dreambooth)
- [Unofficial Implementation on Stable Diffusion](https://github.com/XavierXiao/Dreambooth-Stable-Diffusion)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper