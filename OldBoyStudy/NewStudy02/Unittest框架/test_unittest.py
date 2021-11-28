# -*- coding: utf-8 -*-
# @Time : 2021/11/21 23:30
# @Author : huix
# @File : test_unittest.py
import unittest

class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")
    # setupclass teardownclass作用于demo的整个class类

    def setUp(self) -> None:
        print("setup")
    # 测试开始前调用，例如登陆前

    def tearDown(self) -> None:
        print("teardown")
    # 测试结束后调用，比如关掉数据库的连接

    def test_case01(self):
        print("test01")
        self.assertEqual(2,2,"判断相等")
        self.assertIn("h","this")

    def test_case02(self):
        print("test02")
        self.assertEqual(1,1,"判断相等")

    # 跳过测试用例
    # @unittest.skip
    @unittest.skipIf(1+1==2,"满足1+1=2跳过测试用例")
    def test_case03(self):
        print("test03")
        self.assertEqual(2,3,"判断相等")


class demo1(unittest.TestCase):
    def test_demo1_case01(self):
        print("test demo1 test01")

    def test_demo1_case02(self):
        print("test demo01 test02")


class demo2(unittest.TestCase):
    def test_demo1_case01(self):
        print("test demo2 test01")

    def test_demo1_case02(self):
        print("test demo02 test02")

if __name__=="__main__":
    # 执行方法一
    # main()会运行所有的test开头的测试用例
    # unittest.main()

    # 执行方法二
    # 可以利用测试套件添加哪些需要执行的测试用例进行执行

    # suite = unittest.TestSuite()
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_demo1_case01"))
    #
    # unittest.TextTestRunner().run(suite)

    # 执行方法三
    # 执行多个类(多个套件)

    suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(demo2)
    suiteall = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner().run(suiteall)