---
title: "FastComposer: Tuning-Free Multi-Subject Image Generation with Localized Attention"
time: 2305
author: MIT
link: https://arxiv.org/pdf/2305.10431
accepted: IJCV25
tags:
  - ConceptLearning
  - Personalization
  - Diffusion
  - Text
  - Image
  - Generation
todo: false
scanned: true
read: false
summary: A method for multi-subject personalization without fine-tuning using localized attention.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20250919173337.png]]
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20250919173404.png]]
## Cross Attention Localization
- We observe that traditional cross-attention maps tend to attend to all subjects at the same time, which leads to identity blending in multi-subject image generation (Figure 4 top). 
- We propose to localize cross-attention maps with subject segmentation masks during training to solve this issue.
![[Pasted image 20251015182652.png]]
![[Pasted image 20251015183050.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
- [[Textual Inversion]]
- [[Custom-Diffusion]]
- [[Prompt-to-Prompt]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper