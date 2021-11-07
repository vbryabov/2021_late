import matplotlib
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np
from math import log
from random import uniform
# 日本語フォント用（Linux）
matplotlib.rc('font', family='Noto Sans CJK JP')
'''
# 日本語フォント用（Windows）
matplotlib.rc('font', family='MS Gothic')
'''

class Task4():

    def __init__(self) -> None:
        self.r = np.linspace(1, 5, 400, dtype=np.object)
        self.r2 = np.linspace(3.8, 3.9, 400, dtype=np.object)
        # fig = plt.figure(figsize=(8, 10))
        # self.ax1 = fig.add_subplot(2, 1, 1)
        # self.ax2 = fig.add_subplot(2, 1, 2)
        self.x = uniform(0, 1)

    def f(self, r: float, x: float) -> float:
        "ロジスティック写像を返す関数（x の初期値はランダム）"
        return r * x * (1 - x)

    def f_prime(self, r: float, x: float) -> float:
        "ロジスティック写像の微分を返す関数（x の初期値はランダム）"
        return r * (1 - 2 * x)

    def calc_lambda(self, r: float) -> float:
        "乗数を計算する関数"
        lambda_sum = 0
        x_array = []
        cnt = 10000
        num = self.x

        for i in range(300):
            num = self.f(r, num)

        for i in range(cnt):
            x_array.append(num)
            num = self.f(r, num)

        for i in x_array:
            if self.f_prime(r, i) > 0:
                lambda_sum += log(self.f_prime(r, i))
            else:
                lambda_sum += log(-1 * self.f_prime(r, i))
        lambda_sum /= cnt
        return lambda_sum

    def problem1(self) -> None:
        "リアプノフ指数のr依存性を示したグラフの描画"
        lambda_array = []
        for i in self.r:
            lambda_array.append(self.calc_lambda(i))
        '''
        self.ax1.plot(self.r, lambda_array)
        self.ax1.set_title(
            "リアプノフ指数のr依存性を示したグラフの描画 （$x_0$ = {}）".format(round(self.x, 3)))
        self.ax1.set_xlim(1, 4)
        self.ax1.set_xlabel('$r$')
        self.ax1.set_ylim(-3, 1)
        self.ax1.set_ylabel('リアプノフ指数')
        '''
        plt.figure(figsize=(8, 5))
        plt.plot(self.r, lambda_array)
        plt.title(
            "リアプノフ指数のr依存性を示したグラフの描画 （$x_0$ = {}）".format(round(self.x, 3)))
        plt.xlim(1, 4)
        plt.xlabel('$r$')
        plt.ylim(-3, 1)
        plt.ylabel('リアプノフ指数')
        file_path = '複雑系科学演習/Week4/images/task4_1'
        plt.savefig(file_path, dpi=300)

    def problem2(self) -> None:
        "3周期の窓の領域でのリアプノフ指数のr依存性を示したグラフの描画"
        lambda_array = []
        for i in self.r2:
            lambda_array.append(self.calc_lambda(i))
        '''
        self.ax2.plot(self.r2, lambda_array)
        self.ax2.set_title(
            "リアプノフ指数のr依存性を示したグラフの描画（$x_0 =${}）（３周期の窓）".format(round(self.x, 3)))
        self.ax2.set_xlim(3.825, 3.86)
        self.ax2.set_xlabel('$r$')
        self.ax2.set_ylim(-1, 0.5)
        self.ax2.set_ylabel('リアプノフ指数')
        '''
        plt.figure(figsize=(8, 5))
        plt.plot(self.r2, lambda_array)
        plt.title(
            "リアプノフ指数のr依存性を示したグラフの描画（$x_0 =${}）（３周期の窓）".format(round(self.x, 3)))
        plt.xlim(3.825, 3.86)
        plt.xlabel('$r$')
        plt.ylim(-1, 0.5)
        plt.ylabel('リアプノフ指数')
        file_path = '複雑系科学演習/Week4/images/task4_2'
        plt.savefig(file_path, dpi=300)


    def save_fig(self):
        file_path = '複雑系科学演習/Week4/images/task4'
        plt.savefig(file_path, dpi=300)
        plt.show()

    def plot(self):
        self.problem1()
        self.problem2()
        self.save_fig()


task4 = Task4()
task4.problem1()
task4.problem2()
