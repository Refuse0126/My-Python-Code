"""
Date:2019.7.4
对父类中带有属性管理器的方法进行拓展
"""
class Person:
    def __init__(self,name):
        self._name=name
    @property
    def name(self):
        return  self._name
    @name.setter
    def name(self,newname):
        self._name=newname
    @name.deleter
    def name(self):
        del self._name

#对父类中所有属性管理器方法进行拓展
class Sub1(Person):
    @property
    def name(self):
        print('Sub1 getting name!')
        return super().name

    @name.setter
    def name(self,newname):
        print('Sub1 setting name to ',newname)
        super(Sub1,Sub1).name.__set__(self,newname) #这里要注意，需要把控制流传递到之前定义的name属性的__set__（）方法中。
        #但是唯一能够调用到这个方法的方式就是以类变量而不是实例变量的方式去访问，super(Sub1,Sub1)就是这个作用

    @name.deleter
    def name(self):
        print('Sub1 del the name!')
        super(Sub1,Sub1).name.__delete__(self)

#2.只对父类中个别方法进行重载---需要明确指出拓展的管理器属性,否则虽然该方法可以拓展成功，但是使用其他方法会提示报错
class Sub2(Person):
    @Person.name.getter
    #@property
    def name(self):
        print('Sub2 getting name!')
        return super().name

if __name__=='__main__':
    a=Sub1('python')
    print(a.name)
    a.name='pycharm'
    del a.name

    b=Sub2('python')
    print(b.name)
    b.name='pycharm'
    print(b.name)


