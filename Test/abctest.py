"""
展示了抽象类的基本用法
Date：2019.5.17
"""


from abc import ABCMeta,abstractmethod
class abcSuper(metaclass=ABCMeta):#继承于抽象类，强制约定ABC接口，否则无法继承，也无法创建实例
    def __init__(self):
        pass
    @abstractmethod               #这里的装饰器语法，只是用来标注是个抽象方法，实现ABC的关键还是metaclass=ABCMeta
    def action(self):
        pass

class abcSub(abcSuper):
    def __init__(self):
        pass
    def action(self):           
        print('hello,ABCmeta')

class Super():
    def __init__(self):
        pass
    def action(self):#以自己的方式定义抽象类，需要子类提供行为，但是仍然可以继承和创建抽象类，只是不能用这个方法而已
        assert False,'action must be defined!'

class Sub(Super):
    def __init__(self):
        pass
    def action(self):           
        print('hello,abctest')

def main():
    x=Sub()
    x.action()

    y=abcSub()
    y.action()
    
if  __name__ == "__main__":
    main()
