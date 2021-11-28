from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://web2.qq.com/')
driver.implicitly_wait(5)
jubin1 = driver.current_window_handle
print(jubin1)
# biaodan = driver.find_element_by_xpath('//div[@class_name = "login-pane show"]/ifrme')
# driver.switch_to.frame('biaodan')
# sleep(3)
driver.switch_to.frame('ptlogin')
driver.find_element_by_link_text('QQ手机版').click()
jubinAll= driver.window_handles
print(jubinAll)


# for i in range(0,3):
driver.switch_to.window(jubinAll[1])
    # sleep(3)
    # driver.switch_to.window(jubinAll[1])
driver.find_element_by_link_text('功能介绍').click()
sleep(3)


driver.quit()