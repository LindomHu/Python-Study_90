# -*- coding: utf-8 -*-
# @Time : 2021/11/23 21:31
# @Author : huix
# @File : 05test_pytest_fixture_yield.py

import pytest

@pytest.fixture(scope="module")
# @pytest.fixture

def open():
    print("打开浏览器")
    yield

    print("执行teardwon")
    print("最后关闭浏览器")


def test_search1(open):
    print("test_serch1")
    raise NameError
    pass

def test_search2(open):
    print("test_serch2")
    pass

def test_search3(open):
    print("test_serch3")
    pass

if __name__ == '__main__':
    pytest.main()