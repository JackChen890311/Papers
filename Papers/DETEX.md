---
title: Decoupled Textual Embeddings for Customized Image Generation
time: 2312
author: "\rInstitute of Computing Technology, Chinese Academy of Sciences\r; Harbin Institute of Technology; Tomorrow Advancing Life; Pengcheng Lab"
link: https://arxiv.org/pdf/2312.11826
accepted: AAAI24
tags:
  - ConceptLearning
  - Diffusion
  - Generation
  - Image
  - Personalization
todo: false
scanned: true
read: false
summary: A method for personalization that decoupled the subject with pose and background information.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20250409135154.png]]
# Methodology
💡 Describe the methodology used in this paper
Their method is based on [[Custom-Diffusion]].
![[Pasted image 20250409135229.png]]

# Experiments
💡 List the experiments settings and results of this paper
They utilized foreground (FG) CLIP and DINO score to rule out the influence of background.
![[Pasted image 20250420191806.png]]
![[Pasted image 20250420191818.png]]
# Related Papers
💡 Include any related papers that are relevant to this one
- [[ViCo]]
- [[DreamBooth]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before
They also apply masked diffusion loss like [[Break-A-Scene]]. (Appendix B.1)

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Github Repo](https://github.com/PrototypeNx/DETEX/tree/main)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper