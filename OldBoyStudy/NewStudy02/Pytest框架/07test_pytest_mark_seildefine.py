# -*- coding: utf-8 -*-
# @Time : 2021/11/23 23:19
# @Author : huix
# @File : 07test_pytest_mark_seildefine.py

# mark  自定义标注
# 标注某些是android特有的用例，哪些是iOS特有的用例
# 可以标注模块的类别

import pytest

@pytest.mark.search()
def test_search01():
    print("test_search01")
    raise NameError
    pass

@pytest.mark.search()
def test_search02():
    print("test_search02")
    # raise NameError
    pass

@pytest.mark.search()
def test_search03():
    print("test_search03")
    # raise NameError
    pass

@pytest.mark.login()
def test_login01():
    print("test_login01")
    raise NameError
    pass

@pytest.mark.login()
def test_login02():
    print("test_login02")
    # raise NameError
    pass

@pytest.mark.login()
def test_login02():
    print("test_login02")
    # raise NameError
    pass

# 标注后  可以指定执行某个类别
# pytest -v 07test_pytest_mark_seildefine.py -m search
# pytest -v 07test_pytest_mark_seildefine.py -m login