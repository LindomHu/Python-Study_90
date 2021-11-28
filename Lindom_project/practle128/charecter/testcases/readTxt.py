#第一个 r ：转义，第二个 r：可读
# data_txt = open(r"C:\python34\practle128\class128\data\data.txt",'r')
# content = data_txt.readlines()     # 分行取出文本里面的内容
# print(content)
#
# url =content [0].strip().split('>>')[1]       # 用strip 截掉换行\n的内容，再split用大于号分割，取数组右边的内容
# acount = content[1].strip().split('>>')[1]
# password = content[2].strip().split('>>')[1]
# print(url,acount,password)
#
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.implicitly_wait(3)
# driver.get(url)
# driver.find_element_by_id('account').send_keys(acount)
# driver.find_element_by_id('password').send_keys(password)
# driver.find_element_by_id('submit').click()

names = ['胡一','朱二','张三', '李四','王五','欧阳六']     #定义一个列表
print( names[3],names[0])                                   #取值
print(names[0:3])         #切片，0可以省略
print(names[1:3])         #切片从取值得角度看：顾头不顾尾

name = ['吕七',names,'黄八']
print(name[1])









