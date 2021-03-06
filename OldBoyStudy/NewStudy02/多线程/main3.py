# -*- coding: utf-8 -*-
# @Time : 2021/11/21 16:27
# @Author : huix
# @File : main.py
import _thread
import threading
from time import sleep,ctime
import logging
import time


# 再优化  直接继承threading类来实现
logging.basicConfig(level=logging.INFO)

loops=[2,4]

class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    logging.info("start loop" + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(loop) + " at " + ctime())


def main():
    start_time = time.time()
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
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