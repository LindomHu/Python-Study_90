#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/9/12 23:38 
# @Author : Lindom
# @File : 10Json反序列化.py
# @Software: PyCharm

# 反序列化
# import json
import pickle

def sayhi(name):
    print("hello,",name)
    print("hello2,","lisi")

f = open("test.test","rb")

# data = json.loads(f.read())
data = pickle.load(f)   # === data = pickle.loads(f.read())


f.close()
print(data)
# print(data["age"])
print(data["func"]("lindom"))
