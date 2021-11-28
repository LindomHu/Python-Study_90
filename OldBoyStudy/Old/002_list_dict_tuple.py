# @Time : 2020/6/20 19:39 
# @Author : Lindom
# @File : 002_list_dict_tuple.py 
# @Software: PyCharm Community Edition

list1 = [{'嫉妒':'envy'},{'恨':'hatred'},{'爱':'love'}]
print(list1[2]['爱'])

# 第一步：取出列表中的第三个元素（list1[2]），字典{'爱':'love'}；
# 第二步：取出list1[2]中键'爱'所对应的值，即'love’（list1[2]['爱']）。

dict1 = {1:['cake','scone','puff'],2:['London','Bristol','Bath'],3:['love','hatred','envy']}
print(dict1[3][0])

# 第一步：取出字典中键为3对应的值（dict1[3]），即['love','hatred','envy']。
# 第二步：再取出列表['love','hatred','envy']中的第一个元素（dict1[3][0]）。

tuple1 = ('A','B')
list2 = [('A','B'),('C','D'),('E','F')]

print(tuple1[0])
print(list2[1][1])

# 从代码里，也可看出：1.元组内数据的提取也是用偏移量；2.元组也支持互相嵌套。


townee = [
    {'海底王国':['小美人鱼''海之王''小美人鱼的祖母''五位姐姐'],'上层世界':['王子','邻国公主']},
    '丑小鸭','坚定的锡兵','睡美人','青蛙王子',
    [{'主角':'小红帽','配角1':'外婆','配角2':'猎人'},{'反面角色':'狼'}]
    ]

print(townee[5][1]["反面角色"])

# 列表合并和排序

list1 = [91, 95, 97, 99]
list2 = [92, 93, 96, 98]

# 把 A 组成绩赋值给一个新列表，用来存合并的成绩——这个细节要注意！
list3 = list1.copy()
list3.extend(list2)
print(list3)

list3.sort()
print(list3)
