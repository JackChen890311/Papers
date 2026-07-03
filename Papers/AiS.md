---
title: "Abstraction in Style: Beyond Texture and Color"
time: 2603
author: Shenzhen University; Peking University
link: https://arxiv.org/pdf/2603.29924
accepted: SIGGRAPH26
tags:
  - Image
  - StyleTransfer
todo: false
scanned: true
read: false
summary: A style transfer method that separates structure abstraction and style abstraction
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20260703165556.png]]
## 核心問題
- 傳統的風格遷移技術（如神經風格遷移）通常會強制保留原始目標圖像的幾何結構，僅修改表面的紋理或顏色 。
- 這種做法無法捕捉插畫或非寫實風格藝術中常見的「結構抽象」行為，例如對幾何結構進行簡化、扭曲比例、打破對稱或重新解釋結構關係 。
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20260703165657.png]]
## AiS 框架的兩階段處理方式
AiS 將風格化生成過程拆解為兩個明確的階段，以顯式地分離「結構抽象」與「視覺風格化」 ：  
- **第一階段：結構抽象 (Structural Abstraction)**
    - 將目標圖像轉換為簡化的「隱藏骨幹」(Hidden Backbone)，僅保留物體的語義佈局與拓撲組織 。  
    - 透過「抽象視覺類比遷移」(A-VAT) 學習參考圖像的抽象邏輯，將骨幹轉換為「抽象代理」(Abstraction Proxy)，該代理不僅包含語義結構，還融入了該風格特有的幾何詮釋 。  
- **第二階段：視覺風格化 (Visual Stylization)**
    - 使用「風格化視覺類比遷移」(S-VAT) 將抽象代理渲染為最終圖像，確保輸出結果在視覺外觀（色彩、紋理）上與參考風格保持高度一致 。  
![[Pasted image 20260703165842.png]]
## 關鍵技術：視覺類比遷移 (VAT)
- AiS 的兩個階段皆基於「視覺類比遷移」(Visual Analogy Transfer, VAT) 的機制。該機制利用預訓練的擴散轉換器模型 (Diffusion Transformer) 配合輕量級的 LoRA 進行微調 。  
- VAT 讓模型僅需極少量的參考樣本（平均每種風格 10 個 exemplars），就能學習複雜且與風格相關的結構與外觀轉換邏輯，且無需進行繁瑣的幾何標註或手工特徵設計 。  
# Experiments
💡 List the experiments settings and results of this paper
![[Pasted image 20260703165824.png]]
## 結論
與傳統單階段的風格遷移方法相比，AiS 透過明確建模並解耦抽象過程，能產生結構更連貫、風格忠實度更高且更具可控性的結果，特別是在處理高度抽象或插畫風格時表現優異 。
# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper