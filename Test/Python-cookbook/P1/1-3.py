def fun1():
    #序列拆分单独变量#
    #1.1.普通赋值
    a,b=(1,2)
    a,b='py'
    _,a,b,_='#12#' #不常用的变量名来表示要丢弃的值
    print(a,b)

def fun2():
    #1.2.*表达式拆分任意长度可迭代对象
    first,*main=[0,1,2,3,4,5]
    name,_,(year,_)=('Bob',110,(1995,1))
    print(name,year)
    line='python:^&^&^&%^&$&*^:xinjiang:2019.6.7:/User/python/lib'
    lanuage,*_,date,dir=line.split(':')  #配合字符串处理操作拆分变量
    print(lanuage,date,dir)

def fun3():
    #1.3 固定长度队列
    from collections import deque
    q=deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.append(4)
    print(q)

if __name__=='__main__':
    fun1()
    fun2()
    fun3()
