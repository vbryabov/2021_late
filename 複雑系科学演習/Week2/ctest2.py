from matplotlib import pyplot as plt
import matplotlib
import numpy as np
# 日本語フォント用（Linux）
matplotlib.rc('font', family='Noto Sans CJK JP')
'''
# 日本語フォント用（Windows）
matplotlib.rc('font', family='MS Gothic')
'''

class PlotLogisticGraph():
    def __init__(self, r, s) -> None:
        self.x = 0.7
        self.r = r
        self.s = s
        self.xn = np.linspace(0, 1, 1000)
        self.fig = plt.figure(figsize=(12, 6))
        self.filepath = 'Week2/images/'

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
        ax2 = self.fig.add_subplot(1, 2, 2)
        n = list(range(0, 101))
        ax2.plot(n, self.logistic()[:101])
        ax2.set_title("$r = $" + str(self.r) + ", $x_0 = $" + str(self.x) + 'のときの時系列グラフ')
        ax2.set_xlim(0, 100)
        ax2.set_ylim(0, 1)
        ax2.set_xlabel("$n$")
        ax2.set_ylabel("$x_n$")

    def plot_delta_time_graph_only(self):
        '''時系列グラフの描画のみ'''
        self.fig = plt.figure(figsize=(6, 6))
        n = list(range(0, 101))
        plt.plot(n, self.logistic()[:101])
        plt.title("$r = $" + str(self.r) + ", $x_0 = $" + str(self.x) + 'のときの時系列グラフ')
        plt.xlim(0, 100)
        plt.ylim(0, 1)
        plt.xlabel("$n$")
        plt.ylabel("$x_n$")
        plt.savefig(self.filepath + self.s + '_1', dpi=300)

    def plot_return_map(self):
        '''リターンマップの描画'''
        ax1 = self.fig.add_subplot(1, 2, 1)
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
        
        ax1.plot(spiper_plot_x, spiper_plot_y, marker='o', linestyle='dashed')
        ax1.plot(self.xn, self.xn)
        ax1.plot(self.xn, xn_array)
        ax1.set_title("$r = $" + str(self.r) + ", $x_0 = $" + str(self.x) + 'のときのリターンマップ')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
        ax1.set_xlabel("$x_n$")
        ax1.set_ylabel("$x_{n+1}$")

    def plot_return_map_only(self):
        '''リターンマップの描画のみ'''
        self.fig = plt.figure(figsize=(6, 6))
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
        
        plt.plot(spiper_plot_x, spiper_plot_y, marker='o', linestyle='dashed')
        plt.plot(self.xn, self.xn)
        plt.plot(self.xn, xn_array)
        plt.title("$r = $" + str(self.r) + ", $x_0 = $" + str(self.x) + 'のときのリターンマップ')
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel("$x_n$")
        plt.ylabel("$x_{n+1}$")
        plt.savefig(self.filepath + self.s + '_2', dpi=300)

    def do_plot(self):
        self.plot_delta_time_graph()
        self.plot_return_map()

    def show_graph(self) -> None:
        plt.savefig(self.filepath + self.s, dpi=300)
        # plt.show()


r = [1.50, 2.60, 3.20, 3.50, 3.86, 3.90]

for i in range(len(r)):
    demo = PlotLogisticGraph(r[i], 'ctest2_{}'.format(i + 1))
    demo.do_plot()
    demo.show_graph()

for i in range(len(r)):
    for_report = PlotLogisticGraph(r[i], 'ctest2_{}'.format(i + 1))
    for_report.plot_delta_time_graph_only()
    for_report.plot_return_map_only()