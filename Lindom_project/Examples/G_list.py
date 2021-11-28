# -*- coding: utf-8 -*-
#定义一个空列表
fruits = []
#添加元素
#1、往列表的末尾增加元素:append:末尾添加
fruits.append("banana")
fruits.append("apple")
fruits.append("berry")
fruits.append("mango")
print(fruits)

#2、往列表的中间插入一个元素
fruits.insert(1, "mango")   #在第二个元素之前插入一个mango
print(fruits)
fruits.insert(4, "apple")   #在第五个元素之前插入一个mapple
print(fruits)
#列表的元素删除
#1、按值删除，删除berry
fruits.remove("berry")   #每次remove只会删除一个元素
#删除列表中的所有mango
#fruits.count("mango"):求出列表中有多少个mango
for x in range(fruits.count("mango")):   #根据mango在列表的个数，循环删除
    fruits.remove("mango")
print(fruits)
#2、按照下标来删除
#将列表中的第2个元素删除
fruits.pop(1)
print(fruits)

#列表元素的修改
#将列表中的第二个元素修改为orange
fruits[1] = "orange"
#列表元素的查询，请输出列表元素的第二个元素
print(fruits[1])
#也可以循环列表，查询数据
#请判断一下列表中有没有orange，如果有输出个数
sum = 0 #计数器
for x in fruits:
    if x=="orange":
        sum = sum + 1
if sum>0:
    print("有%d个orange."%sum)
else:
    print("没有orange.")

#将下列数组中的apple单价改为10，并在mango前新增一种水果：orange,20斤，8.5单价
print("-"*100)      #打印一个分隔线
fruits3 = [["banana", 10, 6.5], ["apple", 5, 8], ["mango", 2, 9], ["berry", 8, 20.5]]
o = ["orange", 20, 8.5]
#fruits3[1][2]=10
#fruits3.insert(2,o)
#要用循环语句写出来，行是未知的，要分别判断apple、mango在第几行，列是固定的，然后修改
i = 0
j = 0
while i < len(fruits3):            #用下标来循环
    if fruits3[i][0] == "apple":    #如果当前行的第一列是apple
        fruits3[i][2] = 10           #将第三列的单价改为10
    if fruits3[i][0] == "mango":    #如果当前行的第一列是mango
        j = i                        #记录行号到变量j
    i = i +1                         #累加i
fruits3.insert(j, o)                 #第j个元素之前插入o
print(fruits3)
#改成for循环的写法

#第六种变量数据类型：元组（tuple）,元组是不可修改的数组（列表），没有增删改，用括号表示
t = ("banana","apple","mango","berry")
print(t[0])
