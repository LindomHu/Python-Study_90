# @Time : 2020/7/26 10:13 
# @Author : Lindom
# @File : 007_func.py
# @Software: PyCharm Community Edition


def my_len(words):
    counter = 0
    for i in words:
        counter = counter + 1
    return counter

a = '三根皮带，四斤大豆'
print(my_len(a))
#等价于print(my_len('三根皮带，四斤大豆'))