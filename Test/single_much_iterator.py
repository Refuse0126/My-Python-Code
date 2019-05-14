"""
展示了支持单迭代对象和支持多迭代对象的特性
"""

class Squares:
    """
    single
    """
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

class Squares2:
    """
    much
    """
    def __init__(self, start, stop):
        self.start = start
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return Squares2(self.value + 1, self.stop)

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

def main():
    i=Squares(1,4)
    I=iter(i)
    print(next(I),end=' ' )
    print(next(I))
    I2=iter(i)
    print(next(I2))

    print("-------------\n")
    i=Squares2(1,4)
    I=iter(i)
    print(next(I),end=' ' )
    print(next(I))
    I2=iter(i)
    print(next(I2))

if __name__ == '__main__':
    main()

