"""
综合类小游戏
Date：2019.5.19
"""

from abc import ABCMeta,abstractmethod
from random import randint

class Fighter(metaclass=ABCMeta):
    def __init__(self,hp=100,mp=100):
        self.__hp=hp
        self.__mp=mp

    #获取和设置hp和mp状态
    @property                  
    def hp(self):
        return self.__hp
    @property
    def mp(self):
        return self.__mp
    @hp.setter
    def hp(self,hp):
        self.__hp=hp if hp>0 else 0
    @mp.setter
    def mp(self,mp):
        self.__mp=mp

    #定义攻击模式
    def attack(self,other):         
        index=randint(0,4)
        skill=self.skill[index-1]
        damage=self.damage[skill]
        print('%s使用了%s:'%(self.__class__.__name__,skill),end='\t')
        print('%s受到了%d点伤害!'%(other.__class__.__name__,damage))
        hp=other.hp
        other.hp=(hp-damage)    

    #常用的方法
    def is_alive(self):
        return self.__hp>0
    def __str__(self):
        return '~~~%s~~~:\n'%self.__class__.__name__ + '\t生命值：%d\n'%self.__hp +'\t魔法值：%d\n'%self.__mp

class Huajian(Fighter):
    damage={'普通攻击':8,'商阳指':30,'阳明指':32,'兰摧玉折':35}
    skill=['普通攻击','商阳指','阳明指','兰摧玉折']

class Cangyun(Fighter):
    damage={'普通攻击':10,'盾猛':25,'斩刀':30,'绝刀':40}
    skill=['普通攻击','盾猛','斩刀','绝刀']

def main():
    huajian=Huajian()
    cangyun=Cangyun()
    huihe=0
    print(huajian)
    print(cangyun)
    print('战斗开始！！！！！！！！')
    while huajian.is_alive() and cangyun.is_alive():
        huihe+=1
        print('第%d个回合：'%huihe)
        who=randint(0,1)
        if who==0:
            huajian.attack(cangyun)
        else:
            cangyun.attack(huajian)
        print(huajian)
        print(cangyun)
    winner=huajian if huajian.is_alive() else cangyun
    print('-'*20)
    print('经过了%d个回合，%s获得了胜利！！！！'%(huihe,winner.__class__.__name__))


if  __name__ == "__main__":
    main()



