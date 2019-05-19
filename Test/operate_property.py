"""
操作属性的几种常用方式比较
Date:2019.5.19
"""

#1.类内不定义任何操作属性的方法，外部通过类或实例操作属性：没有操作控制规则，容易被外部修改
class Test1():
    def __init__(self):
        pass

#2.自定义方法接口，在希望受到限制的属性前面加上双下划线，表示“私有”，外部通过self.x无法查看到，不过其他方式总是可以找到属性的
class Test2():
    def __init__(self,data=None):
        self.__data=data
    def getdata(self):
        return self.__data
    def setdata(self,data):
        self.__data=data
    def deldata(slef):
        print('data has been deleted!')
        del slef.__data

#3.对于新式类的属性描述器->操作类属性，因为声明一般是在class顶层赋值，使用property类
class Test3():
    def __init__(self):
        pass
    def getdata(self):
        return self.__data
    def setdata(self,data):
        self.__data=data
    def deldata(slef):
        print('data has been deleted!')
        del slef.__data
    data=property(getdata,setdata,deldata,doc='this is test3')

#4.运算符重载
class Test4():
    def __init__(self,data=None):
        self.data=data
    def __getattr__(self,attrname): #当属性能够正常找到时，不会进入此函数，只有访问不存在的属性时才会进入
        raise AttributeError
    def __setattr__(self,attrname,val):
        self.__dict__[attrname]=val
    def __delattr__(self,attrname):
        print('data has been deleted!') 
        return super().__delattr__(attrname)

#4.property类中定义了三个属性修饰器getter,setter,deleter
class Test5():
    def __init__(self,data=None):
        self.__data=data
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,data):
        self.__data=data
    @data.deleter
    def data(slef):
        print('data has been deleted!')
        del self.__data

#5.__get__,__set__,__del__：属性描述符，不作说明了


def main():
    t=Test1()
    t.name='test1'
    del t.name
    print()

    t=Test2()
    t.setdata('test2')
    t.deldata()
    print()

    t=Test3()
    t.data='test3'
    del t.data
    print()

    t=Test4()
    t.data='test4'
    del t.data


if  __name__ == "__main__":
    main()
