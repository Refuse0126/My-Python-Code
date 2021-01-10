
"""
Date:2021.1.10
4.代理模式
内容：创建用户代理类对象，提供用户操作接口，而代理类仅仅调用组件的实现，
5.外观模式
内容：在代理模式的基础上，如果组件有多个，而组件的接口形式都一致，在代理类中定义统一外观接口，分别调用各个组件的实现

"""
class A:
    def fun(self):
        print("这里是A")
class B:
    def fun(self):
        print("这里是B")

class Manager:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def fun(self):
        self.a.fun()
        self.b.fun()

m = Manager(A(),B())
m.fun()
