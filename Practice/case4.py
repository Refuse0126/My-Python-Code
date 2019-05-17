"""
面向对象的猜数字游戏
Date:2019.5.17
"""
class game():
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.cnt=0
        self.done=False
    def randomint(self):
        from random import randint
        self.anwser=randint(self.start,self.end)
    def check(self,temp):
        if temp==self.anwser:
            self.yes()
            self.done=True
        elif temp>self.anwser:
            self.more()
            self.cnt+=1
        else:
            self.less()
            self.cnt+=1
    def yes(self):
        print('恭喜你，只猜了%d次就猜对啦！'%self.cnt)
    def more(self):
        print('好可惜呀，有点大了！再试一次吧')
    def less(self):
        print('好可惜呀，有点小了！再试一次吧')

def main():
    start=int(input('请输入游戏边界上限：'))
    end=int(input('请输入游戏边界下限：'))
    g=game(start,end)
    g.randomint()
    print('开始游戏吧！我已经准备好啦')
    while True:
        temp=int(input('你猜有多大'))
        g.check(temp)
        if g.done:break
    print('游戏结束，byebye')

if  __name__ == "__main__":
    main()
