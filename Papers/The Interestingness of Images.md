---
title: The Interestingness of Images
time: 1301
author: ETH Zurich; upicto GmbH Zurich; K.U. Leuven
link: https://openaccess.thecvf.com/content_iccv_2013/papers/Gygli_The_Interestingness_of_2013_ICCV_paper.pdf
accepted: ICCV13
tags:
  - Image
  - Theory
todo: true
scanned: false
read: false
summary: A study on the interestingness of images.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20260706112444.png]]
本研究探討了人類對照片產生「興趣」的背後機制。作者透過心理學實驗，發現圖片的趣味性（Interestingness）主要受到三大視覺線索影響：**美感（Aesthetics）、不尋常性/新穎性（Unusualness）以及對特定場景的普遍偏好（General preferences）**。

研究指出，圖片的趣味性與人類「自認為會記住該圖片」的心理預期高度相關，但令人驚訝的是，它與圖片實際上的可記憶性（Actual memorability）卻是毫無關聯甚至是負相關的。基於這些發現，作者開發了一套運算特徵模型來預測圖片的趣味性，並在三個不同語境背景的數據集上驗證了其有效性。

## 關鍵研究發現
- **趣味性 vs. 美感**：兩者具有強烈的正相關（$corr = +0.59$）。然而，有趣的圖片不一定非要具備美感（例如：骷髏頭的圖片很有趣，但不一定美觀）。
- **趣味性 vs. 可記憶性**：
    - **預期記憶（Assumed memorability）**：人類覺得有趣的圖片，往往是他們「想要記住」且「認為自己會記住」的圖片，兩者相關性最高（$corr = +0.63$）。
    - **實際記憶（Actual memorability）**：實驗結果顯示，趣味性與圖片實際能否被記住呈現**負相關**。例如，含有天空的自然風景很有趣，但實際上較不易被記住。
- **場景偏好**：人類普遍更喜歡**自然戶外場景**（如山脈、海岸、開放鄉村），而非人造建築或室內封閉空間。
# Methodology
💡 Describe the methodology used in this paper
## 預測模型的運算方法
作者提出了一套結合三大視覺線索的圖片趣味性預測框架：

1. **不尋常性（Unusualness）**：
    - **全域異常檢測**：利用 LOF（Local Outlier Factor）演算法分析全域特徵（如 RGB 像素、GIST、SIFT 直方圖空間金字塔），找出數據集中的特異圖片。
    - **局部區域組合**：利用超像素（Superpixels）將圖片分割，透過圖割（GraphCut）演算法計算該圖片是否能由數據庫中其他圖片的碎片「常規地」組合出來，以此衡量局部的不尋常度。
2. **美感（Aesthetics）**：
    - 計算圖片的**色彩豐富度（Colorfulness）**、**情緒喚醒度（Arousal）**（基於亮度和飽和度）、**複雜度（Complexity）**（透過 JPEG 壓縮比衡量）、**對比度（Contrast）**以及**邊緣分佈（Edge distribution）**。
3. **普遍偏好（General preferences）**：
    - 使用支持向量迴歸（-SVR）訓練全域圖像特徵（如 GIST 和空間金字塔），藉以學習並分類出人類偏好的場景類別（例如自然風景）。

最後，模型透過貪婪前向特徵選擇（Greedy forward feature selection）與線性組合，將上述特徵融合並預測出最終的趣味性得分。

# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20260706123949.png]]

研究在三種不同語境（Context）強度的數據集上進行測試：
1. **強語境（網路攝影機縮時序列）**：畫面連續變化，異常檢測（Outlier）特徵表現最好，能成功捕捉突發事件。
2. **中等語境（8類場景數據集）**：偏好特徵與全域特徵能發揮較好作用。
3. **無語境（任意照片數據集）**：觀看者缺乏前後文，此時美感與不尋常性成為主導因素。

**總結來說**，圖片的趣味性是可以被計算並預測的，且觀看圖片時的「上下文語境」對於趣味性的評估至關重要。作者也建議，在廣告投放等應用中，選擇「有趣」的圖片比選擇單純「容易讓人記住但乏味」的圖片更能帶來積極的宣傳效果。
# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper