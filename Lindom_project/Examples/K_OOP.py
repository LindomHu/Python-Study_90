# -*- coding: utf-8 -*-
#OOP: object orient programming:面向对象编程
#面向对象的三大特性：封装、继承、多态
#class：类
class father(object):# 封装：定义封装一个father类，继承自object（最原始的类），默认值，可省略
    name = "张三"     #属性，又叫成员变量
    def add(self, x, y):    #方法，又叫成员函数 self:自己
        z = x+y
        return z
if __name__=='__main__':
    #第八种变量类型：对象变量
    zs = father()           #实例化一个，类在使用的时候需要实例化
    ww = father()           #又实例化了一个，他们是分别独立的个体
    print(zs.name)          #张三
    zs.name = "李四"        #zs改名为李四
    print(zs.name)          # 李四
    print(zs.add(10,20))    #30， zs传递给self;  10给x; 20给y

class son(father):          #继承：son这个类继承了father,父子关系，父类(基类)，子类（派生类），子类得到了父类的所有东西
    age=0
    def sub(self, x, y):
        z = x - y
        return z
if __name__=='__main__':
    zsSon = son()           #实例化
    zsSon.add(10,20)        #继承自father
    zsSon.sub(100,80)       #自己定义的
    print(zsSon.name)       #继承自father
    print(zsSon.age)        #自己定义的

class grandSon(son):
    def mul(self, x, y):
        z = x * y
        return z
    def add(self, x, y):    #重写了父类的add方法，重写是多态的一种
        z = (x + y) * 2
        return z
if __name__ == '__main__':
    gzs = grandSon()   #实例化
    print(gzs.add(10,20))      #会做加法，重写了father的加法，60
    gzs.sub(100,40)     #会做减法，来自son
    gzs.mul(10,20)      #会做乘法，自己定义的
    print(gzs.name)     #张三，来自father
    print(gzs.age)      #0,来自son
    father.add(gzs, 10, 20) #又调用了父类的add，但是要给self传值：gzs

#再来定义一个类：
#1:构造函数的作用； 2：变量类型的作用域（成员变量、私有变量(局部变量)）
class Person:
    age=0           #类中的成员变量
    def __init__(self, n, w=8):   #构造函数  init:initial,初始化
        self.name = n    #加上self的变量也是成员变量，但n是私有变量,函数内的局部变量
        self.weight = w #私有变量只在本函数内部有效，成员变量整个类有效
        self.say()          #函数中调用其他成员函数，要加上self
    def say(self):
        print("出生的第一句话：我叫%s,我刚出生%d岁,重%s斤"
              %(self.name, self.age, self.weight))#引用类成员变量都要加self

if __name__ == '__main__':
    p = Person("张三", 30) #实例化同时执行构造函数（如果有参数要传参给构造函数）
    l = Person("李四", 40)
    p.say()                        #又调用了say函数
    print(p.name)                  #调用类中的姓名