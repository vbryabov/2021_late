from matplotlib import pyplot as plt
import numpy as np

a = 1.4
b = 0.3


def henon(x: float, y: float):
    return y+1-a*x**2, b*x


plt.figure(figsize=(8, 8))

x = 0.1
y = 0
for i in range(1000):
    x, y = henon(x, y)
    if i < 249:
        continue
    plt.scatter(x, y, s=5, color='blue')
plt.show()
