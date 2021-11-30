from matplotlib import pyplot as plt
import numpy as np

filepath = '複雑系科学演習/Week9/ctest9.txt'
x_array = []
y_array = []
with open(filepath, encoding='UTF-8') as f:
    while line := f.readline():
        line = line.rstrip()
        x, y = line.split(' ')
        x_array.append(int(x))
        y_array.append(int(y))

plt.figure(figsize=(8, 8))
plt.xlim(0, 500)
plt.ylim(0, 5000)
plt.plot(x_array, y_array)
plt.title('Double-log graph')
plt.xlabel('$N$')
plt.ylabel('$m(N)$')
# plt.show()
plt.savefig('複雑系科学演習/Week9/images/task9', dpi=300)