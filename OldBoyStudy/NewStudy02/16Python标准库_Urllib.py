# -*- coding: utf-8 -*-
# @Time : 2021/11/21 15:01
# @Author : huix
# @File : 16Python标准库_Urllib.py

import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
# print(response)

# 返回响应码
print(response.status)
print("=======================")
# 返回请求后响应里面的一些参数信息
print(response.read())
print("=======================")
# 返回请求的头部信息
print(response.headers)