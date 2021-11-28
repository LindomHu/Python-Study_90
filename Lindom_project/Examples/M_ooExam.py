# -*- coding: utf-8 -*-
#创建一个Siri类,继承自K_OOP.Person
#该类应该具备构造函数，直接指定姓名，体重，年龄，爱好
#添加方法：getName，getAge ,getFavor：获取相关信息
#添加方法: setName:改名，byebye:再见退出
#调用类来实现问答
from Examples.K_OOP import Person
class siri(Person):
    def __init__(self,Name,Age,Height,Favor): #给siri指定姓名，体重，年龄，爱好
        self.Name = Name
        self.Age = Age
        self.Height = Height
        self.Favor = Favor
    def getName(self):
        print("我叫%s,很高兴认识你"%self.Name)
    def getAge(self):
        print('我的年龄是%d'%self.Age)
    def getHeight(self):
        print('我身高%d'%self.Height)
    def getFavor(self):
        print('我叫%s,我的年龄是%d,身高%d,喜欢%s'%(self.Name,self.Age,self.Height,self.Favor))
    def setName(self,newname):
        print('你帮我改名了，改成%s'%newName)
        self.Name = newName
    def byebye(self):
        print('再见了，下次聊')
if __name__ == '__main__':
    #先实例化
    s = siri('stri', 3 , 150, '吃饭' )
    while True:
        x = input("请问你有什么问题吗?")
        if "姓名" in x:  # if 如果，如果在用户的提问中包含 "姓名" 两个字
            s.getName()
        elif "年龄" in x:  # elif 否则如果包含“年龄”
            s.getAge()
        elif '身高' in x:
            s.getHeight()
        elif "爱好" in x:  # 否则如果包含“爱好”
            s.getFavor()
        elif '改名' in x:
            newName = input ('请帮我改个名字，你觉得改成什么好听呢？')
            s.setName(newName)
        elif x == "bye":
            s.byebye()
            break
        else:  # 当前面的都没有满足，则执行这个
            print("你好，我好像没有听明白，能重复一遍吗？")