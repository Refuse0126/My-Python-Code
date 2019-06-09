"""
Date:2019.6.9
"""
#1.12对序列中的元素进行计数统计
import collections
def fun1():
    nums=[1,2,5,4,3,7,3,2,4,3,9]
    cnt_nums=collections.Counter(nums)
    print(cnt_nums.most_common(3))

    nums2=[2,3,5,6,5,7,5,8,9,2,3]
    cnt_nums.update(nums2)
    print(cnt_nums.most_common(3))
    

if __name__=='__main__':
    fun1()
    
