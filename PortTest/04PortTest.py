#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/3/28 下午11:20 
# @Author : huix
# @File : 04PortTest.py 
# @Software: PyCharm

# 接口关联，下一个接口调用参数需要上一个接口的返回值


# 导包
import requests
# 正则
import re

# 接口地址
url = "http://192.168.103.106:1080/webtours/nav.pl?in=home"
headers = {"Chrom/1.0cxcccc"}


# 为了保持和下一个接口建立相同的连接通道
r1 = requests.session()
# 发get请求
res = r1.get(url,headers=headers)

print(res.text)
userSession= re.findall(r'name=userSession value=(.+?)>',res.text)
print(userSession)


# 测试的接口
url_test = "http://192.168.103.106:1080/webtours/login.pl"
para={"usersession":userSession[0],"username":"jojo","password":"bean"}


# 发送post请求
res1 = r1.post(url_test,data=para)
print(res1.text)
