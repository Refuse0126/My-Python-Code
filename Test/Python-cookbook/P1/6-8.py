"""
Date:2019.6.9
"""
#1.6创建一键多值的字典
import collections
def fun1():
    d1=dict()                       
    d1.setdefault('a',[])
    d1['a'].append(1)
    d1['a'].append(2)
    print(d1)

    d2=collections.defaultdict(list)
    d2['a'].append(1)
    d2['a'].append(2)
    print(d2)

    d3=collections.defaultdict(set)
    d3['a'].add(1)
    d3['a'].add(2)
    d3['a'].add(1)
    print(d3)

#1.7创建有序的字典（普通字典键是乱序）,顺序是创建键值时的顺序，而不是键的普通排序
#Ps：OrderedDict内部创建双向链表，能够记住元素加入的顺序，但内存开销大
def fun2():
    d=collections.OrderedDict()
    d['a']=1
    d['b']=2
    d['c']=3
    print(d)

#1.8对字典进行运算时，只会对键遍历,可以根据需要利用zip将字典键值翻转,Ps:zip()创建的是单迭代器
def fun3():
    score={
        'chinese':80,
        'math':85,
        'english':88
    }
    print(max(zip(score.values(),score.keys())))
    print(sorted(zip(score.values(),score.keys()),reverse=True))
    
if __name__=='__main__':
    fun1()
    fun2()
    fun3()
