# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 15:54
# @Author  : jhys
# @FileName: gradient_1d.py

import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d * x
    return lambda t: d * t + y

x = np.arange(0.0, 10, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.plot(x, y2,label="f‘(x)")
plt.plot(x, y,label="f(x)")
plt.legend()
plt.show()