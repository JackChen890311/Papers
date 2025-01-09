---
title: "Lego: Learning to Disentangle and Invert Personalized Concepts Beyond Object Appearance in Text-to-Image Diffusion Models"
time: 2311
author: "INSAIT, Sofia University, Bulgaria\r; ETH Zurich, Switzerland"
link: https://arxiv.org/pdf/2311.13833
accepted: ECCV24
tags:
  - Contrastive
  - Decomposition
  - Diffusion
  - Generation
  - Image
  - Multimodal
  - Personalization
  - Text
  - ConceptLearning
todo: false
scanned: true
read: false
summary: A contrastive-refined method for learning the concept, disentangled with the subject
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20250104152642.png]]

![[Pasted image 20250104152712.png]]
![[Pasted image 20250104152750.png]]
# Methodology
💡 Describe the methodology used in this paper
[[Textual Inversion]] + Subject Separation + Context Loss
![[Pasted image 20250104152739.png]]
- Subject Separation
  Use </sub/> & </sub/>+ </cpt/> to disentangle subject and concept embedding
- Context Loss
  Use contrastive loss + pre-defined positive & negative word
  Kind of like [[ReVersion]]
  ![[Pasted image 20250104155452.png]]

# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20250104153214.png]]
# Related Papers
💡 Include any related papers that are relevant to this one
- [[Textual Inversion]]
- [[ReVersion]]
# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Lego - Google 簡報](https://docs.google.com/presentation/d/1a7x6VAuDoOgh3AGuGM4AeLGBwik8ojHtdrIOgsqROps/edit#slide=id.g307fd35e618_0_27)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper