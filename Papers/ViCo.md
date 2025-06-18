---
title: "VICO: PLUG-AND-PLAY VISUAL CONDITION FOR PERSONALIZED TEXT-TO-IMAGE GENERATION"
time: 2306
author: The University of Hong Kong
link: https://arxiv.org/pdf/2306.00971
accepted: None
tags:
  - ConceptLearning
  - Diffusion
  - Generation
  - Image
  - Personalization
  - Segmentation
todo: false
scanned: true
read: false
summary: A personalization method for T2I model including attention masks.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20250130134547.png]]
![[Pasted image 20250204211803.png]]
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20250130134527.png]]

Read Section 3.3 for details of masking mechanism.
![[Pasted image 20250202175431.png]]

Section 3.3 also mentioned about <end_of_text> token for foreground segmentation, which is mentioned in [[ConceptExpress]].
(However, I still quite not understand it yet)

# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20250130134707.png]]
![[Pasted image 20250130134724.png]]
# Related Papers
💡 Include any related papers that are relevant to this one
- [[Prompt-to-Prompt]]
- This paper has same author as [[ConceptExpress]].
# Appendix
💡 Anything else that’s in this paper but not mentioned before
- The Architecture (Image attention is added every other layer in decoder only)
![[Pasted image 20250301194923.png]]
![[Pasted image 20250301195020.png]]


---
# Resources
💡 Include some useful links for better understanding of this paper
- [Github](https://github.com/haoosz/ViCo)
- [Dataset](https://drive.google.com/drive/folders/1o3iTN5P6PX-DK3Ql_wSdH-swVvGYIG9I)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper