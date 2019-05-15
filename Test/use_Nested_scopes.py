"""
展示了嵌套作用域保留状态信息的基本用法
Date:2019.5.15
"""

#1.在函数内修改全局变量，需要global声明
x=1
def fun1():
    global x
    x+=1
    print(x)
#2.在函数内部仅仅是引用上层作用域（这里值得就是全局变量）的变量，则不需要global声明，也不会出现类似c+中变量未定义的错误
def fun2():
    print(x)

#3.nonlocal声明类似global声明，都是用来在嵌套作用域内修改上层变量，
#不同的是，gloabl是用来修改全局变量，而nonlocal是用来修改上层作用域（通常还是在函数内部）的变量
def main():
    y=2
    def fun3():
        nonlocal y
        y+=1
    fun3()
    print('y=',y)  #y=3
main()

#4.根据变量作用域查找规则实现工厂函数，以保留函数状态信息
def external1(hello):
    def inside(string):
        print(hello,string) #这里的hello,也就是上层作用域传入的参数，因此可以记住上层的状态信息
    return inside
f=external1('hello')
f('python')
f('vscode')

#5.lambda表达式用于嵌套作用域，保留上层函数状态信息
def external2(hello):
    action=(lambda string:print(hello,string))
    return action
f=external2('hello')
f('python')
f('vscode')

#6.使用nonlocal声明修改上层作用域变量，以实现修改状态信息，例如计数器功能
def external3(hello):
    cnt=0
    def inside(string):
        print(hello,string) 
        nonlocal cnt
        cnt+=1
        print('cnt=',cnt)
    return inside
f=external3('hello')
f('python')
f('vscode')
f('github')
