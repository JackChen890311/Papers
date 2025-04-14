---
title: "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension"
time: 1910
author: Facebook AI
link: https://arxiv.org/pdf/1910.13461
accepted: None
tags:
  - Foundation
  - Generation
  - LLM
  - Text
todo: false
scanned: true
read: false
summary: A decoder-encoder architecture LLM.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20250414144221.png]]
# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20250414144238.png]]
# Experiments
💡 List the experiments settings and results of this paper

# Related Papers
💡 Include any related papers that are relevant to this one
- [[BERT]]
- [[GPT]]
# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
BART的概念及用途其實很單純，如Figure 1所示，BART 想要結合: 1) BERT 的雙向Encoder結構 及 2) GPT的left-to-right autoregressive sequence-to-sequence的生成模型。以此堆疊出BART (Bidirectional and Auto-Regressive Transformers) 的編碼及生成網路結構。  
  
如 Figure 1.(c)所呈現的，任何預定要生成postfix 字串的prefix 字串(bidirectionnal encoder的input)，也進行編碼後，將embedding feature 餵給 後段的 decoder, 進行 left-to-right autoregressive sequence-to-sequence 的postfix 字串生成。  
  
同時，在訓練BART時，有別於BERT採用的1) 克漏字訓練 Masked Language Model (MLM) 及 2) 兩個給定的句子是否具有上下文的相依性 Next Sentence Prediction (NSP)。  
BART的pre-training思維是將training document 加入noise，使其成為corrupted text，利用corrupted text 進行encoder編碼，再用decoder 的autoregressive 去生成原始noise-free的text。  
  
基於這個概念，BART嘗試了如Figure 2 的各種加入雜訊(noise)的辦法，不過最後實驗顯示最有效的pre-training noise adding 做法為 (Table 1):  
1) randome shuffling 所有字串裡的token (Sentence Permutation)  
2) 把字串裡 >= 0個連續token 一起遮罩起來，用單一個<mask>標籤取代。  
面對兩種corrupting的手法，BART的目標都是要利用decoder 預測出原始未汙染的字串。所以訓練的 loss function 就是 重建誤差，也就是decoder的output 與 原始未汙染的字串間的entropy 亂度(越小越好)。  
  
BART預訓練完後，就可以如同BERT一樣，做為一個pre-trained Large Language Embedding network，後面再接downstream task，例如text classification，或是 語言翻譯工作 (如Figure 3)  
  
Table 1. 顯示BART在基本的幾個baseline task problem上，贏過BERT 的基礎版本，整體也贏過針對 各別 baseline task problem 做設計的language model。 Table 2~6 則是針對各個task problem的state-of-the arts進行比較。  
  
Table 7 則是BART讀完一段落落長的文章後，給出精簡摘要的範例，藉此來展現BART理解文意並做綜整的quality。