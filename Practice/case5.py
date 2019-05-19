"""
类中引入其他类实例
Date:2019.5.19
"""

class Car():
    def __init__(self,brand='dazhong'):
        self.__brand=brand
    @property
    def brand(self):
        return self.__brand
    def __str__(self):
        print('this is a',self.brand)
    
class Person():
    def __init__(self,name='No-name'):
        self.__name=name
    @property
    def name(self):
        return self.__name
    def drive(self,car):
        print(self.__name,'is driving a',car.brand)

def main():
    bob=Person('Bob')
    bob.drive(Car('porshe'))

if  __name__ == "__main__":
    main()
        
