---
title: "CACHE-TO-CACHE: DIRECT SEMANTIC COMMUNICATION BETWEEN LARGE LANGUAGE MODELS"
time: 2510
author: Tsinghua University; Infinigence AI; The Chinese University of Hong Kong; Shanghai Jiao Tong University; SLAI; Shanghai AI Laboratory
link: https://arxiv.org/pdf/2510.03215
accepted: ICLR26
tags:
  - LLM
  - Agent
  - Cache
todo: false
scanned: true
read: false
summary: A semantic communication adapter between LLMs as part of agentic system.
---
# Summary
💡 Write a brief summary of this paper here
  ![[Pasted image 20261108113007.png]]

本週要介紹的論文 - "CACHE-TO-CACHE: DIRECT SEMANTIC COMMUNICATION BETWEEN LARGE LANGUAGE MODELS"，由北京清華大學及上海交通大學團隊聯合發表。  
**直接先講結論，"LLM AI Agent 技術再這樣發展下去，已經快要沒有我們人類的事了XDDDDD"**  
  
過去多個 AI (Mulitple LLM-based AI Agent)合作時，必須把想法及要溝通的資訊，先將AI Agent 快取記憶體內的特徵編碼向量，轉譯輸出成自然語言文字後講給另一個AI去讀。這個過程，既浪費計算資源又容易因為編碼轉換的資訊損失而漏掉細節。這篇研究讓 AI 直接把腦中的快取記憶體內容（KV 快取編碼向量）傳入至另一個 AI的快取記憶內做資訊融合，省去打字與重讀的時間。實驗證明，這種Cache to Cache 的溝通做法，大幅加快速度並保留最完整的語意。  

# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20261108113032.png]]

**1) 研究動機及目標改善項目**  
  
A. 多模型協作需求 - Sharer 及 Receiver 兩種LLM角色:  
單一 AI 模型再厲害，遇到超長文章或複雜難題時，腦容量和計算力還是會吃不消，因此需要多個模型分工合作。在這種分工中，通常有一個Powerful的 Sharer LLM（分享者）就像是負責在圖書館讀完整本厚書的助理，專門消化龐大的背景資料；而另一個 Receiver LLM（接收者）則像是最後做答題的角色，負責聽取助理回報的重點，整合出最終的正確解答。  
  
B. Sharer 及 Receiver 理解問題的動作叫做 Prefill，其動作目的與具體實作如下:  
Prefill（預填充）的目的，是讓模型在開口回答前，先把整段題目讀進腦袋裡，轉換成隨時能調用的暫存記憶（KV 快取）。具體做法上，Sharer 會把整篇長文章一次讀完，算出自己的專屬記憶；傳統做法下的 Receiver 則得傻傻等 Sharer 講完話，再把 Sharer 講出來的那堆文字重新從頭讀一遍，在自己腦中重新建立一份記憶。  
  
C. Prefill、資訊交換及解碼產生答案流程:  
傳統合作流程非常繁瑣。首先 Sharer 進行預填充讀懂長文章，接著進入解碼階段，像打字機一樣一個字一個字把重點摘要印成文字。等 Sharer 完全印完後，這段文字被傳給 Receiver。Receiver 接著啟動自己的預填充，把這段文字全部重讀並轉成自己的記憶，最後 Receiver 進入解碼階段，同樣一個字一個字推敲，吐出最後的答案。  
  
D. LLM 採用自然語言文字溝通的缺點:  
用人類看得懂的文字溝通非常沒效率。第一是非常浪費時間，一個字一個字透過類神經網路(通常是 Transformer)解碼出來、對方再一個字一個字重讀，中間浪費了大量算力與等待時間。第二是嚴重漏掉細節，AI 腦中高維度的思考脈絡本來很豐富細膩，硬把它精簡壓縮成短短幾句人類文字，很多微妙的關聯與線索直接消失，反而容易讓後面的模型瞎猜而產生幻覺。  
  
E. 直接用Agent 各自記憶體 Cache-to-Cache 溝通的好處:  
Cache-to-Cache（快取直傳）就像讓兩個 AI 擁有心靈感應。Sharer 讀完文章後，不打字輸出，而是直接把腦中已經編碼過的向量資訊（KV 快取值，通常包含對問題上下的理解、答題者的背景等資訊）打包直送至 Receiver 的快取記憶體做資訊融合(information fusion)，並且由 Receiver 基於自已更新後的快取記憶體內容做答題。這樣一來，完全省去了前面打字輸出、後面重新閱讀的兩大耗時步驟。更棒的是，原本腦中複雜細緻的想法完整保留下來，既讓整體回答速度暴增，也讓最後答案更加精準不失真。  
  
F. Figure 5 的 Cache Fuser 架構細節:  
Figure 5 的 Cache Fuser 就像一個專業的「記憶轉接與融合器」，專門負責把 Sharer 的外來記憶無縫接進 Receiver 的大腦中。首先，不同 AI 模型的內部規格通常不一樣，因此架構第一步使用 Projection（線性投影層），就像一個即時翻譯轉接頭，把外來記憶的尺寸與格式轉換成 Receiver 能夠讀懂的維度。轉換完畢後，進入 Dynamic Weighting（動態加權模組），這個模組就像聚光燈，會根據當前要回答的問題，自動挑出外來記憶中最關鍵的重點並加大權重，把不重要的雜訊調小。接下來在 Feature Fusion（特徵融合模組）中，外來重點記憶會和 Receiver 自己原生對問題的理解記憶混和在一起，進行深度的特徵交織。為了避免外來的記憶太過強勢，模組特別加入了 Gate（門控機制），它就像一個水量閥門，會聰明地決定該放多少外部資訊進來，避免反客為主。最後，架構還連了一條 Residual Link（殘差連接），直接把 Receiver 自己原本乾淨的記憶拉一條捷徑疊加上去。殘差連接的好處非常大，它就像一個安全保護傘，確保 Receiver 自己的母語理解能力和原本的思考底子不會被外來記憶給沖淡或帶偏，同時讓模型在深度運算時依然保持穩定，既能平滑吸收同伴傳來的外部經驗，又能牢牢守住自己的推論主導權。  
  
F. 可訓練組件、訓練資料集與損失函數  
在 Figure 5 的架構中，兩個大模型本體都完全被鎖定凍結、不動內部權重，只有 Cache Fuser 裡面的投影轉換矩陣(Projection)、動態加權網路(Dynamic Weighting)與門控調節閥(Gate)是需要透過訓練學習的輕量零件。訓練資料主要採用標準的多篇長文件問答與摘要資料集，讓模型學會對齊外部記憶。訓練時用的損失函數是標準語言模型的預測下一個字交叉熵損失（Next-token Cross-Entropy Loss），也就是讓 Receiver 在吸收融合記憶後，猜對下一個正確答案字的機率越高越好。  
# Experiments
💡 List the experiments settings and results of this paper
**2) 實驗結果**

A. 端到端推論速度與延遲改善實驗:  
這項實驗旨在驗證直傳記憶是否真的能大幅省下溝通時間，對應論文中的 Figure 1 與 Figure 6。作者在長文本問答環境下，精確比對傳統文字轉述與快取直傳兩者的運算耗時。結果顯示，快取直傳砍掉了逐字生成文字與重複閱讀的漫長等待，使得推論反應時間大幅縮短，整體處理速度提升了數倍，上下文越長，省下來的時間就越驚人。  
  
B. 長文本問答準確度測試:  
該實驗目的是確認直接傳送大腦記憶是否比傳送文字摘要更能保留細節並減少答錯，具體數據可參照論文中的 Table 1。作者給予助理模型海量背景資料，分別用打字摘要和直傳記憶兩種方式交給後續模型回答問題。結果顯示，直傳記憶在問答準確率上全面超越傳統文字溝通，證實直接傳送未經破壞的連續思考特徵，能有效避免資訊流失並降低模型瞎掰胡說的機率。  
  
C. 不同複雜度與結構模型的跨界通用性:  
這項實驗想要測試這套記憶轉接器能否在完全不同廠牌、不同大小的模型之間牽線成功，實驗數據呈現在論文的 Table 2。作者挑選了參數規模不同、內部結構有落差的多個模型進行跨界搭配傳遞記憶。測試結果顯示，經過輕量投影與門控調整後，接收者依然能穩定吸收不同架構模型傳來的快取特徵並給出高品質回答，證明此方法具備極佳的跨模型通用彈性。  
  
D. 融合模組內部零件拆解消融實驗:  
此實驗目的是檢驗動態加權、門控閥門與殘差捷徑這幾個零件是否真的缺一不可，詳細比較結果請參見論文的 Table 3。作者刻意在架構中輪流拔除其中一項零件，觀察模型回答分數的變化。結果發現，拿掉殘差捷徑或門控閥門後，模型容易被外來記憶干擾而精神混亂，性能大幅下滑；拿掉動態加權則讓模型抓不到重點，證明所有零件各司其職且缺一不可。

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper