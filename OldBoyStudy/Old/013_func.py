# @Time : 2020/5/31 22:27 
# @Author : Lindom
# @File : 009_func.py
# @Software: PyCharm Community Edition


def test1():
    "没有参数的函数"
    print("from the test1,start studung func")
test1()

def test2(x,y,z):  # x,y,z 为形式参数
    "传递位置参数的函数"
    print(x)
    print(y)
    print(z)

test2(2,5,8)  #2，5，8 为实际参数，调用函数的时候会传递给形式参数

def test3(x,y,z):
    "传递关键字参数的函数"
    print(x)
    print(y)
    print(z)

test3(x=3,y=5,z=9)

def test4(x,y,z=9):  #z=9 为默认参数，调用函数的时候非必须传递
    "位置参数、关键字参数、默认参数的函数结合使用"
    print(x)
    print(y)
    print(z)

test4(1,y=3)

#关键字参数不能写在位置参数前面

def test5(*args,**kwargs):
    "参数组函数，以星号开头"
    print(args)
    print(kwargs)

test5(2,5,13,x=15,y=18,z=20)


#调用函数的时候，*args接收n个位置参数，并转换成元组形式
#调用函数的时候，**kwargs接收n个关键字参数，并转换成字典形式





