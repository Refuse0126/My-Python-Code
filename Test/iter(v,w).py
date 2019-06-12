"""
Date:2019.6.12
"""

#关于iter()函数，如果传递一个可调用对象（例如lambda）及一个哨兵值，将会创建一个迭代器，该迭代器会重复调用提供的可调用对象直到返回哨兵值为止。
def fun1():
    #通常用法是提供一个文件对象，哨兵值为b''，则可以实现固定大小的数据块重复迭代，例如一次迭代N个字节，而不是一行
    import functools 
    with open('test.txt') as f:
        SIZE=2
        record=iter(functools.partial(f.read,SIZE),'')
        for data in record:
            print(data,end='')


if __name__=='__main__':
    fun1()
    
    
    

    
