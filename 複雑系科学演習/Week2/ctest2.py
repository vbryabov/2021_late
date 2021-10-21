from matplotlib import pyplot as plt
import matplotlib
import numpy as np
# 日本語フォント用（Linux）
matplotlib.rc('font', family='Noto Sans CJK JP')
'''
# 日本語フォント用（Windows）
matplotlib.rc('font', family='BIZ UDGothic')
'''

class PlotLogisticGraph():
    def __init__(self, x, r, s) -> None:
        self.x = x
        self.r = r
        self.s = s
        self.xn = np.linspace(0, 1, 1000)
        fig = plt.figure(figsize=(12, 6))
        self.ax1 = fig.add_subplot(1, 2, 1)
        self.ax2 = fig.add_subplot(1, 2, 2)

    def logistic(self) -> list:
        '''ロジスティック回帰の計算'''
        calc_x = self.x
        x_array = [calc_x]
        for n in range(1, 102):
            calc_x = self.r * (1 - calc_x) * calc_x
            x_array.append(calc_x)
        return x_array

    def plot_delta_time_graph(self):
        '''時系列グラフの描画'''
        n = list(range(0, 101))
        self.ax2.plot(n, self.logistic()[:101])
        self.ax2.set_title("$r = $" + str(self.r) + ", $x_0 = $" + str(self.x) + 'のときの時系列グラフ')
        self.ax2.set_xlim(0, 100)
        self.ax2.set_ylim(0, 1)
        self.ax2.set_xlabel("$n$")
        self.ax2.set_ylabel("$x_n$")

    def plot_return_map(self):
        '''リターンマップの描画'''
        xn_array = []
        for i in self.xn:
            xn_array.append(self.r * (1 - i) * i)
        # クモの巣図用の配列
        n = self.logistic()
        spiper_plot_x = []
        spiper_plot_y = []
        for i in range(1, len(n)):
            spiper_plot_x.append(n[i - 1])
            spiper_plot_x.append(n[i])
            spiper_plot_y.append(n[i])
            spiper_plot_y.append(n[i])
        
        self.ax1.plot(spiper_plot_x, spiper_plot_y, marker='o', linestyle='dashed')
        self.ax1.plot(self.xn, self.xn)
        self.ax1.plot(self.xn, xn_array)
        self.ax1.set_title("$r = $" + str(self.r) + ", $x_0 = $" + str(self.x) + 'のときのリターンマップ')
        self.ax1.set_xlim(0, 1)
        self.ax1.set_ylim(0, 1)
        self.ax1.set_xlabel("$x_n$")
        self.ax1.set_ylabel("$x_{n+1}$")

    def do_plot(self):
        self.plot_delta_time_graph()
        self.plot_return_map()

    def show_graph(self) -> None:
        file_path = 'Week2/images/'
        plt.savefig(file_path + self.s, dpi=300)
        plt.show()


r = [1.50, 2.60, 3.20, 3.50, 3.86, 3.90]
x = 0.7
for i in range(len(r)):
    demo = PlotLogisticGraph(x, r[i], 'ctest2_{}'.format(i + 1))
    demo.logistic()
    demo.do_plot()
    demo.show_graph()
