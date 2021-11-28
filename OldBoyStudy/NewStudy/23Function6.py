#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/8 11:20 
# @Author : Lindom
# @File : 23Function6.py 
# @Software: PyCharm Community Edition


# 参数组的定义
# *args  接收n个位置参数，转换成元组的方式
def test1(*args):
    print(args)

test1(1,2,3,4,5,"abc")
test1(*[1,2,3,4,5])

print("\n")
# 定义了位置参数又定义了参数组
def test2(x,*args):
    print(x)
    print(args)


test2(10,2,3,4,5,6)

print("\n")
# **kwargs  接收n个关键字参数转换成字典的方式
def test3(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])
    print("test3:%s"%type(test2))

test3(name="alex",age=8,sex="F")
# test3(**{"name":"alex","age":8})

print("\n")
# **kwargs  参数组一定要往后放
def test4(name,age = 18,**kwargs):
    print(name)
    print(age)
    print(kwargs)
    print("test4:%s"%type(test2))
test4("alex",sex="m",hobby="tesla")

print("\n")
def test5(name,age = 18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    print("test5:%s"%type(test5))
test5("alex",sex="m",hobby="tesla")