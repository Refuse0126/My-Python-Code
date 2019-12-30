"""
2019.12.30
如何获取文件的最后一行，而不用很low的rendlines
f.seek(offs,2)从从后向前移动光标
f.seek(offs,1)相对上个光标位置
f.seek(offs,0)默认从头开始
"""
with open('hello.txt','rb') as f:
    for i in f:
        offs=-5
        while True:
            f.seek(offs,2)
            data=f.readlines()
            if len(data) > 1:
                print('Last Line is : ',data[-1].decode())
                break
            offs*=2
