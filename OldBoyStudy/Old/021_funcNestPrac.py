#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/6 22:38 
# @Author : Lindom
# @File : 021_funcNestPrac.py 
# @Software: PyCharm Community Edition

# seniority = 0

# def Bonus(months):
#     while True:
#         # global seniority
#         if months >0 and months < 6:
#             seniority = 500
#             return seniority
#         elif months >= 6 and months <= 12:
#             seniority = 120 * months
#             return seniority
#         else:
#             seniority = 180 * months
#             return seniority
#             # break
# def main():
#     name = input("请输入您的姓名：")
#     months = int(input("请输入您的工龄（年）："))
#     bonus = Bonus(months)
#     print('%s来了%s个月，获得奖金%s元'%(name,months,bonus))
#
# main()

import random
import time

# 提示：将以下部分封装进函数
def lattery(q,w,e):
    luckylist = [q,w,e]
    a = random.choice(luckylist)
    print('开奖倒计时', 3)
    time.sleep(1)
    print('开奖倒计时', 2)
    time.sleep(1)
    print('开奖倒计时', 1)
    time.sleep(1)
    return a


def main():
    image = '''
     /\_)o<
    |      \\
    | O . O|
     \_____/
    '''
    print(image)
    lucker = lattery("张三","李四","王五")
    print('恭喜%s中奖！'%lucker)

main()