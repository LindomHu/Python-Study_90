#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/16 上午11:48 
# @Author : huix
# @File : base.py 
# @Software: PyCharm


from selenium import webdriver
import os

# 如果需要在多个浏览器上执行，可以加上浏览器browser的判断

class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'gecko':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Safari()

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()