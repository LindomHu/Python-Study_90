
#多个对象定位(需要找到共同属性)
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')
# lianjie = driver.find_elements_by_class_name('mnav')
# number = len(lianjie)
# # print(number)
# for i in range(0,number):
#     print(lianjie[i].text)
#driver.quit()

# lianjie1 = driver.find_elements_by_xpath(".//*[@id='u1']/a")
# number = len(lianjie1)
# print(number)
# for i in range(0,number,1):
#
#     print(lianjie1[i].text)
#driver.quit()


driver.find_element_by_link_text('新闻').click()
lianjie2 = driver.find_elements_by_xpath(".//*[@id='pane-news']/div/ul/li/strong/a")
number = len(lianjie2)
print(number)
for i in range(0,number,1):
    print('\033[35;1m %r \033[0m' %lianjie2[i].text)
driver.quit()

