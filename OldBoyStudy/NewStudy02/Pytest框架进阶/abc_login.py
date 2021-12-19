# -*- coding: utf-8 -*-
# @Time : 2021/12/5 22:23
# @Author : huix
# @File : abc_login.py
import pytest

class login():
    def test_login(self):
        # pass
        print("login")

class case():
    def LoginCases1(self):
        def case_a():
            print("LoginCases === case_a")

    def LoginCases2(self):
        def case_b():
            print("LoginCases === case_b")


if __name__ == '__main__':
    pytest.main()