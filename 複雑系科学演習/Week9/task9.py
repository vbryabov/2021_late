from matplotlib import pyplot as plt
import numpy as np
from random import uniform


def henon(x: float, y: float):
    return y + 1 - a * x ** 2, b * x


def check_in_grid(cnt: int) -> int:
    """分割したマスに点が入っている個数を返す"""
    x = 0.1
    y = 0

    grid_x = np.linspace(-1.5, 1.5, cnt+1, dtype=object)
    grid_y = np.linspace(-0.5, 0.5, cnt+1, dtype=object)
    check = [[False]*cnt for _ in range(cnt)]
    grid_cnt = 0
    """
    for i in range(len(grid_x)-1):
        for j in range(len(grid_y)-1):
            if (grid_x[i] <= x <= grid_x[i + 1]
                    and grid_y[j] <= y <= grid_y[j + 1]):
                check[i][j] = True
    """
    for i in range(3000):
        x, y = henon(x, y)
        if i < 249:
            continue
        for j in range(cnt):
            for k in range(cnt):
                if (grid_x[j] <= x <= grid_x[j + 1]
                        and grid_y[k] <= y <= grid_y[k + 1]):
                    check[j][k] = True
    for i in range(cnt):
        for j in range(cnt):
            if check[i][j]:
                grid_cnt += 1
    return grid_cnt


a = 1.4
b = 0.3
cnt = [10, 50, 100, 500]
for i in cnt:
    print(check_in_grid(i))
