"""
Date:2019.6.11
"""

#4.7对迭代器做切片操作->itertools.islice(iter,start,stop),Ps：返回单迭代器
def fun1():
    values=(i for i in ['a','b','c',1,2,3])
    import itertools
    for i in itertools.islice(values,3,None): 
        print(i)

#4.8跳过可迭代对象的前面一部分内容
def fun2():
    lines="""#Date:2019.6.11
#Author:lixishui
hello python
hello vscode 
byebye! 
"""
    with open('test.txt','w') as f:
        f.writelines(lines)
    
    #1 知道可迭代对象的长度时，可以运用4.7中的对迭代器进行切片操作
    import itertools
    text=open('test.txt')
    for line in itertools.islice(text,2,None):
        print(line,end='')
        
    #2 采用dropwhile()方法对内容前面的部分进行选择过滤
    text.seek(0)  #这里要注意，文件对象是单迭代器
    for line in itertools.dropwhile(lambda line:line.startswith('#'),text):
        print(line,end='')

#4.9元素的排列组合
def fun3():
    items=['a','b','c']
    import itertools
    for i in itertools.permutations(items):  #1 排序
        print(i)
    for i in itertools.combinations(items,2):#2 不重复组合
        print(i)
    for i in itertools.combinations_with_replacement(items,2): #3 重复组合
        print(i)

if __name__=='__main__':
    fun1()
    fun2()
    fun3()
    

    
