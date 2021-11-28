#href="http://im.qq.com/mobileqq/#from=login

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.implicitly_wait(5)
# driver.get('http://web2.qq.com/')
driver.get('https://mail.qq.com')
# bd = driver.find_element_by_xpath('//div[@class = "login_container"]/iframe')
driver.switch_to.frame('login_frame')
# sleep(3)
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('1289608932')
driver.find_element_by_id('p').send_keys('HVTV2008ang1103')
# driver.switch_to.default_content()
# driver.find_element_by_link_text('基本版').click()
driver.find_element_by_id("login_button").click()
sleep(3)

# driver.quit()



