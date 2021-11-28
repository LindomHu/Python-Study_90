#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/9/5 23:38 
# @Author : Lindom
# @File : 07Generator_并行.py 
# @Software: PyCharm

import time

def consumer(name):
    print("%s 准备吃包子啦"%name)
    while True:
        baozi = yield

        print("包子[%s]来了，被[%s]吃了！"%(baozi,name))


def producer(name):
    c1 = consumer("A")
    c2 = consumer("B")
    c1.__next__()
    c2.__next__()
    print("%s开始做包子啦！"%name)
    for i in range(1,11,1):
        time.sleep(1)
        print("做了两个包子，每人一个")
        c1.send(i)
        c2.send(i)

producer("Lindom")


"""
1. 可以被直接作用于for循环的对象叫做可迭代的
2. 可以被next()函数调用并不断返回下一个值的对象叫做迭代器
3. 生成器一定是一个迭代器，因为生成器有next()方法；但迭代器不一定是生成器
"""
