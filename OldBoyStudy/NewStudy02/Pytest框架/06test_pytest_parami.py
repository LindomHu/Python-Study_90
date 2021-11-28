# -*- coding: utf-8 -*-
# @Time : 2021/11/23 21:58
# @Author : huix
# @File : 06test_pytest_parami.py


# 参数传递
import pytest
import sys

"""
- 参数化，前两个变量，后面是对应的数据
- 3+5——>test_input   8——>expect
"""

# test_input == expected  应用场景：测试搜索框
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+5",7),("7*5",30)])
def test_p(test_input,expected):
    # eval  将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == expected

# 参数组合
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,10,12])
def test_p1(x,y):
    print(f"测试数据组合x:{x},y:{y}")


# 方法名作为参数
test_user_data = ["Tome","Jerry"]
@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收并传入的参数
    user = request.param
    print(f"\n 打开登陆的首页，登陆用户:{user}")
    return user

@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""

# @ fixture.skip  跳过执行测试用例
@pytest.mark.skip("此次测试不执行登陆")

@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login1(login_r):
    b = login_r
    print(f"测试用例中login的返回值：{b}")
    assert b != ""


# @ fixture.skip  指定跳过不在什么平台上执行 根据自己的需要来指定
@pytest.mark.skipif(sys.platform == "darwin", reason="此次测试不在mac上执行登陆")

@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login2(login_r):
    c = login_r
    print(f"测试用例中login的返回值：{c}")
    assert c != ""

# xfail   标记测试用例，即使这条用例会运行不通过或者通过
# 标注功能测试尚未实现或不过尚未修复的错误，希望测试由于某种情况下就应该失败
@pytest.mark.xfail
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login3(login_r):
    d = login_r
    print(f"测试用例中login的返回值：{d}")
    assert d != ""
    raise NameError