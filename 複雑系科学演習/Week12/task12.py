from matplotlib import pyplot as plt
from math import floor, log


class HenonMap():
    def __init__(self) -> None:
        """initialize"""
        self.x = 0
        self.y = 0
        self.a = 1.4
        self.b = 0.3
        self.cnt = 1000

    def henon(self):
        """return henon points"""
        return self.a - self.x * self.x + self.b * self.y, self.x

    def preprocessing(self):
        x_array = []
        y_array = []
        for i in range(self.cnt+1000):
            self.x, self.y = self.henon()
            if i < 1000:
                continue
            x_array.append(self.x)
            y_array.append(self.y)
        return x_array, y_array

    def calculate_distances(self) -> list:
        xy_array = self.preprocessing()
        h = [0]*200
        for i in range(self.cnt-1):
            for j in range(i+1, self.cnt):
                r = ((xy_array[0][i] - xy_array[0][j]) ** 2 +
                     (xy_array[1][i] - xy_array[1][j]) ** 2) ** (1 / 2)
                if 0 <= round(r, 3) // (0.01) < 200:
                    h[round(round(r, 3) // (0.01))] += 1
        C = [h[0]]
        for i in range(1, 200):
            C.append(C[-1] + h[i])
        return C

    def add_log(self):
        distance = self.calculate_distances()
        U = []
        W = []
        for k in range(200):
            U.append(0.01 * k + 0.005)
        for C in distance:
            if C > 0:  # log(i) ; i > 0
                W.append(log(C))
        return U, W

    def plot_henon_map(self):
        U = self.add_log()[0]
        W = self.add_log()[1]
        plt.figure(figsize=(10, 8), facecolor='lightgray')
        plt.title('Dependence $W$ and $U$')
        plt.plot(U, W, color='black')
        plt.xlabel('$U$')
        plt.ylabel('$W$')
        plt.savefig('複雑系科学演習/Week12/task12', dpi=300)


task12 = HenonMap()
task12.plot_henon_map()
