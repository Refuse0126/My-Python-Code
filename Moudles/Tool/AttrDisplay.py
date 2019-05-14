"""
工具类：重写__str__，以打印类的所有属性，如果以后写的类，需要此功能，直接继承这个工具类即可
"""
class AttrDisplay:
    "a common display tool"
    def gatherAttrs(self):
        attrs=[]
        for key in sorted(self.__dict__):
            attrs.append('%s=%s'%(key,getattr(self,key)))
        return ','.join(attrs)
    def __str__(self):
        return '[%s: %s]'%(self.__class__.__name__,self.gatherAttrs())

def main():
    class TopTest(AttrDisplay):
        count=0
        def __init__(self):
            self.attr1=TopTest.count
            self.attr2=TopTest.count+1
            TopTest.count+=2
    class SubTest(TopTest):
        pass
    X,Y=TopTest(),SubTest()
    print(X)
    print(Y)

if __name__=='__main__':
    main()
