"""
用递归实现遍历嵌套列表，还没想到一种能万能遍历方式def recursion(fun,Date)，能够实现遍历，并执行fun函数,
Date：2019.5.16
"""
def recursion_list(l):              #1.自定义递归函数一层一层解析
    result=[]
    for item in l:
        if isinstance(item,list):
            for i in recursion_list(item):
                result.append(i)
        else:
            result.append(item)
    return result
    
def main():
    a=[1,[2,3],[4,5,6],[7,8,9,10]]
    print(recursion_list(a))

if  __name__ == "__main__":
    main()
