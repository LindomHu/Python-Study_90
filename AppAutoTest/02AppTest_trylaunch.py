# -*- coding: utf-8 -*-
# @Time : 2021/12/7 20:49
# @Author : huix
# @File : 02AppTest_trylaunch.py
from appium import webdriver
from selenium.webdriver.common.by import By


desired_caps={}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] =  "10"
desired_caps["deviceName"] =  "CLB7N18724007553"
desired_caps["appPackage"] = "com.baidu.searchbox"
desired_caps["appActivity"] = "com.baidu.searchbox.SplashActivity"

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)


# 百度app启动之后“欢迎使用百度页”弹框：<同意>按钮的点击
# 点击弹出的应用权限框的<同意>按钮
# 点击搜索框
# 输入二十大
# 点击搜索
# 点击第三个搜索结果
# 退出界面

# 百度app启动之后“欢迎使用百度页”弹框：<同意>按钮的点击
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[2]").click()

# 点击弹出的应用权限框的<同意>按钮
driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.Button[@text='始终允许']").click()
driver.find_element_by_id("com.baidu.searchbox:id/obfuscated").click()
driver.find_element_by_link_text("搜索").send_keys("二十大")

driver.quit()

