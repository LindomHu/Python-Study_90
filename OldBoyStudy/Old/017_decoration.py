# -*- coding: UTF-8 -*-
# @Time : 2020/6/14 22:39
# @Author : Lindom
# @File : 装饰器.py 
# @Software: PyCharm Community Edition
import time

def timemer(func):
    def wrapper(*args,**kwargs):
        strtat_time = time.time()
        func()
        stop_time = time.time()
        print("the fun run time is %s"%(stop_time-strtat_time))
    return wrapper()

@timemer
def func():
    # num = a+b
    time.sleep(2)
    print("开始运行func函数")

# func()