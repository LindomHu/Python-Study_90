# -*- coding: utf-8 -*-
# @Time : 2021/11/21 12:29
# @Author : huix
# @File : 14Python标准库_OS.py

# os：文件相关

import os

# os.removedirs("test.txt")
# os.mkdir("test.txt")

# 返回当前文件的路径
print(os.getcwd())
print(os.listdir("./"))

print(os.path.exists("test"))
# 判断文件目录跟文件，如果没有，则分别创建并在文件里面写入内容
if not os.path.exists("test"):
    os.mkdir("test")
if not os.path.exists("test/test.log"):
    f = open("test/test.log","w",encoding="utf-8")
    f.write("Hello,os using")
    f.close()