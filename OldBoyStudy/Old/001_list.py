#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/6 21:19 
# @Author : Lindom
# @File : 001_list.py 
# @Software: PyCharm Community Edition


list_1 = {0,1,3,5,7,9}
list_2 = {0,2,4,6,8}
print(type(list_1))

#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)

#并集
print(list_1.union(list_2))
print(list_1 | list_2)

#差集
print(list_1.difference(list_2))
print(list_1 - list_2)

#子集
print(list_1.issubset(list_2))
#父集
print(list_1.issuperset(list_2))
#对称差集
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)

