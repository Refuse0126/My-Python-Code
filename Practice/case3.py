"""
泳池过道和围墙造价练习
Date：2019.5.17
"""
class circle():
    from math import pi
    def __init__(self,r):
        self.r=r
    def getc(self):
        return (2*self.pi*self.r)
    def gets(self):
        return (self.pi*self.r*self.r)

class guodao(circle):
    def __init__(self,r,width):
        circle.__init__(self,r+width)
        self.rr=r
    def getPay(self):
        return (self.gets()-circle(self.rr).gets())*25

class weiqiang(circle):
    def __init__(self,r,width):
        circle.__init__(self,r+width)
    def getPay(self):
        return 32.5*self.getc()

def main():
    r=int(input('请输入泳池的半径和过道宽度：'))
    w=int(input('请输入过道的宽度：'))
    print('泳池过道的造价为：%.2f元'%guodao(r,w).getPay())
    print('围墙的造价为：%.2f元'%weiqiang(r,w).getPay())

if  __name__ == "__main__":
    main()
