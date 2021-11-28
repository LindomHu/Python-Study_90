from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get('file:///C:/Admin/Desktop/select_flower.html')
#driver.find_element_by_id('huahua').click()
xiala = driver.find_element_by_id('huahua')
# sleep(2)
# Select(xiala).select_by_index(2)          #通过下标选择下拉框
# xiala = driver.find_element_by_id('huahua')
# sleep(2)
# Select(xiala).select_by_value('baihehua')    #通过vulue属性选择下拉框
# xiala = driver.find_element_by_id('huahua')
# sleep(2)
# Select(xiala).select_by_visible_text('菊花')  #通过文本选择下拉框
#
# a = Select(xiala).first_selected_option.text    #获取当前选择的文本内容
# print(a)

for i in range(0,6,1):
    random_number = random.randint(1, 3)
    sleep(2)
    Select(xiala).select_by_index(random_number)
    a = Select(xiala).first_selected_option.text
    print(a)
