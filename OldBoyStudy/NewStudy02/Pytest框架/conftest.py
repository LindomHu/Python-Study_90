# -*- coding: utf-8 -*-
# @Time : 2021/11/23 21:16
# @Author : huix
# @File : conftest.py
import pytest

# 测试用例执行时，有的用例需要登陆执行，偶的不需要登陆执行，setup/teardown无法满足。fixture可以。
# conftest模块里面封装公共调用的函数或者方法，当系统执行到参数时先从文件中查找是否有这个名字的变量，之后在conftest.py中找是否有

"""
conftest.py配置需要注意的地方：
    1 conftest文件名时不能换的
    2 conftest.py与运行的用例要在同一个package下，并且有_init_.py文件
    3 不需要import导入conftest.py，pytest用例会自动查找
    4 全局的配置和前期工作都可以写在这里，放在某个包下，就是这个包数据共享的地方

"""
# scope=function
@pytest.fixture()
def login():
    print("这是一个登陆方法")

# 这个函数用于解决自定义mark保warning的错误
def pytest_configure(config):
    # 标签集合
    marker_list = ["search","login"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers",markers
        )

