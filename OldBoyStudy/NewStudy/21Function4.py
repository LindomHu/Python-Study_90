#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/8 10:45 
# @Author : Lindom
# @File : 21Function4.py 
# @Software: PyCharm Community Edition

def test(x,y):
    print(x)
    print(y)

test(2,3)
test(x=1,y=3)
# test(x=1,3)  报错，混到一起按照位置调用传值



# 形参 ：x,y
# 实参：2，3

# 位置参数调用，形参和实参是一一对应的
# 关键字调用，与形参顺序无关，关键字调用移动要在位置参数后面