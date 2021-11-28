# -*- coding: utf-8 -*-
# @Time : 2021/11/14 21:09
# @Author : huix
# @File : 23-2Function7.py

# 仅限关键字传参
def method(*,a):
    """
    :param a: 
    :return: 
    """
    print(a)

method(a=5)


# 解包
# 一个"*"集合或者列表解包
def method1(a1,b1,c1):
    print(a1,b1,c1)

list_a = (3,6,9)
method1(*list_a)

# 两个"*"集合或者列表解包
def method2(a2,b2,c2):
    print(a2)
    print(b2)
    print(c2)

dict = {"a2":1,"b2":2,"c2":3}
method2(**dict)