#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/9/12 23:19 
# @Author : Lindom
# @File : 09Json序列化.py 
# @Software: PyCharm


# 序列化
# import json
import pickle


def sayhi(name):
    print("hello,",name)

info = {
    'name':'alex',
    'age':22,
    'func':sayhi

#     Json只支持简单的转换，不支持函数；而pickle可以
}


# f = open("test.test","w")
# f.write(str(info))


f = open("test.test","wb")
# f.write(json.dumps(info))
pickle.dump(info,f)     # === f.write(pickle.dumps(info))