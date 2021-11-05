import math
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# 日本語フォント用（Linux）
matplotlib.rc('font', family='Noto Sans CJK JP')
'''
# 日本語フォント用（Windows）
matplotlib.rc('font', family='MS Gothic')
'''

def koch(n: int, p1: list, p2: list) -> None:
    "再帰関数をもちいたコッホ曲線の座標を求める関数"
    if n == 0:
        return
    sx = 2 * p1[0] / 3 + p2[0] / 3
    sy = 2 * p1[1] / 3 + p2[1] / 3
    tx = p1[0] / 3 + 2 * p2[0] / 3
    ty = p1[1] / 3 + 2 * p2[1] / 3
    ux = (tx - sx) * math.cos(math.radians(60))  - (ty - sy) * math.sin(math.radians(60)) + sx
    uy = (tx - sx) * math.sin(math.radians(60)) + (ty - sy) * math.cos(math.radians(60)) + sy
    koch(n-1, p1, [sx, sy])
    # print(sx, sy)
    koch_array_x.append(sx)
    koch_array_y.append(sy)

    koch(n-1, [sx, sy], [ux, uy])
    # print(ux, uy)
    koch_array_x.append(ux)
    koch_array_y.append(uy)

    koch(n-1, [ux, uy], [tx, ty])
    # print(tx, ty)
    koch_array_x.append(tx)
    koch_array_y.append(ty)

    koch(n-1, [tx, ty], p2)



n = 8
p1 = [-1, 0]
p2 = [1, 0]
koch_array_x = [p1[0]]
koch_array_y = [p1[1]]
koch(n, p1, p2)
koch_array_x.append(p2[0])
koch_array_y.append(p2[1])
file_path = "複雑系科学演習/Week6/images/"
plt.figure(figsize=(8, 8))
plt.title("{}回繰り返したときの $[-1, 1]$ 間のコッホ曲線".format(n))
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.plot(koch_array_x, koch_array_y)
plt.savefig(file_path + "ctest5_3", dpi=300)
plt.show()