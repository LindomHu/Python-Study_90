#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/12 上午11:33 
# @Author : huix
# @File : 08排序.py 
# @Software: PyCharm


# 冒泡排序
# 升序：重复走访数列，两两比较，如果前面比后面大，就交换位置
# 走访的次数会随着数列排序的完成度越来越少
def sort(arr):
    for i in range(len(arr)-1):
        flag = True
        for j in range(len(arr)-i-1):
            if arr[j+1] > arr[j]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                # print((arr[j], arr[j + 1]))
                flag = False
        if flag:
            flag = True
    return arr


print(sort([1,21,2,3,11,0,4,5,9]))



# 选择排序
#每轮：把最大值或最小值的游标记录下来，然后把这个游标放到开头或者末尾

def sort(arr):
    for k in range(len(arr)-1):
        for i in range(k+1,len(arr)):
            if arr[i] > arr[k]:
                arr[i],arr[k] = arr[k],arr[i]
    return arr


print(sort([1,21,5,12,11,0,4,5,9]))