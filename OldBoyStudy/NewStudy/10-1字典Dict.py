# -*- coding: utf-8 -*-
# @Time : 2021/11/17 22:34
# @Author : huix
# @File : 10-1字典Dict.py


dict1 = {"key1":"1","key2":"2"}
dict2 = dict(a=1,b=3)

print((type(dict1), type(dict2)))

print(dict1.keys())
print(dict1.values())

# 指定key删除字典里面的元素
dict2.pop("b")

# 删除字典里面键值对，并返回
print(dict2.popitem())

print("-----------------------")
# fromkeys
dict3 = {}
dict4 = dict3.fromkeys((1,2,3),"a1")


print(("dict1：%s"%dict1))
print(("dict2：%s"%dict2))
print(("dict4：%s"%dict4))

# 字典推倒式
print({i:i*2 for i in range(1,5)})