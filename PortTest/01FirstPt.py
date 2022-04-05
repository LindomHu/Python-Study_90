#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/2/27 下午5:21 
# @Author : huix
# @File : 01FirstPt.py
# @Software: PyCharm


import requests

# 给接口地址定义名称
url = "http://v.juhe.cn/weather/index"

# 定义一个错误的key值，测试接口的返回值
para = {"cityname":"北京","key":"221ec2c9d854d2859310ea808cb760fd"}


# 发送请求
r = requests.get(url,params=para)
print(r.status_code)

# 获取接口的json数据
# print(r.json())

res1 = r.json()
print(res1["reason"])
assert (res1["error_code"]) == 10012