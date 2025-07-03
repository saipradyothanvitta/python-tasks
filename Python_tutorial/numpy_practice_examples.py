
import numpy as np

# 1. Creating an array
temperatures = np.array([30.5, 31.0, 32.3, 29.8, 28.5])
print("Temperatures:", temperatures)

# 2. Creating a 2D array (image matrix)
image = np.array([[255, 255, 255, 255, 255],
                  [255,   0,   0,   0, 255],
                  [255,   0,   0,   0, 255],
                  [255,   0,   0,   0, 255],
                  [255, 255, 255, 255, 255]])
print("2D Image Matrix:\n", image)

# 3. Statistical calculations
data = np.array([10, 20, 30, 40, 50])
mean = np.mean(data)
std_dev = np.std(data)
print(f"Mean: {mean}, Standard Deviation: {std_dev}")

# 4. Matrix multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
product = np.dot(a, b)
print("Matrix product:\n", product)
