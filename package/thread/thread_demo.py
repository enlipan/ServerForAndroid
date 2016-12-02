import time, threading


def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.currentThread().name, n)
        time.sleep(1)
    print 'thread %s is ended' % threading.currentThread().name


def threadTest():
    print 'thread %s is running' % threading.currentThread().name
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print 'thread %s ended' % threading.currentThread().name


localSchool = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (localSchool.student, threading.currentThread().name)
def process_thread(name):
    localSchool.student = name
    process_student()
t = threading.Thread(target=process_thread,args=('Alice',),name='ThreadA')
t.start()
t.join()