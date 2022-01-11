from matplotlib import pyplot as plt
from math import floor


class HenonMap():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.a = 1.4
        self.b = 0.3
        self.cnt = 1000

    def henon(self):
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
        r_array = []
        for i in range(self.cnt-1):
            for j in range(i+1, self.cnt):
                r = ((xy_array[0][i] - xy_array[0][j]) ** 2 +
                     (xy_array[1][i] - xy_array[1][j]) ** 2) ** (1 / 2)
                r_array.append(round(r, 3))
        return r_array

    def plot_henon_map(self):
        distances = self.calculate_distances()
        # print(len(distances))
        plt.figure(figsize=(10, 8), facecolor='lightgray')
        plt.hist(distances, bins=200, range=(0, 2), color='black')
        plt.title('Histogram about "Henon map" distances')
        plt.xlabel('$h(i),0 \leq i < 200 $')
        plt.ylabel('Count of h(i)')
        plt.savefig('task11', dpi=300)


task11 = HenonMap()
task11.plot_henon_map()
