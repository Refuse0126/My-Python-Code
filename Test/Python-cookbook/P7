"""
Date:2019.7.4
函数用法
"""
#7.5
def fun():
    #1.带默认参数的函数，定义时绑定参数
    x = 1
    def fun1(a=x):
        print('a =',a)
    x=2
    fun1() #这里输出a=1

    #2.lambda函数绑定自由变量和默认参数的区别：前者是在执行时才绑定，后者是在定义时就绑定
    x=10
    f1=lambda y:x+y
    x=20
    f2=lambda y:x+y
    print(f1(10),f2(10))  #lambda在执行时，绑定的x为最新的x值20，结果为30,30
    x=10
    f1=lambda y,x=x:x+y
    x=20
    print(f1(10))       #在定义时，绑定了默认参数x=10，则之后f1对象不再变化

#7.8 让带有N个参数的可调用对象以较少的参数形式调用-functools.partial,lambda
def fun2():
    def fun(a,b,c,d):
        print(a,b,c,d)
    import  functools
    f1=functools.partial(fun,1,2)  #按顺序指定了a，b的值，并返回新的可调用对象，在使用新对象时，只需要提供没有提供的参数即可
    f1(3,4)
    f2=functools.partial(fun,1,d=4) #关键字指定
    f2(2,3)

    f3=lambda a,b,c,d=4:fun(a,b,c,d) #使用带默认参数的lambda函数实现减少函参个数并返回新的可调用对象的效果
    f3(1,2,3)

#7.12 为闭包方法增加属性，看起来像类实例一样
def fun3():
    def person(name=None):
        def manager():
            pass
        def getname():
            return  name  #仅仅是访问上层变量，可以直接访问不需要nonlacal
        def setname(newname):
            nonlocal name
            name=newname
        manager.getname=getname
        manager.setname=setname
        return  manager
    a=person('Bob')
    print(a.getname())
    a.setname('pycharm')
    print(a.getname())

if __name__=='__main__':
    fun()
    fun2()
    fun3()
