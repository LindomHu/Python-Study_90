# -*- coding: utf-8 -*-
#软件开发模式：面向过程、面向对象
#下面定义两个函数，def--define：定义
#函数（function,意思是将一个功能封装为一个函数）
#函数说明：输入两个任意数字，输出相加的结果
# 输入参数：x: 任意数字；y：任意数字
# 输出参数：None，打印输出x+y结果到屏幕
def add(x, y):
    z = x + y
    print(z)
#函数说明：输入两个任意数字，返回相减的结果给调用者
# 输入参数：x: 任意数字；y：任意数字，默认值为0
# 输出参数：x - y结果返回给调用者
def sub(x, y=0):
    z = x - y
    return z  #return(返回) z的值给调用者，return将结束函数的运行
    print("ok")  #return后面的语句不会执行了,给函数划一个句号
#__name__：变量 ，当当前py文件是主入口执行文件的时候，等于__main__
#否则当被其他py文件import的时候，等于所在文件的文件名
if __name__ == '__main__':
    add(10,20)
    y = sub(30,20)  #y接受了函数中return z的值
    x = add(20,30)  #由于add函数没有返回（return），x=None
    m = sub(30) #这里没有给y传值，y用默认值
    n = sub(y=10, x=20)  #传参数的时候，可以用参数名赋值
    print("x|y|m|n : %r|%r|%r|%r"%(x,y,m,n))
    print("认识一下print",end="")
    print("还是这一行")

#习题:写一个函数，输出类似下面的图形，但是，最终有多少行，由输入参数决定
"""
                *
               ***
              *****
             *******
            *********
"""
#x:塔的层数
#1,2,3,4,5,6,7,8,9
#1,3,5,7,9,11,13,15
def starTower(x):
    for i in range(1, x+1):
        print(("*" * (i+(i-1))).center(200))

starTower(8)

cn=int(input("请输入层数："))
for i in range(1,2*cn,2):
    print(('*'*i).center(cn*2))