#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/3 0:13 
# @Author : Lindom
# @File : 20Function3.py
# @Software: PyCharm Community Edition

def test1():
    print("in the func1")

def test2():
    print("in the func1")
    return 1

def test3():
    print("in the func1")
    return 0,11,"hello",[1,"5c","test"],{"age":"18"}

t1 = test1()
t2 = test2()
t3 = test3()

print("from test1 return %s" %type(t1),t1)
print("from test2 return %s" %type(t2),t2)
print("from test3 return %s" %type(t3),t3)



# 总结
'''
1 没有返回值：返回None
2 返回值 = 1：返回object
3 返回值 > 1：返回tuple
'''