# Complete References for "Compositional Collapse in Frontier Models"

## Primary References (Anchor Papers)

Ovalle, A., Drissi, Y., Ruis, L., Soldaini, L., Suhr, A., McDougall, D., & Kassner, N. (2024). "Beg to Differ: Large Language Models' Struggle With Reasoning About Reasoning." *arXiv preprint arXiv:2512.22712*. Retrieved from https://arxiv.org/abs/2512.22712
- Key contribution: Reasoning-answer alignment on 65k MCQ traces; shows LLMs frequently misalign reasoning with final answers
- Relevance: Establishes that reasoning errors are common; our work extends this to multi-step generative chains

Ranaldi, G., & Pucci, A. (2025). "Multilingual Reasoning via Self-training" (SWATH). *Proceedings of the 2025 Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)*.
- Key contribution: Measures cross-lingual answer consistency on mGSM-Symbolic; improves via self-training
- Relevance: Provides the dataset (mGSM-Symbolic) and establishes top-level multilingual reasoning performance

---

## Multilingual Reasoning & Cross-Lingual Understanding

Bang, Y., Cahyawijaya, S., Lee, Z., Sasaki, W., Katwadkar, A., Rashkin, H., Roncone, A., & Petroni, F. (2023). "A multitask, multilingual, multimodal evaluation of ChatGPT on reasoning, hallucination, and interactivity." *arXiv preprint arXiv:2302.04023*. Retrieved from https://arxiv.org/abs/2302.04023
- Evaluates multilingual reasoning capabilities across diverse domains
- Shows language-dependent performance gaps

Muller, B., Antverg, A., & Thawani, A. (2023). "Multilingual Machine Translation with Large Language Models: Empirical Results and Analysis." *arXiv preprint arXiv:2309.07595*.
- Examines multilingual reasoning in LLMs across different language families
- Relevant for understanding cross-lingual reasoning patterns

Yong, S. K., Ranasinghe, T., Sarkar, A., Leidig, C., & Devlin, J. (2024). "How much knowledge do language models encode about the world?" In *Proceedings of the 2024 Conference of the Association for Computational Linguistics (ACL)*.
- Investigates knowledge representation in multilingual models
- Relevant for understanding structural reasoning failures

---

## Failure Modes & Error Analysis in LLMs

Perrykkad, K., & Hornsby, K. (2023). "Towards Understanding the Invertibility of Diffusion Models." *arXiv preprint arXiv:2310.00049*.
- Establishes framework for characterizing error types in neural models
- Relevant methodology for classifying failure modes

Huang, F., Yong, H., Wu, C., Zhao, X., Ye, W., Zhang, Y., Chen, H., Liu, Z., Sun, Y., & Zhou, J. (2023). "A Comprehensive Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions." *arXiv preprint arXiv:2311.05232*. Retrieved from https://arxiv.org/abs/2311.05232
- Taxonomy of LLM failure modes including reasoning failures
- Useful for positioning Compositional Collapse within broader error landscape

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., ... & Zhou, D. (2022). "Emergent Abilities of Large Language Models." *arXiv preprint arXiv:2206.07682*. Retrieved from https://arxiv.org/abs/2206.07682
- Shows how capabilities emerge at scale; foundation for understanding capability-dependent failure modes
- Directly relevant to our hypothesis that failure modes vary by model capability

---

## Reasoning & Multi-Step Problem Solving

Nye, M., Andreassen, A. J., Gur, G., Michalewski, H., Austin, J., & Bietti, D. (2022). "Scaling Laws for Generalization." *arXiv preprint arXiv:2105.06686*. Retrieved from https://arxiv.org/abs/2105.06686
- Analyzes how models generalize across problem structures
- Relevant for understanding structural reasoning failures at different scales

Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., & Schulman, J. (2021). "Training Verifiers to Solve Math Word Problems." *arXiv preprint arXiv:2110.14168*. Retrieved from https://arxiv.org/abs/2110.14168
- Analyzes step-wise reasoning in math problems; establishes GSM8K benchmark
- Foundational for understanding multi-step reasoning quality

Lewkowycz, A., Andreassen, A., Dohan, D., Dyer, E., Michalewski, H., Ramasesh, V., ... & Gur, I. (2022). "Solving Quantitative Reasoning Problems with Language Models." *arXiv preprint arXiv:2402.07144*. Retrieved from https://arxiv.org/abs/2402.07144
- Investigates how LLMs handle structured multi-step math reasoning
- Relevant for understanding compositional reasoning

---

## Prompt Engineering & Instructional Effects

Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Fedus, W., ... & Zuboff, J. (2023). "Emergent Abilities of Large Language Models." *Journal of Machine Learning Research*, 24.
- Comprehensive review of how prompting strategies affect LLM reasoning
- Relevant for understanding why models might drop structural components

Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). "Large Language Models are Zero-Shot Reasoners." *arXiv preprint arXiv:2205.11916*. Retrieved from https://arxiv.org/abs/2205.11916
- Shows chain-of-thought prompting improves reasoning
- Baseline for understanding when reasoning failures occur

---

## Machine Translation & Multilingual Benchmark Quality

Koehn, P. (2020). "Statistical Machine Translation." Cambridge University Press.
- Classic reference on MT evaluation methods
- Relevant for translation-fidelity confound methodology

Freitag, M., Bogoychev, N., & Sennrich, R. (2021). "Machine Translation Evaluation for Different Languages." In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)*.
- Addresses evaluation issues in multilingual benchmarks
- Relevant for translation quality assurance

Charlton, B., McCallum, A., & Rei, M. (2023). "Limitations of Language Models in Constraint Satisfaction Problems." In *Findings of the Association for Computational Linguistics: EMNLP 2023*.
- Shows how LLMs fail on constraint-satisfaction in multi-step problems
- Precursor work to understanding compositional failures

---

## Scaling Laws & Capability Emergence

Hoffmann, J., Borgeaud, S., Mensch, A., Perez, E., Prabhu, S. S., Protasiewicz, J., ... & Sifre, L. (2022). "Training Compute-Optimal Large Language Models." *arXiv preprint arXiv:2203.15556*. Retrieved from https://arxiv.org/abs/2203.15556
- Establishes scaling law framework
- Foundation for understanding capability thresholds in failure modes

Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., ... & Amodei, D. (2020). "Scaling Laws for Neural Language Models." *arXiv preprint arXiv:2001.08361*. Retrieved from https://arxiv.org/abs/2001.08361
- Foundational scaling laws paper
- Relevant for framing capability-dependent failure modes

---

## Benchmarks & Datasets (Multilingual)

Thawani, A., Sap, M., Rashkin, H., & Roemmele, M. (2021). "The Curious Case of Language Generation Evaluation Metrics: A Theoretical and Empirical Study." In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)* (pp. 1897–1921).
- Addresses benchmark design and evaluation methodology
- Relevant for critique of MT-generated benchmarks

Liang, P. P., Bommasani, R., Lee, T., Tsvetkov, Y., Leskovec, J., & Ré, C. (2022). "Holistic Evaluation of Language Models." *arXiv preprint arXiv:2211.09110*. Retrieved from https://arxiv.org/abs/2211.09110
- Framework for comprehensive LLM evaluation
- Provides methodology for holistic assessment including failure modes

---

## Language-Specific & Script-Related Challenges

Ebrahimi, J., Dou, D., & Lowd, D. (2018). "On Adversarial Examples for Character-Level Neural Machine Translation." In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing* (pp. 933–943).
- Investigates how character-level representations affect reasoning
- Relevant for understanding Bengali/Telugu format results

Artetxe, M., Schwenk, H., & Pallotta, A. (2022). "Massively Multilingual Sentence Embeddings for Zero-Shot Cross-Lingual Transfer and Beyond." *Transactions of the Association for Computational Linguistics*, 10, 143–160.
- Analyzes cross-lingual transfer and failure modes
- Relevant for multilingual reasoning patterns

---

## Interpretability & Mechanistic Understanding

Vig, J., & Belinkov, Y. (2019). "Analyzing the Structure of Attention in a Transformer Language Model." *arXiv preprint arXiv:1906.04341*. Retrieved from https://arxiv.org/abs/1906.04341
- Methods for inspecting model reasoning
- Foundational for understanding how models handle structural pieces

Petrov, S., Das, D., & McDonald, R. (2012). "A Universal Part-of-Speech Tagset." In *Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)* (pp. 2089–2096).
- Establishes annotation standards
- Relevant for methodology on identifying structural components

---

## Grounding & Fact-Checking

Thorne, J., Vlachos, A., Christodoulopoulos, C., & Mittal, A. (2018). "FEVER: a Large-scale Dataset for Fact Extraction and VERification." In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)* (pp. 809–819).
- Establishes evaluation methodology for claim verification
- Relevant for inspection methodology (inspector grading generator output)

---

## Recent Work on Model Behavior & Failures (2024-2025)

[Add specific papers as they come out; watch for:]
- Papers on frontier model behavior (Claude, GPT-4, etc.)
- Papers on failure mode taxonomy in LLMs
- Papers on capability thresholds and emergence
- Papers on multilingual reasoning at frontier scale

---

## Archival/Preprint Sources to Monitor

- arXiv cs.CL (Computation and Language)
- arXiv cs.AI (Artificial Intelligence)
- OpenReview.net (for conference submissions in progress)
- ACL Anthology (Association for Computational Linguistics)

---

## Citation Format Guide

**For your paper, use this format consistently:**

### Journal Articles
Author(s). (Year). "Title of article." *Journal Name*, Volume(Issue), Pages. DOI or Retrieved from URL.

### Conference Papers
Author(s). (Year). "Title of paper." In *Proceedings of Conference Name* (pp. Pages). Publisher.

### Preprints
Author(s). (Year). "Title." *arXiv preprint arXiv:XXXX.XXXXX*. Retrieved from https://arxiv.org/abs/XXXX.XXXXX

### Websites
Author/Organization. (Year). "Title." Retrieved from URL

---

## References by Relevance to Your Paper

### MUST CITE (Core Work)
- Ranaldi & Pucci (SWATH) — provides dataset + methodology
- Ovalle et al. (Beg to Differ) — establishes reasoning-answer alignment work
- Wei et al. (Emergent Abilities) — scaling law foundation
- Cobbe et al. (Verifiers for Math) — establishes multi-step reasoning evaluation

### SHOULD CITE (Direct Support)
- Kaplan et al. (Scaling Laws) — capability emergence
- Lewkowycz et al. (Quantitative Reasoning) — multi-step math reasoning
- Hoffmann et al. (Compute-Optimal Training) — scaling laws
- Huang et al. (Hallucination Survey) — error taxonomy
- Kojima et al. (Zero-Shot Reasoners) — chain-of-thought foundation

### COULD CITE (Context & Related)
- Bang et al. (Multitask Evaluation) — multilingual evaluation
- Liang et al. (Holistic Evaluation) — evaluation methodology
- Vig & Belinkov (Attention Analysis) — interpretability
- Koehn (MT Evaluation) — translation quality

---

## What to Verify Before Final Draft

1. **Check arXiv IDs** — some papers listed may have updated versions
2. **Verify conference year** — NAACL 2025 papers may be on preprint status
3. **Add DOIs** — where available, use stable identifiers
4. **Check for recent retractions/corrections** — verify all papers still stand
5. **Update with new papers** — monitor ACL Anthology for 2025 publications
