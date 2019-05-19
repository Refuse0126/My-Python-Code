"""
用到了ABC技术，和属性修饰器，以及运算符重载的简单示例
Date：2019.5.19
"""

from abc import ABCMeta,abstractmethod
class Employee(metaclass=ABCMeta):
    def __init__(self,name,salary=0):
        self.__name=name
        self.__salary=salary
    
    @property
    def name(self):
        return self.__name
    
    @property
    def salary(self):
        return self.__salary

    @abstractmethod
    def job(self):
        pass
        
    def __gt__(self,other):
        return self.salary>other.salary
    def __lt__(self,other):
        return self.salary<other.salary

class Manager(Employee):
    def job(self):
        return 'this is a Manager!'
class Programer(Employee):
    def job(self):
        return 'this is a Programer!'
   

def main():
    m=Manager('Bob',1000)
    p=Programer('dawei',2000)
    print(m.name,m.salary)
    print(p.name,m.salary)
    if m>p:
        print(m.job())
    else:
        print(p.job())

if  __name__ == "__main__":
    main()
