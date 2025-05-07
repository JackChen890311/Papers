---
title: High-Resolution Image Synthesis with Latent Diffusion Models
time: 2112
author: Ludwig Maximilian University of Munich; IWR, Heidelberg University, Germany; Runway ML
link: https://arxiv.org/pdf/2112.10752.pdf
accepted: None
tags:
  - Image
  - Generation
  - Diffusion
todo: false
scanned: true
read: false
summary: Generate images at latent space, also allowing conditioning.
---
# Summary
💡 Write a brief summary of this paper here
An improved version of [[Diffusion Models]] by using latent vector in [[AutoEncoder]] to do [[DDPM]] process, also widely know as stable diffusion (due to stability.ai)

# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20240116204134.png]]
- Cross attention method (Q from image latent, KV from conditioning)
  ![[Pasted image 20250507111646.png]]
- [ Understanding the switch in latent diffusion models](https://ai.stackexchange.com/questions/41714/understanding-the-functionality-of-the-switch-in-the-latent-diffusion-models-do)
	- Summary: Based on the format of conditioning, the switch will switch to different path (image/text/...)
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Github Repo - Latent Diffusion](https://github.com/CompVis/latent-diffusion)
- [Girhub Repo - Stable Diffusion](https://github.com/CompVis/stable-diffusion)
- [穩定擴散模型（Stable diffusion model）](https://www.zhangzhenhu.com/aigc/%E7%A8%B3%E5%AE%9A%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B.html)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper