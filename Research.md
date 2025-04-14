# Main Method
- [[InspirationTree]]
# Based on
- [[Diffusion Models]]
- [[Textual Inversion]]
- [[ReVersion]]
# Related Topics
# Progress
See [Research Status Update](https://docs.google.com/presentation/d/1QU0q0hEk5PCZbOgBpnlIRauD-u8V3l4USPU5P_oWGUg/edit#slide=id.p) for details
## Observation: Consistency Score is Dropping
Original method do not provide any guidance
### Related Papers
- [[Attend-and-Excite]]

## Observation: Background Leakage
Example: Backpack dog from [[Dreambooth]]
### Related Papers
- [[DiffSeg]]
- [[DiffuMask]]
- [[ViCo]]
- [[Break-A-Scene]]
- [[ConceptExpress]]

## Method
Main Idea: Attention Map from [[Prompt-to-Prompt]]
- Background Leakage
	- Attention map foreground segmentation
		- See [[Vico]]
		- Also [[DiffSeg]], [[DiffuMask]]
	- Use mask for foreground and only learns from it
		- How? Refer to [[Break-A-Scene]]
- Guidance
	- Split and merge from [[ConceptExpress]]
	- Refer to [[Attend-and-Excite]] (Works on attention maps)
