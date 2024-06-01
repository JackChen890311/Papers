---
title: "StableRep: Synthetic Images from Text-to-Image Models Make Strong Visual Representation Learners"
time: 2306
author: Google Research; MIT CSAIL
link: https://arxiv.org/pdf/2306.00984
accepted: NeurIPS24
tags:
  - Contrastive
  - Diffusion
  - Image
  - LLM
  - Multimodal
  - Text
todo: false
scanned: true
read: false
summary: A contrastive method for learning visual representation with synthetic image
---
# Summary
💡 Write a brief summary of this paper here
They view text-to-image models (such as [[Latent Diffusion]]) as datasets, which can be sampled from.
![[Pasted image 20240501152918.png]]
# Methodology
💡 Describe the methodology used in this paper
- Comparison with [[SimCLR]] and [[CLIP]] 
![[Pasted image 20240501153025.png]]
- Multi-positive contrastive loss
  ![[Pasted image 20240501153906.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Github Repo](https://github.com/google-research/syn-rep-learn/tree/main)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper