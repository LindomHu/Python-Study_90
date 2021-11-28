#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/25 21:57 
# @Author : Lindom
# @File : 03Decorator.py 
# @Software: PyCharm Community Edition

import time

def timmer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return deco

@timmer         # test1=timmer(test1)
def test1():
    print("in the test1")
    time.sleep(2)
    return test1

@timmer         # test2=timmer(test2)
def test2(name,age):
    print("in the test2:",name,age)
    time.sleep(1)
    return test2

test1()
test2("Lindom",18)