"""
展示了装饰器的基本用法和细节问题
Date:2019.5.18
"""

#1.装饰器原理
def makebold(fn):  
    def wrapped():  
        return "<b>" + fn() + "</b>"  
    return wrapped
   
def makeitalic(fn):  
    def wrapped():  
        return "<i>" + fn() + "</i>"  
    return wrapped  

def fun1():
    return 'python'
    
@makebold
@makeitalic
def fun2():
    return 'python'

#2.计时器装饰
def timeit(fun):
    def wrapped(*args):
        import time
        start=time.clock()
        fun(*args)
        elapsed=time.clock()-start
        print(fun.__name__,'->Time Elapsed:',elapsed,'ms')
    return wrapped

@timeit
def fun3(*args):
    print(*args)

#3.有参数的装饰器,依次类推，可以无限包装
def wrapper_args(log='test'):
    def wrapper(fun):
        def inner(*args):
            #额外细节
            fun(*args)
            #额外细节
            print('this is',log)
            #如果fun是有返回值的函数，这里返回一个临时结果即可
        return inner
    return wrapper

@wrapper_args()
def fun4(*args):
    print(*args)

@wrapper_args('other test')
def fun5(*args):
    print(*args)

#4.类装饰器
class wrapper1_cls():                   #无参数的类装饰器
    def __init__(self,fun):
        self.fun=fun
    def __call__(self,*args):
        #额外细节
        self.fun(*args)
        print('this is',self.__class__.__name__)

class wrapper2_cls():                   #有参数的类装饰器，fun参数则是在回调函数中传入的
    def __init__(self,log='test'):
        self.log=log
    def __call__(self,fun):
        def inner(*args):
            #额外细节
            fun(*args)
            print('this is',self.__class__.__name__)
        return inner

@wrapper1_cls
def fun6(*args):
    print(*args)

@wrapper2_cls(log='other test')
def fun7(*args):
    print(*args)


#5.装饰器的括号
#   @wrapper \n def fun() 
#   => fun=wrapper(fun),,同理，带括号时 => fun=wrapper()(fun)
#   => 装饰器的语法糖加不加括号，取决于该装饰器最外层是否有参数，有则加，没有则不加，，函数装饰器还是类装饰器都一样


#6.装饰器的标签和属性问题，普通的装饰器语法最终函数对象的属性是装饰器中闭包函数的属性
def out(fun):
    def inner(*args):
        #.....
        fun(*args)
        #.....
    return inner
@out
def f1(*args):
    print(*args)


def out2(fun):
    from functools import wraps
    @wraps(fun)                 #采用functools.wraps(fun)声明被装饰的函数，则自动将装饰后的函数属性返还给fun对象
    def inner(*args):
        #...
        fun(*args)
        #...
    return inner
@out2
def f2(*args):
    print(*args)




def main():
    newfun=makebold(makeitalic(fun1)) #通过一层一层嵌套，返回一个包装后的函数对象
    print(newfun())                  

    print(fun2())                     #通过装饰器语法糖，在调用时，会一层一层实现包装逻辑

    fun3('hello,python')              #计时器装饰，新增计时逻辑

    fun4('hello,python')              #无参的函数装饰器
    fun5('hello,python')              #有参的函数装饰器

    fun6('hello,python')              #无参的类装饰器
    fun7('hello,python')              #有参的类装饰器

    
    print(f1.__name__)                #改善装饰器的标签属性问题
    print(f2.__name__)                

if  __name__ == "__main__":
    main()
