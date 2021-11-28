# -*- coding: utf-8 -*-
#try...except...:错误捕捉语句
#被try包裹的语句如果出现错误，则会跳转到except子句中进行错误处理
#一段代码中只要有一行代码错误了，后面的语句都不会被执行了

try:
    print(name)
    x = 1 / 0
    open("不存在的文件.txt")
    print("这句话会不会被执行?")
except Exception as e:              #except:异常
    print("异常了.....")
    print("错误信息：", e)
print("继续运行.....")

#请根据分数(score)，输出相应的得分等级：>=90 优秀; 70~90 良好；60~70及格；<60 不及格
score = input("输入分数:")
try:
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
except:
    print("请输入合法的数字!")
print("GoodBye!")