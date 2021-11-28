#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/8/28 16:38 
# @Author : Lindom
# @File : 05Genarator.py
# @Software: PyCharm Community Edition

# 生成器：只是提供了一种算法，不会事先准备好，节省空间，
# 只有在调用时才会生成相应的数据
# 只记录当前位置，只有一个_next_()方法，往后取一个


L = ((i * 2) for i in range (10))
L.__next__()



