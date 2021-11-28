#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/1 11:17 
# @Author : Lindom
# @File : 12进度条.py 
# @Software: PyCharm Community Edition

import sys,time
count = 0
k = 0
for i in range(11):
    sys.stdout.write("-" + str(k) )  # 标准输出
    k += 10
    sys.stdout.flush()
    time.sleep(0.2)
    count += 1