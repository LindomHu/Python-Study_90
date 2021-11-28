# -*- coding: UTF-8 -*-
# @Time : 2020/6/7 0:11
# @Author : Lindom
# @File : higherFunc.py
# @Software: PyCharm Community Edition

def add(a,b,f):
    #一个函数可以接收另一个函数作为参数，这样的函数就叫高阶函数
    #abs是内置函数，可以将负数转换成正数
    return f(a)+f(b)

res= add(2,-6,abs)
print(res)
