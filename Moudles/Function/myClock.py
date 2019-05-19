"""
定义时钟类，注意给外部提供哪些接口
Date:2019.5.19
"""

from time import time,localtime,sleep
import os
class Clock():
    def __init__(self,hour=0,min=0,sec=0):
        self.hour=hour
        self.min=min
        self.sec=sec
        
    @classmethod       #类方法，用于获取本地时间，通常用来初始化时钟类
    def get_NowTime(cls):
        nowtime=localtime(time())
        return cls(nowtime.tm_hour,nowtime.tm_min,nowtime.tm_sec)

    def __run(self):
        self.sec+=1
        if self.sec==60:
            self.sec=0
            self.min+=1
            if self.min==60:
                self.min=0
                self.hour+=1
                if self.hour==24:
                    self.min=0
                    self.hour=0

    def __showTime(self):
        print('%2d:%2d:%2d'%(self.hour,self.min,self.sec))
                    
    def runtime(self):  #只留了这一个公共接口，
        while True:
            os.system('cls')
            self.__showTime()
            sleep(1)
            self.__run()

    
def main():
    c=Clock().get_NowTime()
    c.runtime()

if  __name__ == "__main__":
    main()
