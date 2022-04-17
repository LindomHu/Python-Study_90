#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/17 上午12:19 
# @Author : huix
# @File : test_FileUpload.py 
# @Software: PyCharm

# from ..base import Base
from selenium import webdriver
from time import sleep

class TestFileUpload():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def testCase_FileUpload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id('uploadImg').send_keys('..testerhome1.png')
        sleep(3)