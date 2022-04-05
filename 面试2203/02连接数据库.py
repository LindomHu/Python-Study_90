#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/3/30 上午11:44 
# @Author : huix
# @File : 02连接数据库.py 
# @Software: PyCharm

import MySQLdb


# 打开数据库连接
db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )


# 使用cusor()方法获取操作游标
cursor = db.cursor()


# 使用excute方法执行sql语句
cursor.excute("SELECT VERSION()")


# 使用fetchone方法获取一条数据
data = cursor.fetchone()


# 关闭数据库连接
db.close()
