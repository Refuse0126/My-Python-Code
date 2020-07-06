import threading
import time
"""
Date:2020-7-4
"""
def fun1():
    print('fun1...')
    time.sleep(3)
    print('fun1 end..')

def fun2():
    print('fun2...')
    time.sleep(5)
    print('fun2 end...')

#正常三个线程是并发的，程序主线程可以看作是父线程，t1,t2是子线程，当父线程先结束，会检验子线程是否完成，否则直到最后一个子线程结束才会推出父线程
def test1():
    t1=threading.Thread(target=fun1)
    t1.start()
    t2=threading.Thread(target=fun2)
    t2.start()
    print('主线程...')

#join方法，在子线程完成之前，父线程会被阻塞，但是同级的子线程不会受到影响，这里t1正常执行，t2和主线程是有这层关系的
def test2():
    t1=threading.Thread(target=fun1)
    t2=threading.Thread(target=fun2)
    t1.start()
    t2.start()
    t2.join()
    print('主线程...')
    
#守护线程和第一种情况基本相反，当父线程结束时，子线程也强制跟着一起退出，这里和情况2同理，只关注守护的父线程，其他子线程不影响
def test3():
    t1=threading.Thread(target=fun1)
    t2=threading.Thread(target=fun2)
    t1.start()
    t2.setDaemon(True)
    t2.start()
    print('主线程...')

#自定义线程类，需要继承标准类，并且定制run方法
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('我的线程开始了')

if __name__=='__main__':
    t1=threading.Thread(target=fun1,name='我的线程')
    t1.setName('线程1')
    t1.start()
    print(threading.active_count())

    t2=MyThread()
    t2.start()


