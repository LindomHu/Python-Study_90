from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.implicitly_wait(5)
sheZhi_link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(sheZhi_link).perform()        #鼠标悬浮
ActionChains(driver).context_click(sheZhi_link).perform()          #单击点击设置

element = driver.find_element_by_id('假设的对象')
ActionChains(driver).double_click(element).perform()                #双击

element_a = driver.find_element_by_id('假设的对象')
element_b = driver.find_element_by_id('假设的对象')
ActionChains(driver).drag_and_drop(element_a,element_b).perform()    #拖放
ActionChains(driver).click_and_hold(element).perform()        #点住某对象并且不释放鼠标
ActionChains(driver).release(element_b).perform()             #释放鼠标
#鼠标拖动（链式写法）
ActionChains(driver).click_and_hold(element_a).move_to_element(element_b).release().perform()
































