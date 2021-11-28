# -*- coding: utf-8 -*-
# @Time : 2021/11/28 15:57
# @Author : huix
# @File : 03test_AllureDemo.py

import allure

@allure.feature("加购模块")
class TestA():
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("加购模块第一条测试用例")
    @allure.story("第一条用例")
    @allure.link("www.baidu.com")
    def test_case1(self):
        with allure.step("步骤一：选择商品"):
            print("选择商品")

        with allure.step("步骤二：点击加入购物车"):
            print("点击加入购物车")
        print("测试用例1")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("加购模块第二条测试用例")
    @allure.story("第二条用例")
    def test_case2(self):
        print("测试用例2")

    @allure.severity(allure.severity_level.MINOR)
    @allure.story("第三条用例")
    def test_case3(self):
        print("测试用例3")

    @allure.severity(allure.severity_level.MINOR)
    @allure.story("第四条用例")
    def test_case4(self):
        print("测试用例4")

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("第五条用例")
    def test_case5(self):
        print("测试用例5-阻塞用例")

@allure.feature("结算模块")
class TestB():
    @allure.title("结算模块第一条用例")
    @allure.story("结算模块第一条用例")
    def test_case1(self):
        print("结算模块测试用例1")

    @allure.title("结算模块第二条用例")
    @allure.story("结算模块第二条用例")
    def test_case2(self):
        print("结算模块测试用例2")

@allure.feature("充值模块")
class TestC():

    @allure.title("充值用例")
    def test_case1(self):
        allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)
    def test_case2(self):
        print("测试用例2")
        allure.attach("<body>这是一段htmlbody代码块</body>", "html网页", attachment_type=allure.attachment_type.HTML)

    def test_case3(self):
        print("测试用例3")
        allure.attach.file("1.jpg", name = "这是截图", attachment_type=allure.attachment_type.JPG)

    def test_case4(self):
        print("测试用例4")
        allure.attach.file("jue.mp4", name = "这是一个视频", attachment_type=allure.attachment_type.MP4)

