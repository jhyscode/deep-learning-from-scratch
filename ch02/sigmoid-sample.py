# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 20:51
# @Author  : jhys
# @FileName: sigmoid-sample.py

import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
