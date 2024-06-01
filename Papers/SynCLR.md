---
title: Learning Vision from Models Rivals Learning Vision from Data
time: 2312
author: Google Research; MIT CSAIL
link: https://arxiv.org/pdf/2312.17742
accepted: None
tags:
  - Contrastive
  - Diffusion
  - Image
  - Multimodal
  - Text
  - LLM
todo: false
scanned: true
read: false
summary: A contrastive method for learning visual representation with all synthetic data
---
# Summary
💡 Write a brief summary of this paper here
Compared to previous works ([[CLIP]] and [[StableRep]]), this paper use synthetic data on both text and image domain.

![[Pasted image 20240501152248.png]]
# Methodology
💡 Describe the methodology used in this paper
- Text generation (Using LLaMa 2 7B)
  ![[Pasted image 20240501152441.png]]
- Image Generation (Using SD 1.5)
  ![[Pasted image 20240501152518.png]]
- Comtrastive method follows [[StableRep]], but includes some more techniques
  ![[Pasted image 20240501152629.png]]
# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20240501152556.png]]
# Related Papers
💡 Include any related papers that are relevant to this one
- [[StableRep]]
# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Github Repo](https://github.com/google-research/syn-rep-learn/tree/main)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper