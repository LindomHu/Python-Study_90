# -*- coding: utf-8 -*-
#判断逻辑值 a 是否为真。 变量类型第四种：bool型，布尔型:真（True） or 假（False）
#bool只有两个取值：True/False
#如果放在IF语句后面，那么什么是真，什么是假？
#真：True;1;200;"abc"
#假：False;0;"";None(相当于JAVA/mysql的Null)

#练习调试：在有效行的行首点空白处一下，或出现一个红色的断点
# debug:调试；variables:变量；debugger:调试器；console:控制台
#step over:下一步（F8）; run to cursor:运行到光标处
#resume program：返回程序继续运行到下一个断点或程序尾
# stop 'XXX'：当前位置停止运行
#mute breakpoints：让所有断点失效
#Restore layout: 恢复布局，当发现某些窗口找不到时可点击

print(True+True+False)    #输出2   ；True=1   False=0

a = ""
if a:
    print("%r是真的！"%a)
else:
    print("%r是假的！"%a)

#例子：提问用户的性别，并做出相应的输出
#input函数永远会返回一个字符串，如果不输直接回车，返回的是空字符串 : ""
answer = input("Are you a schoolboy(y/n)?")
if answer: #表示用户有输入
    if answer == 'y':   #假如用户输入的是 y
        boy = True      #boy是布尔型变量
    elif answer=='n':   #假如用户输入的是 n
        boy = False
    else:               #用户输入了别的字符
        boy = None      #未知，None是一个独立的变量类型：None类型

    if boy:
        print("Hello, My dear boy!")
    elif boy == False:
        print("Hello, My dear girl!")
    else:
        print("Your input is invalid!") #invalid:无效的
else:       #假如用户没有输入直接回车,此时answer等于空串，为假
    print("Please input y or n!")

