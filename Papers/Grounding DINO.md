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
todo: false
scanned: false
read: true
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

**Grounding（定位／語言對齊）**
- 指的是「機制」：將文字片語對應到影像中的特定區域
- 例如給模型 "a red cup"，模型要找出圖片中對應這個描述的那個區域，並畫出框
- GroundingDINO 透過在 backbone、跨模態特徵增強模組、語言引導的 query selection 等多個階段融合文字與影像特徵，讓框的預測直接以輸入文字為條件

**Open-set（開放集合）**
- 指的是「能力」：不受限於訓練時看過的固定類別
- 傳統 closed-set 偵測器（像用 COCO 訓練的 Faster R-CNN）只能輸出訓練時定義的 80 個類別之一
- Open-set 偵測器可以在推論時，透過文字描述新類別、屬性組合、甚至沒看過的物件（例如 "a giraffe wearing a hat"），不受限於固定 taxonomy

**兩者的關係**

| 名詞        | 角色                             |
| --------- | ------------------------------ |
| Grounding | _手段_：文字與影像特徵融合的架構設計            |
| Open-set  | _結果_：這個架構帶來的能力——可偵測近乎無限、未見過的類別 |
簡單說：GroundingDINO 就是「透過 grounding 機制實現的 open-set 物件偵測器」。因為訓練時沒有固定 label set 的限制，模型能靠更換文字 prompt 就做到 zero-shot 偵測未見過的類別。