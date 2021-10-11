import numpy as np
from matplotlib import pyplot as plt
class Ctest3():
    def __init__(self, r: float, s: str) -> None:
        self.r = r
        self.s = s
        self.x = np.linspace(0, 1, 1000)
        fig = plt.figure(figsize=(12, 6))
        self.ax1 = fig.add_subplot(1, 2, 1)
        self.ax2 = fig.add_subplot(1, 2, 2)

    def code_problem1(self) -> None:
        ax1_array = []
        for i in self.x:
            num = i
            for j in range(200):
                num = self.r * num * (1 - num)
            ax1_array.append(num)
        self.ax1.set_xlabel('$x_0$')
        self.ax1.set_ylabel('$x_{200}$')
        self.ax1.plot(self.x, ax1_array, marker='.', linestyle='None')

    def code_problem2(self) -> None:
        ax2_array = []
        x_array = []
        for i in self.x:
            num = i
            for j in range(200):
                num = self.r * num * (1 - num)
                if 150 <= j:
                    ax2_array.append(num)
                    x_array.append(i)
        self.ax2.set_xlabel('$x_0$')
        self.ax2.set_ylabel('$x_{i}:(150 < i < 200)$')
        self.ax2.plot(x_array, ax2_array, marker='.', linestyle='None')

    def show_graph(self) -> None:
        fname = 'images/' + self.s
        plt.savefig(fname, dpi=64, facecolor='lightgray', tight_layout=True)
        plt.show()


r = [1.50, 2.60, 3.20, 3.50, 3.86, 3.90]
for i in range(len(r)):
    demo = Ctest3(r[i], 'ctest3_{}'.format(i + 1))
    demo.code_problem1()
    demo.code_problem2()
    demo.show_graph()