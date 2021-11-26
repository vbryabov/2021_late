from matplotlib import pyplot as plt
from random import uniform


def henon(x: float, y: float):
    return y + 1 - a * x ** 2, b * x


x = uniform(-1, 1)
y = uniform(-1, 1)
a = 1.4
b = 0.3
cnt = 30000
x_array = []
y_array = []
for i in range(cnt):
    x, y = henon(x, y)
    if i < 249:
        continue
    x_array.append(x)
    y_array.append(y)
plt.figure(figsize=(10, 8))
plt.plot(x_array, y_array, linestyle='None', marker='.', markersize=1)
plt.title('Attractor of "Henon map"')
plt.xlim(-2, 2)
plt.ylim(-0.5, 0.5)
# plt.show()
plt.savefig('複雑系科学演習/Week8/images/task8_1', dpi=300)
