from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.implicitly_wait(3)
# driver.find_element_by_id('kw').send_keys('happy',Keys.ENTER.keys.CONTROL+'a')

baidutupian = driver.find_element_by_xpath('.//*[@id="lg"]/map/area')
ActionChains(driver).context_click(baidutupian).send_keys(Keys.DOWN*7,Keys.ENTER).perform()
driver.find_element_by_xpath(".//*[@id='kw']").send_keys(Keys.CONTROL+'v')
driver.find_element_by_xpath('.//*[@id="su"]').click()






