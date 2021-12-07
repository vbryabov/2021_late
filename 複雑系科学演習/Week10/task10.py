from matplotlib import pyplot as plt


class HenonMap():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.a = 1.4
        self.b = 0.3
        self.cnt = [10000, 100000, 1000000]
        self.xlimit = [[-2, 2], [1.4, 1.6], [1.46, 1.47]]
        self.ylimit = [[-2, 2], [0.4, 0.6], [0.46, 0.47]]

    def henon(self):
        return self.a - self.x * self.x + self.b * self.y, self.x

    def preprocessing(self, cnt):
        x_array = []
        y_array = []
        for i in range(cnt+1000):
            self.x, self.y = self.henon()
            if i < 1000:
                continue
            x_array.append(self.x)
            y_array.append(self.y)
        return x_array, y_array

    def plot_henon_map(self):
        for i in range(3):
            xy_points = self.preprocessing(self.cnt[i])
            plt.figure(figsize=(8, 8), facecolor='lightgray')
            plt.title('Attractor of "Henon map"')
            plt.xlabel('$x$')
            plt.ylabel('$y$')
            plt.xlim(self.xlimit[i][0], self.xlimit[i][1])
            plt.ylim(self.ylimit[i][0], self.ylimit[i][1])
            plt.plot(xy_points[0], xy_points[1],
                     linestyle='None', marker='.', markersize=1, color='black')
            plt.savefig('複雑系科学演習/Week10/images/task10_'+str(i+1), dpi=300)


task10 = HenonMap()
task10.plot_henon_map()
