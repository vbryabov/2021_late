from matplotlib import pyplot as plt
import numpy as np


class Task6():
    def __init__(self) -> None:
        self.x = 0.1                                        # 初期値 x0 = 0.1
        self.xn = np.linspace(0, 1, 1000)                   # 横軸の範囲と刻み幅
        self.tent_y = []                                    # テント写像のグラフを描くための配列
        for i in self.xn:
            if 0 <= i <= 0.5:
                self.tent_y.append(2 * i)
            else:
                self.tent_y.append(2 * (1 - i))
        self.filepath = '複雑系科学演習/Week6/images/task6'

    def tent(self) -> list:
        "リターンマップでのテント写像の座標を持つ配列を返す"
        calc_x = self.x
        x_array = [calc_x]
        for _ in range(1, 102):
            if 0 <= calc_x <= 0.5:
                calc_x = 2 * calc_x
            else:
                calc_x = 2 * (1 - calc_x)
            x_array.append(calc_x)
        return x_array

    def plot_return_map(self) -> None:
        "リターンマップの描画（テント写像）"
        plt.figure(figsize=(6, 6), facecolor='turquoise',
                   linewidth=1, edgecolor='black')
        n = self.tent()
        spiper_plot_x = [self.x]                            # クモの巣図用の配列(x)
        spiper_plot_y = [0]                                 # クモの巣図用の配列(y)
        for i in range(1, len(n)):
            spiper_plot_x.append(n[i - 1])
            spiper_plot_x.append(n[i])
            spiper_plot_y.append(n[i])
            spiper_plot_y.append(n[i])

        plt.plot(spiper_plot_x, spiper_plot_y, marker='o',
                 linestyle='dashed', color='black', alpha=0.7)
        plt.plot(self.xn, self.xn, color='green', alpha=0.9)
        plt.plot(self.xn, self.tent_y, color='red', alpha=0.9)
        plt.title("Return map of \"Tent map\", $x_0 = $" + str(self.x))
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.xlabel("$x_n$")
        plt.ylabel("$x_{n+1}$")
        plt.savefig(self.filepath, dpi=300)


task = Task6()
task.plot_return_map()
