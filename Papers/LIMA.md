---
title: "LIMA: Less Is More for Alignment"
time: 2305
author: Meta AI; University of Southern California; Tel Aviv University; Carnegie Mellon University
link: https://arxiv.org/pdf/2305.11206
accepted: None
tags:
  - LLM
  - Alignment
  - InstructionTuning
  - DataEfficiency
todo: false
scanned: true
read: false
summary: Fine-tuning a 65B LLaMa on only 1,000 curated examples (no RLHF) matches or beats RLHF-tuned models, showing alignment mostly teaches style/format while knowledge comes from pretraining.
---
# Summary
💡 Write a brief summary of this paper here
- Proposes the **Superficial Alignment Hypothesis**: a model's knowledge and capabilities are learned almost entirely in pretraining, while alignment only teaches *which sub-distribution of formats* to use when talking to users.
- Test: **LIMA** = LLaMa 65B supervised fine-tuned on exactly **1,000** curated prompt-response pairs (~750K tokens), **no RLHF, no preference modeling**, no multi-turn data.
- Result: LIMA is preferred over Alpaca 65B (52K examples) and OpenAI DaVinci003 (RLHF) most of the time; outputs are equal-or-better than **GPT-4 in 43%**, Bard 58%, Claude 46% of cases. 88% of responses meet the prompt requirement, 50% are "excellent".
- Takeaway: both *scale of data* and *RLHF* may be far less important than pretraining quality + a small, diverse, high-quality alignment set.
![[LIMA Fig1 Human Preference.png]]

# Methodology
💡 Describe the methodology used in this paper here
- **Data (1,000 examples, ~750K tokens)** — inputs diverse, outputs uniformly styled as a helpful assistant:

| Source | # | Avg input len | Avg output len |
|---|---|---|---|
| Stack Exchange (STEM) | 200 | 117 | 523 |
| Stack Exchange (Other) | 200 | 119 | 530 |
| wikiHow | 200 | 12 | 1,811 |
| Pushshift r/WritingPrompts | 150 | 34 | 274 |
| Super-Natural Instructions | 50 | 236 | 92 |
| Authors (manual, Group A) | 200 | 40 | 334 |

- **Quality filtering** (Stack Exchange): keep self-contained titles, top answers with score ≥10, drop <1200 or >4096 chars, drop first-person ("I", "my") and cross-references ("as mentioned"), strip links/images/HTML, keep code blocks and lists.
- **Diversity control**: 75 STEM + 99 other exchanges sampled with temperature τ=3; wikiHow sampled category-first then article.
- **Manual authoring**: 200 prompts + hand-written answers in a uniform assistant tone ("acknowledge the question, then answer") — hypothesized to act like a chain-of-thought cue. Includes **13 toxic/malicious prompts** with refusal answers.
- **Training**: 15 epochs, AdamW (β1=0.9, β2=0.95, wd=0.1), lr 1e-5 → 1e-6 linear decay, no warmup, batch 32, max len 2048.
  - Special **end-of-turn (EOT)** token to separate speakers instead of reusing EOS.
  - **Residual dropout**: p_d=0.0 at bottom layer → 0.3 at top (0.2 for smaller models).
- **Checkpoint selection**: perplexity does *not* track generation quality (Appendix B), so checkpoints are picked manually between epoch 5–10 on a 50-example dev set.
- Test set: 300 prompts (r/AskReddit 70 + authors' Group B 230), dev: 50.

# Experiments
💡 List the experiments settings and results of this paper
- **Human preference study** (300 prompts, crowd annotators, tie-discounted agreement 78–82%; GPT-4 as annotator agrees with humans ~78–79%):

| Baseline | LIMA wins | Tie | LIMA loses |
|---|---|---|---|
| Alpaca 65B (52K data) | 53% | 21% | 26% |
| DaVinci003 (RLHF) | 44% | 21% | 35% |
| Bard | 33% | 25% | 42% |
| Claude | 24% | 22% | 54% |
| GPT-4 | 18% | 25% | 57% |

- **Absolute quality** (50 random test prompts): 50% Excellent, 38% Pass, 12% Fail.
- **Out-of-distribution** (20 prompts, no related task in training): 45% Excellent / 35% Pass / 20% Fail → similar to in-distribution, i.e. it generalizes to unseen task types.
- **Safety**: only 13 safety examples; responds safely to 80% of 30 sensitive test prompts (6/10 explicit malicious). Explicit requests are refused; implicit harmful intent (e.g. drugging a dog) is often answered.
- **Ablations (7B LLaMa, ChatGPT 6-point Likert scoring, 2,000 examples per setting)**:
  - *Diversity*: filtered Stack Exchange (3.83) ≫ wikiHow (3.49) — homogeneous "how-to" prompts hurt.
  - *Quality*: filtered (3.83) vs unfiltered Stack Exchange (3.33) → +0.5 from filtering alone.
  - *Quantity*: 2K → 32K examples (16×) shows **no improvement, plateau** — data volume alone does not buy alignment.
- **Multi-turn**: zero-shot dialogue is surprisingly coherent but 6/10 chats fail within 3 turns (45.2% excellent, 35.7% fail). Adding **30 dialogue chains** (1,030 examples) raises excellent to 76.1%, failures 15/42 → 1/46 turns; better in 7/10 conversations.
![[LIMA Fig5 Diversity Quality.png]]
![[LIMA Fig6 Data Quantity.png]]
![[LIMA Fig3 Absolute Analysis.png]]
![[LIMA Fig7 Dialogue Turns.png]]
- **Limitations**: curating such examples is expensive and hard to scale; LIMA is not product-grade robust (an unlucky decode or adversarial prompt can produce a weak answer).

# Related Papers
💡 Include any related papers that are relevant to this one
- LLaMa — pretrained base model (Touvron et al., 2023, arXiv 2302.13971).
- Stanford Alpaca — 52K self-instruct distilled data, the main data-quantity baseline (Taori et al., 2023).
- Self-Instruct / Unnatural Instructions / Vicuna — automatic instruction-data generation, i.e. quantity-over-quality.
- FLAN / T0 / Super-Natural Instructions — large-scale instruction tuning (Chung et al., 2022; Sanh et al., 2022; Wang et al., 2022).
- InstructGPT — RLHF alignment baseline (Ouyang et al., 2022); DaVinci003 is its product.
- Constitutional AI — RL from AI feedback, Claude baseline (Bai et al., 2022).
- [[DPO]] — later, simpler preference optimization; contrast with LIMA's "no preference data at all".
- [[Chinchilla]] — the pretraining scaling-laws view that LIMA complements ("alignment scaling" is different).
- [[T5]] / [[BART]] — classic pretrain-then-finetune framing that LIMA pushes to an extreme.

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- **Fig. 9 / Appendix B**: validation perplexity *rises* while ChatGPT-rated generation quality also rises during fine-tuning — classic perplexity is anti-correlated with alignment quality here.
- **Appendix D**: exact ChatGPT 6-point helpfulness rubric used for the 7B ablations (1 = not helpful … 6 = highly helpful, well structured).
- **Appendix E**: format-following is extremely sample-sensitive — removing just **6** examples with structural constraints (bulleted summary, product page with Highlights/About/How to Use) breaks structured output (e.g. a marketing plan rambles instead of using the requested section headers). Adding them back enables zero-shot structured generation for unseen formats.
- **Fig. 10**: six sample training examples across sources (Stack Exchange STEM/Other, wikiHow-like, manually authored chitchat/advice), showing the uniform "acknowledge then answer / bullets" output style.
- **Annotation interface (Fig. 11)**: two answers shown per prompt, options A better / B better / neither; annotators asked to imagine they were the prompter.

---
# Resources
💡 Include some useful links for better understanding of this paper
- Paper: https://arxiv.org/abs/2305.11206
- PDF: https://arxiv.org/pdf/2305.11206
- HTML: https://arxiv.org/html/2305.11206v1
- LLaMa (base model): https://arxiv.org/abs/2302.13971
- Stanford Alpaca: https://github.com/tatsu-lab/stanford_alpaca

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- The core claim is a *decomposition* claim: pretraining = knowledge, SFT = style/format. It predicts that a weak base model cannot be rescued by more alignment data — worth testing on modern small models (does 1K examples still suffice at <1B params?).
- "Diversity of prompts, uniformity of responses" is the operative design rule; the wikiHow-vs-Stack-Exchange ablation is the cleanest evidence and is cheap to reproduce.
- Suspicious detail: the 43%-vs-GPT-4 number comes from crowd annotators over 300 prompts; response style/length alone can bias such preferences. A length- and format-controlled re-run would be more convincing.
- The 13 safety examples yielding 80% safe responses is a very thin basis for a safety claim, and the implicit-intent failure (Benadryl for a neighbor's dog) shows exactly the failure mode of "style alignment without values".
- Question: is the 30-dialogue-chain jump (45% → 76% excellent) a data effect or a *loss-masking/format* effect (multi-turn teaches EOT usage)? An ablation on response-only loss would separate these.
- Follow-up worth reading: how far does this scale down in data *and* up in curation cost — what's the actual quality/cost frontier versus self-instruct distillation at 10K–100K examples?
