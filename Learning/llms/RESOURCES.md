# LLM Training Feasibility — Resources

## Knowledge

- [Llama 3 herd of models paper (Meta AI)](https://ai.meta.com/research/publications/the-llama-3-herd-of-models/)
  Primary source. Reports the 405B model's training compute (30.8M H100 GPU-hours) and infrastructure. Use for: real frontier-scale training numbers.
- [Louie Peters cost estimate for Llama 3.1 405B](https://x.com/_LouiePeters/status/1816443587053092917)
  ~$60M training cost, ~100 days on 16k H100s. Use for: putting a dollar figure on frontier training.
- [Understanding & Estimating GPU Memory Demands for Training LLMs (Max Shapp, Medium)](https://medium.com/@maxshapp/understanding-and-estimating-gpu-memory-demands-for-training-llms-in-practise-c5ef20a4baff)
  Breaks down the ~16-20 bytes/parameter training-memory rule (weights + gradients + Adam optimizer states). Use for: the memory wall math.
- [How much VRAM for fine-tuning? (Modal blog)](https://modal.com/blog/how-much-vram-need-fine-tuning)
  Practical VRAM figures and why fine-tuning (esp. LoRA) is far cheaper than full training. Use for: the realistic at-home alternatives.

## Wisdom (Communities)

- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)
  High-signal community running/fine-tuning open models on consumer hardware. Use for: what's actually feasible at home, GPU choices, LoRA fine-tuning help.

## Gaps
- Need a good primary source on dataset scale/curation (trillions of tokens) for the data wall — current figure is from the Llama 3 paper but a dedicated data-curation reference would be better.
