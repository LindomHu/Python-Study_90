# Author:LindomHui
# coding=---UTF-8---


# import sys
f = open("file_Mks","r",encoding="utf-8")               #打开原来的文件（需要修改的文件）
f_new = open("file_Mks.bak","w",encoding="utf-8")       #打开一个新文件（如果没有也会新建）

# find_str = sys.argv[1]
# replace_str = sys.argv[2]
for line in f:
    if "马克思主义理论体系" in line:
        line = line.replace("马克思主义理论体系","马克思主义")  #用“马克思主义”替代 “马克是主义理论体系”
    f_new.write(line)      #把改过的新内容和原来的内容一起写进新文件
f.close()
f_new.close()              #关闭文件

'''
1 列表、元组操作   列表和元组都是有序的，列表可以增删改，可以嵌套任何类型，元组是只读的
2 字符串操作    字符串是不可以修改的
3 字典操作  无序的，可以嵌套列表等等
4 集合
5 文件操作
6 文件编码和转码

'''