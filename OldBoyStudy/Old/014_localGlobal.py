# -*- coding: UTF-8 -*-
# @Time : 2020/5/31 22:13
# @Author : Lindom
# @File : 014_localGlobal.py
# @Software: PyCharm Community Edition

name = 56   #name为全局变量,局部变量不能直接改全局
def change_Name(name):
    print("before name",name)

    name = 33
    print("after name",name)

change_Name(name)
print(name)
print("\n")

name2 = ["lindom","test"]   #列表
def change_Name2(name2):
    print("before name2",name2)

    name2[0] = "Lindom"    #全部变量为一个列表时，局部就可以直接改
    print("after name2",name2)

change_Name2(name2)
print(name2)
print("\n")

name3 = {"name":"lindom","sex":"true"}   #字典
def change_name3(name3):
    print("before name3",name3)
    name3["name"] = "Lindom"            #全部变量为一个字典时，局部就可以直接改
    print("after name",name3)

change_name3(name3)
print(name3)