"""
instance.__dict__只会找到实例属性
dir(instance)会找到实例以及继承而来的所有属性
Date：2019.5.17
"""
class Super():
    string='class'              #类属性中，
    def __init__(self):
        self.string='self'      #实例属性和类属性同名时，会覆盖掉类属性，因此尽量避免两个名称空间属性同名
        self.x=1

def main():
    a=Super()
    print(dir(a))               #列表中的string属性，是实例的属性，因为向上搜索时，实例的搜索层级最低，最快找到
    print(a.__dict__)           

if  __name__ == "__main__":
    main()
