from matplotlib import pyplot as plt
from math import log, sqrt


def henon_map(x, y):
    return a-x*x*+b*y, x


x0 = 0.0
y0 = 0.0
a = 1.4
b = 0.3
x = x0
y = y0
c = []
d = []
h = [0]*200
for i in range(2000):
    x, y = henon_map(x, y)
    if i < 10:
        print(x, y)
    if i >= 1000:
        c.append(x)
        d.append(y)
print(c[:10])
print(d[:10])
for i in range(1000):
    for j in range(1000):
        if i < j:
            xx = (c[i] - c[j]) ** 2
            yy = (d[i] - d[j]) ** 2
            r = sqrt(xx + yy)
            h[round(r / (0.01))] += 1
print(h)
