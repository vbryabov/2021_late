import matplotlib
from matplotlib import pyplot as plt
import numpy as np
class Mandelbrot():
    def __init__(self, cnt: int) -> None:
        self.z0 = complex(0, 0)
        self.cnt = cnt
        self.a = np.linspace(-2, 2, 1000)   # -2 <= a <= 2
        self.b = np.linspace(-2, 2, 1000)
        self.fig = plt.figure(figsize=(8, 8))
    
    def calc_madelbrot(self) -> float:
        for i in self.a:
            z = self.z0                     # 初項 z0
            c = complex(self.a, self.b)     # c = a + bi
            for j in range(self.cnt):
                z = z * z + c               # z = z^2 + c
                if -2 > z or z > 2:
                    return i                # 発散するならそこで終了する
            return self.cnt                 # 無限大に発散しない場合は回数を返す
        z = self.z0
        for i in range(self.cnt):
            z = z**2 + c

