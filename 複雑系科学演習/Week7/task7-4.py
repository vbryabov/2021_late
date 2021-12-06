from matplotlib import pyplot as plt
import numpy as np
from random import uniform


class Week7Task4():
    def __init__(self) -> None:
        self.x = uniform(0, 1)
        self.r = 1 + 8**(1 / 2)
        self.xn = np.linspace(0, 1, 1000)
        self.fig = plt.figure(figsize=(6, 6), facecolor='turquoise',
                              linewidth=1, edgecolor='black')

    def preprocessing(self, x: float) -> float:
        """前処理"""
        return(self.r * x * (1 - x))

    def code_problem4(self):
        """r = 1 + √8のときのグラフ"""

        fff_array_x = []
        fff_array_y = []
        for i in self.xn:
            fff_array_x.append(i)
            fff_array_y.append(self.preprocessing(
                self.preprocessing(self.preprocessing(i))))
        plt.plot(fff_array_x, fff_array_y, color='red',
                 label='$y = f^{(3)}(x_n)$')
        plt.plot(self.xn, self.xn, color='green', label='$x_{n+3} = x_n$')
        plt.title('Return map of "Logistic map" ($x_n$ to $x_{n+3}$)')
        plt.xlabel('$x_n$')
        plt.ylabel('$x_{n+3}$')
        plt.legend(loc='best')
        plt.savefig('複雑系科学演習/Week7/images/tast7_4')

task = Week7Task4()
task.code_problem4()
