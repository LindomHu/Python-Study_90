from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
# driver.implicitly_wait(5)
# driver.set_window_size(300,500)     #调整窗口大小
# sleep(3)
# driver.maximize_window()            #最大化
# driver.refresh()                   #刷新
# driver.get('http://www.qq.com')
# sleep(3)
# driver.back()                     #返回
# print(driver.title)               #打印标题
# print(driver.current_url)         #打印当前的url



# driver.quit()
#截图

# driver.get_screenshot_as_file(r'C:\python34\practle128\picture\tupianl.jpg')
# driver.get('http://www.qq.com')
# driver.get_screenshot_as_file('./picture/tupian2.jpg')
driver.find_element_by_id('kw').send_keys('苹果')
driver.find_element_by_id('su').click()
sleep(3)
if driver.title == '苹果_百度搜索':
    print('欢迎来到苹果搜索界面' )
    driver.get_screenshot_as_file('./picture/tuppingguo.jpg')
    driver.back()
    if driver.title == '百度一下，你就知道':
        print('截图成功')
else:
    print('未到达苹果搜索界面')







