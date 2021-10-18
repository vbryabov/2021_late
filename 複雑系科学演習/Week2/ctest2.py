from matplotlib import pyplot as plt
import numpy as np

class PlotLogisticGraph():
    def __init__(self, x, r, s) -> None:
        self.x = x
        self.r = r
        self.s =s
        self.xn = np.linspace(0, 1, 1000)

    def logistic(self) -> list:
        calc_x = self.x
        x_array = [calc_x]
        for n in range(1, 102):
            calc_x = self.r * (1 - calc_x) * calc_x
            x_array.append(calc_x)
        return x_array

    def plot_delta_time_graph(self):
        n = list(range(0, 101))
        plt.plot(n, self.logistic()[:101])
        plt.title("$r = $" + str(self.r) + ", $x_0 = $" + str(self.x))
        plt.xlim(0, 100)
        plt.ylim(0, 1)
        plt.xlabel("$n$")
        plt.ylabel("$x_n$")
    

    def plot_return_map(self):
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
        # plt.plot(self.logistic()[:101], self.logistic()[1:], marker='.', linestyle='None')
        plt.plot(spiper_plot_x, spiper_plot_y, marker='o', linestyle='dashed')
        plt.plot(self.xn, self.xn)
        plt.plot(self.xn, xn_array)
        plt.title("$r = $" + str(self.r) + ", $x_0 = $" + str(self.x))
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel("$x_n$")
        plt.ylabel("$x_{n+1}$")
    

    def show_graph(self) -> None:
        file_path = 'images/'
        plt.savefig(file_path + self.s, dpi=600)
        plt.show()


r = [1.50, 2.60, 3.20, 3.50, 3.86, 3.90]
x = 0.7
for i in range(len(r)):
    demo = PlotLogisticGraph(x, r[i], 'ctest2_{}'.format(i + 1))
    demo.logistic()
    demo.plot_delta_time_graph()
    demo.show_graph()