#PQ - Max Heap
#https://www.udemy.com/course/master-the-coding-interview-big-tech-faang-interviews/learn/lecture/22374636#questions
class PriorityQueue():
    def __init__(self):
        self.heap=[]

    def swapp(self,i,j):
        temp=self.heap[i]
        self.heap[i]=self.heap[j]
        self.heap[j]=temp
        return [self.heap[i],self.heap[j]]

    def parent(self, i):
        return (i-1)//2

    def lchild(self,i):
        return (i*2)+1

    def rchild(self,i):
        return (i*2)+2

    def peek(self):
        return self.heap[0]

    def push(self, value):
        self.heap.append(value)
        i=len(self.heap)-1
        while i>0:
            if self.heap[i]>self.heap[self.parent(i)]:
                self.swapp(i,self.parent(i))
                # temp=self.heap[i]
                # self.heap[i]=self.heap[self.parent(i)]
                # self.heap[self.parent(i)]=temp
                i=self.parent(i)
            else:
                break
        return self.heap

    def delete(self, value):
        a=self.heap.pop()
        i=-150
        for j in range(0, len(self.heap)):
            if self.heap[j]==value:
                i=j
        self.heap[i] = a
        while self.lchild(i)<len(self.heap) or self.rchild(i)<len(self.heap):
            if self.heap[self.lchild(i)]>self.heap[self.rchild(i)]:
                if self.heap[self.lchild(i)]>self.heap[i]:
                    self.swapp(self.lchild(i), i)
                    i=self.lchild(i)
            elif self.heap[self.lchild(i)]<self.heap[self.rchild(i)]:
                if self.heap[self.rchild(i)] > self.heap[i]:
                    self.swapp(self.rchild(i), i)
                    i = self.rchild(i)
        return self.heap
abc=PriorityQueue()
abc.push(15)
abc.push(10)
abc.push(5)
abc.push(7)
abc.push(20)
abc.push(40)
print(abc.peek())
print(f"Parent: {abc.parent(len(abc.heap)-1)}")
print(abc.heap)
print("##########################################")
#print(abc.delete(15))
#print(abc.heap)