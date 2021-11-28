# -*- coding: utf-8 -*-
#定义一个字典(dictionary)，第七种变量(数据类型)，简称：dict
#定义一个字典 ,字典实际上是一个键值对的组合，格式：{键1：值1，键2：值2，......}
dict = {"name":"banana", "ID":1, "price":10}
#1、字典中的 键 是不允许重复的
#2、字典是无序的。查字典要根据 键 来查 值

#定义一个字典：将hrdb中的员工steven.king定义为一个字典
#请输出该字典的的 姓 名
#增加元素：所在国家、所在城市
#删除元素：入职日期
#将部门ID,职位ID分别修改为对应的部门名称，职位名称
#采用循环遍历的方式输出Steven.king的详细信息
dictKing = {}       #定义了一个空字典
#往字典中增加元素
dictKing["eId"] = 100
dictKing["fName"] = "steven"
dictKing["lName"] = "king"
dictKing["hDate"] = "1987-06-17"
dictKing["jobId"] = "AD_PRES"
dictKing["salary"] = 24000
dictKing["dId"] = 90
print(dictKing)
#查字典
#dictKing.get("fName") ： 输出字典中fName对应的值, get :获取
#dictKing["lName"] ：输出字典中lName对应的值
print("dictKing中的姓名是：%s.%s."%(dictKing.get("fName"),
                                       dictKing["lName"]))
#增加元素：所在国家、所在城市
dictKing["Country"]="China"
dictKing["City"] = "BeiJing"
#删除元素：入职日期
del dictKing["hDate"]
print(dictKing)
#将部门ID,职位ID分别修改为对应的部门名称，职位名称
dictKing["dId"] = "Executive"
dictKing["jobId"] = "President"
#采用循环遍历的方式输出Steven.king的详细信息，items：项目
for key,value in dictKing.items():
    print("%s:%s"%(key,value))