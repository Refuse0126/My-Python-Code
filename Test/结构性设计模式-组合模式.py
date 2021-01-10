
"""
Date:2021.1.10
3.组合模式
内容：将对象组合成树形结构以表示”部分-整体“结构，使得用户对于单个对象或组合对象的使用形式保持一致
主要元素：抽象接口，叶子组件，复合组件,客户端组件

"""

# -----抽象组件（接口）----
from abc import ABCMeta,abstractmethod
class Interface(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

# ----叶子组件---
class Point(Interface):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("Point:({x},{y})".format(x=self.x,y=self.y))

# ---复合组件---
class Line(Interface):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        print("Line:Point({x1},{y1}),Pint({x2},{y2})".format(x1=self.p1.x,y1=self.p1.y,x2=self.p2.x,y2=self.p2.y))


# ---客户端组件---
class Picture(Interface):
    def __init__(self,*args):
        self.children = []
        for i in args:
            self.children.append(i)
    def draw(self):
        print("-----复合组件----")
        for i in self.children:
            i.draw()
        print("-----复合组件----")

a= Point(1,1)
a.draw()

b = Line(Point(0,0),Point(2,2))
b.draw()

c = Picture(a,b)
c.draw()

pic = Picture(a,b,c)
pic.draw()
