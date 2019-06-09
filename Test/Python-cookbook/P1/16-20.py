"""
Date:2019.6.9
"""
#1.16筛选序列中的元素
nums=[-2,0,2,1,-5,0,-3,4]
def fun1():
    L1=[i for i in nums if i>0]
    L2=(i for i in nums if i>0)
    L3=filter((lambda x:x>0),nums)
    mask=[0,0,2,3,0,0,0,7]
    import itertools 
    L4=itertools.compress(nums,mask)#这里的mask不是类似切片索引，而是针对掩码中的顺序每一项检查，为真则选出否则弃掉
    print(L1,list(L2),list(L3),list(L4),sep='\n')
    
#1.20将多个映射合并为单个映射(字典的update方法也可以合并两个字典，但会创建新的字典映射，之后对两个字典的操作不会影响到新字典)
def fun2():
    import collections 
    a={'x':1,'y':2}
    b={'y':0,'z':3}
    c=collections.ChainMap(a,b) #记录了底层两个字典的映射关系，而非创建合并后的新字典
    print(c['x'],c['y'],c['z'])
    a['x']='x'
    print(c['x'])               #对两个字典的操作会体现出来
    
if __name__=='__main__':
    fun1()
    fun2()
    
    
