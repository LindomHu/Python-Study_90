#-*- coding: gbk -*-
f1 = open('test.txt','r',encoding='gbk')
f2 = open('testCopy.txt','w',encoding='gbk')

f2.write('���д�㶫����������')
f2.write('��һ�����Կ�\n,�ţ��ٻ�����\n\n')

while True:
    r = f1.readline()
    if r:
        f2.write(r)
        print(r,end = '')
    else:
        break
f1.close()
f2.close()

