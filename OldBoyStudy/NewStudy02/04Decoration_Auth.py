#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/25 22:27 
# @Author : Lindom
# @File : 04Decoration_Auth.py 
# @Software: PyCharm Community Edition

import time
user="lindom"
passwd = "abc123"

def func(func):
    def wrapper(*args,**kwargs):
        username = input("Please input your username:")
        password = input("Please input your password:")
        if username == user and password == passwd:
            print("\033[32;1m you pass the Autification\033[0m")
            return func(*args,**kwargs)
        else:
            exit("\033[31;1m Invalid username or password\033[0m")
    return wrapper


def index():
    print("Welcome to index page")

@func
def home():
    print("Welcome to the home page")
    return "from home page"

@func
def bbs():
    print("Welcome to the bbs page")

index()
print(home())
bbs()