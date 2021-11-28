#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/15 18:58 
# @Author : Lindom
# @File : 26高阶函数.py 
# @Software: PyCharm Community Edition


# 把函数当做一个实际参数传入
def add(a,b,f):
    return f(a)+f(b)


res = add(6,-3,abs)
print(res)