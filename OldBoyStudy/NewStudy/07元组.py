# -*- coding: utf-8 -*-
# @Time : 2021/11/14 20:53
# @Author : huix
# @File : 07元组.py

#定义函数
# def method(a):
#     '''
#     :param a:
#     :return:
#     '''
#     print(a)
#     # 如果return后面什么都不带或者不写return值，则函数返回None
#     return a + 1
#
# # method(2)
# print(method(0))


# 定义元组
tuple_1 = (1,2,3)
list_1= ["a","b","d"]
# 元组是不可变，以下这行代码运行将会报错
# 元祖是可以嵌套列表（list）的，并且嵌套以后可以改变元组中列表里面的元素
# TypeError: 'tuple' object does not support item assignment
# tuple_1[0] = "5"

tuple_1 = (1,2,3,list_1)
tuple_1[3][2] = "c"
print(tuple_1)
# print(type(tuple_1))
print(tuple_1.index(list_1))   // 返回元素在元组中的下标

# 元组可以转换成集合
tuple_2 = ()
t_to_Set1 = set(tuple_2)
t_to_Set1.add(10)
t_to_Set1.add(20)
print(t_to_Set1)
print(type(t_to_Set1))

