class Node():
    def __init__(self, value):
        self.value=value
        self.next=None

class Queue():
    def __init__(self):
        self.first=None
        self.last=None
        self.length=0

    def peek(self):
        return self.first

    def enqueue(self, value):
        nn = Node(value)
        if self.length == 0:
            self.first = nn
        else:
            self.last.next = nn
        self.last = nn
        self.length += 1


    def dequeue(self):
        self.first=self.first.next
        self.length-=1

    def display(self):
        data=self.first
        while data:
            print(data.value, end=" ")
            data=data.next

abc=Queue()
abc.enqueue(1)
abc.enqueue(2)
abc.enqueue(3)
abc.enqueue(4)
abc.enqueue(5)
abc.display()
print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
abc.dequeue()
abc.display()
print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
abc.dequeue()
abc.display()
# print(abc.last.value)
# abc.dequeue()

#print(abc.last.value)