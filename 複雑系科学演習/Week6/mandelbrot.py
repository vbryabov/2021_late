import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize                     # カラーマップを自在に操作するために必要
from numba import jit                                       # 計算の高速化


# 日本語フォント用（Linux）
matplotlib.rc('font', family='Noto Sans CJK JP')
'''
# 日本語フォント用（Windows）
matplotlib.rc('font', family='MS Gothic')
'''

@jit
def mandelbrot(a, b, n_max):
    "複素数を用いてマンデルブロ集合の座標を求める関数"
    a_num, b_num = np.meshgrid(a, b)
    n_grid = len(a_num.ravel())                             # 組み合わせの総数
    z = np.zeros(n_grid)                                    # マンデルブロ集合のデータ格納用空配列


    for i in range(n_grid):
        c = complex(a_num.ravel()[i], b_num.ravel()[i])     # c = a + bi
        n = 0
        z0 = complex(0, 0)
        while np.abs(z0) < np.inf and not n == n_max:
            z0 = z0 ** 2 + c                                # 漸化式を計算
            n += 1
        
        if n == n_max:
            z[i] = 0
        else:
            z[i] = n
    z = np.reshape(z, a_num.shape)                          # 2次元配列に変換
    z = z[::-1]                                             # imshow()で上下逆になるので上下反転
    return z


a = np.linspace(-2, 2, 2000)
b = np.linspace(-2, 2, 2000)
z = mandelbrot(a, b, 100)
file_path = "複雑系科学演習/Week6/images/"
plt.figure(figsize=(8, 8))
plt.xlabel('$a$')
plt.ylabel('$b$')
plt.title("$-2 \leqq a \leqq 2, -2 \leqq b \leqq 2$ のときの Mandelbrot 集合")
plt.imshow(z, cmap='jet', norm=Normalize(vmin=0, vmax=100), extent=[-2, 2, -2, 2])
plt.savefig(file_path + "ctest5_1", dpi=300)
plt.show()
