---
title: "InstructPix2Pix: Learning to Follow Image Editing Instructions"
time: 2211
author: University of California, Berkeley
link: https://arxiv.org/pdf/2211.09800.pdf
accepted: CVPR23
tags:
  - Image
  - Generation
  - Diffusion
  - Personalization
  - ImageEditing
todo: false
scanned: true
read: false
summary: A natrual language based generated image modifier.
---
# Summary
💡 Write a brief summary of this paper here
Training an instruction to image network on synthetic data obtained by combining GPT3 and [[Prompt-to-Prompt]] on [[Latent Diffusion]]
![[Pasted image 20240316171851.png]]
# Methodology
💡 Describe the methodology used in this paper
Their method consists of two parts
- Generating an image editing dataset
- Training a diffusion model on that dataset

They also modify the [[Classifier-Free Guidance]] with multiple conditioning:
![[Pasted image 20250112145107.png]]

# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
This is a follow-up work of [[Prompt-to-Prompt]]
# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
 - [Github Repo](https://github.com/timothybrooks/instruct-pix2pix)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper