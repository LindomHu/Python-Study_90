from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.implicitly_wait(5)
print(time.time())
time = time.strftime('%Y%m%d%H%M%S')
path = './picture/pic' + str(time)+ '.png'
driver.get_screenshot_as_file(path)
