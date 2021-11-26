from matplotlib import pyplot as plt
import numpy as np
from random import uniform


def henon(a: float, x: float, y: float):
    """エノン写像の(x, y)座標を返す関数"""
    return y + 1 - a * x ** 2, b * x


a = np.arange(0, 1.5, 0.01, dtype=object)   # 課題２の a の範囲
b = 0.3                                     # b = 0.3 に固定
x0 = uniform(-1, 1)                         # ランダムの初期値x0（[-1, 1]の範囲）
y0 = uniform(-1, 1)                         # ランダムの初期値y0（[-1, 1]の範囲）
x_array = []                                # x の値を保存するための配列
a_array = []                                # a の値を保存するための配列

for i in a:                                 # 各 a のときの振る舞いを計算する
    x = x0
    y = y0
    for j in range(500):
        x, y = henon(i, x, y)
        if x < -1.5 or 1.5 < x:             # プロットの範囲外なら終了（オーバーフローを避けるため）
            break
        if j < 249:                         # 250 < xn < 500 の範囲外なら配列に入れない
            continue
        x_array.append(x)
        a_array.append(i)

plt.figure(figsize=(10, 8))
plt.plot(a_array, x_array, linestyle='None', marker='.', markersize=1)
plt.title('Branching diagram of "Henon map"')
plt.xlim(0, 1.6)
plt.ylim(-1.5, 1.5)
# plt.show()
plt.savefig('複雑系科学演習/Week8/images/task8_2', dpi=300)
