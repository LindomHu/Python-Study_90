#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/1 22:59 
# @Author : Lindom
# @File : 16With语句.py
# @Software: PyCharm Community Edition

# f = open("yesterday","r",encoding="utf-8")

# with语句会自动关闭文件
with open("yesterday","r",encoding="utf-8") as f, \
        open("yesterday2","r",encoding="utf-8") as f2:
    for line in f:
        print(line)
