# 【作业】登录然之--点击CRM（电话标志）--点击联系人--点击添加联系人
# （所属客户选新增，所有下拉框随机选）--填写各个字段（姓名，客户，邮箱，电话不能重复）
# --点击保存--退出--关闭浏览器
# 验证点：
# 1. 点击登录之后，验证已经成功登陆，登录不成功截图
# 2. 点击保存后，验证记录是否保存成功，保存不成功也需要截图

from selenium import webdriver
from time import sleep
import time
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.implicitly_wait(5)
# driver.get('http://localhost:805/ranzhi/www')
driver.get("http://demo.ranzhi.org/sys/index.php?m=user&f=login&referer=L3N5cy9pbmRleC5waHA=")

# driver.find_element_by_id("account").clear()
# driver.find_element_by_id("account").send_keys("huhuixiang")
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("1234567891")
driver.find_element_by_id("submit").click()
sleep(2)
title = driver.title

if title == '然之协同':
    print('登录成功，欢迎来到\033[42;1m%s\033[0m'%title)       #打印然之协同的欢迎标题

    driver.find_element_by_xpath(".//*[@id='s-menu-1']/button").click()    #点击客户管理

    driver.switch_to.frame("iframe-1")    #跳进客户管理的表单
    sleep(1)
    # driver.find_element_by_xpath(".//*[@id='mainNavbar']/div[2]/ul/li[5]/a").click()
    driver.find_element_by_xpath(".//*[@id='mainNavbar']/ul/li[6]/a").click()    #点击联系人
    for i in range(1, 6, 1):
        driver.find_element_by_xpath(".//*[@id='menuActions']/a").click()
        time_now = time.strftime("%Y%m%d%H%M%S")
        realName = "张总" + str(time_now)

        driver.find_element_by_id("realname").clear()
        driver.find_element_by_id("realname").send_keys(realName)
        customerName = "daKeHu" + str(time_now)
        driver.find_element_by_id("newCustomer").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(customerName)
        sex_Option = ['genderm','genderf']
        Option = random.choice(sex_Option)
        driver.find_element_by_id(Option).click()

        driver.find_element_by_id("dept").clear()
        driver.find_element_by_id("dept").send_keys("IT")
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("test")
        driver.find_element_by_id("join").clear()
        driver.find_element_by_id("join").send_keys("20180304")
        Email = '88' + str(time_now)[10:14] + '@qq.com'
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(Email)
        telNumber = "135" + str(time_now)[6:14]
        driver.find_element_by_id("mobile").clear()
        driver.find_element_by_id("mobile").send_keys(telNumber)
        phoneNumber = '88' + str(time_now)[9:14]
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys(phoneNumber)
        driver.find_element_by_id("fax").clear()
        driver.find_element_by_id("fax").send_keys(phoneNumber)
        QQ = '88' + str(time_now)[10:14]
        driver.find_element_by_id("qq").clear()
        driver.find_element_by_id("qq").send_keys(QQ)

        type1 = driver.find_elements_by_xpath(".//*[@id='type']/option")
        option_number1 = len(type1)
        number1 = random.randint(1,option_number1 - 1 )
        Select(driver.find_element_by_id("type")).select_by_index(number1)

        type2 = driver.find_elements_by_xpath(".//*[@id='size']/option")
        option_number2 = len(type2)
        number2 = random.randint(1, option_number2 - 1 )
        Select(driver.find_element_by_id("size")).select_by_index(number2)

        type3 = driver.find_elements_by_xpath(".//*[@id='status']/option")
        option_number3 = len(type3)
        number3 = random.randint(1, option_number3 - 1)
        Select(driver.find_element_by_id("status")).select_by_index(number3)

        type4 = driver.find_elements_by_xpath(".//*[@id='level']/option")
        option_number4 = len(type4)
        number4 = random.randint(1, option_number4 - 1)
        Select(driver.find_element_by_id("level")).select_by_index(number4)
        driver.find_element_by_id("desc").clear()
        driver.find_element_by_id("desc").send_keys(u"添加重要级别联系人")

        driver.find_element_by_id('submit').click()
        sleep(3)
        title2 = driver.title
        if title2 == '联系人列表 - 然之协同':
            print('The contact is saved \033[31;1msuccessfully.\033[0m')
            sleep(2)
        else:
            aaa = time.strftime('%Y%m%d%H%M%S')
            Screenshot = '../picture/pic' + str(aaa) + '.png'
            driver.get_screenshot_as_file(Screenshot)
            print('The contacts is saved \033[033;471m failed.\033[0m,please anew Operate')
            break
        sleep(2)

else:
    text1 = driver.find_element_by_xpath("html/body/div[2]/div/div/div[1]/div").text
    aaa = time.strftime('%Y%m%d%H%M%S')
    path = '../picture/pic' + str(aaa) + '.png'
    driver.get_screenshot_as_file(path)
    sleep(1)
    print(print('登录失败，错误提示为：\033[37;1m%r\033[0m' % text1))
    driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/button").click()
driver.quit()