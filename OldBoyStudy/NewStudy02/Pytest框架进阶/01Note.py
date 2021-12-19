# -*- coding: utf-8 -*-
# @Time : 2021/11/30 00:09
# @Author : huix
# @File : 01Note.py



"""
常用参数
- pytest -k 'add' -v
- pytest -k 'add or div' -v   收集包含"add或div"的用例并执行（满足表达式的）
- pytest --collect-only     只收集不执行

- pytest -m P0      只执行加上了P0标签的用例  @pytest.mark(P0)
- pytest -m P1     只执行加上了P1标签的用例  @pytest.mark(P1)

- pytest --junit-xml=./result  生成一个执行结果的xml文件


"""