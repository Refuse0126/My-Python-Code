"""
描述符和元类
Date:2020.1.8
"""
class My_property():
    """
    将描述符应用到装饰器中，模拟静态属性property，其底层实现也是个描述符原理
    """
    def __init__(self,fun):
        self.fun=fun
    def __get__(self, instance, owner):
        if instance:
            print('__get__')
            res=self.fun(instance)
            #把返回值添加到实例的属性字典里，则下次访问该属性时则会直接去属性字典里找到，不用再触发描述符的__get__
            #这是对于非数据描述符而言，实现惰性属性
            setattr(instance,self.fun.__name__,res)
            return res
        else:
            return self

class Test1():
    def __init__(self,name):
        self.name=name

    @My_property
    def myname(self):
        return self.name

class My_metaclass(type):
    """
    type就是元类的一种:cls=type(clsname,(bases,),{属性集})，
    继承元类，实现自定义元类，
    """
    def __init__(self,clsname,bases,property):
        pass
    def __call__(self,*args,**kwargs):
        print('即将实例化...')
        #用来创建一个对象，返回给要实例化的对象
        obj=object().__new__(self)
        self.__init__(obj,*args,**kwargs)
        return obj

class Test2(metaclass=My_metaclass):
    #一旦指定元类，实例化时，Test2()久会触发元类的__call__方法，在回调方法里显示调用Test2的__init__ 并返回一个实例对象
    def __init__(self,name,age):
        self.name=name
        self.age=age
if __name__=='__main__':
    a=Test1('hello python')
    print(a.myname)
    print(a.myname) #非数据描述符修饰过myname属性，则会优先查找实例的属性字典而不是进入描述符的__get__方法

    b=Test2('hi pycharm',2020)
    print(b.name,b.age)
