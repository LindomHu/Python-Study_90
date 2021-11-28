# from selenium import webdriver
# from time import sleep
# driver = webdriver.Firefox()
# driver.implicitly_wait(3)
# driver.get('file:///C:/Admin/Desktop/teacher-03/jingGao.html')
# driver.find_element_by_id('jingGao1').click()
# sleep(3)
# driver.switch_to.alert.accept()
#
# driver.find_element_by_id('jingGao2').click()
# sleep(3)
# driver.switch_to.alert.dismiss()
#
# driver.find_element_by_id('jingGao3').click()
# sleep(3)
# driver.switch_to.alert.send_keys('警告框输入，Null')
# sleep(3)
# driver.switch_to.alert.dismiss()
#
# driver.quit()


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random


driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get('http://www.baidu.com')

shenZhi = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(shenZhi).perform()
driver.find_element_by_xpath('.//*[@id="wrapper"]/div[6]/a[1]').click()
xiaLa = driver.find_element_by_xpath(".//*[@id='nr']")
sleep(2)
random_nb = random.randint(1,3)
sleep(2)
Select(xiaLa).select_by_index(random_nb)
a = Select(xiaLa).first_selected_option.text
print('\033[42;1m%r\033[0m'%a)
#保存设置
driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").send_keys(Keys.ENTER)
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
driver.close()





