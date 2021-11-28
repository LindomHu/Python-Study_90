#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/1 9:50 
# @Author : Lindom
# @File : 10File_Op.py 
# @Software: PyCharm Community Edition

"""
流程：打开文档；通过句柄进行文件操作；关闭文件
data = open("yesterday",encoding="utf-8").read()
"r":可读
"w":可写并会创建一个文件
"a":追加,不能读
"""

'''
f = open("yesterday",'a',encoding="utf-8")  # 文件句柄
# data = f.read()
# print(data)

f.write("When I was young I listen to the radio")
data = f.read()
print(data)
'''

f = open("yesterday","r",encoding="utf-8")

# 小需求：在文件第九行里面插入一行分割线
# high bige
count = 0
for line in f:
    if count == 9 :
        print("-------------------")
        count += 1
        continue
    print(line.strip())
    count += 1

# low loop
'''
for index, line in enumerate (f.readlines()):
    if index == 9:
        print("-------------------")
        continue
    print(line.strip())
'''

f.close()