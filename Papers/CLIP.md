---
title: Learning Transferable Visual Models From Natural Language Supervision
time: 2103
author: OpenAI
link: https://arxiv.org/pdf/2103.00020.pdf
accepted: ICML21
tags:
  - Contrastive
  - Image
  - Text
  - Multimodal
  - Foundation
  - Zero-Shot
todo: false
scanned: true
read: false
summary: A powerful contrasitve foundation model for projecting text & image into a same latent space.
---
# Summary
💡 Write a brief summary of this paper here
- CLIP is pretrianed large text-image pair dataset LAION, and can be used for multiple downstream tasks
- Use the idea of contrastive learning to pull same text & image pair together while push others away
![[Pasted image 20240414102309.png]]
# Methodology
💡 Describe the methodology used in this paper
- The image encoder are ResNet series or [[ViT]] series
- The text encoder are GPT series
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [CLIP 介紹](https://blog.infuseai.io/openai-%E7%9A%84-multimodal-%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF-%E4%B8%8B-clip-connecting-text-and-images-2e9962905504)
- [Demo Page](https://openai.com/research/clip)
- [Github Repo](https://github.com/openai/CLIP)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper