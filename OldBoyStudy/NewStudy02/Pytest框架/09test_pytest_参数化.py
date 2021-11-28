# -*- coding: utf-8 -*-
# @Time : 2021/11/27 15:02
# @Author : huix
# @File : 09test_pytest_参数化.py


# class TestClassDemo():
#     def test_data1(self):
#         a = 10
#         b = 20
#         print(a + b)
#
#     def test_data2(self):
#         a = 11
#         b = 20
#         print(a + b)
#
#     def test_data3(self):
#         a = 1
#         b = 20
#         print(a + b)

# 使用pytest参数化
import pytest
import yaml


class TestClassDemo():
    @pytest.mark.parametrize(("a","b"),[(10,20),(11,20),(1,20)])
    def test_data(self,a,b):
        print(a + b)

# 使用Yaml方式传参
class TestClassDemo1():
    @pytest.mark.parametrize(("x","y"),yaml.safe_load(open("./data.yaml")))
    def test_data1(self,x,y):
        print(x + y)