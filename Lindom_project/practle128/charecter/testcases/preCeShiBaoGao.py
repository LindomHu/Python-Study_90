import unittest
from HTMLTestRunner import HTMLTestRunner

class people(unittest.TestCase):
    def test_kids(self):
        print("我六岁")

    def test_grandma(self):
        print("我60了")

if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(people("test_kids"))

    # 定义生成测试报告的执行器,wb: write binary
    report = open(r"C:\python34\practle128\class128\report\111.html","wb")
    runner = HTMLTestRunner(stream = report,title="我在测试人类的年纪",description="现在测试小孩的年纪")
    runner.run(suite)