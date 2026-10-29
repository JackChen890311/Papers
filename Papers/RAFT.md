---
title: "RAFT: Adapting Language Model to Domain Specific RAG"
time: 2403
author: UC Berkeley
link: https://arxiv.org/pdf/2403.10131
accepted: COLM 2024
tags:
  - RAG
  - LLM
  - FineTuning
  - DomainAdaptation
  - ChainOfThought
todo: false
scanned: true
read: false
summary: RAFT is a simple post-training recipe for domain-specific RAG — fine-tune on (question + golden doc + distractor docs) → Chain-of-Thought answer that quotes the golden span verbatim, deliberately removing the golden doc in a fraction of samples so the model learns both to read and to ignore distractors.
---
# Summary
💡 Write a brief summary of this paper here
- RAG-prompting alone = "open-book exam without studying"; plain SFT = "memorizing the book but not bringing it". **RAFT** = study *for* an open-book exam.
- Training data: `Q + D* + D₁…D_k → A*`, where `A*` is a CoT answer with **verbatim quotes** from the golden doc.
- Key twist: for a `(1−P)` fraction of questions, **no golden doc at all** (distractors only) → forces parametric memorization instead of always copying the context.
- Retriever-agnostic, SFT-only, test-time is standard top-k RAG. LLaMA2-7B + RAFT beats DSF, DSF+RAG, and even GPT-3.5+RAG on HotpotQA, HuggingFace, Torch Hub, TensorFlow Hub.
![[RAFT Fig2 Method Overview.png]]

# Methodology
💡 Describe the methodology used in this paper
- **Task framing (Sec. 2)** — three exam types: closed-book (plain LLM), open-book (LLM + retriever), **domain-specific open-book** (retriever + a *known, fixed* corpus). RAFT targets the third.
- **Standard SFT** `{Q → A}`; RAG inference `{Q + D → A}` — the train/test mismatch RAFT removes.
- **Data construction (Sec. 3)**
  - `P%`: `Q + D* + D₁ + … + D_k → A*` (one or more golden docs, rest distractors).
  - `(1−P)%`: `Q + D₁ + … + D_k → A*` (all distractors) → compels memorization rather than pure extraction.
  - Default: 1 golden + 4 distractors.
- **CoT + citation target** — answers generated with GPT-4-1106 in the form `##Reason: … ##Answer: …`, where the reason embeds exact spans inside `##begin_quote## … ##end_quote##`. Quoting trains grounded extraction; the reasoning chain prevents loss collapse / overfitting to short answers.
- **Why it works** — combines reading (context extraction) with memorization, and explicitly teaches the model to *disregard* irrelevant retrieved text (robustness to imperfect retrieval).
- **Inference** — unchanged standard top-k RAG; method only changes the fine-tuning data, not the retriever.

# Experiments
💡 List the experiments settings and results of this paper
- **Datasets**: PubMedQA (biomedical, binary yes/no), HotpotQA (multi-hop Wikipedia), APIBench/Gorilla (HuggingFace Hub, Torch Hub, TensorFlow Hub → correct API call); NQ + TriviaQA for ablations.
- **Baselines**: LLaMA2-7B 0-shot; LLaMA2-7B + RAG; DSF (domain SFT, no docs); DSF + RAG; GPT-3.5 + RAG reference.
- **Main results (accuracy, Table 1)**

| Method | PubMed | HotPot | HuggingFace | Torch Hub | TensorFlow |
|---|---|---|---|---|---|
| GPT-3.5 + RAG | 71.60 | 41.5 | 29.08 | 60.21 | 65.59 |
| LLaMA2-7B | 56.5 | 0.54 | 0.22 | 0 | 0 |
| LLaMA2-7B + RAG | 58.8 | 0.03 | 26.43 | 8.60 | 43.06 |
| DSF | 59.7 | 6.38 | 61.06 | 84.94 | 86.56 |
| DSF + RAG | 71.6 | 4.41 | 42.59 | 82.80 | 60.29 |
| **RAFT (LLaMA2-7B)** | **73.30** | **35.28** | **74.00** | **84.95** | **86.86** |

- Biggest gains vs. base+RAG: **+35.25 HotpotQA**, **+76.35 Torch Hub**; vs. DSF: **+30.87 HotpotQA**, **+31.41 HuggingFace**. Adding RAG to DSF actually *hurts* (Hotpot 6.38 → 4.41, TF 86.56 → 60.29) — the model never learned to read context.
- PubMedQA is near-saturated / binary, so RAFT ≈ DSF+RAG (73.3 vs 71.6).
- **CoT ablation (Table 2)** — removing the reasoning chain costs **−9.66 HotpotQA**, **−14.93 HuggingFace**, **−5.0 PubMed** (Torch Hub slightly favors no-CoT: 86.56 vs 84.95).

| | PubMed | HotpotQA | HuggingFace | Torch Hub | TensorFlow |
|---|---|---|---|---|---|
| RAFT w/o CoT | 68.30 | 25.62 | 59.07 | 86.56 | 83.21 |
| RAFT | 73.30 | 35.28 | 74.00 | 84.95 | 86.86 |

- **How much golden data? (Sec. 4.4, Fig. 5)** — `P = 100%` (always golden) is *not* optimal; best P is dataset-dependent (~40% NQ, ~60% TQA, 100% HotpotQA). Mixing golden-free samples helps in-domain RAG.
![[RAFT Fig5 P Golden Ratio.png]]
- **Robustness to top-k (Sec. 5, Fig. 6)** — models trained with distractors degrade far more gracefully as test-time `k` grows; training on golden-only (`Train D*`) is consistently worst. Optimal train-time doc count varies (NQ ≈ 3–4, TriviaQA ≈ 3, HotpotQA ≈ 1–2; the text and the figure caption disagree slightly).
![[RAFT Fig6 Test-Time Documents.png]]
- **Qualitative (Fig. 4)** — on a HotpotQA screenwriter question, DSF answers with a film title (`The Family Man`) while RAFT returns `David Weissman` with a grounded reasoning chain: SFT on QA pairs alone can *damage* context-reading ability.

# Related Papers
💡 Include any related papers that are relevant to this one
- [[Gorilla]] (Patil et al., 2023) — APIBench source for the HuggingFace/Torch/TensorFlow domains; same codebase.
- [[Self-RAG]] (Asai et al., 2023), RA-DIT (Lin et al., 2023), REPLUG (Shi et al., 2023) — fine-tuning LLMs for RAG; RAFT differs by assuming a *fixed* target corpus (in-domain) rather than generalizing to unseen documents.
- [[Atlas]] (Izacard et al., 2023), [[RETRO]] (Borgeaud et al., 2022), kNN-LM — retrieval-augmented pretraining / retrieval-augmented LM lineage.
- [[Lost in the Middle]] (Liu et al., 2023), Shi et al. 2023 (*LLMs can be easily distracted by irrelevant context*), System 2 Attention (Weston & Sukhbaatar, 2023) — the distractor-robustness motivation.
- [[Chain-of-Thought]] (Wei et al., 2022) — the reasoning-format ingredient; LIMA (Zhou et al., 2023), Self-Instruct (Wang et al., 2022) — instruction-tuning / data-recipe lineage.
- [[HotpotQA]] (Yang et al., 2018), [[PubMedQA]] (Jin et al., 2019), [[Natural Questions]], TriviaQA — evaluation sets. Xiong et al. 2023 — the "memorization" alternative to RAG.

# Appendix
💡 Anything else that's in this paper but not mentioned before
- **Training cost/details are thin**: no hyperparameters (LR, epochs, batch size), no data sizes, no retriever specification. Reproducibility relies on the released code.
- **Data generation prompt (Fig. 3)** — GPT-4-1106 is given question + context + verified answer and asked for `##Reason: {reason} ##Answer: {answer}`; Gorilla's APIBench already ships reasoning traces so no generation needed there.
- **Prompt template** (base) — `Question:`, `context:` (concatenated docs), `Instruction: …`, then CoT answer; quotes delimited by `##begin_quote## … ##end_quote##`.
- **Not studied** — out-of-domain generalization (explicitly out of scope, opposite of RA-DIT/ChatQA), long-context vs. RAG trade-offs, and whether RAFT transfers to larger models.
- **Potential leakage concern** — distractor-only training samples deliberately teach memorization of answers, which interacts with privacy/unlearning questions (raised in the memorization related-work section but not measured).

---
# Resources
💡 Include some useful links for better understanding of this paper
- arXiv: https://arxiv.org/abs/2403.10131
- Code (Gorilla repo, `raft/`): https://github.com/ShishirPatil/gorilla
- COLM 2024 accepted list: https://colmweb.org/2024/AcceptedPapers
# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- [[論文介紹] RAFT: Adapting Language Model to Domain Specific RAG](https://datasciocean.com/paper-intro/raft-adapting-language-model-to-domain-specific-rag/)
## RAFT 想解決的問題

RAFT 想解決的問題就是怎麼把既有的 LLM 搭配 RAG 方法應用在 Specific Domain 上。為了要讓 Retrieval-Augmented LLM 可以理解 Domain Knowledge，作者考慮兩種方法：

- In-Context Learning + RAG：其實就是一般的 RAG，透過 Retriever 根據 Query 從 External Database 取出相關的 Document，並且將這些 Document 作為 Demonstration 放在 LLM 的 Context 中，讓 LLM 根據這些額外的 Domain-Specific Document 來回答 Query
- Supervised Fine-Tuning：直接將 LLM 訓練在 Domain-Specific 的資料集上，相當於讓 LLM 記住這些 Domain-Specific Knowledge

但是作者認為上述兩種方法都有一些缺點，並且用「考試」的例子來說明：

- In-Context Learning + RAG : 像是在考試的時候帶著一本參考書，根據考題現場翻書找答案，但是在考前都沒讀過書中的內容
- Supervised Fine-Tuning : 像是在考試前都把參考書的內容背下來了，但是考試的時候沒有帶任何參考書進去翻

其實我覺得這個比喻還蠻有趣的！為了再更清楚的描述 RAFT 想要處理的問題，作者透過「考試」來舉例：

- Closed-Book Exam：像是我們一般在使用一個不具有 RAG 功能的 LLM，LLM 僅能根據它內部的知識來回答 Query，而沒有辦法參考其他 External Document
- Opened-Book Exam：像是在 LLM 加上 RAG 的技巧，讓它可以存取到 External Document
- Domain-Specific Opened-Book Exam：則是指 LLM 一樣有 RAG 可以使用，可以存取到 External Document，但是不管是 User 的 Query 或是 External Document 都是針對某一個 Specific Domain (ex. 企業中的資料)

而本篇論文所提出的方法 RAFT 也是針對 Domain-Specific Opened-Book Exam 的任務！

## RAFT 所提出方法

RAFT 的概念在於：將「In-Context Learning + RAG」與「Supervised Fine-Tuning」的概念結合在一起，讓 LLM 在考試**前**學習根據問題從外部知識中**找到**答案或是**記住**答案；而在考試**時**，也一樣可以透過 RAG 技術取得外部的知識從中找到答案，或者是根據自己的記憶回答問題。

在 RAFT 中，訓練資料集中的一個訓練樣本包含以下元素：

- Question
- A Set of Document：可以分為 Golden Document (一定可以推導出答案) 或是 Distractor Document (不包含答案相關的資訊)
- Answer：可以從 Golden Document 得到，且 Answer 是以 Chain-of-Thought Style 方式呈現，也就是它不單單只是一個 Answer 還包含了怎麼得到這個 Answer 的 Reasoning 過程

針對訓練資料集中 P% 的 Question，其 K 個 Document 中定會有一個 Golden Document，其餘都是 Distractor Document；而針對 Fraction (1 - P)% 的 Question，其 K 個 Document 全部都是 Distractor Document。 RAFT 就使用這樣的訓練資料集，透過 Supervised Fine-Tuning 的方式訓練模型。

看到這裡，我的第一個想法是：「天阿！RAFT 方法也未免太簡單了吧」，但是也覺得蠻有趣的。畢竟很多 RAG 的方法本來就會同時把 Golden 和 Distractor Document 提供給 LLM，讓 LLM 可以學習從這麼多 Document 中找到重要的資訊，同時不被其他的 Distractor Document 所影響。

而 RAFT 做得更極端，是直接只提供 Distractor Document，連一個 Golden Document 都沒有！

作者強調之所以要有一部分的 Question 全都搭配 Distractor Document，是為了讓模型學會「記住」答案，而不是所有問題都從 Document 中找答案。此外，作者也特別強調，在訓練資料集中，針對 Answer 有提供 Reasoning 過程 (Chain-of-Thought Style)，且還有 Cite 到 Document 中的一些內容，可以明顯提昇模型的表現。而現在因為有很強的 LLM 要生成這些 Chain-of-Thought Style 的 Answer 其實也不難！最後，RAFT 訓練後的模型，就遵照一般 RAG 的方式對進行 Inference。

## 讀後想法與疑問

- 這篇的貢獻其實是「data recipe」而非「model」：沒有新架構、沒有新 loss、沒有新 retriever，賣點是 P%_golden、distractor 數量、CoT+quote 這三個超參數。也因此最大的隱憂是 **overfitting to the corpus**——作者自己在 Related Works 就承認測試集和訓練文件相同，所以「in-domain 變強」能不能推廣到新文件、新 retriever 完全沒有驗證。
- `P = 100%` 不是最佳這點最反直覺，但也可以讀成另一種解釋：模型一旦發現「context 裡一定有答案」，就會退化成純粹的 copy machine；留一部分沒有 golden 的樣本，等於逼它在 reading 和 parametric memory 之間做 routing。這其實很像 Self-RAG 想學的「什麼時候該 retrieve / 什麼時候該憑記憶回答」，只是 RAFT 是用資料分佈隱式地教，而非顯式地訓練 reflection token。
- 疑問：Table 1 裡 DSF+RAG 比 DSF 還差（Hotpot 6.38 → 4.41、TF 86.56 → 60.29），這個幅度大到有點可疑，是否因為 DSF 的答案格式（只有答案、沒有 CoT）導致 RAG 場景下 prefix 干擾嚴重？如果 DSF 也用 CoT 訓練，baseline 會不會就吃掉一半的 gap？這點 paper 沒有做 ablation（CoT ablation 只做在 RAFT 上）。
- 實務上最便宜可行的做法：如果要落地到公司內部文件 QA，最小成本版本就是拿 `top-k + 1 golden + 幾個 distractor`，用 GPT-4 生成 quote-style CoT 答案，然後 LoRA SFT。難點反而不在演算法，而在「怎麼確保 golden document 真的被標對」以及「distractor 要從哪裡採樣才夠 hard」。
