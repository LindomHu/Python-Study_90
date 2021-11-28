#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2021/9/20 11:58 
# @Author : Lindom
# @File : atm.py 
# @Software: PyCharm

import os
import sys


# 可以找到项目脚本文件的父目录
Base_DIR = os.path.dirname( os.path.dirname( ( os.path.abspath(__file__))))


sys.path.append(Base_DIR)
from conf import settings
from core import main


main.login()
settings.Conf()