---
title: "ReVersion: Diffusion-Based Relation Inversion from Images"
time: 2303
author: S-Lab, Nanyang Technological University
link: https://arxiv.org/pdf/2303.13495.pdf
accepted: SIGGRAPH24 (Asia)
tags:
  - Image
  - Generation
  - Diffusion
  - Personalization
  - ConceptLearning
todo: false
scanned: true
read: false
summary: Capture relations between images with a special token and can be used for diffusion model.
---
# Summary
💡 Write a brief summary of this paper here
Relational version of [[Textual Inversion]]
![[Pasted image 20240314230850.png]]

The use t-SNE on text embedding space and found that words with same POS will come closer.
![[Pasted image 20250104182408.png]]
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20240314231337.png]]
- Add Steering Loss to learn the </R/> ([[InfoNCE]] on POS)
![[Pasted image 20250104182653.png]]
- Also with a Relation-Focal Importance Sampling: 
  A skew sampling method which favors a larger t for better catch high level relationship
![[Pasted image 20250104182854.png]]
Total Loss:
![[Pasted image 20250104183026.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
- [[Textual Inversion]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper