# -*- coding: utf-8 -*-
# @Time : 2021/11/21 21:47
# @Author : huix
# @File : 18Python第三方库.py


# pytest：单元测试框架  跟内置框架Unitest一样  并且更加灵活好用
# requests：网络请求的库，比urllib更加灵活

"""
使用第三方库，首先需要使用pip install xxxx进行安装
pip install pytest
pip install ruquests

第三方库官网：pypi.org
"""

import requests

# r = requests.get("http://www.baidu.com")
r = requests.get("http://www.pypi.org/post",data={"key":"value"})
r.encoding = "utf-8"

# print(r.text)
print(r.content)
print(r.url)