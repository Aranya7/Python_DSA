class min_PQ():
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


abc=min_PQ()
abc.push(15)
abc.push(10)
abc.push(5)
abc.push(7)
abc.push(20)
abc.push(40)
abc.delete(7)
print(abc.peek())
#print(f"Parent: {abc.parent(len(abc.heap)-1)}")
print(abc.heap)
