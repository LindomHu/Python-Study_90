from selenium import webdriver
from time import sleep

driver = webdriver. Firefox()
driver.get('http://www.baidu.com')
driver.implicitly_wait(5)
driver.find_element_by_link_text('新闻').click()
#juBinAll= driver.window_handles
# driver.switch_to.window(juBinAll[0])

driver.find_element_by_partial_link_text('谱写社会主义文化繁荣').click()
sleep(2)
juBinAll= driver.window_handles
driver.switch_to.window(juBinAll[1])
sleep(2)
driver.find_element_by_link_text('历史').click()
juBinAll = driver.window_handles
driver.switch_to.window(juBinAll[2])
sleep(3)
driver.find_element_by_link_text('美丽中国').click()
sleep(2)
juBinAll = driver.window_handles
driver.switch_to.window(juBinAll[0])

driver.find_element_by_link_text('百度首页').click()
# sleep(2)
# driver.quit()






