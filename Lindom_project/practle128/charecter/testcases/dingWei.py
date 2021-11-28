# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.get('http://www.thepaper.cn')
# driver.find_element_by_id('search-key').send_keys('新闻').click()
# driver.find_element_by_name('新闻').click()
# driver.find_element_by_partial_link_text('自行车').click()
# # driver.find_element_by_link_text('工信部：确保取消流量“漫游”费7月1日如期兑现').click()

from selenium import webdriver        #导入webdriver 它就是selenium 的一个工具

driver = webdriver.Firefox()           #打开火狐浏览器
driver.implicitly_wait(5)             #隐形等待 100 秒（以秒为单位）
driver.get('http://localhost/ranzhi/www')    # 打开然之网址
driver.find_element_by_xpath('//tbody/tr/td/input').send_keys('huhuixiang') #用 xpath定位，相对定位输入用户名
# driver.find_element_by_id('account').send_keys('huhuixiang')       #用ID定位

# driver.find_element_by_name('password').send_keys('1234567891')    #用name定位
driver.find_element_by_xpath('//tbody/tr/td/input[@name="password"]').send_keys('1234567891')
driver.find_element_by_xpath('//tr/td/input[@id="submit"]').click()      # @指定属性

driver.find_element_by_xpath('//div/button[@id="start"]').click()
# driver.find_element_by_id('start').click()
#driver.find_element_by_partial_link_text('退出').click()
driver.find_element_by_xpath('//ul/li/*[@href="/ranzhi/www/sys/user-logout.html"]').click()

driver.close()


