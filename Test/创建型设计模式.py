Date：2021.1.10
"""
1.设计模式--简单工厂
内容：不直接暴露对象类的实现细节，而是通过工厂类选择性向用户开放
class A
class B
class Factory:
    def __init__(self,args):
        #通过解析args，来创建不同的具体对象
"""

"""
2.设计模式--工厂方法
内容：简单工厂的基础上，工厂类提供一个创建对象的方法，由其子类实现决定具体创建什么对象
class A
class B
class Factory:
    #抽象方法
    def Create():
class A_Factory:
    def Create():
        #创建A
class B_Factory:
    def Create():
        #创建B 
"""


"""
3.设计模式--抽象工厂
内容：工厂方法的基础上，定义一些接口，用于创建一些创建对象所需要的一系列组件（对象的不同取决于组件的不同）
# ---对象类----
class A:
    def __init__(slef,a,b)
        pass

# ---抽象组件类（不同的产品对象有不同的组件类型，需要有N个子类表现）----
class a
class b
# ---抽象工厂----
class abc_Factory:
    #抽象方法
    def Create_a():
    def Create_b():  

# ---具体产品工厂----
class A_Factory(abc_Factory):
    def Create_a():
        return a
    def Create_b():
        retrun b
class B_Factory(abc_Factory):
    def Create_a():
        return a
    def Create_b():
        retrun b

# --客户端--
x = A_Factory()     #创建组件实例
demo = A(x.a,x.b)   #传参创建产品对象

"""

"""
4.设计模式--建造者
内容：抽象工厂的基础上，产品对象A或者产品对象B 不是直接创建，而是通过一个创建类Builder类完成，Builder类内部能够控制组件a，b的建造顺序，来实现具体的A，B产品差异

class Builder()
    self.__init__(self,a,b):
        #A或B的组装逻辑
        return A或B
"""
