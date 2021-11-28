# -*- coding: utf-8 -*-
# @Time : 2021/11/14 19:30
# @Author : huix
# @File : 06猜数字游戏练习.py

import random
computer_number = random.randint(1,101)

while True:
    xiaoming_number = int(input("请输入一个1～100之间猜的数字："))
    if computer_number > xiaoming_number:
        print("猜小了")
    elif computer_number < xiaoming_number:
        print("猜大了")
    elif computer_number == xiaoming_number:
        print("恭喜猜对了")
        break
