#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/3/30 上午11:09 
# @Author : huix
# @File : 01启动浏览器.py 
# @Software: PyCharm

from selenium import webdriver

driver = webdriver.safari()
driver.implicity(3)
driver.get("http://mail.qq.com")




