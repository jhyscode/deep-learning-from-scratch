# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 16:59
# @Author  : jhys
# @FileName: numpy_sample.py

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#绘制图形
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle='--', label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend(loc='upper right')
plt.show()