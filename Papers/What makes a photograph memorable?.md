---
title: What makes a photograph memorable?
time: 1301
author: MIT
link: https://people.csail.mit.edu/torralba/publications/Isola_memorabilityPhotos_PAMI2014.pdf
accepted: PAMI13
tags:
  - Image
  - Theory
todo: false
scanned: true
read: false
summary: A study on the memorability of photos.
---
# Summary
💡 Write a brief summary of this paper here
![[Pasted image 20260703173400.png]]
## 核心摘要與發現
- **可記憶性是影像的內在屬性**：研究證實，影像能否被記住並非完全因人而異的客觀主觀感受，而是一種**內在且穩定**的屬性。不同觀看者對同一張照片是否容易記住，具有高度的一致性。
- **時間上的穩定性**：一張影像如果在短時間內（約 36 秒）容易被記住，在長時間後（約 40 分鐘）同樣也具備較高的可記憶性，這代表可記憶性在時間延遲下是穩定的。
- **主觀預測不準確**：人類往往**無法準確預測**哪些影像真正具有記憶點。實驗顯示，人們主觀認為「最容易被記住」的照片，其真正的測試表現甚至可能輸給被認為「最難被記住」的照片。
## 應用價值
自動預測影像可記憶性的技術在未來有廣泛的應用場景：
- **教育領域**：設計更深植人心的教科書圖表或語言學習圖卡。
- **使用者介面與設計**：創造更易辨識的圖示、令人印象深刻的廣告、商標或網站封面。
- **影像處理**：從大量的相簿或影片中，自動篩選出最精華、最不容易被遺忘的畫面。

# Methodology
💡 Describe the methodology used in this paper
![[Pasted image 20260703173422.png]]
## 1. 視覺記憶遊戲（The Visual Memory Game）
研究團隊利用 Amazon Mechanical Turk 平台招募了 665 名受試者進行線上實驗。
- **實驗流程**：受試者會觀看一系列連續播放的影像，每張影像顯示 1 秒，間隔 1.4 秒。
- **任務目標**：當受試者看到**完全重複**的影像時，必須按下空白鍵。
- **影像分類**：影像分為「目標影像（Targets）」與「干擾影像（Fillers）」。干擾影像用於控制重複的間隔，並作為「注意力檢查（Vigilance task）」以確保受試者認真作答。
## 2. 評分與一致性測試
- 團隊根據受試者正確偵測到重複照片的百分比，為每張影像定義了「可記憶性得分（Ground truth memorability score）」。
- 將受試者隨機分成兩組進行對比，發現兩組的評分具有高度的斯皮爾曼等級相關係數（$\rho = 0.75$），證實了人類在影像記憶上的一致性。

## 排除環境與脈絡干擾

研究人員進一步測試了影像在資料集中的出現頻率（例如特定物件或場景類別的普遍性），發現影像的**語意頻率與其可記憶性之間沒有強烈相關性**（相關係數接近於零）。這說明影像的可記憶性主要來自影像本身的特徵，而非單純因為它「稀有」或「常見」。
# Experiments
💡 List the experiments settings and results of this paper
## 數據集（Dataset）的建構細節
研究團隊建立了一個用於基準測試的數據集，其設計與清洗流程非常嚴謹：
- **影像來源**：從著名的 **SUN Dataset**（場景理解數據集）中隨機抽樣。所有影像皆被統一裁切並縮放為 $256 \times 256$ 像素。
- **結構組成**：包含 2,222 張目標影像（Targets）與 **8,220 張干擾影像（Fillers）**。
- **視覺遊戲的排程（Sequencing）**：
    - 影像每張顯示 1 秒，間隔 1.4 秒。
    - **干擾影像**的重複間隔非常短（僅隔 1 至 7 張影像），作為「注意力檢查（Vigilance Task）」，用以即時篩選掉不專心的受試者。
    - **目標影像**的重複間隔較長（相隔 91至 109 張影像，約隔 4 分鐘），這才是真正用來計算可記憶性得分的數據。
- **數據清洗與評分**：每張目標影像平均由 **78 名受試者** 進行評分。若受試者在注意力檢查中的答錯率過高，其整組數據會被直接剔除，以確保最終標註的「可記憶性得分（Ground Truth Memorability Score）」具備極高精確度。

## 模型與影像特徵分析（Image Features）
為了探究「究竟是影像中的什麼元素讓人記住？」，研究團隊測試了多種不同層次的影像特徵描述符（Descriptors），並比較它們與可記憶性的相關性：
### 1. 低階與中階視覺特徵（Low/Mid-level Features）
- **GIST**：一種全局紋理與場景結構的描述符，用來捕捉空間架構（如開放度、粗糙度）。
- **SIFT（Scale-Invariant Feature Transform）**：利用密集的 SIFT 特徵捕捉局部邊緣與紋理變化。
- **HOG（Histogram of Oriented Gradients）**：常用於物件偵測，捕捉影像中的邊緣方向與形狀特徵。
- **Color Histograms（顏色直方圖）**：分析影像的色彩分佈。
- **研究發現**：單純依靠這些低階的視覺特徵（如顏色、簡單紋理），**無法**很好地預測影像的可記憶性，這說明記憶點與更高階的語意理解有關。
### 2. 高階語意特徵（High-level Semantic Features）
- **物件與場景標籤（Object & Scene Labels）**：研究團隊為影像中出現的物件（如人、車、樹）以及場景類別（如廚房、海灘）進行標註。
- **屬性（Attributes）**：標註影像的抽象屬性，例如「人工的（man-made）」、「自然的（natural）」、「封閉的（enclosed）」等。
- **研究發現**：**語意特徵的預測效果遠好於低階視覺特徵**。例如，含有「人（People）」或「室內場景/人工構造物」的影像，通常具備顯著較高的可記憶性；而廣闊的自然風景（如山脈、森林）雖然美麗，但可記憶性通常較低。
## 預測模型（Memorability Predictor）的訓練
在確立了哪些特徵有效後，研究團隊訓練了自動預測模型：
- **演算法**：主要採用支持向量機（SVM, Support Vector Regression）**與**脊迴歸（Ridge Regression）等機器學習模型。
- **訓練方式**：將上述各種特徵描述符作為輸入向量，以受試者測試出的「可記憶性得分」作為回歸目標（Label）進行訓練。
- **預測表現**：模型最終達到了與人類自身高度相關的預測表現。這成功證明了「影像可記憶性」是一個可以透過計算機視覺技術來量化與自動預測的屬性，為後續 AI 領域（如後來利用 CNN/深度學習進行的可記憶性預測研究，如 LabelMe、MemNet 等）奠定了關鍵的基準。
# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not mentioned before
## 2011 vs 2014 version
2014 年 PAMI 期刊版本，相較於 2011 年的版本，在「高層級語義與屬性」上的核心發現如下：
- **語義層級越高，越好記**：大腦記住照片主要看「畫面有什麼（語義）」，而非「照片美不美」。顏色、構圖等低層特徵對記憶度幾乎沒有貢獻。
- **「人」與「動作」最吸睛**：照片中只要出現清晰的人臉、人體，或是人類正在進行的具體社會互動與動態動作，記憶度會顯著飆升。
- **物體與場景的記憶排行榜**：
    - **最容易記住**：日常室內場景、具備功能性的 man-made 物體（如車輛、工具、椅子）。
    - **最容易忘記**：自然風光（如森林、山脈、海灘）。大腦容易將其歸類為重複的背景，因此極易被遺忘。
- **獨特性與動態感加分**：偏離常態、具有衝突感的畫面結構（獨特性），以及傳達出即將發生改變的畫面（動態感），能大幅加深大腦的印象。

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper