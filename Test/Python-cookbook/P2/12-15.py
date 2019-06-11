"""
Date:2019.6.11
"""
#2.12文本清理和过滤
def fun1():
    line='hello,python are\tyou\nok!'
    line=line.replace(',',' ')
    line=line.replace('\t',' ')
    line=line.replace('\n',' ')
    print(line)                         #1 多用一次str.replace

    import re                           #2 re.sub替换
    result=re.sub(r'(,;)\s*',' ',line)
    print(result)

    remap={                             #3 自定义转换表，调用str.translate重映射
        ord(','):' ',
        ord('\t'):' ',
        ord('\n'):' ',
        ord(';'):' '
    }
    result=line.translate(remap)
    print(result)

#2.13 字符串文本对齐str.rjust/centry,format()
def fun2():
    line='hello,pytho'          
    print(line.rjust(20,'@'))
    print(line.center(20,'*')) #可选填充字符

    print(format(line,'@>20'))
    print(format(line,'*^20'))

#2.14字符串连接与合并
def fun3():
    lines=['hello','python','are you ok']
    print('hello'+' '+'python')    #简单的工作用+即可完成
    print(' '.join(lines))
    lines=(i for i in lines)       #join可以将序列或者可迭代对象中的片段进行合并连接
    print(' '.join(lines))


class mis_val(dict):            #这里需要指定为dict的子类
    def __missing__(self,key):
        return '{'+key+'}'

#2.15给字符串中的变量名做插值处理
def fun4():
    line='{name} is {age}!'
    result=line.format(name='Bob',age='20') #1.format
    print(result)

    name='Bob'
    age=20
    result='%(name)s is %(age)d'%{'name':'Bob','age':20} #2.基于字典的格式化表达式
    result2='%(name)s is %(age)d'%vars()                 #vars()内部也是变量字典集
    print(result,result2)

    name='Bob'
    age=20
    result=line.format_map(vars())          #3.format_map+vars()
    print(result)

    #上面两种方法的共同缺点是无法处理字符串中的变量缺值状况
    #可以自定义一个带有__missing__方法的类来包装传入format_map的参数
    result='today is {Date}'.format_map(mis_val(vars())) #4.自定义缺值类包装参数
    print(result)


if __name__=='__main__':
    fun1()
    fun2()
    fun3()
    fun4()
    
    
