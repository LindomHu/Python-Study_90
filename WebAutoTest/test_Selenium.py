#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/5 18:20 
# @Author : Lindom
# @File : test_Selenium.py
# @Software: PyCharm

import selenium
from selenium import webdriver

def test_selenium():
    # 注意Chrome的首字母是大写的
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.close()

# test_selenium()