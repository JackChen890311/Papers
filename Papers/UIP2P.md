---
title: "UIP2P: Unsupervised Instruction-based Image Editing via Cycle Edit Consistency"
time: 2412
author: ETH Zurich; Technical University of Munich; Google Switzerland
link: https://arxiv.org/pdf/2412.15216
accepted: ICLR25
tags:
  - Diffusion
  - Generation
  - Image
  - Text
  - Multimodal
  - ImageEditing
todo: false
scanned: false
read: true
summary: Unsupervised Instruct Pix2Pix with better performance.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20241228154907.png]]

They found that there are some bias incurred in the [[InstructPix2Pix]] dataset
![[Pasted image 20241229161139.png]]
# Methodology
💡 Describe the methodology used in this paper
Very insteresting method, kind of like GAN/Autoencoder.

![[Pasted image 20241228154949.png]]

Cycle Edit Consistency (CEC):
 - Text and Image Direction Consistency
   ![[Pasted image 20241229171024.png]]
 - Attention Map Consistency
   ![[Pasted image 20241229171137.png]]
 - Reconstruction Consistency
   ![[Pasted image 20241229171205.png]]
 - Unified Prediction with Varying Diffusion Steps
   ![[Pasted image 20241229171215.png]]
So the total loss:
![[Pasted image 20241229171334.png]]
# Experiments
💡 List the experiments settings and results of this paper
- Use LLM to generate instructions
![[Pasted image 20241229171453.png]]
![[Pasted image 20241229171537.png]]
# Related Papers
💡 Include any related papers that are relevant to this one
- [[InstructPix2Pix]]
- [[Prompt-to-Prompt]]
# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper