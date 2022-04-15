#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/12 上午11:13 
# @Author : huix
# @File : 07二分查找.py 
# @Software: PyCharm


def sort(arr,num):
    i,j = 0,len(arr)-1
    # 0,4

    while i<=j:
        mid = (i+j)    // 2    # 2
        print(mid)
        if arr[mid]<num:    #arr[2]=4
            i = mid+1
            print("i:",i)
        elif arr[mid]>num:
            j = mid-1
            print("j:",j)
        else:
            return True
    return False


print(sort((2, 3, 4, 5, 9, 6), 3))