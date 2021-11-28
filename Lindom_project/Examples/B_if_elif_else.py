# -*- coding: utf-8 -*-
#IF语句, 分支判断语句,完整的语法如下：
"""
elif：else if：否则如果

格式：
if  条件表达式:
    如果上面的条件表达式是成立的则执行这一段代码
    注意：这段代码隶属于if,需要缩进，并且左对齐
elif  条件表达式：
    ......
elif  条件表达式：
    ......
else:
    .....

"""
a = 3           #一个等于表示赋值
b = 2
#表达式中的比较符号还可以包括：>, <, >=, <=, ==, !=
#数字比较,注意缩进，缩进代表子语句，同一个层次的子语句必须缩进整齐
#tab键用来缩进，宽度相当于4 个空格，shift tab:往回缩进
if a >= b:
    print("a更大！")
    print("也许a等于b！")
else:
    print("b更大!")

str1 = "haha"       #一个等号表示赋值
#字符串的比较
if str1 == 'haha':      #两个等号表示比较
    print("haha")
else:
    print("no haha")
#等价于：
if str1 != 'haha':      #不等于
    print("no haha")
else:
    print("haha")
# 字符串也有大小，会一个字符一个字符的比较, 字符大小参照ASCII码表
# 字符串大小可用于字符串排序，如手机的通讯录排序
if str1 > "hb":
    print("haha")
else:
    print("hb更大")
