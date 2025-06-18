---
title: "Diffuse, Attend, and Segment: Unsupervised Zero-Shot Segmentation using Stable Diffusion"
time: 2308
author: Georgia Institute of Technology; Google
link: https://arxiv.org/pdf/2308.12469
accepted: CVPR24
tags:
  - Segmentation
  - Diffusion
  - Image
todo: false
scanned: true
read: false
summary: "An unsupervised and\r zero-shot segmentation algorithm using a pre-trained stable diffu\rsion model."
---
# Summary
💡 Write a brief summary of this paper here
Utilize the self-attention layers in stable diffusion models to achieve unsupervised segmentation.
- The pre-trained stable diffusion model has learned inherent concepts of objects within its attention layers
![[Pasted image 20250130135751.png]]
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20250301182803.png]]
- When extracting attention maps, they set t = 300 and run diffusion process only once
![[Pasted image 20250513214836.png]]
# Experiments
💡 List the experiments settings and results of this paper
Refer to [[DiffuMask]] for semantic segmentation.
- Utilizing cross attention
![[Pasted image 20250301185620.png]]
# Related Papers
💡 Include any related papers that are relevant to this one
- [[DiffuMask]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before
- [[LDM]] Architecture
![[Pasted image 20250301195344.png]]

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Github Repo](https://github.com/google/diffseg)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper