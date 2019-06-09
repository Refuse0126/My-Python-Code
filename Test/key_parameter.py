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

if __name__=='__main__':
    fun()
    
