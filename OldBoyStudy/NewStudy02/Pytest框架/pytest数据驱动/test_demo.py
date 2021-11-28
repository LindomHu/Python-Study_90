# -*- coding: utf-8 -*-
# @Time : 2021/11/27 15:32
# @Author : huix
# @File : test_demo.py
import pytest
import yaml

class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的IP是",env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的IP是",env["dev"])
