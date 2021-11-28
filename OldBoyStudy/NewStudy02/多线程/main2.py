# -*- coding: utf-8 -*-
# @Time : 2021/11/21 16:27
# @Author : huix
# @File : main.py
import _thread
import threading
from time import sleep,ctime
import logging
import time

# 优化main脚本：优化main脚本当中的主线程_thread的函数，使用threading实现，避免需要加上sleep来规避子线程被强杀
# 也可以通过锁来实现，但是相对threading来说更麻烦

logging.basicConfig(level=logging.INFO)

loops=[2,4]

def loop(nloop,nsec):
    logging.info("start loop" + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(loop) + " at " + ctime())


# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(4)
#     logging.info("end loop1 at " + ctime())

def main():
    start_time = time.time()
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
            threads[i].start()

    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())
    stop_time = time.time()
    func_time = stop_time - start_time
    print("the allfunction run time is %s" % (stop_time - start_time))

if __name__ == "__main__":
    main()