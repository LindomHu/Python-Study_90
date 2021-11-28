# -*- coding: utf-8 -*-
#这里使用逻辑符号：或与非(or/and/not)(JAVA的是||/&&/！),优先级：非 - 与 - 或
a = 1
b = 2
c = True
if a==1 and b==2 and c:             #返回真
    print("上面的条件都是对的")
else:
    print("这句不会执行")

if a==1 and (b==3 or c):            #返回真
    print("上面的条件也是对的")
else:
    print("这句不会执行")

if a==1 and (b==3 or not c):        #返回假 b==3 等价于 not b!=3
    print("上面的条件错了")
else:
    print("这句终于执行了")

"""
#例子：足球俱乐部招人要求是:如果男性， 18~30岁，身高>=175cm 或者 如果女性，18~30岁，身高>=170cm
age = int(input("您的年龄:"))     #提示用户输入年龄，并将用户输入的年龄转换成整数型以用作大小比较
gender = input("您的性别（M/F）:") #M:男性； F:女性
height = float(input("您的身高（CM）:"))
#一行分为两行写的时候，可以加一个 \
if age >= 18 and age <= 30 and  ((gender == 'M' and height >= 175) \
    or (gender == 'F' and height >= 170)):
    print("合格")
else:
    print("不合格")
"""
#请根据分数(score)，输出相应的得分等级：>=90 优秀; 70~90 良好；60~70及格；<60 不及格
#多分支判断语句的特点是：只要进入了一个分支，执行完分支内语句后就会直接跳出if结构语句
#例如： 下面的72分会进入“良好”，之后就跳出整个if 语句。
score = input("输入分数:")
#将score转换为float型
score = float(score)
if score>=90:
    print("优秀")
elif score>=70:
    print("良好")
elif score>=60:
    print("及格")
else:
    print("不及格")
print("GoodBye!")
#规则总结：
#1、字符串不能和整数或浮点数相加、比较等
#2、字符串不能用来比较数字的大小，必须要转换成数字才能真的比较大小
#3、input语句永远会得到一个字符串
#4、input中你不能限制用户的输入，用户可以输入不合法的数据库，代码中需要做处理
