#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/1 22:43 
# @Author : Lindom
# @File : 15文件修改.py 
# @Software: PyCharm Community Edition

# 实现在某一行替换掉原来的文件
f = open("yesterday","r",encoding="utf-8")
f_new = open("yesterday.bak","w",encoding="utf-8")

for line in f:
    if "夜晚的微风" in line:
        line = line.replace("夜晚的微风","今日的暖光")
    f_new.write(line)

f.close()
f_new.close()

