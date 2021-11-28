# -*- coding: utf-8 -*-
# @Time : 2021/11/21 16:27
# @Author : huix
# @File : main.py
import _thread
from time import sleep,ctime
import logging
import time

logging.basicConfig(level=logging.INFO)


def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(3)
    logging.info("end loop0 at " + ctime())


def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(4)
    logging.info("end loop1 at " + ctime())

def main():
    start_time = time.time()
    logging.info("start all at " + ctime())
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1,())

    # 引用_thread后，当主线程结束当的时候，所有的还没运行的或正在运行的子线程都会强制结束
    sleep(6)
    logging.info("end all at " + ctime())
    stop_time = time.time()
    func_time = stop_time - start_time
    print("the allfunction run time is %s" % (stop_time - start_time))

if __name__ == "__main__":
    main()