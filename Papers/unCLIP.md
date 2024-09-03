---
title: Hierarchical Text-Conditional Image Generation with CLIP Latents
time: 2204
author: OpenAI
link: https://arxiv.org/pdf/2204.06125.pdf
accepted: None
tags:
  - Diffusion
  - Generation
  - Image
  - Multimodal
  - Text
todo: false
scanned: true
read: false
summary: A text-to-image model that utilize pretrained CLIP model
---
# Summary
💡 Write a brief summary of this paper here
Also known as dalle-2.
Proposed a two-stage model:
- A prior that generates a CLIP image embedding given a text embedding (from text caption + encoder)
- A decoder that generates an image conditioned on the image embedding (GLIDE)
So there will be 2 losses:
- Prior: loss(zi, zi^) given y
- Decoder: loss(zt, zt^) given zi
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20240414164617.png]]
![[Pasted image 20240424233220.png]]

# Experiments
💡 List the experiments settings and results of this paper
- The authors demonstrate that applying a Prior and conditioning over the resulting image embeddings attains improved diversity while enabling image variations and interpolations
# Related Papers
💡 Include any related papers that are relevant to this one
- [[CLIP]]
# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [【DALLE·2/unCLIP】基於CLIP的分層文字條件影像生成](https://blog.csdn.net/weixin_45378275/article/details/129732266)
- [Everything you need to know about GLIDE and DALL-E 2](https://medium.com/@zaiinn440/everything-you-need-to-know-about-glide-and-dall-e-2-82902e3798f3)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper