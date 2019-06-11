"""
Date:2019.6.11
"""
#4.13 生成器函数实现管道机制：当生成器被串联起来的时，迭代中的每个yield语句都为管道中下个阶段的处理过程产出数据
def fun1():
    def gen1(n):
        temp=1
        while temp<=n:
            yield temp
            temp+=1
    def gen2(iterator):
        for i in iterator:    #关键要知道这里的参数是可迭代对象
            yield i**2
    g0=gen1(5)      #数据产出
    g1=gen2(g0)     #数据产出
    print(list(g1)) #数据消费    

#4.14 用yield from取代递归，来实现嵌套序列的扁平化处理
def fun2():
    a=[1,[2,3,[4,5,6,[7,8,9,10]]]]
    def recursion_list(l):              #1.自定义递归函数一层一层解析
        result=[]
        for item in l:
            if isinstance(item,list):
                for i in recursion_list(item):
                    result.append(i)
            else:
                result.append(item)
        return result
    print(recursion_list(a))

    def recursion_yield(iterator):      #2.定义yield from递归生成器函数
        import collections
        for item in iterator:
            if isinstance(item,collections.Iterable):
                yield from recursion_yield(item)
            else:
                yield item
    print(list(recursion_yield(a)))


if __name__=='__main__':
    fun1()
    fun2()
    
    

    
