#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/2 23:38 
# @Author : Lindom
# @File : 19Function2.py 
# @Software: PyCharm Community Edition
import time

def logger():
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    with open("test.log","a+",encoding="utf-8") as f:
        f.write("%s start write log\n" %time_current)

def test1():
    print("in the test1")
    logger()

def test2():
    print("in the test2")
    logger()

def test3():
    print("in the test3")
    logger()

def test4():
    print("in the test4")
    logger()

test1()
test2()
test3()
test4()


# 函数的作用
'''
1 重复利用
2 可扩展性
3 保持一致性

'''