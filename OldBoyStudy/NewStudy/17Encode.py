#!/usr/bin/env python


# python2的默认编码是 ascii
# python3的默认编码是 utf-8
# Windows系统的默认编码是 gbk


s = "你好"
print(s.encode()) #如果括号内不写，默认转成默认的编码utf-8
s_to_gbk= s.encode("gbk")
print(s_to_gbk)

to_utf8 = s_to_gbk.decode("gbk").encode("utf-8")
print(to_utf8)

