# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 20:47
# @Author  : jhys
# @FileName: buy_apple.py

import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
from ch05.layer_naive import *

apple = 100
apple_num = 2
tax = 1.1

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# forward
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

# backward
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print("price:", int(price))
print("dApple:", dapple)
print("dApple_num:", int(dapple_num))
print("dTax:", dtax)