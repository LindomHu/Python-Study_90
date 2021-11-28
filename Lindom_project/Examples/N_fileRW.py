#-*- coding: gbk -*-
f1 = open('test.txt','r',encoding='gbk')
f2 = open('testCopy.txt','w',encoding='gbk')

f2.write('随便写点东西，不换行')
f2.write('换一行试试看\n,嗯，再换两行\n\n')

while True:
    r = f1.readline()
    if r:
        f2.write(r)
        print(r,end = '')
    else:
        break
f1.close()
f2.close()

