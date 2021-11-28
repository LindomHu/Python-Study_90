# from selenium import webdriver

# driver = webdriver.Firefox()
# driver.implicitly_wait(5)
# driver.get('http:/www.baidu.com')
# size = driver.find_element_by_id('kw').size     #获取大小
# print(size)
# anNiu = driver.find_element_by_id('su')          #获取对象的属性
# print(anNiu.get_attribute('value'))
# text = driver.find_element_by_link_text('hao123').text    #获取文本
# print(text)
# a = driver.find_element_by_link_text('新闻').is_displayed()
# print(a)                                           #判断一个对象是否显示（显示：Ture，不显示：Fualse）


from selenium import webdriver
import time
from time import sleep
driver=webdriver.Firefox()
driver.implicitly_wait(5)
driver.get('http://127.0.0.1/ranzhi/www/')
array1=['Apple','Pear','admin']
array2=['123','123','123456']
for i in range(0,3,1):
    driver.refresh()
    driver.find_element_by_id('account').send_keys(array1[i])
    driver.find_element_by_id('password').send_keys(array2[i])
    driver.find_element_by_id('submit').click()
    sleep(5)
    title=driver.title
    if title=='然之协同':
        print('登录成功')
        driver.find_element_by_id('start').click()
        driver.find_element_by_xpath("//a[@href='/ranzhi/www/sys/user-logout.html']").click()
    else:
        text = driver.find_element_by_xpath("html/body/div[2]/div/div/div[1]/div").text
        print(text)
        t = time.strftime('%Y%m%d%H%M%S')
        picture = './picture/' + str(t) + '.jpg'
        driver.get_screenshot_as_file(picture)
        driver.find_element_by_xpath("//div[@class='modal-footer']/button[@class='btn btn-primary']").click()







