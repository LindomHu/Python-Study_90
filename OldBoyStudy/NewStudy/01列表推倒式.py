# -*- coding: utf-8 -*-
# @Time : 2021/11/15 00:21
# @Author : huix
# @File : 01列表推倒式.py

list_squre = []
for i in range(1,5):
    list_squre.append(i**2)
print(list_squre)


list_squre2 = [i**2 for i in range(1,5)]
print(list_squre2)


list_squre3 = [i**2 for i in range(1,5) if i !=1]
print(list_squre3)

list_squre4 = [i*j for i in range(1,5) for j in range(1,5)]
print(list_squre4)