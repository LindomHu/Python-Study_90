#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/1 0:33 
# @Author : Lindom
# @File : 09集合基本操作.py 
# @Software: PyCharm Community Edition

list_1 = set([5,6,1,2,0,99,3])
list_2 = set([0,3,4,8])


# 添加一项
list_2.add(5)

# 添加多项
list_2.update([88,99])
print("add:",list_2)

# 删除一项
list_1.remove(99)
print("remove:",list_1)

# 任意删除一项并且返回删除的字符
print("pop:",list_1.pop())
print("pop:",list_1.pop())

# 判断某个字符是否在这个集合里  a in X
# 其它类型判的断也是这种写法
print(5 in list_1)

# 浅copy
list_c = list_2.copy()
print("copy:",list_c)

# discard与remove
# discard删除集合里面不存在的元素不会报错，remove会报错
# list_1.discard(111)
# list_1.remove(111)

# Ⅲ oldboy-11