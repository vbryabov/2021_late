from matplotlib import pyplot as plt
import numpy as np
from random import uniform


def henon(x: float, y: float):
    return y + 1 - a * x ** 2, b * x

def check_in_grid(cnt: int, x: float, y: float) -> None:
    """1領域内に点があるかどうか判定"""
    grid_x = np.linspace(-1.5, 1.5, cnt+1, dtype=object)
    grid_y = np.linspace(-0.5, 0.5, cnt+1, dtype=object)
    for i in range(len(grid_x)-1):
        for j in range(len(grid_y)-1):
            if (grid_x[i] <= x <= grid_x[i + 1]
                and grid_y[i] <= y <= grid_y[i + 1]):
                check[i][j] = True

x = uniform(-1, 1)
y = uniform(-1, 1)
a = 1.4
b = 0.3

cnt = 10
check = [[False]*cnt for _ in range(cnt)]
grid_number = 0
x_array = []
y_array = []
for i in range(30000):
    x, y = henon(x, y)
    if i < 249:
        continue
    check_in_grid(10, x, y)
    x_array.append(x)
    y_array.append(y)
for i in range(cnt):
    for j in range(cnt):
        if check[i][j]:
            grid_number += 1
print(grid_number)
for i in check:
    print(*i)
"""
plt.figure(figsize=(10, 8))
plt.plot(x_array, y_array, linestyle='None', marker='.', markersize=1)
plt.title('Attractor of "Henon map"')
plt.xlim(-2, 2)
plt.ylim(-0.5, 0.5)
plt.show()
"""