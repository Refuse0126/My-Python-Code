"""
查找某路径下所有指定类型的文件（两种方式，一种listdir递归，一种os.walk遍历）
Date：2019.6.24
"""

def mylistdir(dir,tag):#其中tag为关键词，可以是拓展名，也可以是关键字，类似Ctrl+find
    import os
    import fnmatch
    for item in os.listdir(dir):
        tempdir=os.path.join(dir,item) #!!!!!!!!!!!!!!!!!!!这里要使用全路径进行类型检测，才能实现递归的效果!!!!!!!!!!!!!!!!
        if os.path.isdir(tempdir):
            yield from mylistdir(tempdir,tag)
        elif fnmatch.fnmatch(item,tag):
            yield item


def get_dir_files(dir, suffix): # 查找根目录，文件后缀 
    import os
    res = []
    for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
        for filename in files:
            name, suf = os.path.splitext(filename) # =>文件名,文件后缀
            if suf == suffix:
                #res.append(os.path.join(root, filename)) # =>吧一串字符串组合成路径
                res.append(filename)
    return res

if __name__=='__main__':
    print(list(mylistdir('./','*.py')))  #fnmatch需要有通配符*
    print(list(get_dir_files('./','.py')))
   
