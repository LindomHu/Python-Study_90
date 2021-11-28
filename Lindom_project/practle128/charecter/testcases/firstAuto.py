from selenium import webdriver


driver = webdriver.Firefox()
driver.implicitly_wait(10)                 #隐性等待
# driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('我正在学习自动化')

driver.get( "http://127.0.0.1:805/ranzhi/www")
driver.find_element_by_id("account").clear()
driver.find_element_by_id("account").send_keys("huhuixiang")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("1234567891")
driver.find_element_by_id("submit").click()
driver.find_element_by_id("start").click()
driver.find_element_by_link_text(u"退出").click()



