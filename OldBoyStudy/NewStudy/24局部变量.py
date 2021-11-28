#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/11 23:06 
# @Author : Lindom
# @File : 24局部变量.py 
# @Software: PyCharm Community Edition

school = "Oldboy edu"

def chageName(name):
    #global school  #声明school是全局变量
    school = "Mage Linux"
    print("before change",name,school)
    name = "Lindom"  # 局部变量只在函数里生效 这个函数就是这个变量的作用域
    print("after change",name,school)

name = "lindom"
chageName(name)
print(name,school)

#列表 字典 集合是可以在函数里面直接当做全局变量来改的，在外面打印会生效