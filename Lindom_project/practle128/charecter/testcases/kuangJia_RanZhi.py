
#导入模块、工具、函数
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from time import sleep
import time
import random
from selenium.webdriver.support.select import Select

class RanZhi(unittest.TestCase):             #定义一个然之的类
    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        self.driver = driver
        time_now = time.strftime("%Y%m%d%H%M%S")
        # print(time_now)
        realName = "xiaoHong" + str(time_now)
        self.realName = realName
        customerName = "daKeHu" + str(time_now)
        self.customerName = customerName
        telNumber = "135" + str(time_now)[6:14]
        self.telNumber = telNumber
        phoneNumber = "88"+str(time_now)[9:14]
        self.phoneNumber = phoneNumber
        Email = '88' + str(time_now)[10:14] + '@qq.com'
        self.Email = Email
        QQ = '88' + str(time_now)[10:14]
        self.QQ = QQ
        driver.get('http://localhost:805/ranzhi/www')

        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("huhuixiang")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1234567891")
        driver.find_element_by_id("submit").click()
        sleep(2)
        T1 = driver.title
        if T1 == '然之协同':
            print('登陆成功，欢迎来到\033[42;1m%r\033[0m' % T1)

            driver.find_element_by_xpath(".//*[@id='s-menu-1']/button").click()
            sleep(1)
            driver.switch_to.frame('iframe-1')
            sleep(1)
            driver.find_element_by_xpath(".//*[@id='mainNavbar']/div[2]/ul/li[5]/a").click()

        else:
            text1 = driver.find_element_by_xpath("html/body/div[2]/div/div/div[1]/div").text
            aaa = time.strftime('%Y%m%d%H%M%S')
            path = '../picture/pic' + str(aaa) + '.png'
            driver.get_screenshot_as_file(path)
            sleep(1)
            print(print('登录失败，错误提示为：%r' % text1))
            driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/button").click()

    def tearDown(self):
        driver = self.driver
        driver.quit()

    def test_addContact(self):
        driver = self.driver
        print('这里放置添加联系人脚本')
        driver.find_element_by_xpath(".//*[@id='menuActions']/a").click()
        driver.find_element_by_id("realname").clear()
        realName = self.realName
        driver.find_element_by_id("realname").send_keys(realName)
        driver.find_element_by_id("newCustomer").click()
        driver.find_element_by_id("name").clear()
        customerName = self.realName
        driver.find_element_by_id("name").send_keys(customerName)
        sex_Option = ['gender1','gender2']
        Option = random.choice(sex_Option)
        driver.find_element_by_id(Option).click()

        driver.find_element_by_xpath(".//*[@id='contactForm']/div/div/table/tbody/tr[3]/td/label").click()
        driver.find_element_by_id("dept").click()
        driver.find_element_by_id("dept").clear()
        driver.find_element_by_id("dept").send_keys("12345")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("IT")
        driver.find_element_by_id("join").clear()
        driver.find_element_by_id("join").send_keys("20180304")
        driver.find_element_by_id("desc").clear()
        driver.find_element_by_id("desc").send_keys(u"中觉得好的话")
        driver.find_element_by_id("email").clear()
        Email = self.Email
        driver.find_element_by_id("email").send_keys(Email)

        driver.find_element_by_id("mobile").clear()
        telNumber = self.telNumber
        driver.find_element_by_id("mobile").send_keys(telNumber)
        driver.find_element_by_id("phone").clear()
        phoneNumber = self.phoneNumber
        driver.find_element_by_id("phone").send_keys(phoneNumber)
        driver.find_element_by_id("fax").clear()
        telNumber = self.telNumber
        driver.find_element_by_id("fax").send_keys(telNumber)
        driver.find_element_by_id("qq").clear()
        QQ = self.QQ
        driver.find_element_by_id("qq").send_keys(QQ)

        type1 = driver.find_elements_by_xpath(".//*[@id='type']/option")
        option_number1 = len(type1)
        # 产生随机数
        number1 = random.randint(1, option_number1 - 1)
        # 随机选择下拉框的值
        Select(driver.find_element_by_id("type")).select_by_index(number1)

        type2 = driver.find_elements_by_xpath(".//*[@id='size']/option")
        option_number2 = len(type2)
        # 产生随机数
        number2 = random.randint(1, option_number2 - 1)
        # 随机选择下拉框的值
        Select(driver.find_element_by_id("size")).select_by_index(number2)

        type3 = driver.find_elements_by_xpath(".//*[@id='status']/option")
        option_number3= len(type3)
        # 产生随机数
        number3 = random.randint(1, option_number3 - 1)
        # 随机选择下拉框的值
        Select(driver.find_element_by_id("status")).select_by_index(number3)

        type4 = driver.find_elements_by_xpath(".//*[@id='level']/option")
        option_number4 = len(type4)
        # 产生随机数
        number4 = random.randint(1, option_number4 - 1)
        # 随机选择下拉框的值
        Select(driver.find_element_by_id("level")).select_by_index(number4)

        driver.find_element_by_id("submit").click()
        sleep(2)

        T2 = driver.current_url
        if T2 == 'http://localhost/ranzhi/www/crm/contact-browse.html':
            sleep(2)
            print('\033[31;1m 联系人保存成功 \033[0m' )
            driver.switch_to.default_content()
            driver.find_element_by_id("start").click()
            driver.find_element_by_link_text(u"退出").click()
        else:
            # text2 = driver.find_element_by_xpath(".//*[@id='submit']").text
            aaa = time.strftime('%Y%m%d%H%M%S')
            path = '../picture/pic' + str(aaa) + '.png'
            driver.get_screenshot_as_file(path)
            sleep(2)
            print(print('联系人保存失败，请重新添加'))

    def test_deleteContact(self):
        driver = self.driver
        print('这里放置删除联系人的脚本')
        jiLu = (driver.find_elements_by_xpath(".//*[@id='contactList']/tbody/tr"))
        nB = len(jiLu)
        if nB > 0:
            for i in range(0, nB):
                driver.find_element_by_link_text("更多").click()
                driver.find_element_by_link_text("删除").click()
                driver.switch_to.alert.accept()
                print('联系人第%r次删除成功'%(i+1))
                sleep(1)
        else:
            print('当前页面无记录,无法删除')

if __name__ == "__main__":
    suite_lianXiRen = unittest.TestSuite()
    suite_lianXiRen.addTest(RanZhi("test_addContact"))
    suite_lianXiRen.addTest(RanZhi('test_deleteContact'))

    fp = open(r'C:\python34\practle128\class128\report\123.html','wb')
    runner = HTMLTestRunner(stream=fp, title="测试然之", description="现在测试然之联系人模块")
    runner.run(suite_lianXiRen)



