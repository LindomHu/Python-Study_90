
from caculator128 import *         #导入被测的桩
import unittest

class TestCaculator128(unittest.TestCase):   #def  定义一个类
    def setUp(self):
        print('test begain')

    def tearDown(self):
        print('test end')

    def test_jia2(self):
        # 连接数据库
        # 。。。。。。
        pass

    def test_jia(self):            #def  定义一个函数
        cal = Caculator128()      #实例化
        result = cal.jia(10,10)  #等号左边赋值，右边调用
        if result == 20:
            print('jia test pass')
        else:
            print('test fail,result is not 20.is %r'%result)

    def test_jian(self):
        cal = cacuLator128()      #实例化
        result = cal.jian(20,10)  #等号左边赋值，右边调用
        if result == 10:
            print('jian test pass')
        else:
            print('test fail,result is not 10.is %r'%result)

    def test_chu(self):
        cal = cacuLator128()  # 实例化
        result = cal.chu(30, 0)  # 等号左边赋值，右边调用
        if result == 3:
            print('chu test pass')
        else:
            print('test fail,result is not 3.is %r' % result)

if __name__ == '__main__':
    # TestCaculator128().test_jia()
    # TestCaculator128().test_jian()
    # TestCaculator128().test_chu()
    ABC =  unittest.TestSuite()
    ABC.addTests([TestCaculator128('test_jia'),TestCaculator128('test_jian'),
                                  TestCaculator128('test_chu')])
    zhixingQi = unittest.TextTestRunner()
    zhixingQi.run(ABC)
    # unittest.main()

