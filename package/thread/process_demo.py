#coding=utf-8
from multiprocessing import Process,Queue
import os
import time
import random


print 'Process %s start...' % os.getpid()

# 子线程返回0 ，父线程返回子线程pid
pid = os.fork()

if pid == 0:
    print 'I am child process %s and my parent is %s' % (os.getpid(),os.getppid())
else:
    print 'I %s just created a child process %s' % (os.getpid(),pid)


def write(q):
    for value in ['a','b','c']:
        print 'put value %s to Queue...' % value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print 'Get value %s from Queue.' % value

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
