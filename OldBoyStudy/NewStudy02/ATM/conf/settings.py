#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/9/20 12:46 
# @Author : Lindom
# @File : settings.py 
# @Software: PyCharm


def Conf():
    with open("conf.config","w+",encoding="utf-8") as f:
        f.write("This is a file with conf")
        print("You have open the conf.config")

# Conf()