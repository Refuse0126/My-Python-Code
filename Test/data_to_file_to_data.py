"""
展示了常用的数据和文本之间的转换方法
数据格式化转换工具pickle的基本用法:依次写入（读取数据），似乎无法一次性完成
Date:2019.5.15
"""
import pickle
data1=[1,2,3]
data2={'name':'Bob','age':20}
with open('test.pkl','wb') as f:
    pickle.dumps(data1,f)
    pickle.dump(data2,f)

with open('test.pkl','rb') as f:
    print(pickle.load(f))
    print(pickle.load(f))
    
data1=[1,2,3]
data2={'name':'Bob','age':20}
with open('test.txt','w') as f:
    print(data1,file=f)
    print(data2,file=f)
print([eval(line.rstrip()) for line in open('test.txt','r')])
