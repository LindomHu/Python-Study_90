#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/28 17:04 
# @Author : Lindom
# @File : 06Fibnacci.py 
# @Software: PyCharm Community Edition


# 斐波那契数列
def Fib(Max):
    n,a,b = 0,0,1
    while n < Max:
        # print(b)
        yield b     # 改成生成器
        a,b = b,a+b
        n+=1
    return "---done---"
# return在生成器的作用：在出现异常时返回消息

F = Fib(6)
while True:
    try:
        x = next(F)
        print("F:",x)
    except StopIteration as e:
        print("Generator return value:",e.value)
        break

print(F.__next__())
print(F.__next__())
print(F.__next__())
print("干点别的事")
print(F.__next__())
print(F.__next__())
print(F.__next__())
print(F.__next__())
print(F.__next__())


