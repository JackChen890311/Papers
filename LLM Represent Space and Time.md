# Summary
23/10
- [[LLM]]s learn linear representations of space and time across multiple scales.
- Various experiments to show that the representations are robust and unified across different entity types  (e.g. cities and landmarks)
- Identify individual “space neurons” and “time neurons"

---

![[Pasted image 20231016155138.png]]
 
 ---
# Experiments
- Datasets: Space & Time Dataset (Like cities, historical figures, newspaper headlines)
- LLM: LLaMa2, with embedding from different layers
- Method: Linear Probing (Just a Simple Linear Layer)
- Experiments:
	- Original Settings with different layers
	- Linear vs MLP
	- Different Prompt
	- Hold-out of Entities
	- PCA on extracted features
	- “space neurons” and “time neurons"
 ---
 
![[Pasted image 20231016160233.png]]

---

![[Pasted image 20231017191241.png]]

---

![[Pasted image 20231017190746.png]]

---

![[Pasted image 20231017190851.png]]

![[Pasted image 20231017190903.png]]

---

![[Pasted image 20231017190949.png]]

---

![[Pasted image 20231017191006.png]]

---
# PDF
![[LANGUAGE MODELS REPRESENT SPACE AND TIME.pdf]]