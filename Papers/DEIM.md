---
title: "DEIM: DETR with Improved Matching for Fast Convergence"
time: 2412
author: Intellindust AI Lab; City University of Hong Kong; Great Bay University; Hefei Normal University
link: https://arxiv.org/pdf/2412.04234
accepted: CVPR25
tags:
  - ObjectDetection
  - Image
todo: false
scanned: true
read: false
summary: A improved version of DETR.
---
# Summary
💡 Write a brief summary of this paper here
[[DETR]] + Dense O2O Matching +  Matchability-Aware Loss (MAL)

![[Pasted image 20260804220228.png]]
# Methodology
💡 Describe the methodology used in this paper

# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
- [[DETR]]
- [[DINO (DETR)]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper

| 模型 | DETR | DINO | DEIM |
| :--- | :--- | :--- | :--- |
| **核心問題** | 建立端到端偵測框架 | 收斂慢、訓練不穩 | 收斂慢 (O2O 監督稀疏 + 低品質匹配) |
| **解法方向** | Transformer + Hungarian matching | 去噪訓練 + query 初始化改良 | 匹配策略密度化 + loss 設計 |
| **匹配方式** | 標準 O2O | 標準 O2O (+去噪輔助分支) | Dense O2O (仍是一對一，但正樣本更多) |
| **定位** | 開創性架構 | 收斂與精度優化 | 訓練效率與即時偵測優化 (常搭配 RT-DETR/D-FINE) |
### DETR 是什麼概念

你可以把物件偵測想成:「圖片丟進去,吐出一堆框框,告訴你這裡有貓那裡有狗」。

DETR 的做法很潮:CNN 抽完特徵後丟進 Transformer,直接讓一群「query」(可以想成一群偵探,每個人負責去圖上找一個物件)去猜框的位置跟類別。用 Hungarian matching 把預測框跟真實框「一對一」配對(誰跟真實答案最像就配誰),配對成功的當正樣本學,沒配到的當負樣本壓下去。

問題是:**這些偵探一開始都亂猜**,誰跟誰配對在訓練初期非常不穩,常常「明明框歪了但信心卻很高」,導致模型要花超久時間(500 epoch!)才能學會怎麼好好配對、好好收斂。這是 DETR 系列共同的痛點。

---

### DINO 做的事:讓偵探一開始就比較靠譜

DINO 沒有動「一對一配對」這個規則本身,而是想辦法讓訓練過程更穩、更快抓到重點:

1. **Contrastive Denoising(去噪訓練)**:額外塞一批「已經知道答案、但故意加了雜訊」的假 query 進去訓練,讓模型練習「這個歪掉的框應該修回哪裡」,順便用對比的方式讓模型分清楚「這是同一個物件的微調 vs. 這其實是別的物件」,等於是給模型開小灶惡補。
2. **Mixed Query Selection**:不要讓所有偵探從零開始瞎猜位置,而是先看 encoder 覺得哪裡「長得像有東西」,把這些位置當作偵探的起始站(anchor),但偵探要找什麼「內容」(content query)還是讓它自己學,不要死板套用。
3. **Look Forward Twice**:讓每一層修正框位置時,连带地讓修正的梯度也能回傳去優化上一層的參數,不要浪費每一層的學習機會。

➡️ 一句話:**DINO 讓偵探們一開場就站對位置、少走冤枉路**,配對機制沒變,但訓練效率和穩定性大幅提升。

---

### DEIM 做的事:嫌棄「一對一」給的線索太少,想辦法多塞一點

DEIM 換個角度想:就算偵探站得再對,**一張圖能配對成功的正樣本還是太少**(因為是一對一),尤其小物件常常配不到。而且早期配對常常配到「框歪但信心爆表」的爛配對,這種爛例子學多了反而有害。

它的解法很直接:

1. **Dense O2O Matching**:規則還是一對一沒變,但用 mosaic、mixup 這種資料增強手法,把好幾張圖拼成一張、疊出更多物件,這樣同一張訓練圖裡能配對成功的正樣本數量就自然變多了——不改規則,但是增加「案件數量」讓偵探多練習。
2. **Matchability-Aware Loss (MAL)**:針對案件數量變多後隨之而來的「爛配對變多」問題,設計一個新的 loss,依照配對品質高低動態調整權重——配得準的多學一點,配得爛的少學一點,不要被雜訊帶偏。

➡️ 一句話:**DEIM 覺得問題出在「線索(正樣本)太少+品質參差不齊」,所以想辦法多塞線索、再把線索分好壞來學**。效果是訓練時間直接砍半,搭配 RT-DETR、D-FINE 用單張 4090 訓練一天就能衝到 53.2% AP。