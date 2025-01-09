---
title: "RecMind: Large Language Model Powered Agent For Recommendation"
time: 2308
author: "School of Computing and Augmented Intelligence, Arizona State University\r; Amazon Alexa AI"
link: https://arxiv.org/pdf/2308.14296
accepted: None
tags:
  - LLM
  - Text
  - Recommendation
todo: false
scanned: true
read: false
summary: Use LLM as pipeline controller for recommedation system
---
# Summary
💡 Write a brief summary of this paper here
Use [[LLM]] as pipeline controller, with external helpers like memory and tools
(But most tasks are for a given user_x, which means it need user history)
![[Pasted image 20240903112315.png]]
# Methodology
💡 Describe the methodology used in this paper
Self-inspiring:
- Variation of ToT (Tree-of-Thoughts)
- Retaining all the explored state
- Thought, Action, Observation (ReAct)
![[Pasted image 20240903112522.png]]
---
Memory
- Personalized memory
- World knowledge
- Domain specific knowledge
- Real time data (e.g. web access)

Tools
- Database access
- Web search
- Text Summarization

# Experiments
💡 List the experiments settings and results of this paper
Dataset
- Amazon Review (3 Categories)
- Yelp

Tasks
- Rating Prediction: Better
- Direct Recommendation: Not as good as pre-trained expert
- Sequential Recommendation:  Not as good as pre-trained expert
- Explanation Generation: Better
- Domain Transfer: Better

# Related Papers
💡 Include any related papers that are relevant to this one

# Appendix
💡 Anything else that’s in this paper but not metioned before

---
# Resources
💡 Include some useful links for better understanding of this paper

# Personal Notes
💡 Personal thoughts, reflections, or questions about this paper