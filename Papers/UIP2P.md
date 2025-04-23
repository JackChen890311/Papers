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
summary: Unsupervised InstructPix2Pix with better performance.
---
# Summary
💡 Write a brief summary of this paper here
Main task: Instruction based image editing.
![[Pasted image 20241228154907.png]]

Limitations of previous work:
- [[InstructPix2Pix]] trained on only synthetic data
- Its abilities are constrained by the quality of [[Prompt-to-Prompt]],  which introduces biases
![[Pasted image 20241229161139.png]]
# Methodology
💡 Describe the methodology used in this paper
Very insteresting method, kind of like Autoencoder (Original -> Editted -> Original).
![[Pasted image 20241228154949.png]]

Cycle Edit Consistency (CEC):
 - CLIP Direction Loss
   ![[Pasted image 20241229171024.png]]
 - Attention Map Consistency Loss
   ![[Pasted image 20241229171137.png]]
 - CLIP Similarity Loss
   ![[Pasted image 20241229171205.png]]
 - Reconstruction Loss
   ![[Pasted image 20241229171215.png]]
So the total loss:
![[Pasted image 20241229171334.png]]
# Experiments
💡 List the experiments settings and results of this paper
- Implementation
![[Pasted image 20250112150327.png]]
- Use LLM to generate instructions
![[Pasted image 20241229171453.png]]
![[Pasted image 20241229171537.png]]
![[Pasted image 20250110151553.png]]
# Related Papers
💡 Include any related papers that are relevant to this one
- [[InstructPix2Pix]]
- [[Prompt-to-Prompt]]
- [[HIVE]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [CC Dataset](https://ai.google.com/research/ConceptualCaptions/download)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper