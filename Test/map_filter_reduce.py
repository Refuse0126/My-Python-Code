"""
展示了常用几个函数式编程工具的用法
Date:2019.5.16
"""
a=[1,2,3]
b=[4,5,6]
print(list(map((lambda x:x+1),a)))      #针对一个序列，传入的必须是一元操作函数
print(list(map((lambda x,y:x+y),a,b)))  #同理，传入几个序列，传入的函数必须是几元操作函数

print(list(filter((lambda x:x>2),a)))   #传入的函数需要返回逻辑变量，真则保留，最后收集到一个新列表中

from functools import reduce
print(reduce((lambda x,y:x+y),a))       #传入二元操作函数，并且将每一次的结果用到下一次操作，最终返回一个结果

