from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import random
# 日本語フォント用（Linux）
matplotlib.rc('font', family='Noto Sans CJK JP')
'''
# 日本語フォント用（Windows）
matplotlib.rc('font', family='MS Gothic')
'''

class Task3():
    def __init__(self) -> None:
        self.r = np.linspace(1, 4, 200, dtype=object)
        self.r2 = np.linspace(3.8, 3.9, 200, dtype=object)
        fig = plt.figure(figsize=(10, 10))
        self.ax1 = fig.add_subplot(2, 1, 1)
        self.ax2 = fig.add_subplot(2, 1, 2)

        # 初期値を[0, 1]でランダムにとる
        self.x = random.uniform(0, 1)

        # 固定点
        self.u1 = list(map(lambda x: 0, self.r))
        self.u2 = list(map(lambda x: 1 - 1 / x, self.r))
        self.u3 = list(map(lambda x: 0, self.r2))
        self.u4 = list(map(lambda x: 1 - 1 / x, self.r2))

        # 乗数
        self.lambda1 = self.r
        self.lambda2 = list(map(lambda x: 2 - x, self.r))
        self.lambda3 = self.r2
        self.lambda4 = list(map(lambda x: 2 - x, self.r2))

        self.filepath = "複雑系科学演習/Week3/images/task3"

    def proprocessing(self, r: float) -> list:
        '''グラフに入れるための前処理'''
        x_array = []
        r_array = []
        num = self.x
        for i in range(150):
            num = r * num * (1 - num)
            if i < 40:
                continue
            x_array.append(num)
            r_array.append(r)
        return x_array, r_array

    def code_problem1(self):
        self.ax1.set_title(
            '初期値$x_0 = {}$（ランダム）のときのロジスティック写像の分岐図'.format(round(self.x, 3)))
        self.ax1.set_xlabel('$r$')
        self.ax1.set_ylabel('$x_n$')
        for i in range(len(self.r)):
            if -1 <= self.lambda1[i] <= 1:
                self.ax1.scatter(self.r[i], self.u1[i], color='b', s=1)
            elif -1 <= self.lambda2[i] <= 1:
                self.ax1.scatter(self.r[i], self.u2[i], color='b', s=1)
            else:
                result = self.proprocessing(self.r[i])
                self.ax1.scatter(result[1], result[0],  color='b', s=1)

    def code_problem2(self):
        self.ax2.set_title(
            '初期値$x_0 = {}$（ランダム）のときのロジスティック写像の分岐図'.format(round(self.x, 3)))
        self.ax2.set_xlabel('$r$')
        self.ax2.set_ylabel('$x_n$')
        for i in range(len(self.r2)):
            if -1 <= self.lambda3[i] <= 1:
                self.ax2.scatter(self.r2[i], self.u3[i], color='b', s=1)
            elif -1 <= self.lambda4[i] <= 1:
                self.ax2.scatter(self.r2[i], self.u4[i], color='b', s=1)
            else:
                result = self.proprocessing(self.r2[i])
                self.ax2.scatter(result[1], result[0],  color='b', s=1)

    def save_fig(self):
        plt.savefig(self.filepath, dpi=300)
        plt.show()

    def do_plot(self):
        self.code_problem1()
        self.code_problem2()
        self.save_fig()


week_3 = Task3()
week_3.do_plot()
