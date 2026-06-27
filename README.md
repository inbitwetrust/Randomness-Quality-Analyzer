# Randomness Quality Analyzer: Statistical Evaluation of Pseudo-Random Number Generators (PRNGs)

## Abstract

The generation of high-quality pseudo-random numbers is a cornerstone of modern computational science, underpinning domains ranging from cryptographic security protocols to large-scale Monte Carlo simulations. The fundamental challenge lies in distinguishing between true stochastic entropy and deterministic patterns that may arise from computational limitations or flawed algorithmic design. A pseudo-random generator is considered robust if its output is indistinguishable from true white noise, requiring rigorous statistical validation to ensure that no underlying periodicity or correlation exists.

This research project introduces a structured methodology for the empirical analysis of random sequences via visual and statistical abstraction. By transforming numerical sequences into grayscale spatial matrices, we facilitate the identification of non-random structural artifacts that traditional linear tests might overlook. This visual approach is complemented by information-theoretic metrics—specifically Shannon Entropy—which quantifies the degree of uncertainty, and the Runs Test, which evaluates the sequential independence of data points.

The objective of this framework is to provide a quantitative benchmark for assessing the viability of random number generation algorithms. Through this comparative analysis of synthetic noise versus pattern-induced sequences, we demonstrate that high-entropy results alone are insufficient for declaring randomness, and that spatial independence remains a critical diagnostic criterion in the validation of computational unpredictability.

## Implementation Overview & Technical Specifications

The system is composed of a modular pipeline designed to generate, visualize, and audit random data streams. It operates exclusively on image-based data structures, utilizing the `.png` format to ensure lossless integrity of the pixel values being analyzed.

### Core Modules

#### 1. Data Generation
* **`GoodRandomGenerator.py`**: Employs high-entropy sources to produce 300x300 matrices of uniform noise.
* **`BadRandomGenerator.py`**: Introduces deliberate mathematical periodicity (modulo-based patterns) to serve as a control group for algorithm failure.

#### 2. Analytical Engine (`CheckRandomnessQuality.py`)
* **Input:** Accepts 8-bit grayscale `.png` files as input.
* **Shannon Entropy Analysis:** Calculates the probability distribution of pixel values across the [0, 255] range, providing a measure of information density.
* **Runs Test:** Executes a sequential fluctuation analysis to detect non-random trends, utilizing z-score normalization to determine statistical significance against expected random behavior.
* **Output:** Generates a weighted performance metric, offering a final "Quality Score" and an algorithmic diagnosis.

## Methodology & Verification

To verify the fidelity of the results, the system enforces a standardized 300x300 matrix resolution. This scale ensures a sufficient sample size (N=90,000) to minimize statistical variance, allowing the Runs Test and entropy metrics to converge towards theoretical expectations. The resulting diagnostic output distinguishes between "Excellent Randomness" (high entropy, low sequential correlation) and "Algorithmic Failure" (structured patterns or sequential bias).

## Setup & Execution

Follow these steps to initialize the environment and run the evaluation suite:

### 1. Environment Initialization

```bash
# Clone the repository
git clone https://github.com/inbitwetrust/Randomness-Quality-Analyzer.git
cd Randomness-Quality-Analyzer

# Create and activate virtual environment
# On Windows: python -m venv myenv
# On macOS/Linux: python3 -m venv myenv
python -m venv myenv

# Activate the environment
# On Windows: myenv\Scripts\activate
# On macOS/Linux: source myenv/bin/activate
source myenv/bin/activate  

# Install dependencies
pip install numpy matplotlib scipy pillow
```

### 2. Execution Guide

* **To generate a high-entropy image:**
  ```bash
  python GoodRandomGenerator.py
  ```

* **To generate a test pattern (for algorithm failure validation):**
  ```bash
  python BadRandomGenerator.py
  ```

* **To audit a target image:**
  ```bash
  python CheckRandomnessQuality.py path/to/your/image.png
  ```

## Authorship

**George W. Aravidis** 
Email address: du3mceskwd5wfy.gyf92@slmail.me

## License

This project is licensed under the **MIT License**.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, provided that the above copyright notice and this permission notice are included in all copies or substantial portions of the Software.
