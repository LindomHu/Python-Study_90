#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2022/4/13 上午11:59 
# @Author : huix
# @File : 09tag处理.py 
# @Software: PyCharm



import pandas as pd
from collections import Counter

path = ()
dp = pd.read_csv(path+"tag.csv", header=0)

data = dp.values

tags = data[:,2]
rtemp = Counter(tags)

r = rtemp.most_common(N)
selTag = [item[0] for item in r]

selData = [item for item in data if item[2] in selTag]
selData.sort(key=lambda selData:(selData[0],selData[1]))


resultData = [selData[0]]
for item in selData[1:]:
    if(item[0] == resultData[-1][0] and item[1] == resultData[-1][1]):
        resultData[-1][2] += "|"+item[2]
    else:
        resultData.append(item)


db = pd.DataFrame(resultData)
db.to_csv(path + 'selectedTags.csv', header = False, index = False)
