#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/2/27 下午5:52 
# @Author : huix
# @File : 02GetPt.py 
# @Software: PyCharm

import requests

# 定义接口地址
url = "http://v.juhe.cn/weather/uni"

# 定义一个错误的key
para = {"key":"2213yuehfuh9191uh13432421e"}

# 发送请求
r = requests.get(url,params=para)


res = r.json()
print(res["resultcode"])
print(res["error_code"])