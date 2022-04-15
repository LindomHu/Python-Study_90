#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/13 下午4:25 
# @Author : huix
# @File : test_ActionChains.py 
# @Software: PyCharm
import pytest
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.by import By


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.skip  # 跳过这个用例集
    def testCase_click(self):
        """
        打开"http://sahitest.com/demo/clicks.htm"
        运用ActionChains进行一个点击、双击和右键操作
        """
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_doubleclick = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        element_right = self.driver.find_element_by_xpath("/html/body/form/input[4]")

        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_right)
        action.perform()
        time.sleep(2)

    # @pytest.mark.skip
    def testCase_move(self):
        """
        打开百度网页
        运用ActionChains移动到"设置"按钮
        """
        self.driver.get("http://baidu.com")
        element_move = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(element_move).perform()
        time.sleep(2)

    def testCase_dragdrop(self):
        """
        打开 https://sahitest.com/demo/dragDropMooTools.htm
        将dragme的div分别拖到下面四个items的div上，拖到了颜色会变
        """
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        element_drag = self.driver.find_element_by_id("dragger")
        element_target1 = self.driver.find_element(By.XPATH,"/html/body/div[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(element_drag,element_target1).perform()
        time.sleep(1)

        # 第二种方式定位和拖动
        element_target2 = self.driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(5)")
        action.click_and_hold(element_drag).move_to_element(element_target2).release().perform()
        time.sleep(1)

        element_target3 = self.driver.find_element(By.XPATH,"/html/body/div[4]")
        action.click_and_hold(element_drag).move_to_element(element_target3).release().perform()
        time.sleep(1)

        element_target4 = self.driver.find_element(By.XPATH,"/html/body/div[5]")
        action.click_and_hold(element_drag).move_to_element(element_target4).release().perform()
        time.sleep(1)