"""
机选双色球
"""
from random import randint
def randm_select():
    red=[]
    for i in range(6):
        tmp=randint(1,32)
        while True:
            if not tmp in red:
                break
            else: 
                tmp=randint(1,32)
        red.append(tmp)
    red.sort()
    blue=randint(1,12)
    red.append(blue)
    print('此次机选号码为：',red)

def main():
    n=int(input('你要机选机组号码？'))
    for i in range(n):
        randm_select()

if  __name__ == "__main__":
    main()
