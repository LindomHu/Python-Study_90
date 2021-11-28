#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/16 23:00 
# @Author : Lindom
# @File : 02Decorator.py 
# @Software: PyCharm Community

import time


# 高阶函数
def bar():
    time.sleep(2)
    print("in the bar")

def test1(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time is %s" % (stop_time - start_time))

test1(bar)