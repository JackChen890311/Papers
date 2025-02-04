---
tags:
  - Metric
  - Clustering
todo: true
summary: A metric for evaluating the similarity between two clustering results.
---
# Summary
💡 Write a brief summary of this paper here
NMI stands for Normalized Mutual Information.
Threre are multiple normalization methods: arithimetic, geometric, min and max.
![[Pasted image 20250129182307.png]]
![[Pasted image 20250129182337.png]]
Where I(X, Y) is [[MI]] and H(X) and H(Y) are [[Entropy]].
# Resources
💡 Include some useful links or related papers for better understanding of this concept
- [normalized_mutual_info_score — scikit-learn 1.6.1 documentation](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.normalized_mutual_info_score.html)