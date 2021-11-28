# -*- coding: utf-8 -*-
# @Time : 2021/11/14 18:20
# @Author : huix
# @File : 03if语句练习.py

# 分支结构
# x = 0
# if 2 < x < 5:
#     y = x - 1
#
# else:
#     if x > -1:
#         y = 2 * x - 1
#
#     else:
#         y = x + 1 - 5
# print(y)

# 多重结构
x = 1
if 2 < x < 5:
    y = x - 1

elif -1 < x < 2:
    y = 2 * x - 1

elif x > 5:
    y = x + 1 - 5

print(y)