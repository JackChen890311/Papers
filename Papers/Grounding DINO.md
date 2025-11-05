---
title: "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection"
time: 2303
author: Tsinghua University; International Digital Economy Academy (IDEA); The Hong Kong University of Science and Technology; The Chinese University of Hong Kong (Shenzhen); Microsoft Research; South China University of Technology
link: https://arxiv.org/pdf/2303.05499
accepted: ECCV24
tags:
  - ObjectDetection
  - Image
  - Text
  - Foundation
todo: true
scanned: false
read: false
summary: A contrastive-based and fusion method for open set object detection.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20251015175156.png]]
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20251015175219.png]]
## Text processing
![[Pasted image 20251020110216.png]]
## Loss Functions
> Following previous [[DETR]]-like works, we use the L1 loss and the [[GIOU]] loss for bounding box regressions. We follow [[GLIP]] and use contrastive loss between predicted objects and language tokens for classification
- L1 Loss, GIOU Loss for bounding box
- Contrastive Loss for classification
# Experiments
💡 List the experiments settings and results of this paper
## Implementation
![[Pasted image 20251020110901.png]]
# Related Papers
💡 Include any related papers that are relevant to this one
- [[DINO (DETR)]]
- Grounding Idea from [[GLIP]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [十分钟解读Grounding DINO-根据文字提示检测任意目标](https://zhuanlan.zhihu.com/p/627646794)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
![[Pasted image 20251022121506.png]]