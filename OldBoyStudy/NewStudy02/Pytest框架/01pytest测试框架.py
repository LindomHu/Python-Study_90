# -*- coding: utf-8 -*-
# @Time : 2021/11/22 23:16
# @Author : huix
# @File : 01pytest测试框架.py

"""
pytest是一个非常成熟的全功能的python测试框架

-优点：
>> 简单灵活，容易上手
>> 支持参数化
>> 测试用例的skip和xfail，自动失败重试等处理
>> 能支持简单的单元测试和复杂的功能测试，还可以结合selenium/appium等自动化测试、接口口自动化测试（pytest+request）
>> 具有很多第三方插件，并且可以自定义扩展，比较好用的的如pytest-allure（完美html测试报告），pytest-xdist（多cpu分发等）
>> 可以很好的和jenkins集成。

-文档：https://docs.pytest.org/en/latest/contents.html#toc
-第三方库：http://pypi.org/search/?q=pytest

-pytest安装与依赖
* pip install -U pytest U    表示升级
* pip install pytest-sugar=
* pip install pytest-rerunfailures
* pip install pytest-xdist
* pip install pytest-assume
* pip install pytest-html

* pip list  查看
* pip -h    帮助


-测试文件
* test_*.py
* *_test.py

-用例识别
* Test*类包含的所有的test_*的方法（测试类不能带有_init_方法）
* 不在class中的所有的test_*方法

-pytest也可以执行unitest框架写的测试用例和方法

-常用的参数
* pytest -v 03test_pytest_test.py    打印用例运行的详细日志
* pytest -v -s 03test_pytest_test.py  带上控制台日志打印
* pytest -v -s 03test_pytest_test.py::TestDemo02    如果有多个类，指定执行TestDemo02这个类
* pytest 03test_pytest_test.py -k "TestDemo01 and not test_two"   跳过TestDemo01类中test_two用例
* pytest -x 03test_pytest_test.py   一旦运行到报错就停止运行
* pytest 03test_pytest_test.py --maxfail=[num]     当运行错误达到num的时候就停止运行

"""

"""
场景：测试失败时需要重新运行n次（bug或问题重现），要在重新运行之间添加延迟时间，间隔n秒再运行
安装：pip install pytest-rerunfailures
执行：
* putest --reruns 3 -v -s 03test_pytest_test.py   测试失败时需要重新运行3次   
* pytest -v --reruns 5 --reruns-delay 1    测试失败时需要重新运行5次，每条运行后间隔1秒

"""

"""
场景：一个方法中写了多条断言，通常第一条过不去，下面就不执行了。我们想报错也都执行一下

安装：pip install pytest-assume
执行：
* pytest.assume(1==4)
* pytest.assume(2==4)
"""
"""

pytest在pycharm里面运行，设置里面搜索"pytest"，将测试框架选择成pytest即可

pytest执行的优先级（）执行顺序：
模块级（module）>函数级（function）>类级（class）>方法级（method）>类里面的（setup/teardown）运行在调用方法的前后

"""

