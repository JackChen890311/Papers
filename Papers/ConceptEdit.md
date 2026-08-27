---
title: Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervision
time: 2608
author: Shanghai Jiao Tong University; Ant Group
link: https://arxiv.org/pdf/2608.16812
accepted: None
tags:
  - ImageEditing
  - ConceptLearning
  - Image
todo: false
scanned: true
read: false
summary: Proposes ConceptEdit, a paradigm for instruction-based image editing that scales edit concept diversity (1,000+ fine-grained categories) and uses dense supervision via compositional edits to boost training efficiency and performance.
---
# Summary
💡 Write a brief summary of this paper here

![[Pasted image 20260827190352.png]]

Introduces ConceptEdit, which scales edit concepts to 1,000+ fine-grained categories and uses dense supervision via compositional edits, achieving SOTA on ImgEdit-Bench and GEdit-Bench.

# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20260827190416.png]]

- **Concept Library**: LLM-driven taxonomy of 1,000+ fine-grained edit concepts, preventing VLM distribution collapse
- **Synthesis Pipeline**: Library construction → semantic matching → image synthesis → instance-specific VQA filtering
- **Dense Supervision**: Compositing multiple spatially disjoint edits into single pairs for richer training signals

# Experiments
💡 List the experiments settings and results of this paper

- **Setup**: Z-Image base model, Qwen3.5-122B for instructions, FLUX.2-klein-9B for synthesis
- **Results**: ConceptEdit1000 w/ Comp scores 3.48 (2M) and 3.75 (5M) on ImgEdit-Bench, outperforming ScaleEdit by +0.31 and +0.44
- **Ablations**: 1.5× faster convergence with dense supervision; +9% precision, +30% recall with VQA filtering

# Related Papers
💡 Include any related papers that are relevant to this one

- [[InstructPix2Pix]], FLUX.1 Kontext, Bagel, Emu3.5 (editing models)
- MagicBrush, UltraEdit, ScaleEdit, UnicEdit (editing datasets)

# Appendix
💡 Anything else that's in this paper but not mentioned before

- Concept library uses stochastic exploration for novel concepts
- Dense supervision: VLM aggregator enforces spatially disjoint edits
- Appendix includes I2I translation discussion, dataset comparisons, hardware details

---
# Resources
💡 Include some useful links for better understanding of this paper

- https://arxiv.org/abs/2608.16812
- https://arxiv.org/html/2608.16812v1

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
