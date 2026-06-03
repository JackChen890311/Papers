---
title: "Back to Basics: Let Denoising Generative Models Denoise"
time: 2511
author: MIT
link: https://arxiv.org/pdf/2511.13720
accepted: CVPR26
tags:
  - Theory
  - Diffusion
todo: false
scanned: true
read: false
summary: Improve diffusion quality by ask diffusion models direct predict original image noise.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20260603161618.png]]
![[Pasted image 20260603161813.png]]
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20260603161746.png]]
![[Pasted image 20260603161854.png]]
- **核心主張**：擴散模型（Diffusion Models）應回歸「去噪」本質，**直接預測乾淨圖像（x-prediction）**，而非主流的預測雜訊（ε）或混合量。
- **理論基礎**：基於「流形假設」，乾淨資料存在於低維度空間，而雜訊充滿高維空間。在極高維度（如原始像素）下預測雜訊會導致模型災難性崩潰，預測乾淨資料則容易得多。
- **極簡架構（JiT）**：提出 **Just image Transformers (JiT)**。完全使用標準 ViT 直接處理原始像素的大圖像塊（如 16x16）。**徹底捨棄潛在空間（Latent Space）、分詞器（Tokenizer）及任何額外損失函數**。
    
- **關鍵成果**：
    - 在 ImageNet 256x256 與 512x512 的原始像素生成上，x-prediction 輕鬆成功，而預測雜訊則完全失敗。
    - 在網路中引入「降維瓶頸（Bottleneck）」不僅節省算力，反而還能提升生成品質。
        
- **總結意義**：證明了「直接去噪」的強大潛力。這套無需複雜前置處理的極簡範式，為未來處理缺乏優質分詞器的高維自然數據（如視覺、氣象、蛋白質等）提供了全新方向。
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