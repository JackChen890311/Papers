---
title: Concept Decomposition for Visual Exploration and Inspiration
time: 2305
author: Tel Aviv University; Google Research; Reichman University
link: https://arxiv.org/pdf/2305.18203.pdf
accepted: SIGGRAPH23 (Asia)
tags:
  - Diffusion
  - Generation
  - Image
  - Personalization
todo: false
scanned: false
read: true
summary: A method for visual concept decomposition on diffusion models using text embedding.
---
# Summary
💡 Write a brief summary of this paper here
A simple yet effective method for visual concept decomposition, can be useful for inspiration generation
![[Pasted image 20240318123809.png]]

# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20240318124019.png]]
- Three steps in total: Generate Images→Extend text embedding table→Train Model
	- Three phases in training: Binary Reconstruction→Coherency Test→Binary Reconstuction
		- Binary Reconstruction: “A photo of sl sr” needs to be able to capture the original concept well, so the objective is predicting the noise from the given description (same as LDM). Only text embedding is trainable in the whole process.
		- Coherency: Mean cosine similarity of each pair from two sets of images in the CLIP latent space. Then calculate coherency score using C(Il, Il) + C(Ir, Ir) + (min(Cl, Cr) - C(Il, Ir)) (In-Cluster Coherency+ Minimum Difference Gain on Cross-Cluster Coherency)
		  ![](https://lh7-us.googleusercontent.com/e-2qRqymz8orbn-FmNI5yYXvcRSstEcqISoWi188Z5E2fkoDw199jpNC3U4q0g8IzCUHv5HNLgC86hQMQfbxdvKFY0jQ0GP5LRYvKamU50iqOrDXmX5oCGQMd1LaMxpUToOmsl8r6dtHZLrAUmqSYGvECA=s2048)
		  ![](https://lh7-us.googleusercontent.com/GQieclxC_ol4wMsoPeXqVS--Hi3aPEDePBDL7M6dmMyH5D-IrIgzPwJ9kgxkSx468QJWJLcQE-Cuam6U5ZJfRYEgoa9WGDNwh9Uh2UwOeXH4Py0zrA9iOuus4yqM12tVCNdAjrLm1WFa64ygeKwUdVYcrA=s2048)
	- After 200 steps of binary reconstruction on 4 different seeds, do a coherency test to choose the best seed, then continue the binary reconstruction on the best seed to 1000 steps.
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
- This work is based on [[Textual Inversion]]
- [[DreamBooth]]

# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Demo Page](https://inspirationtree.github.io/inspirationtree/)
- [Github Repo](https://github.com/google/inspiration_tree)
- [Presentation](https://docs.google.com/presentation/d/1b-sNWDZZDjIHQDepvjW9TMKC5l8EuX2b2gXfgvTqXLs/edit#slide=id.p)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper