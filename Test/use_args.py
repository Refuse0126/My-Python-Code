"""
展示了可变参数和Key_only参数的基本用法
Date：2019.5.15
"""

def fun1(*pargs):
    print(pargs)    #元组
def fun2(**kargs):
    print(kargs)    #字典
def fun3(*pargs,ch='\n',**kargs):
    print(pargs,ch)
    print(kargs,ch)
#1.普通的收集调用
fun1(1,2,3,4,5)
fun2(name='Bob',age=20)
#2.将已有的元组和字典进行解包调用
fun1(*(1,2,3,4,5))
fun2(**{'name':'Bob','age':20})
#使用key_only参数，既可以接收任意多个参数，也可以接收作为关键字传递的配置选项，
# 注意key_only参数声明只能在*之后，**之前，调用时候则无所谓，是通过关键字传递的
fun3(1,2,3,ch='!',a=4,b=5)
