---
title: "VILA: Learning Image Aesthetics from User Comments with Vision-Language Pretraining"
time: 2303
author: Google Research
link: https://arxiv.org/pdf/2303.14302
accepted: CVPR23
tags:
  - Image
  - Aesthetic
  - LLM
  - Text
todo: false
scanned: true
read: false
summary: A method for learning image aesthetic based on user comment.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20260706143857.png]]

這篇論文介紹了名為 **VILA**（Vision-Language Aesthetics）的視覺語言美學學習框架，旨在從網路上的**圖片與使用者評論對**（image-comment pairs）中學習圖片的美學特徵。

以下是該研究的核心要點：
- **核心動機**：傳統的圖片美學評估（IAA）主要依賴人類標記的分數（如平均意見分數 MOS），這簡化了人類對美學的感知。相比之下，自然語言評論包含更豐富的情感、風格、構圖和主題等美學資訊。
- **方法設計**：
    1. **VILA-P（預訓練階段）**：基於 [[CoCa]]（Contrastive Captioners）架構，利用對比損失（Contrastive Loss）和生成損失（Generative Loss）在圖片-評論對上進行預訓練，無需人工標籤即可學習到泛化性強的美學語義。
    2. **VILA-R（微調階段）**：設計了一種輕量級的**基於排名的適配器（Rank-based Adapter）**。在凍結預訓練權重的情況下，以文字「good image」作為錨點，透過調整圖片嵌入的殘差，使高美學質量的圖片靠近錨點、低美學質量的圖片遠離錨點。
- **主要成果**：
    - 在 AVA-Captions 資料集上的美學文本生成（Aesthetic Captioning）表現超越前人研究。
    - 具備強大的**零樣本（Zero-shot）學習能力**，在零樣本風格分類與零樣本美學評估任務中，表現甚至超越了許多需要監督學習的基準模型。
    - 透過 VILA-R 適配器微調（僅需訓練約 0.1% 的參數），在 AVA 資料集上達到了最先進的（State-of-the-art）美學評估效能。
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20260706143916.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper