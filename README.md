# Randomness-Quality-Analyzer
Statistical Evaluation of Pseudo-Random Number Generators (PRNGs)

## Abstract

The generation of high-quality pseudo-random numbers is a cornerstone of modern computational science, underpinning domains ranging from cryptographic security protocols to large-scale Monte Carlo simulations. The fundamental challenge lies in distinguishing between true stochastic entropy and deterministic patterns that may arise from computational limitations or flawed algorithmic design. A pseudo-random generator is considered robust if its output is indistinguishable from true white noise, requiring rigorous statistical validation to ensure that no underlying periodicity or correlation exists.

This research project introduces a structured methodology for the empirical analysis of random sequences via visual and statistical abstraction. By transforming numerical sequences into grayscale spatial matrices, we facilitate the identification of non-random structural artifacts that traditional linear tests might overlook. This visual approach is complemented by information-theoretic metrics—specifically Shannon Entropy—which quantifies the degree of uncertainty, and the Runs Test, which evaluates the sequential independence of data points.

The objective of this framework is to provide a quantitative benchmark for assessing the viability of random number generation algorithms. Through this comparative analysis of synthetic noise versus pattern-induced sequences, we demonstrate that high-entropy results alone are insufficient for declaring randomness, and that spatial independence remains a critical diagnostic criterion in the validation of computational unpredictability.
