# -*- coding: utf-8 -*-
# @Time : 2021/11/14 19:16
# @Author : huix
# @File : 04For循环结构.py

# 求1～100之间偶数的和

# 第一种方式：利用取余求出偶数再累积求和
result = 0

# for i in range(101):
#     if i%2==0:
#         result = result + i
# print(result)

# 第二种方式：利用python中的range求出偶数再累积求和
for i in range (2,101,2):
    result = result + i
print(result)
