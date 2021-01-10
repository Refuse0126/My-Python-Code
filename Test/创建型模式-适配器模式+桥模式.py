
"""
1.适配器模式
内容：将已有的接口，适配为用户希望的接口形式
class A:
    def pay():
        pass
class B:
    def cost():
        pass
#当用户都希望用pay这个接口时
#类适配器，通过继承直接兼容接口,,,这种方式，就需要所有接口不同的类都创建一个适配子类，但是内部不需要做出任何判断
class Adapt_B(B):
    def pay():
        self.cost()
#对象适配器，通过传入对象，来兼容接口,,,这种方式，就需要在传入对象的时候，做出类型判断，调整接口兼容的策略
class Adapt：
    def __init__(x):
        self.x = x
    def pay():
        self.x.pay()
"""

"""
2.桥模式
内容：将对象的几个维度分离，使其可以独立变化，，相当于是一层嵌套装饰，

class Shape:                   #N种shape
    def __init__(self,color):
        self.color = color
    def draw():
        self.color.paint()
class Color:
    def paint(self,paint):    #N种shape，这里都N种实现方式，可以把这里设计为抽象，然后子类实现
        pass
# --客户端--
a = Shape(Color())
a.draw()
"""
