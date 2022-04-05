#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/15 23:48 
# @Author : Lindom
# @File : 01Decorator.py
# @Software: PyCharm Community Edition


# 装饰器
'''
1 定义：本质上是函数，装饰其它函数，就是为其它函数添加附加功能
2 原则：1)不能修改被装饰函数的源代码
      2)不能修改被装饰函数的调用方式
3 实现装饰器知识储备
    1)函数即“变量”
    2)高阶函数
        a:把一个函数名当做实参传给另外一个函数
        （在不修改被装饰函数源代码的情况下为其添加功能）
        b:返回值中包含函数名
        （不修改函数的调用方式）
    3)嵌套函数
'''


import time
# from time import sleep,ctime
# import logging

# logging.basicConfig(level=logging.INFO)

def timmer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s"%(stop_time - start_time))
    return wrapper()

@timmer
def test1():
    time.sleep(2)
    print("run the funcrion in the test1 ")

@timmer
def test2():
    time.sleep(1)
    print("run the function in the test2")


# test1()


