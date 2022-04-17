#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/17 上午12:18 
# @Author : huix
# @File : test_TouchAction.py 
# @Software: PyCharm


from selenium import webdriver
from selenium import TouchActions
from time import sleep

class TestTouchAction_scroll():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()

    def test_TouchAction(self):
        """
        1-打开页面：http://www.baidu.com
        2-想搜索框输入"测试"
        3-通过 TouchAction 点击搜索
        4-滑倒页面最底部
        5-点击第二页
        """
        self.driver.get("http://www.baidu.com")
        elemnet_input = self.driver.find_element_by_id("kw")
        element_serch = self.driver.find_element_by_id("su")
        elemnet_input.click()
        action = TouchActions(self.driver)
        action.tap(element_serch)

        action.scroll_from_element(elemnet_input,0,100000).perform()
        sleep(2)