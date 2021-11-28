#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/1 11:38 
# @Author : Lindom
# @File : 14File_Op3.py 
# @Software: PyCharm Community Edition

f = open("yesterday","r+",encoding="utf-8")
f2 = open("yesterday","rb")
f3 = open("yesterday","wb")
# "r+"  读写(追加)
# "w+"  写读，会先创建一个文件再写再读 ----没什么用
# "a+"  追加读
# "rb" "wb"  以二进制模式读、写（内部以二进制的模式处理）

print(f.readline())
print(f.readline())
print(f.readline())
f.write("\n------开始写了------")

f.read()

print(f2.readline())
print(f2.readline())
print(f2.readline())

# 以二进制的模式写
f3.write("hello python\n".encode())

f.close()