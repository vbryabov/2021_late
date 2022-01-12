from matplotlib import pyplot as plt


def henon_calc(n: int) -> list:
    x, y = [0], [0]
    for i in range(n):
        y.append(x[-1])
        x.append(a - x[-1] ** 2 + b * y[-1])
    return x, y


def henon_plot(n: int, pattern: int) -> None:
    plt.figure(figsize=(12, 6))
    plt.title(f'Hennon attractor / {n}points')
    if pattern == 2:
        x1, x2, y1, y2 = 1.4, 1.6, 0.4, 0.6
        plt.xlim(x1, x2)
        plt.ylim(y1, y2)
    elif pattern == 3:
        x1, x2, y1, y2 = 1.46, 1.47, 0.46, 0.47
        plt.xlim(x1, x2)
        plt.ylim(y1, y2)
    plt.grid()
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.plot(henon_calc(n), color='red')
    plt.show()


a, b = 1.4, 0.3
for i in range(3):
    henon_plot(10 ** (4 + i), i + 1)
