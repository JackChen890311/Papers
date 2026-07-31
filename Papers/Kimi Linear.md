---
title: "KIMI LINEAR: AN EXPRESSIVE, EFFICIENT ATTENTION ARCHITECTURE"
time: 2510
author: Kimi Team
link: https://arxiv.org/pdf/2510.26692
accepted: None
tags:
  - Foundation
  - Theory
  - LLM
todo: false
scanned: true
read: false
summary: A delta based linear attention block.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20260731162935.png]]
**要解決的問題**
一般 Transformer 的 attention,每生成一個 token,都要回頭看過去**所有**的 token,準確但很貴——context 越長,算力和 KV cache 都線性(甚至更糟)成長。Linear attention 這條研究線想把整個過去壓縮成一個**固定大小的 state**(像 RNN 的 hidden state),便宜、大小不變,但代價是沒辦法完美回顧過去,只能靠一個壓縮過的摘要。

**第一層直覺:state 是一塊記憶矩陣**
把模型的記憶想成一個矩陣 `S`,每個 token 都會更新它:「寫入新資訊、順便忘掉一些舊資訊」。整個 linear attention 研究的重點,就是設計「怎麼寫、怎麼忘」這條規則。

**第二層直覺:delta rule(差量寫入)**
最陽春的 linear attention 只會不斷把新的 key-value 加進 `S` 裡——沒有東西會被移除,記憶會像永遠不擦的白板一樣飽和。"delta rule"(來自 DeltaNet)的做法是:寫入新的 key-value 之前,先看看記憶**目前**對這個 key 會預測出什麼,只寫入「預測值跟真實值之間的差(誤差)」。這更接近聯想記憶(像 Hopfield network)該有的更新方式——是在**修正**已有的關聯,而不是盲目疊加新東西。

**第三層直覺:gating(遺忘機制)**
Gated DeltaNet 加了一個「遺忘閘門」——每個 head 一個純量值,每一步用它來決定:寫入新的 delta 之前,整個記憶狀態要先衰減多少。這就像一顆旋鈕控制「所有東西一起淡忘的速度」。

**第四層,也是 KDA 真正的貢獻**
KDA 在這個 delta rule 上加了更細粒度的 gating——不是整個 state 共用一個遺忘值,而是對記憶狀態的每一個維度/channel 獨立做遺忘。 具體來說,不是整個 head 共用一個 α 值控制衰減,而是每個 channel 都有自己的 α,也就是用一個對角矩陣裝著每個 channel 各自的衰減率,而不是一個純量。 [Note](https://note.com/okssusucha/n/n083671bf2cb9?hl=en)[Medium](https://medium.com/@cenghanbayram35/kimi-linear-a-revolutionary-attention-mechanism-for-ai-models-03f4de12047c)

**直覺比喻**:記憶不是一塊白板配一個統一速度的板擦——而是很多條獨立的軌道(對應不同的語義維度),有些軌道該保留很久,有些該很快消失(比如「這篇文章在講什麼主題」該慢慢淡忘,「上一個標點符號是什麼」該很快就忘)。單一純量的遺忘閘門逼所有軌道用同一個速度遺忘;逐 channel 的 gating 則讓模型自己學會哪些維度是長期記憶、哪些是短期記憶,把固定大小的 state 用得更有效率。

**這為什麼重要(實務上)**
這種更細粒度的 gating 讓模型能更有效利用有限的固定大小 RNN 記憶, 加上論文提出的 hardware-efficient chunkwise 演算法(用一種特化版的 Diagonal-Plus-Low-Rank 轉移矩陣),讓一個混合架構(KDA + 一般 attention 交錯)在效能上超越 full attention,同時把 KV cache 用量砍到最多省 75%,在 1M context 下解碼吞吐量最多快 6 倍。 [arXiv](https://arxiv.org/abs/2510.26692)[arXiv](https://arxiv.org/abs/2510.26692)

但要注意這是個**混合架構**,不是完全取代 attention:實際設計是把 KDA 這種 linear attention 層跟一般 full-attention 層以 3:1 的比例交錯排列——三層便宜的 linear attention 處理局部序列結構,一層 full attention 保留全局資訊流通。 所以比較誠實的解讀是,正如有評論指出的:如果 linear attention 真的完全打贏了 full attention,那個比例應該是 4:0,而不是 3:1——full attention 依然在做重要的工作,只是佔比變少了。 [Morph](https://www.morphllm.com/kimi-k3)[Acing AI](https://acingai.com/articles/linear-attention-kimi-k3)
**一句話總結**:KDA = delta rule 的線性 attention(寫入「修正量」而不是原始值)+ 逐 channel 可調的遺忘機制(不是全體共用一個遺忘速度,而是讓每個特徵維度學會自己的衰減節奏)——讓這個固定大小的記憶,能更細膩地控制「該保留什麼、該丟掉什麼」。
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

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper