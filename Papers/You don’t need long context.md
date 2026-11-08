---
title: "You don't need long context"
time: 2611
author: NVIDIA
link: https://arxiv.org/pdf/2611.05306
accepted: None
tags:
  - LongContext
  - Agent
  - ContextCompaction
  - EfficientInference
  - LLM
todo: false
scanned: true
read: false
summary: Frontier LLMs lose little to no accuracy on long-horizon (SWE agents, tool use) and long-input (long-document QA) tasks when forced to work with short 8–48K contexts via frequent compaction and selective reading — yielding 2.2×–233× cost savings — and even keeping only one action per context works, which the authors generalize into the notion of Semantic State Space Models (SSSMs).
---
# Summary
💡 Write a brief summary of this paper here
- **Claim**: long contexts are *not necessary* for "long-context" tasks. An agent that keeps its context short by **compacting frequently** and by **reading long inputs selectively** matches (often beats) the full-context baseline on almost every benchmark tested, while being far cheaper.
- **Cost motivation**: token generation cost grows with context depth. Serving a 256K window instead of 16K costs **3.6× (GLM 5.2), 5.6× (Kimi K2.6), 7× (Qwen 3 Coder Next)** more per generated token (Fig. 1); on-device (DGX Spark) inter-token latency roughly **doubles** (Fig. 2).
- **Assumption under attack**: context windows (200K–1.05M) already exceed whole novels/Bibles (Table 1), yet input-context length does not itself prove that a task *needs* long context.
- Three research questions, all answered **yes**: (RQ1) long-horizon tasks without long context; (RQ2) long-input tasks without long context; (RQ3) long-horizon tasks with **at most one action per context**.
- Deliverable beyond the experiments: **Semantic State Space Models (SSSMs)** — models post-trained to carry an *explainable natural-language state* between single-action turns (a "semantic" analogue of an SSM's hidden state).

![[LongContext Fig1 Cost per 1M Output Tokens.png]]

# Methodology
💡 Describe the methodology used in this paper
- **Definitions** fixed up front: *long context* ≈ approaching a large fraction of typical windows (≳256K); *short context* ≈ 16K–50K tokens; *long-horizon task* = many sequential dependent actions; *long-input task* = task whose input alone would be a long context.
- **Key reduction**: a long-input task can always be turned into a long-horizon task by storing the input as files and giving the model a **selective reading tool** — so only one mechanism needs to be studied twice.
- **Harnesses**: bare ReAct loop, one Bash action per turn — `mini-swe-agent` for SWE/terminal tasks, and a generalized `mini-agent` for the rest. Only system prompt + task in the first message; everything else lives in the environment.
- **Three context regimes** (Fig. 3), reported as "total context limit / compaction threshold":
  - **FHA** (Full-History Accumulation): baseline, history never truncated.
  - **EoCC** (End-of-Conversation Compaction): compact once the threshold is hit, restart a fresh conversation with task + recap.
  - **SAC** (Single-Action Compaction): exactly one environment action per conversation; only a compact semantic state is carried over.
- **Compaction quality matters more than quantity** (Appendix A): best compactions are *not* summaries but **briefs for future execution** — (1) verbatim/near-verbatim task, (2) current occupation, intent and next steps, (3) artifacts relevant to future execution: decomposed plan, completion criteria, pointers to evidence.
- **Long-input handling** (Appendix E): documents exposed as `input01.txt…`; agent uses `grep`, `sed`, `head`, plus helpers `doc-stats`, `docs-list`, `doc-read` (bounded ≤8K chars), `doc-syn` (synonym expansion). Prompt explicitly forbids dumping whole documents.
- **Models**: closed — **Claude Opus 4.5**, **GPT 5.6 Sol** (main accuracy runs); cloud open-weight — GLM 5.2, Kimi K2.6, Qwen 3 Coder Next (throughput study); local — Qwen 3.6 27B, Qwen 3 Coder Next, Gemma 4 31B, Step 3.7 Flash, MiniMax M2.7 (DGX Spark, NVFP4/GGUF 3–4 bit), spanning hybrid linear/softmax, sliding-window, gated GQA and full softmax attention.
- **Cost model** (Appendix B): measure peak decode throughput vs window size → 16K/256K ratio; round to **r = 0.20**; anchor retail price at max window, interpolate linearly in W down to r× at 16K; keep the vendor's 5:1 output:input and 10:1 input:cached-input ratios → *Estimated Optimized Retail Cost* (EORC).

![[LongContext Fig3 Context Management Regimes.png]]

# Experiments
💡 List the experiments settings and results of this paper
- **Benchmarks — long-horizon**: SWE-bench Verified (500), SWE-bench Multilingual (300, 9 languages), Terminal-Bench 2.1 (89), FRAMES (824, agentic Wikipedia search), τ²-bench (184, simulated user + policy), BFCLv3 (200 long-context multi-turn episodes). **Long-input**: LongBench v2 (503), LOONG (1,600 multi-doc), AA-LCR (100, ~100K tokens), NIAH (125, 16K–500K), RULER (13 tasks @256K/500K), Counting-Stars (192), BABILong (550, 64K–1M).
- **RQ1 — long-horizon, EoCC vs FHA**: accuracy deltas range **−3.7 to +5.6 pp (Opus 4.5)** and **−3.3 to +4.4 pp (GPT 5.6 Sol)** over 22 configurations; only ≤5/22 configs lose >2 pp. Estimated cost savings **2.2×–8.8× (Opus)** and **2.4×–5.0× (GPT)**.
  - SWE-bench Verified: Opus 70.0 → 74.8 (24K/18K), GPT 84.4 → 88.8 (48K/36K); the tightest 16K/12K costs 1.2 pp for Opus.
  - Terminal-Bench: Opus 47.2 → 52.8 (32K/24K); GPT 87.6 → 88.8 at 48K, −2.2 pp at 16K.
  - Weak spots: **FRAMES always loses** 1.3–3.7 pp (Opus) / 1.5–3.3 pp (GPT) at 7.7× / 3.8× lower cost; SWE-bench Multilingual −2.0/−1.6 pp at 16K/12K; τ²-bench within 1.1 pp.
- **RQ2 — long-input, selective reading + EoCC**: deltas **−0.4 to +40.0 pp (Opus)** and **+1.0 to +30.9 pp (GPT)**; savings **6.5×–54.6× (Opus)** and **4.4×–233.3× (GPT)**.
  - NIAH 60/80% → **100%/100%** with zero compactions (pure selective reading); RULER recall 62.5→95.7 (Opus), 65.5→96.4 (GPT); BABILong +24.9/+23.3 pp; Counting-Stars exact-match 65.1/76.6 → 81.2/81.2.
  - LOONG avg 70.1→80.2 (Opus), 79.3→84.6 (GPT) with 13–17× lower cost; AA-LCR 65→84% (Opus).
  - Conversation length stays **bounded as document length grows** (Figs. 7–8); typical long-input runs need **0 median compactions** — selective reading does nearly all the work.
- **RQ3 — SAC (one action per context)**: Opus SWE-bench 70.0 → 70.2, Terminal-Bench 47.2 → **51.8**; GPT 84.4 → 82.4, 87.6 → 84.3. Median peak live context 7–9K, **max falls from 130–200K to 15–37K**.
- **Open-weight models** (Appendix D): robust — Qwen 3.6 27B (68.6 → 65.0), MiniMax M2.7 (72.6 → 67.8) down to 16K/12K; fragile — **Qwen 3 Coder Next collapses 53.0 → 3.6** on SWE-bench Verified at 16K/12K because its verbose trajectories leave too little room to progress between compactions.
- **Token-spend accounting**: under compaction, *new* input tokens rise and cached tokens fall, output tokens rise modestly; total conversation length does **not** blow up → savings are not eaten by re-work.

![[LongContext Fig5 Long-Horizon Results.png]]

![[LongContext Fig6 Long-Input Results.png]]

# Related Papers
💡 Include any related papers that are relevant to this one
- SWE-bench (Jimenez et al., 2024) and SWE-agent (Yang et al., 2024) — the agentic SWE setting and agent-computer interface this paper builds on; SWE-smith for SWE-bench Multilingual.
- ReAct (Yao et al., 2023) — the minimal thought/action loop both harnesses implement; `mini-swe-agent` (SWE-agent team).
- Terminal-Bench (2026), τ²-bench (Barres et al., 2025), BFCL (Patil et al., 2025) — long-horizon tool-use / multi-turn benchmarks.
- LongBench v2 (Bai et al., 2025), LOONG (Wang et al., 2024), AA-LCR (2025), RULER (Hsieh et al., 2024), BABILong (Kuratov et al., 2024), Counting-Stars (Song et al., 2025), NIAH (Kamradt, 2023) — the long-input suite that the paper reinterprets as retrieval tasks.
- "Lost in the middle" (Liu et al., 2024) — evidence that long contexts are poorly used even when available.
- State-space models: S4 (Gu et al., 2022), Mamba (Gu & Dao, 2024), HiPPO/linear state-space layers (Gu et al., 2021) — the architectural analogue behind the SSSM proposal.
- Turing (1937) — cited as the conceptual argument: bounded input + finite state suffices for anything computable.
- Compression-efficiency baselines used as comparison points for the 3.6–7× savings: QUIK (Ashkboos et al., 2024), additive quantization (Egiazarian et al., 2024), structured sparsity (Busato & Pool, 2020).

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- **SSSM definition** (§5.1): a model post-trained to (1) read a natural-language state description, (2) reason about the next action, (3) act, (4) register the outcome, (5) rewrite the state description so a *different inference instance* can continue. Explains why context could be constant-cost by design; argued to be more token- *and* data-efficient than full-history training.
- **Why compaction is lossy but fixable** (§3.1): a coin-toss tool example guarantees information loss under any fixed compaction budget; the fix is not a bigger window but **logging every message and exposing it via selective reading** — i.e. "need-to-know" information ≠ "must-be-in-context" information.
- **Compaction prompts** (Appendix G): both harnesses use a fixed handoff template — objective, established facts (paths/symbols/errors), applied changes with verification status, verification runs, dead ends, remaining plan + immediate next command + completion condition.
- **Task/token bookkeeping**: results tables report *total length* (sum of final sub-conversation lengths) separately from *peak length*, to show re-work does not silently reinflate cost.
- **Skeptical aside on NIAH**: the whole needle-in-a-haystack paradigm presupposes long-context tasks exist; with a filesystem + grep it becomes a trivially solved retrieval task (100% for both models).
- **Scope limits** stated by the authors: cannot rule out tasks where long context genuinely helps, and does not show every task is short-context solvable.

---
# Resources
💡 Include some useful links for better understanding of this paper
- Paper: https://arxiv.org/abs/2611.05306 · PDF: https://arxiv.org/pdf/2611.05306 · HTML: https://arxiv.org/html/2611.05306v1
- NVIDIA DLER lab page: https://nv-dler.github.io
- Project Moonshot — Local Frontier Intelligence: https://research.nvidia.com/labs/lpr/lfi/
- Harnesses used: https://github.com/swe-agent/mini-swe-agent

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- The strongest result is not "compaction is fine" but **"the information needed to solve a task is tiny relative to its input"** — the near-zero median compaction counts on long-input benchmarks say the agent never even needed the documents it was given.
- Potential conflation: selective reading is a *retrieval* success. Tasks where the evidence must be aggregated over the entire document (e.g., global counting, style/structural questions, "does this contract contradict itself anywhere") may not degrade gracefully under grep-and-read. BABILong/Counting-Stars are the closest stress test and they *improve*, which is suspicious — likely because grep with known entity strings is near-oracle.
- EoCC's compaction template bakes in a very human notion of a "handoff brief". It would be interesting to see how sensitive accuracy is to that prompt versus to the threshold — the paper reports threshold sweeps but not template ablations.
- SAC's peak contexts (~8–9K median, 15–37K max) are shockingly small for SWE work; if that holds with open models, KV-cache and serving economics change fundamentally (a 16K-window model could be served 7× faster).
- The failure mode to watch is Qwen 3 Coder Next: verbose models spend their whole budget on narration, so short-context training/verbosity control becomes a first-class requirement, not an afterthought.
- Fair criticism they preempt: cost savings use an *estimated* interpolated retail price (r=0.20, linear in W), not actual vendor pricing. The real retail prices are flat per token, so the savings only materialize for whoever serves the model, not necessarily for API buyers.
- Open question: can a model be post-trained to *prefer* short contexts (SSSM) without losing the ability to notice that something is missing from its state? Compaction errors are silent by construction.
