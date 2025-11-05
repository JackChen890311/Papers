---
title: "DINO: DETR with improved denoising anchor boxes for end-to-end object detection"
time: 2203
author: The Hong Kong University of Science and Technology; Dept. of CST., BNRist Center, Institute for AI, Tsinghua University; International Digital Economy Academy (IDEA); The Hong Kong University of Science and Technology (Guangzhou)
link: https://arxiv.org/pdf/2203.03605
accepted: None
tags:
  - ObjectDetection
  - Text
  - Image
todo: false
scanned: true
read: false
summary: Introducing denoising anchor boxed to DETR.
---
# Summary
💡 Write a brief summary of this paper here
Problems in [[DETR]]:
- Converge too slow
- Hard to match the meaning of queries
DINO introduces "denoising anchor boxes" to DETR for better performance.
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20251017171033.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
- [[DETR]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [論文筆記 — DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object Detection](https://watson-john.medium.com/%E8%AB%96%E6%96%87%E7%AD%86%E8%A8%98-dino-detr-with-improved-denoising-anchor-boxes-for-end-to-end-object-detection-3c933b8d0d88)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
## Denoising
它的核心思想是：

> 在訓練時「故意」加入一些被**擾亂的（noised）ground-truth boxes**，
> 讓模型學會如何**還原正確的物件位置與分類**。

這種方式讓模型更快學會「query → object」的 mapping，
就像在語言模型中用「masked language modeling」訓練一樣。

## ⚙️ 四、運作方式（直觀講解）
1.	取出真實的 GT boxes
	每張圖的 ground truth：[class_i, box_i]
2.	生成 noisy versions
	在 box 的中心位置、大小、或標籤上加一點擾動（noise）：
	\text{noisy\_box} = \text{box} + \epsilon
	例如：中心點偏移 10%，或類別錯一個。
3.	加入到 decoder 輸入
	這些 noisy boxes 當作「denoising queries」輸入 transformer decoder。
	模型要學會把它們修正回原來的正確 box。
4.	同時還有正常的 detection queries
	這些 queries 負責真正的物件偵測（和 Hungarian matching）。