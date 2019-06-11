"""
Date:2019.6.11
"""
#4.10 enumerate产生索引-值的序列
def fun1():
    with open('test.txt') as f:
        for n,line in enumerate(f,1):
            print(n,': ',line,end='')

#4.11 zip(a,b)将两个序列元素对应绑定
def fun2():
    a=['a','b','c']
    b=[1,2,3,4]
    for i,j in zip(a,b):                                #1 默认zip取较短输入序列
        print(i,j)
    b=[1,2,3,4]
    import itertools
    for i,j in itertools.zip_longest(a,b,fillvalue=0):  #2 取较长输入序列的长度，缺少对应元素取0
        print(i,j)

#4.12 itertools.chain接收多个序列，返回一个迭代器可以实现连续遍历序列中的元素
def fun3():
    a=['a','b','c']
    b=[1,2,3]
    import itertools
    for i in itertools.chain(a,b):
        print(i)


if __name__=='__main__':
    fun1()
    fun2()
    fun3()
    

    
