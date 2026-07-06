---
title: "CoCa: Contrastive Captioners are Image-Text Foundation Models"
time: 2205
author: Google Research
link: https://arxiv.org/pdf/2205.01917
accepted: None
tags:
  - Image
  - Text
  - Foundation
  - Contrastive
  - Captioning
todo: false
scanned: true
read: false
summary: A contrastive captioner foundation VLM.
---
# Summary
💡 Write a brief summary of this paper here

這篇論文介紹了由 Google Research 提出的基礎模型 **CoCa**（Contrastive Captioners），它是一個將視覺語言的「對比式學習」與「生成式式（描述）學習」相結合的極簡模型架構。

以下是該研究的核心要點：
- **核心動機**：過去的視覺基礎模型通常各自獨立——單一編碼器（如 ImageNet 預訓練）缺乏自然語言能力；雙編碼器（如 CLIP）擅長跨模態對齊但缺乏聯合理解能力；編碼解碼器（如 SimVLM）擅長生成但無法產出對齊的文本向量。CoCa 旨在**將這三種範式（單編碼器、雙編碼器、編碼解碼器）統整於單一模型中**。
- **方法設計**：
    - **解耦的文字解碼器（Decoupled Text Decoder）**：將解碼器分為前半部的**單模態解碼器（Unimodal Decoder）**與後半部的**多模態解碼器（Multimodal Decoder）**。前半部省略交叉注意力（Cross-Attention）以提取純文字特徵；後半部則加入交叉注意力以融合圖像與文字特徵。
    - **雙重優化目標**：在單模態輸出上計算**對比損失（Contrastive Loss）**，並在多模態輸出上自迴歸地計算**描述損失（Captioning Loss）**。兩個任務共享同一個計算圖，極具訓練效率。
    - **注意力池化器（Attentional Poolers）**：針對對比學習（全球特徵）與描述生成（區域特徵）的不同需求，客製化設計了任務特徵適配器。
- **主要成果**：
    - CoCa 採端到端、從頭開始（from scratch）的大規模預訓練，將所有標籤皆視為文本處理。
    - **零樣本轉移（Zero-shot Transfer）**：在 ImageNet 分類上達到 86.3% 的零樣本準確率。
    - 在微調或凍結特徵評估下，於視覺識別（ImageNet 達到 91.0%）、跨模態檢索（MSCOCO、Flickr30K）、多模態理解（VQA）以及圖像描述生成（NoCaps）等多項下游任務中皆創下當時最先進的（State-of-the-art）全新紀錄。
# Methodology
💡 Describe the methodology used in this paper

# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper
- [[CVPR2023 Tutorial Talk] Recent Advances in Vision Foundation Models 近期視覺基礎模型的進展](https://hackmd.io/@YungHuiHsu/S1nPk2eET)
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
![[Pasted image 20260706144517.png]]