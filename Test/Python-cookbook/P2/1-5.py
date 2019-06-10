"""
Date:2019.6.10
"""
#2.1 任意多个个分割符拆分字符串->re.split()
def fun1():
    import re
    line='hello python,are@you;ok'
    words=re.split('[;,@\s]\s*',line)  #捕获组在[]中，则丢弃分隔符
    print(words)

#2.2字符串开头结尾做简单的文本匹配->str.startwith/endwith
def fun2():
    line='http://www.baidu.com.cn'
    print(line.startswith('http'),line.endswith('cn'))
    flag=['http','ftp']
    print(line.startswith(tuple(flag))) #将可选的匹配字段放进元组中，可以同时检查

#2.3通配符做字符串匹配入门->fnmatch(兼容大小写)/fnmatchcase（严格遵守大小写）
def fun3():
    import fnmatch
    print(fnmatch.fnmatch('test.txt','*.txt'),
          fnmatch.fnmatch('somebody_birthday2019.csv','*birthday[0-9]*.csv'))
    print(fnmatch.fnmatch('test.txt','*.TXT'),fnmatch.fnmatchcase('test.txt','*.TxT'))

#2.4  re模块入门
def fun4():
    line='2019/6/10'
    import re
    mode=re.compile(r'(\d+)/(\d+)/(\d+)') #模式预编译
    result=mode.match(line)               #文本匹配，match只匹配字符串开头
    print(result) 
    print(result.groups())                #定义正则表达式引入捕获组，可以保留每个组的内容
    result=re.findall(r'(\d+)/(\d+)/(\d+)','Date:2019/6/10')#findall方法可以匹配全文
    print(result)

#2.5查找和替换re.sub('模式','替换模式','文本'，flags=re.IGNORECASE)不区分大小写
def fun5():
    line='2019/6/10'
    print(line.replace(r'/','-')) #str.replace实现简单的文本替换
    import re
    result=re.sub(r'(\d+)/(\d+)/(\d+)',r'\1-\2-\3',line)#\1表示\d转换后的顺序，取决前面定义捕获组的数量
    print(result)


if __name__=='__main__':
    fun1()
    fun2()
    fun3()
    fun4()
    fun5()
    
    
