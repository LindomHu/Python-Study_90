#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/5 18:20 
# @Author : Lindom
# @File : test_selenium.py
# @Software: PyCharm

import selenium
from time import sleep
from selenium import webdriver
from WebAutoTest.base import Base

class TestBaidu(Base):
    def test_selenium(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com/")
        sleep(3)
    # test_selenium()