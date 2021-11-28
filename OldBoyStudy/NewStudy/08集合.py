#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/1 0:02 
# @Author : Lindom
# @File : 08集合.py
# @Software: PyCharm Community Edition

# 集合


"""
集合是由不重复元素组成的无序的集
集合的作用：
1.去重
2.关系测试
"""
# 定义集合
list={1,2,3}
list_1 = [1,4,6,8,3,8,0,9]  # list_1为一个列表
list_1 = set(list_1)        # list_1会转变成集合

list_2 = set([2,6,0,1,11,7,66,0])

print(list_1)
print(type(list),type(list_1))
print(list_2)

# 交集
print(list_1.intersection(list_2))
print(list_1 & list_2)
print("---------------------")

# 并集
print(list_1.union(list_2))
print(list_1 | list_2)
print("---------------------")

# 差集
# in list_1 but not in list_2
print(list_1.difference(list_2))
print(list_1 - list_2)
# in list_2 but not in list_1
print(list_2.difference(list_1))
print("---------------------")

# 子集 返回bool值
list_3 = set([1,3,0])
print(list_1.issubset(list_2))
print(list_3.issubset(list_1))
print("---------------------")

# 父集  返回bool值
print(list_1.issuperset(list_2))
print(list_1.issuperset(list_3))
print("---------------------")

# 对称差集  取出两个集合里面都没有的放到一起
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)
print("---------------------")

# isdisjoint:判断两个集合是否有交集，没有返回true，有返回false
print(list_3.isdisjoint(list_1))