"""
展示了静态方法、实例方法、类方法的用法区别
Date：2019.5.18
"""
#1.类中的静态方法、实例方法和类方法
class Test():
    def __init__(self):
        pass
    def method():               #普通的静态方法看作是类内定义的普通函数，调用时只能用类进行调用，因为没有self参数，无法用实例调用
        print('hello python!')
    @staticmethod               #用staticmethod进行装饰后，则该方法除了用类进行调用外，还可以用实例调用，看起来就像是实例方法一样，
    def static_method():
        print('hello python!')
    @classmethod                #可以两种方式都可以调用，并且在调用时，内部能够实现调用主体到类的自动转换
    def class_method(cls):
        print(cls.__name__)
        print('hello python!')
        
def main():
    t=Test()
    Test.method()

    t.static_method()
    Test.static_method()

    t.class_method()
    Test.class_method()

if  __name__ == "__main__":
    main()
