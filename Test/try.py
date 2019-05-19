"""
展示了try语句的基本用法
Date：2019.5.19
"""

class MyError1(Exception):
    def __init__(self,error_string=None):
        self.error_string=error_string
    def __str__(self):
        return self.__class__.__name__

class MyError2(Exception):
    def __init__(self,error_string=None):
        self.error_string=error_string
    def __str__(self):
        return self.__class__.__name__

def action():
    #raise MyError1()
    raise MyError2('this is MyError(args)')


def main():
    try:
        action()
    except MyError1 as error1:                  
        print(error1)
        #rasie                                  #必要工作完成后，可以选择继续上传当前异常到顶层，取决于这个异常是否有必要终止程序
    except MyError2 as error2:                  #as模式，可以使得处理器能够访问到异常类实例中的属性，这个实例是在try代码块中产生的异常类实例,可能携带参数
        print(error2.error_string)
    else:
        print('great! action() has no error!')   #没有以上异常（是否有其他异常不管）即会进入else，
    finally:                                    #不管异常与否，定义最终清理工作
        print('after action~~')

if  __name__ == "__main__":
    main()
