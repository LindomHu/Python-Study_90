#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/17 上午12:35 
# @Author : huix
# @File : test_Fileupload1.py 
# @Software: PyCharm


from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains


class TestFileUpload():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def testCase_FileUpload(self):
        self.driver.get("https://deershare.com/send")
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/div[3]/button').send_keys('..testerhome1.png')
        # print(self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/button').text)
        sleep(2)