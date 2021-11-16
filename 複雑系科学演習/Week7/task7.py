from matplotlib import pyplot as plt
import numpy as np
from random import uniform


class Task7():
    def __init__(self) -> None:
        # 初期値 x0 = 0.1
        self.x = uniform(0, 1)
        self.xn = np.linspace(0, 1, 1000)                   # 横軸の範囲と刻み幅
        self.fig = plt.figure(figsize=(12, 6), facecolor='turquoise',
                              linewidth=1, edgecolor='black')

    def logistic(self, r) -> list:
        "リターンマップでのロジスティック写像の座標を持つ配列を返す"
        calc_x = self.x
        x_array = []
        for i in range(1, 501):
            calc_x = r * calc_x * (1 - calc_x)
            if 250 <= i <= 500:
                x_array.append(calc_x)
        return x_array

    def plot_time_series_graph(self, r: float) -> None:
        "時系列グラフの描画（ロジスティック写像）"
        ax1 = self.fig.add_subplot(1, 2, 1)
        n = list(range(250, 501))
        ax1.plot(n, self.logistic(r), marker='.', color='black')
        ax1.set_title(
            "Time series graph \"Logistic map\", $x_0 = $" + str(round(self.x, 3)))
        ax1.set_xlim(250, 500)
        ax1.set_ylim(0, 1)
        ax1.set_xlabel("$x_n$")
        ax1.set_ylabel("$n$")

    def plot_return_map(self, r) -> None:
        "リターンマップの描画（ロジスティック写像）"
        ax2 = self.fig.add_subplot(1, 2, 2)
        n = self.logistic(r)
        spider_array_x = []                                 # クモの巣図用の配列(x)
        spider_array_y = []                                 # クモの巣図用の配列(y)
        for i in range(1, len(n)):
            spider_array_x.append(n[i - 1])
            spider_array_x.append(n[i])
            spider_array_y.append(n[i])
            spider_array_y.append(n[i])
        logistic_y = []                                     # テント写像のグラフを描くための配列
        for i in self.xn:
            logistic_y.append(r * i * (1 - i))

        ax2.plot(spider_array_x, spider_array_y, marker='o',
                 linestyle='dashed', color='black', alpha=0.7)
        ax2.plot(self.xn, self.xn, color='green',
                 alpha=0.9, label="$x_{n+1} = x_n$")
        ax2.plot(self.xn, logistic_y, color='red',
                 alpha=0.9, label="Logistic map")
        ax2.set_title(
            "Return map of \"Logistic map\", $x_0 = $" + str(round(self.x, 3)))
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.set_xlabel("$x_n$")
        ax2.set_ylabel("$x_{n+1}$")
        ax2.legend(loc='best')

    def code_problem1(self) -> None:
        r = 3.8285
        self.fig = plt.figure(figsize=(12, 6), facecolor='turquoise',
                              linewidth=1, edgecolor='black')
        self.plot_time_series_graph(r)
        self.plot_return_map(r)
        plt.savefig('複雑系科学演習/Week7/images/task7_1')

    def code_problem2(self) -> None:
        r = 3.8284
        self.fig = plt.figure(figsize=(12, 6), facecolor='turquoise',
                              linewidth=1, edgecolor='black')
        self.plot_time_series_graph(r)
        self.plot_return_map(r)
        plt.savefig('複雑系科学演習/Week7/images/tast7_2')

    def preprocessing(self, x: float) -> float:
        r = 3.8284
        return(r * x * (1 - x))

    def code_problem3(self):
        r = 3.8284
        self.fig = plt.figure(figsize=(6, 6), facecolor='turquoise',
                              linewidth=1, edgecolor='black')

        fff_array_x = []
        fff_array_y = []
        for i in self.xn:
            fff_array_x.append(i)
            fff_array_y.append(self.preprocessing(
                self.preprocessing(self.preprocessing(i))))

        n = self.logistic(r)
        spider_array_x = []                                 # クモの巣図用の配列(x)
        spider_array_y = []                                 # クモの巣図用の配列(y)
        for i in range(3, len(n), 3):
            spider_array_x.append(n[i - 3])
            spider_array_x.append(n[i])
            spider_array_y.append(n[i])
            spider_array_y.append(n[i])
        plt.plot(spider_array_x, spider_array_y, marker='o',
                 linestyle='dashed', color='black', alpha=0.7)
        plt.plot(fff_array_x, fff_array_y, color='red', label='$Logistic map$')
        plt.plot(self.xn, self.xn, color='green', label='$x_{n+3} = x_n$')
        plt.title('Return map of "logistic map" ($x_n$ to $x_{n+3}$)')
        plt.xlabel('$x_n$')
        plt.ylabel('$x_{n+3}$')
        plt.savefig('複雑系科学演習/Week7/images/tast7_3')


task = Task7()
task.code_problem1()
task.code_problem2()
task.code_problem3()
