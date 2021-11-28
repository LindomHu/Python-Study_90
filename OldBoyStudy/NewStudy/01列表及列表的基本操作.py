# -*- coding: utf-8 -*-
# @Time : ${DATE} ${TIME}
# @Author : huix
# @File : ${NAME}.py

list_a = [1,3,5,11,16,2]

print(list_a[0])
print(list_a[3])
print(list_a[-1])

# 切片 (0,3]
print(list_a[0:-1])
print(list_a[1:3])

print("\n")
# append
list_b = [1,0,11,9]
list_b.append(20)
print(list_b)   #[1,0,11,9,20]

list_b.insert(5,30)
print(list_b)   #[1,0,11,9,20,30]

# 根据元素的值删除
list_b.remove(0) #[1,11,9,20,30]

# 根据列表的索引来删除，并且会返回删除的值
list_b.pop(0)
print(list_b)   #[0,11,9,20,30]

# 对列表的元素进行排序（默认升序）
list_b.sort()
# 对列表的元素进行降序排序
list_b.sort(reverse=True)
print(list_b)

# 将列表中的元素反转
list_b.reverse()
print(list_b)
