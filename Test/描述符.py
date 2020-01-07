"""
类描述符的原理和简单应用
date:2020.1.7
"""
class Typed:
    """
    （描述符是一个类，同时也只能作为另外一个类的类属性存在）
    self:所属类的类属性即这个描述符类的一个实例
    instance:所属类的实例
    cls:所属类
    触发过程：在所属类中创建描述符实例，x=Typed(),然后所属类的实例对象self.x在类中找到属性，发现为描述符后，转为查找self.__dict__['x'].__get__()这个方法，另外两个同理
    只有__set__会在instance实例赋值操作时候做到检测，其他时候只是在操作instance实例属性
    """
    def __init__(self, key, type_):
        self.key = key
        self.type_ = type_
    #如果只有一个__get__方法，则为非数据描述符，则查找优先级会低于所属类实例的属性查找，即数据描述符和实例属性重名时，
    #则优先会找到描述符实例
    def __get__(self, instance, cls):
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError('must be %s' % self.type_)
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        del instance.__dict__[self.key]

def decorate(**kwargs):
    def wrapped(obj):
        #将传入的参数:类型 创建类描述符属性，并加入类属性字典中
        for key,val in kwargs.items():
            setattr(obj,key,Typed(key,val))
        return obj
    return wrapped

#类装饰器，用来检测传参类型
@decorate(name=str,age=int)
class A:
    def __init__(self, name,age):
        self.name = name
        self.age=age

if __name__=='__main__':
    a = A(name='hello', age='2020')
    print(A.__dict__)
