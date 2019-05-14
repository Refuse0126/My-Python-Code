"""
展示了shelve模块的基本用法
将数据对象按照键存储到db文件中，再按照存入键的顺序把数据对象提取出来
Date：2019.5.14
"""
from person import Person,Manager
bob=Person('Bob Smith')
sue=Person('Sue Jones',job='dev',pay=100000)
tom=Manager('Tom Jones',50000)

import shelve
db=shelve.open('persons_db')    #db is a dict
for obj in (bob,sue,tom):
    db[obj.name]=obj            #key_store
db.close()


#import shelve
#db=shelve.open('persons_db')
#for key in db:
#    print(key,'=>',db[key])
