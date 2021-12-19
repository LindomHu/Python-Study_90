# -*- coding: utf-8 -*-
# @Time : 2021/12/7 20:49
# @Author : huix
# @File : 02AppTest_trylaunch.py


from appium import webdriver

desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="10.0"
desired_caps["devicenName"]="CLB7N18724007553"
desired_caps["appPackage"]="]="
desired_caps["appActivity"]="com.android.settings.Settings"
driver=webdriver.Remote("http://local:4723/wd/hub",desired_caps)
driver.quit()
