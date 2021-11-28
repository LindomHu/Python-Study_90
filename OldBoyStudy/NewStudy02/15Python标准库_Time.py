# -*- coding: utf-8 -*-
# @Time : 2021/11/21 14:48
# @Author : huix
# @File : 15Python标准库_Time.py


import time

"""
time.time  : 从纪元的时间开始到现在的秒数(单位是秒)
time.localtime  ： 元组的格式返回时间
"""
print(time.time())
print(time.localtime())
print(time.asctime())
# 利用time.strftime进行时间格式转换
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 想获取两天前的时间
now_timestamp = time.time()
twoDays_before = now_timestamp - 60*60*24*2
twoDays_BeforeTime_tuple = time.localtime(twoDays_before)
print(time.strftime("%Y-%m-%d %H-%M-%S",twoDays_BeforeTime_tuple))