# -*- coding: utf-8 -*-
#需要安装pymysql:用python写的专门操作mysql数据库的外部库
#cmd下的安装命令：pip install pymysql
#检查pymysql有没有装好：菜单file--setting--project XXX--project interpreter

import pymysql
class tb_to_csv(object):
    def __init__(self, host, port, db, user, password, charset):  # 在构造函数里面连上并登陆数据库
        # 连接并登陆数据库，得到一个成员变量，连接对象
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user,
                                    password=password, charset=charset)

    def execSql(self,strSql):    # 执行sql语句，并写入文件
        cur = self.conn.cursor()  #从连接中实例化出一个游标，用游标可以来执行SQL语句
        cur.execute(strSql)          #用游标执行（execute）sql语句，结果被存放在游标中
        data = cur.fetchall()     #fetch:获取，从游标中获取所有查询结果，赋值给data变量
        f = open("emp_data.csv", "w", encoding="utf-8")#创建打开一个文件用于保存结果 'w'可读
        for d in data:            #循环每一行
            line=""               #定义一个变量用于存储一行的字符串
            for c in d:           #循环每一行的每一列
                line = line + "," + str(c)
            line = line.lstrip(",")#左修剪掉line左边的逗号,strip,剪掉最左边和最右边的符号或字符
            f.write(line + "\n")         #将一行数据写入文件
            print(line)
        f.close()                 #关闭文件
        cur.close()               #关闭游标
    def close(self):  # 断开连接
        self.conn.close()

if __name__ == '__main__': #当被调用的.py的文件运行时，if_name_ =='_main_'之下的代码不会被执行
    x = tb_to_csv("127.0.0.1", 3306, "hrdb", "root", "", "utf8")  # 实例化
    x.execSql("select * from employees")  # 执行sql语句并将结果写入csv文件
    x.close()  # 数据库一定要记得关闭断开连接
