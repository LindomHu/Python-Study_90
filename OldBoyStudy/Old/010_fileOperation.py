# Author:LindomHui
# coding=---UTF-8---

#data = open("wait",encoding="utf-8").read()
f = open("wait_2","a",encoding="utf-8")  #文件句柄  r为可读,w为可写（会覆盖创建）,a为追加
                                            #r+:既能读又能写
# data = f.read()
# print(data)

f.write("我爱北京天安门，\n")
f.write("天安门上太阳升,\n")
f.write("duo la la mi fa su")


#print(data)