import numpy as np
import matplotlib.pyplot as plt
import datetime

def generate_bad_random_grid(size=300):
    data = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            data[i, j] = (i + j) % 15 * 17  

    noise = np.random.randint(0, 30, (size, size))
    data = np.clip(data + noise, 0, 255)

    return data

grid = generate_bad_random_grid(300)
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"BadImage-{timestamp}.png"

plt.imsave(filename, grid, cmap='gray')
print(f"Created 'bad' image (300x300): {filename}")
print("You can now run CheckRandomnessQuality.py with this file.")
