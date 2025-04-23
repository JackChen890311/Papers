---
tags:
  - Metric
todo: false
summary: A metric for evaluating the diversity of GenAI outputs.
---
# Summary
💡 Write a brief summary of this paper here
The **Vendi Score** is a relatively new metric proposed for evaluating **diversity** in generative AI outputs — especially in fields like image generation, text generation, and creative tasks.

---

### 🧠 **What is the Vendi Score?**
- The **Vendi Score** measures the **effective number of distinct outputs** a model generates.
- It’s designed to capture both **variety** and **distribution balance** — meaning not just how many different samples you generate, but whether they are meaningfully distinct from one another.
- The core idea is rooted in **entropy** and **probability distributions**, but applied to **feature embeddings** rather than raw outputs.
### 🔬 **How does it work?**
1. First, a set of generated samples (e.g., images or texts) are passed through a **feature extractor** (usually a pretrained model like CLIP for images or a language model for text) to get embeddings.
2. The pairwise similarity of these embeddings is calculated.
3. Using these similarities, the Vendi Score computes a **soft count** of how many effectively different clusters or modes the set contains.
4. The higher the Vendi Score, the more **diverse** and **balanced** the outputs are.
### 💡 **Why is it useful?**
- Traditional diversity metrics like **Fréchet Inception Distance (FID)** or **Inception Score (IS)** are often biased toward quality rather than pure variety.
- The Vendi Score gives a **more nuanced view of diversity** — especially valuable when you're evaluating creative generation (e.g., art, designs, novel ideas) where variety matters more than strict realism.
- It’s particularly helpful in detecting **mode collapse** — when a generative model only outputs slight variations of the same thing.
### 📈 **In short:**
- **Vendi Score** ≈ Measures how many distinct “ideas” or “concepts” a model is generating, rather than just counting samples.
- Higher score = better variety and balance.
# Resources
💡 Include some useful links or related papers for better understanding of this concept