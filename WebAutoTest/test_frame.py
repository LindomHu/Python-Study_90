#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/16 下午5:41 
# @Author : huix
# @File : test_frame.py 
# @Software: PyCharm

from WebAutoTest.base import Base
from time import sleep


# 多个页面切换处理
class TestFrame(Base):
    """
    1-打开 https://www.runoob.com//try/try.php?filename=jqueryui-api-droppable页面
    2-获取到<请托拽我>的text，并打印出来
    3-获取<点击运行>这个按钮的test并打印
    """
    def test_Frame(self):
        self.driver.get("https://www.runoob.com//try/try.php?filename=jqueryui-api-droppable")
        # 切换 frame
        self.driver.switch_to.frame("iframeResult")
        (self.driver.find_element_by_xpath('//*[@id="draggable"]'))
        # element_drg1 = self.driver.find_element_by_xpath('//*[@id="droppable"]')
        # action = ActionChains(self.driver)
        # action.drag_and_drop(element_drg,element_drg1).perform()
        sleep(1)

        # 再切换回去
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
        sleep(2)