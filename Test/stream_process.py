"""
展示了流处理的基本步骤
Date:2019.5.14
"""
class Process():
    def __init__(self,reader,writer):
        self.reader=reader             #reader和writer对象必须具有read和write方法
        self.writer=writer
    def process(self):
        while True:
            data=self.reader.read()    #读取数据
            if not data:print() ;break 
            data=self.converter(data)  #处理数据
            self.writer.write(data)    #写入数据
    def converter(self):
        assert False, 'converter must be defined!'

class Uppercase(Process):
    def converter(self,data):
        return data.upper()

class MyRead():
    data='python'
    def __init__(self):
        self.idx=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.idx==6:
            return False
        char=MyRead.data[self.idx]
        self.idx+=1
        return char
    def read(self):
        return next(self)

if __name__=='__main__':
    import sys
    read=MyRead()
    obj=Uppercase(read,sys.stdout)
    obj.process()

