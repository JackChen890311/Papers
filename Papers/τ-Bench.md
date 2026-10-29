---
title: "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
time: 2406
author: Sierra
link: https://arxiv.org/pdf/2406.12045
accepted: None
tags:
  - Agent
  - Benchmark
  - ToolUse
  - UserSimulation
  - LLM
todo: false
scanned: true
read: false
summary: A benchmark for tool-agent-user interaction in realistic customer-service domains, where an LM-simulated user and an agent with APIs and policy documents must reach a unique ground-truth database state, evaluated with a new reliability metric pass^k.
---
# Summary
💡 Write a brief summary of this paper here
- τ-bench (Tool-Agent-**U**ser Interaction Benchmark): dynamic conversations between an LM-simulated user and an agent that has domain APIs + a written policy document; evaluates the final **database state** against an annotated unique goal state.
- Key gap targeted: existing agent benchmarks give all information upfront (no human-in-the-loop) and do not test adherence to domain-specific rules.
- New metric **pass^k** (all k i.i.d. trials succeed) measures reliability/consistency, in contrast to pass@k (at least one of k succeeds).
- Result: even gpt-4o with function calling solves <50% of tasks on average (61.2% retail, 35.2% airline), and pass^8 drops below 25% in retail.

![[TauBench Fig1 Overview.png]]

# Methodology
💡 Describe the methodology used in this paper
- **POMDP formulation** $(\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{T},\mathcal{R},\mathcal{U})$ with $\mathcal{S}=\mathcal{S}_{db}\otimes\mathcal{S}_{user}$, $\mathcal{A}=\mathcal{A}_{db}\cup\mathcal{A}_{user}$: the agent acts on (1) databases via API tools and (2) a simulated user via natural language.
- **Domain components** (modular, easy to extend):
  - JSON databases (hidden from agent and user), only accessible through Python API tools (write / non-write).
  - Markdown **domain policy** placed in the agent's system prompt (procedures, restrictions, e.g., "basic economy cannot be modified").
  - JSON task instance = hidden user instruction + annotation of ground-truth write actions (and required output strings).
- **User simulation**: gpt-4-0613 with the task instruction as system prompt; it sees only the agent–user chat, not the agent–tool history; episode ends on `###STOP###`.
- **Reward** $r = r_{action}\times r_{output}\in\{0,1\}$: final DB must equal the unique annotated goal DB **and** all required information (e.g., prices) must appear in agent-to-user messages — rule-based, cheap, and faithful while allowing arbitrary dialogue paths.
- **pass^k** = $\mathbb{E}_{task}\left[\binom{c}{k}/\binom{n}{k}\right]$ over n trials with c successes; pass@k = $1-\mathbb{E}\left[\binom{n-c}{k}/\binom{n}{k}\right]$. Default main metric is pass^1.
- **Construction (3 stages)**: (I) manual design of minimal-but-realistic schemas/APIs/policies → (II) gpt-4 generates sampling code for data entries (manually debugged) → (III) manual task annotation iterated with gpt-4-turbo agent runs until the outcome is provably unique.
- **Domains**: τ-retail (500 users, 50 products, 1,000 orders; 7 write + 8 read tools; 115 tasks) and τ-airline (500 users, 300 flights, 2,000 reservations; 6 write + 7 read tools; 50 tasks, more complex ad-hoc rules).
- **Agent baselines**: native function calling (FC), text-formatted ReAct, and Act-only; max 30 actions per task; temperature 0 (agent) / 1.0 (user), ≥3 trials per task.

# Experiments
💡 List the experiments settings and results of this paper
- **Models**: gpt-4o, gpt-4-turbo, gpt-4-32k, gpt-3.5-turbo, claude-3 opus/sonnet/haiku, gemini-1.5 pro/flash, mistral-large, mixtral-8x22b, llama-3-70B (only last two open-weight).

![[TauBench Table2 Main Results.png]]

- **Main results (pass^1)**: gpt-4o best (61.2 retail / 35.2 airline / 48.2 avg); claude-3-opus 39.5 avg; open-weight llama-3-70B only 14.6 avg → large gap to proprietary models and everything far from solved.
- **Method comparison**: natively supported FC consistently beats text ReAct and Act-only; adding reasoning traces helps text methods; adding a "think" function to FC did not help.
- **Consistency (pass^k)**: for gpt-4o, >60% pass^1 becomes <25% at pass^8 — agents are fragile to mere conversational stochasticity.

![[TauBench Fig4 PassHatK.png]]

- **Policy ablation** (remove policy from system prompt): gpt-4o drops 61.2→56.8 (retail) and 33.2→10.8 (airline); gpt-3.5 barely changes → models mostly act by commonsense and under-use the policy, especially weaker models.
- **Failure analysis** (36 genuine failures out of 115 gpt-4o retail trajectories, 1 trial each):
  - Wrong argument / complex DB reasoning (33.3%): correct tool but wrong arguments; hallucinated IDs: 0.46 per task for gpt-4o vs 2.08 (gpt-3.5 FC) and 6.34 (gpt-3.5 Act).
  - Wrong decision / rule following (25.0%): violates policy (e.g., issues two exchange calls when only one is allowed).
  - Wrong information (22.2%): omits or miscalculates required info, which can derail the user's request.
  - Partially resolves compound requests (19.4%): stops after the first of several user requests; more ground-truth writes ⇒ lower success.

![[TauBench Fig5 Failure Breakdown.png]]

- **Cost**: gpt-4o FC agent $0.38 + gpt-4 user sim $0.23 per retail task (~$200 for one trial over all tasks); 95.9% of agent cost is input tokens (long policy + tool definitions).

# Related Papers
💡 Include any related papers that are relevant to this one
- [[ReAct]] — text-formatted thought/action baseline used here.
- [[Reflexion]] / self-reflection — unsuitable for user-in-the-loop settings (one shot at serving the user).
- ToolEmu — LM-emulated tool execution, focused on safety risks; single-turn instructions.
- ToolBench, Berkeley Function Calling Leaderboard (BFCL), MetaTool — tool/function-calling benchmarks with all info given upfront.
- Task-oriented dialogue: MultiWOZ-style static datasets (schema-driven), rule-based/symbolic user simulators, and crowdsourced human evaluation.
- LM-as-user-simulator work (Generative Agents, NPC simulation, WebShop / web-search human-in-the-loop).
- Follow-up work: τ²-bench extends this to dual-control settings (agent + user both acting on the environment).

# Appendix
💡 Anything else that’s in this paper but not mentioned before
- Task validation: each τ-retail task was run with >40 gpt-4-turbo trials; tasks with zero/low success were manually inspected and fixed (Figure 7).
- Retail policy constraints that simplify annotation: each pending order can be canceled/modified only once, each delivered order returned/exchanged only once, items cannot be exchanged for another product type.
- Airline policy includes multi-hop rules over membership tier × cabin class (baggage allowance, payment-method combination, 24h cancellation window) — main source of difficulty.
- Reward limitation (acknowledged): $r=1$ is necessary but not sufficient — e.g., a return executed without explicit user confirmation still scores 1 while violating policy.
- Simulator limitations: instruction typos/ambiguity; users lack domain knowledge; the simulator LM itself may mis-reason, miscalculate, lose long-context memory, or drift from its instruction.
- Curation bias: user prompts were tuned using the gpt-4-turbo FC agent, which may implicitly bias task difficulty toward that model's failure modes.
- Future directions: more complex domains (medical, tax, legal), systematic uniqueness checks, richer metrics (e.g., LM-based rule-following checks), domain-specific fine-tuning or agent scaffolding.

---
# Resources
💡 Include some useful links for better understanding of this paper
- [Paper (arXiv:2406.12045)](https://arxiv.org/abs/2406.12045) · [HTML](https://arxiv.org/html/2406.12045v1)
- [Code & data (sierra-research/tau-bench)](https://github.com/sierra-research/tau-bench)
- [Sierra blog on τ-bench](https://sierra.ai/blog/benchmarking-ai-agents)

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper
- The most transferable idea is **pass^k vs pass@k**: for user-facing agents, retries are not free, so reliability (all k succeed) matters more than discovery. Worth reporting alongside success rate in any agent eval.
- Evaluation via final DB state is elegant: it removes noisy LLM-as-judge trajectory grading, but trades off the ability to detect rule violations that do not change the DB (no confirmation, wrong intermediate reads).
- Because the user simulator is gpt-4-0613, part of the measured failure rate is *simulator* failure (miscalculation, forgetting the instruction). Absolute numbers should be read as a lower bound on agent capability.
- Interesting follow-up question: how much of the airline gap comes from long-context policy reading vs. multi-hop numerical reasoning? The policy-removal ablation only partially disentangles this.
- pass^8 <25% suggests the bottleneck is decision consistency, not raw capability — methods that verify/self-check against the policy before a write action seem the natural next step.
