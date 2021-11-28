

import unittest   #导入
class Animal(unittest.TestCase):
    def setUp(self):
        print('动物出窝了')
    def tearDown(self):
        print('动物回去了')

    def test_dog(self):
        print('wongwongwong')
    def test_cat(self):
        print('mamama')
    def test_duck(self):
        print('gagaga')
    def test_chicken(self):
        print('jijizaza')
if __name__ == '__main__':
    #unittest.main()


    buru = unittest.TestSuite()        #
    buru.addTest(Animal('test_dog'))
    buru.addTest(Animal('test_cat'))

    jiaqin = unittest.TestSuite()
    jiaqin.addTests([Animal('test_duck'),Animal('test_chicken')])

    zhixingQi = unittest.TextTestRunner()
    zhixingQi.run(jiaqin)






