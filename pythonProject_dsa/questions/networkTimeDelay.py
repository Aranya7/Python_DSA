#https://leetcode.com/problems/network-delay-time/
#https://www.udemy.com/course/master-the-coding-interview-big-tech-faang-interviews/learn/lecture/22505068#questions
class min_PQ(): # ACTUAL SOLUTION BELOW THIS CLASS
    def __init__(self):
        self.heap=[]

    def peek(self):
        return self.heap[0]

    def parent(self,i):
        return (i-1)//2

    def lchild(self,i):
        return (i*2)+1

    def rchild(self,i):
        return (i*2)+2

    def swapp(self,i,j):
        temp=self.heap[i]
        self.heap[i]=self.heap[j]
        self.heap[j]=temp
        return [self.heap[i],self.heap[j]]

    def push(self, value):
        self.heap.append(value)
        i=len(self.heap)-1
        while i>0:
            if self.heap[i]<self.heap[self.parent(i)]:
                self.swapp(i, self.parent(i))
                i=self.parent(i)
            else:
                break
        return self.heap

    def pop(self):
        return self.heap.pop(0)

    def delete(self,value):
        a=self.heap.pop()
        x=float('-inf')
        for i in range(len(self.heap)):
            if self.heap[i]==value:
                x=i
                break
        self.heap[x]=a
        while self.lchild(x)<len(self.heap) or self.rchild(x)<len(self.heap):
            if self.heap[self.lchild(x)]<self.heap[self.rchild(x)]:
                if self.heap[self.lchild(x)]<self.heap[x]:
                    self.swapp(self.lchild(x),x)
                    x=self.lchild(x)
            elif self.heap[self.rchild(x)]<self.heap[self.lchild(x)]:
                if self.heap[self.rchild(x)]<self.heap[x]:
                    self.swapp(x, self.rchild(x))
                    x=self.rchild(x)

        return self.heap

def networkDelayTime(times, n, k):
    adjist=[[] for _ in range(n)]
    for i in times:
        adjist[i[0]-1].append([i[1]-1,i[2]])
    distances=[float('inf') for _ in range(n)]

    heap=min_PQ()
    heap.push(k-1)
    while len(heap.heap)!=0:
        currver=heap.pop()
        for i in adjist[currver]:
            neib=i[0]
            weight=i[1]
            if distances[currver]+weight<distances[neib]:
                distances[neib]=distances[currver]+weight
                heap.push(distances[neib])
    ans = max(distances)
    return ans if ans!=float('inf') else -1



times=[[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6],[3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(networkDelayTime(times, 5, 1))
