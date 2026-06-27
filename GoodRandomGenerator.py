import numpy as np
import matplotlib.pyplot as plt
import datetime

SIZE = 300
grid = np.random.randint(0, 256, (SIZE, SIZE), dtype=np.uint8)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"GoodImage-{timestamp}.png"

plt.imsave(filename, grid, cmap='gray')
print(f"Image created (300x300): {filename}")
