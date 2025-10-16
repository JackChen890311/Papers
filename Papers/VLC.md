---
title: "Visual Layout Composer: Image-Vector Dual Diffusion Model for Design Layout Generation"
time: 2401
author: Simon Fraser University; Adobe Research
link: https://aminshabani.github.io/visual_layout_composer/pdfs/visual_layout_composer.pdf
accepted: CVPR24
tags:
  - Layout
  - Image
  - Diffusion
todo: false
scanned: true
read: false
summary: A diffusion based method for design layout generation given various assets.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20251015180131.png]]
# Methodology
💡 Describe the methodology used in this paper
- Contrary to the original Stable Diffusion, which uses text prompts, we pass the processed image condition feature as the input to the cross-attention layers
- Use attention score for information exchange between the image and vector
- Use cross attention loss from [[FastComposer]]
![[Pasted image 20251015180147.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
- [[FastComposer]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper