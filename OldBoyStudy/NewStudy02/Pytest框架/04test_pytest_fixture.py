# -*- coding: utf-8 -*-
# @Time : 2021/11/23 21:04
# @Author : huix
# @File : 04test_pytest_fixture.py

import pytest


def test_case1(login):
    print("test_case1，要登陆")
    pass

def test_case2():
    print("test_case2,不要登陆")
    pass

def test_case3(login):
    print("test_case3，需要登陆")
    pass

if __name__ == '__main__':
    pytest.main()