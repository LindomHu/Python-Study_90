from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.implicitly_wait(5)
# driver.get("http://localhost:805/ranzhi/www")
driver.get("http://demo.ranzhi.org/sys/index.php?m=user&f=login&referer=L3N5cy9pbmRleC5waHA=")

# driver.find_element_by_id("account").clear()
# driver.find_element_by_id("account").send_keys("huhuixiang")
# driver.find_element_by_id("password").clear()
# driver.find_element_by_id("password").send_keys("1234567891")
driver.find_element_by_id("submit").click()
time.sleep(3)
title = driver.title
if title == '然之协同':
    print('登陆成功，欢迎进入\033[42;1m%r\033[0m'%title)
    # driver.find_element_by_xpath("//li[@id='s-menu-7']/button").click()
    driver.find_element_by_xpath(".//*[@id='s-menu-2']/button").click()

    # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe-7 | ]]
    driver.switch_to.frame('iframe-2')
    driver.find_element_by_link_text(u"转账").click()

    driver.find_element_by_link_text(u"转账").click()
    payment = driver.find_elements_by_xpath(".//*[@id='payment']/option")
    option_number = len(payment)
    a = random.randint(1,option_number - 1 )
    Select(driver.find_element_by_id("payment")).select_by_index(a)

    receipt = driver.find_elements_by_xpath(".//*[@id='receipt']/option")
    option_number1 = len(receipt)
    b = random.randint(1,option_number1)
    Select(driver.find_element_by_id("receipt")).select_by_index(b)

    driver.find_element_by_id("money").clear()
    driver.find_element_by_id("money").send_keys("10000")
    driver.find_element_by_id("fee").clear()
    driver.find_element_by_id("fee").send_keys("20")

    # ajaxForm = driver.find_elements_by_xpath(".//*[@id='ajaxForm']/table/tbody/tr[8]/td/select/option")
    # option_number3 = len(ajaxForm )
    # d = random.randint(1, option_number3 - 1)
    # Select(driver.find_element_by_id("handlers_chosen")).select_by_index(d)

    driver.find_element_by_id("desc").click()
    driver.find_element_by_id("desc").clear()
    driver.find_element_by_id("desc").send_keys(u"转账")
    driver.find_element_by_id("submit").click()
    Select(driver.find_element_by_id("receipt")).select_by_visible_text("hhx2")
    driver.find_element_by_id("submit").click()

    receipt = driver.find_elements_by_xpath(".//*[@id='receipt']/option")
    option_number1 = len(receipt)
    b = random.randint(1, option_number1 - 1)
    Select(driver.find_element_by_id("receipt")).select_by_index(b)
    driver.find_element_by_id("submit").click()
    time.sleep(2)
    title1 = driver.title
    if title1 == '现金记账 - 然之协同':
        print('记转账成功，当前页面为\033[43;1m%r\033[0m'%title1)
    else:
        time_now = time.strftime('%Y%m%d%H%M%S')
        jietu1 = '../picture/pip1'+str(time_now)+'.jpg'
        driver.get_screenshot_as_file(jietu1)
        print('记转账失败，请再重新记账')
else:
    text = driver.find_element_by_xpath("html/body/div[2]/div/div/div[1]/div").text

    time_now = time.strftime('%Y%m%d%H%M%S')
    jietu = '../picture/pip' + str(time_now) + '.jpg'
    driver.get_screenshot_as_file(jietu)
    print('登录失败，请重新登陆,错误提示为%r.'%text)