#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/2 23:09 
# @Author : Lindom
# @File : 18Function.py 
# @Software: PyCharm Community Edition

"""
1 面向对象  ——华山派 ——>类 ---》class
2 面向过程  ——少林派 ——>过程 ---》def
3 函数式编程 ——逍遥派 ——>函数 ---》def

"""
# 定义函数
def func1():
    """test1"""
    print("in the func1")
    return 0

# 定义过程
def func2():
    """test2"""
    print("in the func2")

x = func1()
y = func2()

# 定义函数和过程 都可以调用
# 过程就是没有返回值的函数

print("from func1 return is %s" %x)
print("from func2 return is %s" %y)


