from matplotlib import pyplot as plt
import numpy as np


def henon(a: float, x: float, y: float):
    return y + 1 - a * x ** 2, b * x


a = np.linspace(0, 1.5, 150, dtype=object)
b = 0.3
x = 0.1
y = 0
x_array = []
y_array = []
for i in a:
    for j in range(500):
        x, y = henon(i, x, y)
        if j < 249: continue
        x_array.append(x)
        y_array.append(y)

plt.figure(figsize=(8, 8))
plt.plot(x_array, y_array, linestyle='None', marker='.', markersize=10)
plt.show()