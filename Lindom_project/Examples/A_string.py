# -*- coding: utf-8 -*-
#上面这行不是注释，它声明了当前代码采用的字符编码格式：utf-8,必须放在第一行
#ascii编码表,gbk,unicode(utf-8)
#修改编辑器文字大小：file--settings--editor--colors & fonts--font--size改为18
#单行注释
"""
多行注释
"""
'''
这也是多行注释
'''
#打印一行字符串到屏幕
print('hello world, 你好， python！')
#这一段讲的是字符串操作：
#什么是变量，以及变量类型
#变量的命名规则：变量只能用字母、数字、下划线；不能以数字开头，文件命名也要遵循这个规则
#变量名可以在规则范围内任意取
#首先介绍三种类型的变量：
#字符串型(string), 整数型(integer)，浮点型(float)
name = "张三"     #name字符串变量， 值要用引号引起来
age = 25           #age是整数型变量
weight = 75.5678    #weight是浮点型变量
# %s：字符串占位符，执行时后面的字符串变量内容会替代这个占位符
# %d 整数占位符, 后面须对应整形变量
# %f 浮点占位符，后面须对应浮点型变量
str1 = 'My name is %s, welcome to the python world'%name
str2 = "My age is %d."%age
str3 = "我的体重是%.3f。"%weight   #.3表示小数精度为3，四舍五入
print(str1)
print(str2)
print(str3)
#%r : Random,随机占位符， 万能占位符
print("随机占位：%r"%name)
print("随机占位：%r"%age)
print("随机占位：%r"%weight)

#如何输出换行和转义
#\ :转义符，表示斜杠后面的内容仅仅代表它原始的意思,\n : 换行
print("python的安装路径是：c:\\nython34,换一行\n新的行")
print('Welcome to the python\'s world!')

#实际上我们有两种方法实现字符串的拼接
#下面做一个例子，利用上面的三个变量拼出一句完整的句子
#方法1
str4 = "我是：%s,我今年%d了，我的体重是%.3fKG"%(name,age,weight)
print(str4)
#方法2：用 “+” 做字符串相加
#字符串是不能直接和整数以及浮点数相加，必须要全部转换为字符串
#变量类型转换函数：str(20):转换为字符'20'；int('20')：转换为整数20；float('2.5')：转换为浮点型2.5
str5 = "我是：" + name + ",我今年" + str(age) + "了，我的体重是" + str(weight) + "KG"
print(str5)

#下面学习标准输入函数,input:输入
"""
answer = input("请问你的姓名：")   #x = input(y) ：y：提示信息；x：得到用户的输入
print("哦，你叫：%s"%answer)
"""
# 模拟苹果的siri的简单回答
myname = 'Siri'
myage = 18
myfavor = "吃饭喝茶看电影，旅游..."
x = input("请问你有什么问题吗?")
if "姓名" in x:  # if 如果，如果在用户的提问中包含 "姓名" 两个字
    print("我叫：%s,很高兴认识你!" % myname)
elif "年龄" in x:  # elif 否则如果包含“年龄”
    print("我今年%d!"%(myage))
elif "爱好" in x:  # 否则如果包含“爱好”
    print("我叫：%s,我今年%d!我喜欢%s" %(myname, myage, myfavor))
else:  # 当前面的都没有满足，则执行这个
    print("你好，我好像没有听明白，能重复一遍吗？")
