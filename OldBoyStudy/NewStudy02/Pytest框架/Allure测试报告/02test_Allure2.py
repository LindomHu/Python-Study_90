# -*- coding: utf-8 -*-
# @Time : 2021/11/27 22:05
# @Author : huix
# @File : 02test_Allure2.py

import pytest


def test_success():
    """this test success"""
    assert True

def test_failure():
    """this test fails"""
    assert False

def test_skip():
    """this test skip"""
    pytest.skip("for a reason!")

def test_broken():
    raise Exception("exception!")