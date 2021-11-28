from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://web2.qq.com/')
driver.implicitly_wait(8)
# biaodan = driver.find_element_by_xpath('//div[@class_name = "login-pane show"]/ifrme')
# driver.switch_to.frame('biaodan')
# sleep(3)
driver.switch_to.frame('ptlogin')       #切换表单，括号里面的是 id 或者 name
driver.find_element_by_link_text('QQ手机版').click()








