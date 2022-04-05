#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/2/27 下午6:18 
# @Author : huix
# @File : 03Post_ip.py
# @Software: PyCharm


import requests


url = "http://v.juhe.cn/weather/ip"
# # 正确的参数
# para = {"ip":"58.215.185.154","key":"221ec2c9d854d2859310ea808cb760fd"}

# 错误的参数-ip
para = {"ip":"58.215.184","key":"221ec2c9d854d2859310ea808cb760fd"}

# 发送post请求
r = requests.post(url,data=para)

# 获取json数据
print(r.json())

res = r.json()
print(res["error_code"])


