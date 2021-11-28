# -*- coding: utf-8 -*-
#While循环语句
count = 0
while count < 9:  #当count<9则一直循环
    print('The count is:%d'%count)
    count = count + 1       #变量值累加
print("Good bye!")

#for循环的写法
for count in range(9):
    print('The count is:%d' % count)
print("Good bye!")

#请判断下面的输出是多少？
#continue: 继续循环 ； break：强制中断循环
i = 94
while i<100:
    i += 1          #等价于 i = i + 1
    if i%2==0:      #%：求余数，2%2=0：2/2等于1余0; 3%2=1,返回的是除法后的余数
        continue    #继续循环，下一句跳转到while i<100，for循环同样适用
    if i>95:
        break       #中断循环，下一句跳出循环语句，for循环同样适用
print(i)
#for循环的写法
for i in  range(94, 100):
    if i % 2 == 0:  # %：求余数，2%2=0：2/2等于1余0; 3%2=1,返回的是除法后的余数
        continue  # 继续循环，下一句跳转到while i<100，for循环同样适用
    if i > 95:
        break  # 中断循环，下一句跳出循环语句，for循环同样适用
print(i)

#将siri的简单回答的例子改为可以循环提问，
#如果用户输入"bye"则退出程序

# 模拟苹果的siri的简单回答
myname = 'Siri'
myage = 18
myfavor = "吃饭喝茶看电影，旅游..."

while True:
    x = input("请问你有什么问题吗?")
    if "姓名" in x:  # if 如果，如果在用户的提问中包含 "姓名" 两个字
        print("我叫：%s,很高兴认识你!" % myname)
    elif "年龄" in x:  # elif 否则如果包含“年龄”
        print("我今年%d!"%(myage))
    elif "爱好" in x:  # 否则如果包含“爱好”
        print("我叫：%s,我今年%d!我喜欢%s" %(myname, myage, myfavor))
    elif x=="bye":
        print("下次聊...")
        break
    else:  # 当前面的都没有满足，则执行这个
        print("你好，我好像没有听明白，能重复一遍吗？")
