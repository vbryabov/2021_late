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


class Report_3():
    def __init__(self, r: float, s: str) -> None:
        self.r = r
        self.s = s
        self.x = random.uniform(0, 1)
        self.xn = np.linspace(0, 1, 1000)
        self.filepath = "複雑系科学演習/Week3/images/"

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
        plt.title("$r = $" + str(self.r) + ", $x_0 = $" + str(round(self.x, 3)) + '（ランダム）における\n' +
                  '$x_n (150 < n < 200)$のときのリターンマップ')
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel("$x_n$")
        plt.ylabel("$x_{n+1}$")
        plt.savefig(self.filepath + self.s, dpi=300)


r = [1.50, 2.60, 3.20, 3.50, 3.86, 3.90]
for i in range(len(r)):
    report_3 = Report_3(r[i], "report4_{}".format(i + 1))
    report_3.plot_return_map()
