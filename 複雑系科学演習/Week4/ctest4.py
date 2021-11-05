from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import random

# 日本語フォント用（Linux）
matplotlib.rc('font', family='Noto Sans CJK JP')
'''
# 日本語フォント用（Windows）
matplotlib.rc('font', family='MS Gothic')
'''

class Ctest4():
    def __init__(self) -> None:
        self.r = np.linspace(1, 4, 200, dtype=object)
        self.r2 = np.linspace(3.8, 3.9, 200, dtype=object)
        fig = plt.figure(figsize=(10, 10))
        self.ax1 = fig.add_subplot(2, 1, 1)
        self.ax2 = fig.add_subplot(2, 1, 2)

        # self.x = 0.1    # 初期値を0.1と仮定
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
        
        self.filepath = "複雑系科学演習/Week4/images/"

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
        self.ax1.set_title('初期値$x_0 = {}$（ランダム）のときのロジスティック写像の分岐図'.format(round(self.x, 3)))
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
        self.ax2.set_title('初期値$x_0 = {}$（ランダム）のときのロジスティック写像の分岐図'.format(round(self.x, 3)))
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
        plt.savefig(self.filepath + 'ctest4', dpi=300)
        plt.show()

    def do_plot(self):
        self.code_problem1()
        self.code_problem2()
        self.save_fig()



class Report_3():
    def __init__(self, r: float, s: str) -> None:
        self.r = r
        self.s = s
        self.x = random.uniform(0, 1)
        self.xn = np.linspace(0, 1, 1000)
        self.filepath = "複雑系科学演習/Week4/images/"

    def logistic(self, x: float, cnt: int) -> list:
        num = x
        num_array = [x]
        for i in range(cnt):
            num = self.r * num * (1 - num)
            num_array.append(num)
        return num_array

    def pre_processing(self, cnt: int) -> float:
        '''初期変動の影響をなくすための前処理'''
        num = self.x
        for i in range(cnt):
            num = self.r * num * (1 - num)
        return num

    def plot_return_map(self):
        '''初期変動が影響しないリターンマップの描画'''
        plt.figure(figsize=(6, 6))
        # 処理
        x = self.pre_processing(150)
        n = self.logistic(x, 50)
        xn_array = []
        for i in self.xn:
            xn_array.append(self.r * (1 - i) * i)
        # クモの巣図用の配列
        spiper_plot_x = []
        spiper_plot_y = []
        for i in range(1, len(n)):
            spiper_plot_x.append(n[i - 1])
            spiper_plot_x.append(n[i])
            spiper_plot_y.append(n[i])
            spiper_plot_y.append(n[i])
        
        plt.plot(spiper_plot_x, spiper_plot_y, marker='o', linestyle='dashed')
        plt.plot(self.xn, self.xn)
        plt.plot(self.xn, xn_array)
        plt.title("$r = $" + str(self.r) + ", $x_0 = $" + str(round(self.x, 3)) + '（ランダム）における\n' +\
            '$x_n (150 < n < 200)$のときのリターンマップ')
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel("$x_n$")
        plt.ylabel("$x_{n+1}$")
        plt.savefig(self.filepath + self.s, dpi=300)


r = [1.50, 2.60, 3.20, 3.50, 3.86, 3.90]

# レポート課題, 課題２
# week_3 = Ctest4()
# week_3.do_plot()

# レポート課題, 課題１
for i in range(len(r)):
    report_3 = Report_3(r[i], "report4_{}".format(i + 1))
    report_3.plot_return_map()