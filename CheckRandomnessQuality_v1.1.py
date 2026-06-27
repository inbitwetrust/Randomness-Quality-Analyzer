import sys
import numpy as np
from PIL import Image
from scipy.stats import entropy

def analyze_randomness(filename):
    try:
        img = Image.open(filename).convert('L')
        data = np.array(img).flatten()
        
        value_counts = np.bincount(data, minlength=256)
        prob_distribution = value_counts / len(data)
        shannon_entropy = entropy(prob_distribution, base=2)
        entropy_score = (shannon_entropy / 8.0) * 100
        
        greater = (data[1:] > data[:-1])
        runs = np.sum(greater[:-1] != greater[1:])
        
        n = len(data)
        expected_runs = (2 * n - 1) / 3
        std_dev_runs = np.sqrt((16 * n - 29) / 90)
        
        z_score = abs(runs - expected_runs) / std_dev_runs
        run_score = max(0, 100 - (z_score * 2)) 
        
        final_score = (entropy_score * 0.4) + (run_score * 0.6)
        
        print(f"--- Analysis of file: {filename} ---")
        print(f"Dimension: {int(np.sqrt(n))}x{int(np.sqrt(n))}")
        print(f"Shannon Entropy: {shannon_entropy:.4f} (Score: {entropy_score:.2f}%)")
        print(f"Runs Test Score: {run_score:.2f}%")
        print(f"Final Score: {final_score:.2f}%")
        
        if final_score > 90:
            print("Evaluation: Excellent randomness.")
        elif final_score > 75:
            print("Evaluation: Acceptable randomness.")
        else:
            print("Evaluation: BAD algorithm - Patterns detected!")

    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python CheckRandomnessQuality.py <filename.png>")
    else:
        analyze_randomness(sys.argv[1])
