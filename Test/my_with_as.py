"""
Date:2019.5.19
"""
class MyEniormentManager():
    """
    自定义环境管理协议，日后有需要可以继承用来traceback
    """
    def __enter__(self):                                    #环境管理器入口，并返回一个对象来支持环境管理协议
        print('entry the my-enviorment-manager....')
        return self     
    def __exit__(self,exc_type,exc_value,exc_traceback):    #无异常时，三个参数都返回None,否则会携带异常相关的参数
        if exc_type is None:
            print('exited myu-enviorment-manager normally!')
        else:
            print('rasie an exception',exc_type)
            return True                                    #捕获异常后，默认返回False，异常上传顶层终止程序，返回True则修复异常

    

if  __name__ == "__main__":
    with MyEniormentManager() as x:
        pass
    with MyEniormentManager() as x:
        raise TypeError
    
