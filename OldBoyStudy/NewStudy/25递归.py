#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/11 23:29 
# @Author : Lindom
# @File : 25递归.py 
# @Software: PyCharm Community Edition

# 递归的最大次数是999层
# 特性：
'''
1 必须有一个明确的结束条件
2 每递归一次时，问题规模相比上次递归都应有所减少
'''

def cacl(n):
    print(n)
    if int(n/2) > 0:
        return cacl( int(n/2) )
    print("——>",n)
cacl(10)



