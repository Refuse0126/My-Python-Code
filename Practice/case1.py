"""
输入学生成绩，并计算平均分
Date：2019.5.15
"""
def main():
    scroe=[None]*3
    for i in range(0,3):
        tmp=dict()
        tmp['name']=input('请输入第%d个同学的姓名：'%(i+1))
        tmp['scr']=int(input('他的成绩为：'))
        scroe[i]=tmp
    print('成绩录入完毕！情况如下：\n',scroe)
    x=sum([x['scr'] for x in scroe])/3
    print('所有同学的平均分为：%.2f'%x)

if __name__ == "__main__":
    main()
