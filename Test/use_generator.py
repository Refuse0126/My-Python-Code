"""
展示基本的生成器函数和生成器表达式的用法
Date:2019.5.16
"""
#1.生成器函数
def mymap1(fun,*args):
    for item in zip(*args): 
        yield fun(*item)
    
#2.生成器表达式
def mymap2(fun,*args):
    return (fun(*item) for item in zip(*args))


#学习手册习题6
def addDict(d1,d2):
    new=dict()
    for i in d1:
        new[i]=d1[i]
    for i in d2:
        if i in new:continue
        else:
            new[i]=d2[i]
    return new

#学习手册习题

def main():
    print(list(mymap1((lambda x:x+1),[1,2,3])))
    print(list(mymap2((lambda x:x+1),[1,2,3])))
    newdict=addDict({'name':'Bob','age':20},{'name':'python','job':'student'})
    print(newdict)

if  __name__ == "__main__":
    main()
