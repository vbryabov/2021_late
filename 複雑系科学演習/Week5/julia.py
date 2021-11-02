import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize                 # カラーマップ操作
from numba import jit                                   # 計算の高速化
from random import uniform
import matplotlib

# 日本語フォント用（Linux）
matplotlib.rc('font', family='Noto Sans CJK JP')
'''
# 日本語フォント用（Windows）
matplotlib.rc('font', family='MS Gothic')
'''

@jit                                                 # NumbaによるJust In Time Compileを実行
def julia(x, y, n_max, a, b):
    x_num, y_num = np.meshgrid(x, y)             # ReとImの組み合わせを計算
    n_grid = len(x_num.ravel())                         # 組み合わせの総数
    z = np.zeros(n_grid)                             # ジュリア集合のデータ格納用空配列

    # zにジュリア集合に属するか否かのデータを格納していくループ
    for i in range(n_grid):
        c = complex(a, b)                            # 複素数cを定義

        # イタレーション回数nと複素数z0を初期化
        n = 0
        z0 = complex(x_num.ravel()[i], y_num.ravel()[i])

        # z0が無限大になるか、最大イタレーション数になるまでループする
        while np.abs(z0) < 1e20 and not n == n_max:
            z0 = z0 ** 2 + c                         # 漸化式を計算
            n += 1                                   # イタレーション数を増分

        # z0が無限大に発散する場合はn, 収束する場合は0を格納
        if n == n_max:
            z[i] = 0
        else:
            z[i] = n
    z = np.reshape(z, x_num.shape)                      # 2次元配列(画像表示用)にリシェイプ
    z = z[::-1]                                      # imshow()で上下逆になるので予め上下反転
    return z


# 実部と虚部の軸データ配列、最大イタレーション数を設定
x = np.linspace(-2, 2, 2000)
y = np.linspace(-2, 2, 2000)
n_max = 100

a = -1
b = 0.1

# 関数を実行し画像を得る
z = julia(x, y, n_max, a, b)


file_path = "複雑系科学演習/Week5/images/"
plt.figure(figsize=(8, 8))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("$-2 \leqq x \leqq 2, -2 \leqq y \leqq 2$ のとき、\n" +\
    "$a = ${0}, $b = ${1}のときの Julia 集合".format(round(a, 3), round(b, 3)))

plt.imshow(z, cmap='seismic', norm=Normalize(vmin=0, vmax=n_max), extent=[-2, 2, -2, 2])
plt.savefig(file_path + "ctest5_2", dpi=300)
plt.show()
