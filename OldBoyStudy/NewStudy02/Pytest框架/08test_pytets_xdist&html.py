# -*- coding: utf-8 -*-
# @Time : 2021/11/23 23:43
# @Author : huix
# @File : 08test_pytets_xdist&html.py


# 并发执行测试用例
# 安装xdist
# pip install pytest-xdist

# 执行：pytest 07test_pytest_mark_seildefine.py -n 3


# pytest-html生成测试报告
# 安装html
# pip install pytest-html

# 生成测试报告：pytest -v -s --html=report.html --self-contained-html