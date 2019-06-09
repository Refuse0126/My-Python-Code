def fun4():
    #1.4 heapq堆模块
    import heapq
    nums=[-1,3,0,-5,6,1,4,25,20,23,8,-9]
    largest3=heapq.nlargest(3,nums)
    print(largest3)
    smallest3=heapq.nsmallest(3,nums)
    print(smallest3)
    print(min(nums))
    heapq.heapify(nums) #列表元素以堆的形式排列，heap[0]始终是堆内最小的元素
    print(nums[0])
    #Ps效率上来说：（1）找列表内最大最小的元素-》min，max （2）找较小N个最大最小元素-》largest，smallest （3）找较大N最大最小元素-》排序分片

import heapq
class PriorityQueue():
        def __init__(self,queue=[]):
            self.__queue=queue
            self.__index=0
        def push(self,val,priority):
            #函数原型是heappush(queue,val)，这里插入的元素是一个元组，可以指定优先级，并且对于相同优先级的元素可以通过索引来操作
            heapq.heappush(self.__queue,(priority,self.__index,val)) 
            self.__index+=1
        def pop(self):
            print(heapq.heappop(self.__queue))

def fun5():
    #1.6用heapq模块实现优先级队列,每次操作（例如pop）都是对优先级最高的元素
    q=PriorityQueue()
    q.push('hello',1)
    q.push('vscode',2)
    q.push('python',1)
    q.pop()
    q.pop()
    q.pop()
if __name__=='__main__':
    fun4()
    fun5()
