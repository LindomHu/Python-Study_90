# -*- coding: UTF-8 -*-
# Author:LindomHui

# 递归

def calc(n):
    print(n)
    if int(n/2)>0:
        return calc(int(n/3))
    print("-->>",n)
calc(20)

def calc1(m):
    print(m)
    if int((m*1/2))>1/2:
        return calc1(int(m*1/2))
    print("-->>>",m)
calc1(10)