#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/12 上午11:03 
# @Author : huix
# @File : 06函数中的参数组.py
# @Software: PyCharm



def demo1(*args):
    print(args)


def demo2(**kwargs):
    for x,y in kwargs.items():
        print(x,y)


demo1(1,2,3,"a","b","c")
demo2(x="test",y="test1")