# 三条测试用例
import pytest


class TestDemo01():
    def test_one(self):
        print("开始执行test_one用例")
        x = "this"
        # assert "h" in x
        pytest.assume("h" not in "x")
        pytest.assume("h" == x)
        pytest.assume("H" in "x")


    def test_two(self):
        print("开始执行test_two用例")
        x = "hello"
        assert "e" in x

    def test_three(self):
        print("开始执行test_three用例")
        x = "hello"
        y = "hello world"
        assert y in x


class TestDemo02():
    def test_a(self):
        print("开始执行test_a用例")
        x = "this"
        assert "s" in x

    def test_b(self):
        print("开始执行test_b用例")
        x = "hello"
        assert "s" in x

    def test_c(self):
        print("开始执行test_c用例")
        x = "hello"
        y = "hello world"
        assert x in y

if __name__ == '__main__':
    # pytest.main("-v -x TestDemo01")
    pytest.main("-v","-s","TestDemo01")