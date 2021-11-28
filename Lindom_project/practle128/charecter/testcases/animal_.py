# step 1：导入unittest
import unittest


# step 2: 继承TestCase
class Animal(unittest.TestCase):
    # 在每一个方法执行前自动运行
    def setUp(self):
        print("动物出窝了")

    # 在每一个方法执行后自动运行
    def tearDown(self):
        print("动物回去了")

    # step 3:定义以test开头的方法
    def test_dog(self):
        print("汪汪汪")

    def test_cat(self):
        print("喵喵喵")

    def test_duck(self):
        print("嘎嘎嘎")

    def test_chicken(self):
        print("叽叽喳喳")


if __name__ == "__main__":
    # 执行所有的方法:执行顺序是先数字，再大写，再小写
    # unittest.main()

    # 构建testsuite（测试套件），并且取名叫buRu
    buRu = unittest.TestSuite()
    # 往套件内添加测试用例
    buRu.addTest(Animal("test_dog"))
    buRu.addTest(Animal("test_cat"))

    jiaQin = unittest.TestSuite()
    jiaQin.addTests([Animal("test_duck"), Animal("test_chicken")])

    # 定义一个执行器,并且取名叫zhiXingQi
    zhiXingQi = unittest.TextTestRunner()

    # 执行用例
    zhiXingQi.run(jiaQin)


