class Node():
    def __init__(self, value):
        self.value=value
        self.next=None

class Stack():
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0

    def display(self):
        data=self.top
        while data:
            print(data.value, end=" ")
            data=data.next

    def peek(self):
        return self.top
    def push(self, value):
        nn=Node(value)
        if self.length==0:
            self.top=nn
            self.bottom=nn
        else:
            # ab=self.top
            # self.top = nn
            # self.top.next=ab
            nn.next=self.top
            self.top=nn
        self.length+=1
        return self.top

    def pop(self):
        self.top=self.top.next
        self.length-=1
# 10,14,16,19,20
# B        T
abc=Stack()
abc.push(1)
abc.push(2)
abc.push(3)
abc.push(4)
abc.push(5)
print(F"Top: {abc.top.value}")
print(F"Bottom: {abc.bottom.value}")
print(F"Length: {abc.length}")
abc.display()
abc.pop()
print("#################")
abc.display()
abc.pop()
print("#################")
abc.display()
print(abc.peek().value)