#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/6 上午11:27 
# @Author : huix
# @File : test_wait.py 
# @Software: PyCharm

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        # 如果driver没有配置环境变量，需要在括号里面指定对应driver的路径
        # self,driver = webdriver.Firefox(executable_path="")

        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_testwait(self):
        self.driver.get("http://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        # time.sleep(2)   直接等待

        # 显式等待
        # 设置等待条件：当找到"目前已经有 181 个团队加入了 TesterHome"这个header的时候，再去点击-求职面试圈，否则就等待6秒，然后超时会自动报错[TimeoutException]
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@class="pull-right hidden-mobile"]')) >= 1
        # WebDriverWait(self.driver,6).until(wait)

        WebDriverWait(self.driver,6).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="team-name"]')))
        self.driver.find_element_by_link_text("求职面试圈").click()
        # time.sleep(2)
        self.driver.find_element_by_partial_link_text("接口自动化").click()
        print("hello,接口自动化")