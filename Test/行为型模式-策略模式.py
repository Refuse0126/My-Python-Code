from abc import ABCMeta,abstractmethod
"""
Date:2021.1.10
7.策略模式
内容：将不同的算法进行包装，使其可以相互转化，使得用户仅仅关注算法-数据即可
"""

class Strategy_A():
    def excute(self, data):
        a,b = data
        print(a+b)
class Strategy_B():
    def excute(self, data):
        a,b = data
        print(a*b)

class Hander:
    def excute(self,s,*data):
        #额外逻辑
        s.excute(data)

h = Hander()
h.excute(Strategy_A(),2,3)
h.excute(Strategy_B(),2,3)

