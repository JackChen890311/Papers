---
title: "Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models"
time: 2301
author: Tel Aviv University
link: https://arxiv.org/pdf/2301.13826
accepted: ACM23
tags:
  - ConceptLearning
  - Diffusion
  - Generation
  - Image
  - Personalization
todo: true
scanned: false
read: false
summary: A attention based loss term for improving semantic generation.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20250227174234.png]]

# Methodology
💡 Describe the methodology used in this paper
They found that stable diffusion will have some failure cases:
![[Pasted image 20250227181909.png]]

And propose a attention based loss term for improvement:
- Identify the most neglected patch of subjects
- Add it to loss (max L => min (max(G(A))) => minimum of maximum of attention maps => most neglected attended patch)

![[Pasted image 20250227181930.png]]
# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20250227190455.png]]
# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Github Repo](https://github.com/yuval-alaluf/Attend-and-Excite)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper