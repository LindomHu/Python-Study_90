# 登录联系人页面--用脚本自动识别页面上联系人记录总数
# 无记录--脚本输出：当前页面无记录
# 有记录--全部清空
# 1. 清空后验证页面已经没有记录了

from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(5)
time_now =  time.strftime("%Y%m%d%H%M%S")
realName = "xiaoHong"+str(time_now)
customerName = "daKeHu"+str(time_now)
telNumber = "135"+str(time_now)[6:14]
Email = '88'+str(time_now)[10:14]+'@qq.com'
QQ = '88'+str(time_now)[10:14]

# driver.get('http://localhost:805/ranzhi/www')
driver.get("http://demo.ranzhi.org/sys/index.php?m=user&f=login&referer=L3N5cy9pbmRleC5waHA=")
# driver.find_element_by_id("account").clear()
# driver.find_element_by_id("account").send_keys("huhuixiang")
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("1234567891")
driver.find_element_by_id("submit").click()
sleep(2)

T1 = driver.title
if T1 == '然之协同':
    print('登陆成功，欢迎来到\033[42;1m%r\033[0m' %  T1)
    driver.find_element_by_xpath("//li[@id='s-menu-1']/button").click()
    driver.switch_to.frame('iframe-1')
    driver.find_element_by_link_text("联系人").click()
    sleep(3)
    jiLu = (driver.find_elements_by_xpath(".//*[@id='contactList']/tbody/tr"))     #查找编号共同属性赋值给jilu
    nB = len(jiLu)

    if 4 < nB :
        for i in range(0,nB):

            driver.find_element_by_link_text("更多").click()
            driver.find_element_by_link_text("删除").click()
            print('联系人第%r删除成功'%(i+1))
            driver.switch_to.alert.accept()
            sleep(2)

    else:
        print('当前页面无记录,联系人删除0次,请添加再删除')

else:
    text1 = driver.find_element_by_xpath("html/body/div[2]/div/div/div[1]/div").text
    aaa = time.strftime('%Y%m%d%H%M%S')
    path = '../picture/pic' + str(aaa) + '.png'
    driver.get_screenshot_as_file(path)
    sleep(1)
    print(print('登录失败，错误提示为：%r' %  text1))
    driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/button").click()
driver.quit()

