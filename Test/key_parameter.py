"""
Date:2019.6.9
"""
#很多函数中隐藏的查询标记key参数，返回可调用对象，用于序列查询标记
student=[
    {'name':'b','age':2},
    {'name':'a','age':1},
    {'name':'c','age':3}
]
def fun():
    sort1=sorted(student,key=lambda k:k['name'])#这里的k就是前面的student
    import operator
    sort2=sorted(student,key=operator.itemgetter('name'))#相比lambda用法效率更快
    print(student,list(sort1),list(sort2),sep='\n')
#key参数也同样适用于对类实例针对某个标记进行查询
class Test():
    def __init__(self,id):
        self.id=id
    def __repr__(self):        #这里注意，__str__只在用户层面才有作用，底层层面都是调用__repr__
        return '%d'%(self.id)

def fun2():
    test=[Test(2),Test(1),Test(3)]
    sorte1=sorted(test,key=lambda k:k.id)            #lambda还是通用
    import operator
    sorte2=sorted(test,key=operator.attrgetter('id'))#接口不同，用法类似
    print(test,list(sorte1),list(sorte2),sep='\n')

if __name__=='__main__':
    fun()
    fun2()
    
