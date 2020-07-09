import time
import os
"""
Date:2020-7-9
"""

#1.生成器函数yield实现用户态切换
def test1():
    print('111')
    recv = yield '断点1'    #这里可以有接收send方法的接收值，也可以有返回值
    print(recv)
    print('222')
    yield '断点2'
def fun1():
    f = test1()
    print(next(f))
    res=f.send('可以继续下行了...') #这里的send方法内部就是next+传值
    print(res)

#2.协程就是在遇到IO操作自动切换的原理

if __name__=='__main__':
    fun1()
    
    print('主进程end...')


