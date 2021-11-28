#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/9/7 23:28 
# @Author : Lindom
# @File : 08内置方法.py 
# @Software: PyCharm

# all：全部元素为真才是真
print( all([-1,0,9]) )

# any：只要有一个为真就是真
print( any([-1,0,9]))


# bin 把一个整数转成二进制
print(bin(1))
print(bin(10))


def sayhi(n):
    print(n)

sayhi(2)

# lambda
# (lambda n:print(n))(2)
calc = lambda n:print(n)
calc(5)

# filter   过滤
# res = filter(lambda  n:n>5,range(10))
res = map(lambda n:n*2,range(10))
for i in res:
    print(i)


# globals()
# locals()
def test():
    local_var = 333

    print(locals())
test()
print(globals())


# sorted()   排序
a = { 6:2,4:0,10:9,2:10,-3:5,3:2,8:7}

print( sorted(a.items()))   # 根据字典里面的key做升序排序
# 根据字典里面的value做升序排序
print( sorted(a.items(),key = lambda x:x[1]))


# zip  拉链
a1 = [1,2,3,4,5,6]
b1 = ['a','b','c','d']

for i in zip(a1,b1):
    print(i)

# import 'Decoration'






