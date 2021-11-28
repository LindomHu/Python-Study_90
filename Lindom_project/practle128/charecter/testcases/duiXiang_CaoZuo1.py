
from selenium import webdriver
from time import sleep
import time

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get('http://localhost/ranzhi/www')
udL1 = ['apple','pear','admin','huhuixiang']
udL2 = ['123','123','123','1234567891']
for i in range(0,4,1):
    driver.refresh()

    driver.find_element_by_id('account').send_keys(udL1[i])
    driver.find_element_by_id('password').send_keys(udL2[i])
    driver.find_element_by_id('submit').click()
    sleep(2)
    T = driver.title
    if T == '然之协同':
        print('第%r次登陆成功，欢迎来到\033[42;1m%r\033[0m'%((i+1),T))
        driver.find_element_by_id("start").click()
        sleep(1)
        driver.find_element_by_link_text("退出").click()

    else:
        text = driver.find_element_by_xpath("html/body/div[2]/div/div/div[1]/div").text
        aaa = time.strftime('%Y%m%d%H%M%S')
        path = '../picture/pic' + str(aaa) + '.png'
        driver.get_screenshot_as_file(path)
        sleep(1)
        print(print('第%r次登录失败，错误提示为：%r' %(i + 1,text)))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/button").click()
driver.quit()



