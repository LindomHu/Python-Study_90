#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/8 下午5:29 
# @Author : huix
# @File : 05遍历字典.py 
# @Software: PyCharm




dict = {
    "name":"tester","ege":"18","height":"170"}


for i in dict.keys():
    print(i)
    for j in dict.values():
        print(j)
