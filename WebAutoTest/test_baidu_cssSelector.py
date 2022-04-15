#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/11 下午11:57 
# @Author : huix
# @File : test_baidu_cssSelector.py 
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestBaidu():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("http://www.baidu.com")

    def teardown(self):
        self.driver.quit()

    def testBaidu(self):

        # self.driver.find_element(By.XPATH,'//*[@id="s_kw_wrap"]/input').send_keys("测试")
        self.driver.find_element(By.CSS_SELECTOR,'.s_ipt').send_keys("测试")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '#su').click()
