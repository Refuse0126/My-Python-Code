"""
Date:2019.7.4
"""
#1.自定义字符串的输出格式-类内定义__fromat__()方法，
class myDate:
    format_dict = {
        "ymd": "{0.year}-{0.month}-{0.day}"   #这里一定要是0，用于后面fmt.format(self)，能够匹配0和self，
    }
    def __init__(self,year,month,day):
         self.year=year
         self.month=month
         self.day=day
    def __format__(self,format_sepc="ymd"):
         fmt=self.format_dict[format_sepc]
         return  fmt.format(self)
def fun1():
    d = myDate(2019, 7, 4)
    print(format(d, "ymd"))
    
if __name__=='__main__':
    fun1()
