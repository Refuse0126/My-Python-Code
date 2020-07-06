import multiprocessing
import time
import os
"""
Date:2020-7-6
"""

#---------------进程间通信：队列，管道，Manager(数据共享)
#1.进程队列通信
def test1(q):
    print(id(q))
    print(q.get())
    time.sleep(2)
def fun1():
    q=multiprocessing.Queue()
    t=multiprocessing.Process(target=test1,args=(q,))
    t.start()
    print(id(q))
    q.put('这是一个进程队列...')  
    t.join()                    #join方法一定要放在发送端的后面，否则会卡在其他进程获取中

#2.管道通信
def test2(son):
    print(id(son))
    son.send('爸爸你好...')
    print(son.recv())
    son.close()
    time.sleep(2)
    
def fun2():
    parent,son=multiprocessing.Pipe()
    t=multiprocessing.Process(target=test2,args=(son,))
    t.start()
    print(id(parent))
    print(parent.recv())
    time.sleep(1)
    parent.send('儿子乖...')  
    t.join()                   

#3.Manager数据共享
def test3(d,l):
    print(id(d),id(l))
    print(d,l)
    d['job']='teacher'
    l.append(2)

def fun3():
    with multiprocessing.Manager() as manager:
        d=manager.dict(name='David',age=20)
        l=manager.list()
        l.append(1)
        print(id(d),id(l))
        t=multiprocessing.Process(target=test3,args=(d,l,))
        t.start()
        t.join()
        print(d,l)

#4.进程同步:这里举的例子是当一个进程使用屏幕输出时，其他进程不得同时执行，
def test4(r,i):
    r.acquire()
    print(i)
    r.release()
    time.sleep(1)

def fun4():
    r=multiprocessing.Lock()
    ts=[]
    for i in range(10):
        t=multiprocessing.Process(target=test4,args=(r,i,))
        t.start()
        ts.append(t)
    for i in range(10):
        ts[i].join()

#5.进程池--线程的信号量有一点共通
def test5(i):
    print(i)
    time.sleep(0.1)
    return '进程%s结束...'%os.getpid()

#这里的参数一定要有，否则会报错，且args是子进程执行成功后的返回值
def callback(args):
    print(args)
    
def fun5():
    p=multiprocessing.Pool(5)
    for i in range(10):
        #p.apply(func=test5,args=(i+1,))  #进程同步接口
        p.apply_async(func=test5,args=(i+1,),callback=callback) #子进程执行成功后则会在主进程中调用回调函数
    p.close()
    p.join()

if __name__=='__main__':
    #fun1()
    #fun2()
    #fun3()
    #fun4()
    fun5()


    print('主进程end...')


