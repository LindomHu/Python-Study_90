#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/1 10:55 
# @Author : Lindom
# @File : 11File_Op2.py 
# @Software: PyCharm Community Edition

f = open("yesterday","r",encoding="utf-8")
f2 = open("yesterday2","a",encoding="utf-8")
#  游标的定位 是按照字符的计数
print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())

# 游标回到文件初始位置
f.seek(0)
print(f.tell())

# 打印当前文件编码
print(f.encoding)

# 返回文件句柄在操作系统中的编号
print(f.fileno())
print(f2.fileno())

# 判断文件是否可读，可写，游标能否回到初始位置,文件是否关闭
print("是否可读",f.readable())
print("是否可写",f.writable())
print("游标是否可到初始位置",f.seekable())
print("文件是否关闭",f.closed)

# f.flush()   实时刷新到硬盘上/进度条

# 截断，游标会从头开始截断
f2.truncate(10)

f.close()


