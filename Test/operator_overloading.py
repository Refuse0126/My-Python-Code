"""
展示了迭代器原理和常用的运算符重载原理
Date：2019.5.18
"""

#定义多迭代器类的两种方式，本质上都是在Iter调用时，创建不同于self的实例即可
#单迭代器返回自身即可，将self的状态信息刷新，但仍然是同一个self
class muchIterator1():
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.status=0
    def __iter__(self):
        return muchIterator1(self.status,self.end)      #1.每次Iter，传入self.status创建新的实例，以保留每个迭代器的状态信息
    def __next__(self):
        if self.status==self.end:
            raise StopIteration
        else:
            tmp=self.status
            self.status+=1
            return tmp

class muchIterator2():
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return Next2(self.start,self.end)              #2.每次Iter，创建新实例时，虽然传入参数一样，但本质上对象不同，从而可以同时激活多个迭代器

class Next2():
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.status=0
    def __next__(self):
        if self.status==self.end:
            raise StopIteration
        else:
            tmp=self.status
            self.status+=1
            return tmp

#__getattr__和__set__attr__的基本用法
class attrTest():
    def __init__(self):
        pass
    def __getattr__(self,attrname):
        if attrname in self.__dict__:
            return self.__dict__[attrname]
        else:
            try:
                raise AttributeError 
            except AttributeError:
                return 'AttributeError'+attrname
    def __setattr__(self,attrname,val):
            self.__dict__[attrname]=val                 #注意这里属性赋值的语法不是self.attrname=val，因为本质上还是__setattr__，会无限递归


#用__setattr__模拟实例属性的私有性
class PrivateExc(Exception):pass
class Privacy():
    privates=['name','age','job']
    def __init__(self):
        pass
    def __setattr__(self,attrname,val):
        if attrname in self.privates:
            try:
                raise PrivateExc(attrname,self)
            except PrivateExc:
                print('PrivateExc:',attrname)
        else:
            self.__dict__[attrname]=val

#重载加号运算符
class Caculator():
    def __init__(self,num):
        self.num=num
    def __add__(self,x):
        return self.num+x
    def __radd__(self,x):
        return x+self.num
    def __iadd__(self,x):
        self.num+=x
        return self

#重载回调表达式，实现API接口的设计,例如把二元操作函数接口修改为一元操作接口
class Adaptor():
    def __init__(self,num):
        self.num=num
    def __call__(self,other):
        return self.num+other

def main():
    x=muchIterator1(0,5)
    I1=iter(x)
    print(next(I1))
    print(next(I1))
    I2=iter(x)
    print(next(I2))

    y=muchIterator2(0,5)
    I1=iter(y)
    print(next(I1))
    print(next(I1))
    I2=iter(y)
    print(next(I2))

    z=attrTest()
    print(z.age)
    z.name='Bob'
    print(z.name)

    p=Privacy()
    p.x=1
    p.name='Bob'

    c=Caculator(1)
    print(c+1)
    print(1+c)
    c+=1
    print(c.num)

    a=Adaptor(1)
    print(a(1))

if  __name__ == "__main__":
    main()
