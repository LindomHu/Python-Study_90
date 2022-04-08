#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/5 下午11:52 
# @Author : huix
# @File : test_testerhome.py 
# @Software: PyCharm


# 编写测试用例

from selenium import webdriver
import time


class TestTesterHome():
    def setup(self):
        self.driver = webdriver.Chrome()
        # 如果driver没有配置环境变量，需要在括号里面指定对应driver的路径
        # self,driver = webdriver.Firefox(executable_path="")

        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_testerhome(self):
        self.driver.get("http://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_partial_link_text("接口自动化").click()
        time.sleep(2)
        try:
            # driver.save_screenshot("") 截图并保存
            picture_url = self.driver.save_screenshot('./testerhome1.png')
            print("%s ：截图成功！！！" % picture_url)
        except BaseException as msg:
            print("%s ：截图失败！！！" % msg)

