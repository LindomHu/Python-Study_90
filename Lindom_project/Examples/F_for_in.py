# -*- coding: utf-8 -*-
#数组又叫列表（list）：分为一维列表、二维列表、多维列表，第五种变量
#一维列表： 将一串变量或值合并到一个列表变量中，如下：
fruits1 = ["banana", "apple", "mango", "berry"]
fruits2 = ["banana", 10, 6.5]
#二维列表：将一维列表又组成一个一维列表，如下：
fruits3 = [["banana", 10, 6.5], ["apple", 5, 8], ["mango", 2, 9], ["berry", 8, 20.5]]
#把上面的二维列表列成表格：
"""
品名     数量  单价
"banana" 10   6.5
"apple"  5    8
"mango"  2    9
"berry"  8    20.5
"""
#读取数组中的元素，可以用下标直接获取，下标从0开始计数
print("我今天吃了好多%s。"%fruits1[3])
#二维列表的下标有行和列：fruits3[行号][列号]   加减乘除： + - * /
mSum = fruits3[0][1] * fruits3[0][2]        #  10（第1行第2列） * 6.5（第1行第3列）
print("我今天买了%d斤%s,单价是%.2f一斤，总共花了%.2f元人民币"
      %(fruits3[0][1], fruits3[0][0], fruits3[0][2], mSum))

#循环语句：for 变量 in 集合
#意思就是说在某一个集合中循环取值赋给 变量 ，直到值被取完
for j in "hello 你好 python! ":
    print(j)
#下面开始循环一维数组,依次输出所有水果名称
for fruit in fruits1:
    print(fruit)                    #这里输出的是一个一个的水果名称
#下面开始循环二维数组,依次输出所有水果名称以及信息
for fruit in fruits3:
    print(fruit)                    #这里输出的是水果的一维数组

#用循环语句的嵌套(两个for嵌套)遍历fruits3二维数组，一个一个的输出里面的所有元素
'''
banana
10
6.5
apple
5
8
......
'''
print("-" * 100)
for fruit in fruits3:           #循环二维数组的每一行
    for f in fruit:             #循环每一行的每一列
        print(f)                #输出每一个元素

#习题1：把二维数组采用两层循环嵌套的方式，按照下列格式输出：
fruits3 = [["banaba", 10, 6.5], ["apple", 5, 8], ["mango", 2, 9], ["berry", 8, 20.5]]
"""
|   Name  | Amount |  Price   |
|  banana |   10   |   6.5    |
|  apple  |   5    |    8     |
|  mango  |   2    |    9     |
|  berry  |   8    |   20.5   |
"""
print("-" * 100)
#"name".center（10）：name居中，不够的前后补空格，最长10个字符宽度
title = "|" + "Name".center(10) + "|" + "Amount".center(10) + "|" + "Price".center(10) + "|"
print(title)
for fruit in  fruits3:
    line = '|'                       #先定义一个变量，用于保存一行数据
    for f in fruit:
        line = line + str(f).center(10) + "|"        #将一行数据做累加，拼接成一行字符串
    print(line)


#第二种for循环
#第二种循环，指定循环次数 range :范围
#range(5)：[0,1,2,3,4]
for i in range(5):          #就是： for(i=0;i<5;i=i+1)
    print(i)

#i第一个值取1，循环到<10，每循环一次 i 加 2,步长为2
#range(1, 10, 2):[1,3,5,7,9]
for i in range(1, 10, 2):   #就是： for(i=1;i<10;i=i+2)
    print(i)

#冒泡排序：用冒泡排序方法对下列数组进行排序（升序）
#len(array):取数组的长度（元素个数）；range(5, 0, -1)  ： [5,4,3,2,1]
array = [8,5,6,4,9,1]
for i in range(len(array)-1, 0, -1):#倒过来取值，第一个是5，依次递减，i取值：5 4 3 2 1, #for(i=5;i>0;i=i-1)
    for j in range(i):  #j的最大取值取决于i的大小
        if array[j] > array[j + 1]: #如果当前位置数据比下一个数据要大
            array[j], array[j + 1] = array[j + 1], array[j]  # 将两个值互换
            # tmp = array[j]
            # array[j]=array[j+1]
            # array[j+1] = tmp
        print(array)                #每循环完一次后的数组当前结果
print(array)

#习题:写一段循环语句代码，输出下面的图形
"""
                *
               ***
              *****
             *******
            *********
"""
for i in range(1, 10, 2):
    print(("*" * i).center(20))

#习题：用for循环打印出99乘法表
"""
1x1=1
2x1=2	2x2=4
3x1=3	3x2=6	3x3=9
4x1=4	4x2=8	4x3=12	4x4=16
5x1=5	5x2=10	5x3=15	5x4=20	5x5=25
6x1=6	6x2=12	6x3=18	6x4=24	6x5=30	6x6=36
7x1=7	7x2=14	7x3=21	7x4=28	7x5=35	7x6=42	7x7=49
8x1=8	8x2=16	8x3=24	8x4=32	8x5=40	8x6=48	8x7=56	8x8=64
9x1=9  9x2=18	9x3=27	9x4=36	9x5=45	9x6=54	9x7=63	9x8=72	9x9=81
"""
print("-" * 100)
print("你\t好")  #\t:制表符（tab键）
print("")         #换一行
print("张三", end="")#end="" 表示打印完成后不换行，默认是换行的
print("ok！")

for i in range(1, 10):
    for j in range(1,i+1):
        print("%dx%d=%d\t"%(i,j,i*j), end="")
    print("")

for i in range(1, 10):
    line=""
    for j in range(1,i+1):
        line = line + "%dx%d=%d\t"%(i,j,i*j)
    print(line)