---
title: "AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models without Specific Tuning"
time: 2307
author: The Chinese University of Hong Kong; Shanghai Artificial Intelligence Laboratory; Stanford University
link: https://arxiv.org/pdf/2307.04725.pdf
accepted: ICLR24
tags:
  - Image
  - Video
  - Multimodal
  - Add-on
todo: false
scanned: true
read: false
summary: Learned a transferable motion module for Text-to-Image models.
---
# Summary
💡 Write a brief summary of this paper here
AnimateDiff extends personalized text-to-image (T2I) models into an animation generator without model-specific tuning by learning transferable motion modules / priors from video data.
![[Pasted image 20240210154517.png]]
# Methodology
💡 Describe the methodology used in this paper
- Motion Module: Reshape input, then do self-attention along the time dimension with a zero-initialized output project layer.
	![[Pasted image 20240210154531.png]]
- ICLR24 Model Sturcture
	- Three Stages: Domain Adapter, Motion Module, Motion LoRA
![[Pasted image 20240210154421.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Demo Page](https://animatediff.github.io/)
- [Github Repo](https://github.com/guoyww/AnimateDiff)
- [First version of this paper](https://arxiv.org/pdf/2307.04725.pdf)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper