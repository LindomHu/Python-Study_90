#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/16 上午11:32 
# @Author : huix
# @File : test_window.py
# @Software: PyCharm


# 多窗口切换处理

from WebAutoTest.base import Base
from time import sleep


class TestWindow_Baidu(Base):
    """
    1-打开百度
    2-点击登陆
    3-弹框中点击立即注册，输入用户名和账号
    4-返回刚才的登陆页，点击登陆
    5-输入用户名和密码，点击登陆
    """
    def test_BaiduRegister(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("s-top-loginbtn").click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self.driver.find_element_by_id("TANGRAM__PSP_11__regLink").click()
        sleep(2)
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        # 将当前所有的窗口赋值给windows
        windows = self.driver.window_handles
        # 切换到注册页面的窗口
        self.driver.switch_to.window(windows[-1])

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("r_username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("132000000000")
        self.driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("r_password")
        sleep(2)
        # 切换到登陆页面的窗口
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("17673115841")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("abc12345aaaa")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(2)