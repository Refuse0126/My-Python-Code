"""
介绍文件、文件夹的操作常用到的os模块和shutil模块
Date:2019.6.12
"""
import os
import shutil
#基本用法
def fun1():
    cwd=os.getcwd()             #获取当前工作目录 !!!!!!这里要注意，返回的是调用目录，而不是脚本所在的目录
    print(os.listdir(cwd))      #返回目录下所有文件
    print(os.path.isdir(cwd))    #判断是否是目录
    file=os.path.join(cwd,'main.py')#将路径和文件名拼接成绝对路径的文件名
    print(os.path.isfile(file)) #判断是否是文件
    print(os.path.exists(file)) #判断路径是否存在

    pathname,filename=os.path.split(file)      #拆分路径名和文件名
    print(pathname,filename)    
    print(os.path.splitext(file))   #分离拓展名
    pathname=os.path.dirname(file)  #返回路径名
    filename=os.path.basename(file) #返回文件名
    file='C:/Users/123/Desktop/VScode/python/WorkSpace/main.py'
    print(os.stat(file))            #返回文件属性
    print(os.path.getsize(file))    #获取文件大小
    print(os.path.getmtime(file))         #返回最后修改时间，getatime-最后一次访问时间  getctime-最后元数据更改时间

#找出目录中某个类型文件的几种方法
def fun2():
    dir=os.getcwd()
    filenames=[file for file in os.listdir(dir) if file.endswith('.txt')]
    print(filenames)

    import fnmatch
    filenames=[file for file in os.listdir(dir) if fnmatch.fnmatch(file,'*.txt')] #这里要使用通配符*
    print(filenames)

    import glob
    filenames=glob.glob('*.txt')
    print(filenames)


#应用：查找某个路径下所有的某个类型文件(两种方式，一种listdir递归，一种os.walk遍历)
def fun3():
    def mylistdir(dir,tag):#其中tag为关键词，可以是拓展名，也可以是关键字，类似Ctrl+find
        import fnmatch
        for item in os.listdir(dir):
            tempdir=os.path.join(dir,item) #!!!!!!!!!!!!!!!!!!!这里要使用全路径进行类型检测，才能实现递归的效果！！！！！！！！！！！！！！
            if os.path.isdir(tempdir):
                yield from mylistdir(tempdir,tag)
            elif fnmatch.fnmatch(item,tag):
                yield item
           
    dir=os.getcwd()
    print(list(mylistdir(dir,'*.py')))

def fun4():
    def get_dir_files(dir, suffix): # 查找根目录，文件后缀 
        res = []
        for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
            for filename in files:
                name, suf = os.path.splitext(filename) # =>文件名,文件后缀
                if suf == suffix:
                    #res.append(os.path.join(root, filename)) # =>吧一串字符串组合成路径
                    res.append(filename)
        return res
    print(get_dir_files('./','.py'))

if __name__=='__main__':
    fun1()
    fun2()
    fun3()
    fun4()
   
   

    
