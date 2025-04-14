---
title: "An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion"
time: 2208
author: Tel Aviv University; NVIDIA
link: https://arxiv.org/pdf/2208.01618.pdf
accepted: None
tags:
  - Image
  - Diffusion
  - Generation
  - Personalization
  - Multimodal
  - Text
todo: false
scanned: true
read: false
summary: A method for simple personalization on diffusion models using text embedding.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20240314231718.png]]
# Methodology
💡 Describe the methodology used in this paper
Use a new token to represent the given concept (initializing using similar concept), then try to reconstruct it. Through out the whole training process, only text embedding is trainable. The trained text embedding is useful and can be combined with different prompts. 
![[Pasted image 20240314231741.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
- [[DreamBooth]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Github Repo](https://github.com/rinongal/textual_inversion)
- [Dataset](https://drive.google.com/drive/folders/1d2UXkX0GWM-4qUwThjNhFIPP7S6WUbQJ)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
Compared with [[DreamBooth]]
![[Pasted image 20250409140117.png]]