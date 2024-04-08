class NewNode():
    def __init__(self,value):
        self.value=value
        self.next=None


class LinLi():

    def __init__(self, value):
        self.head=NewNode(value)
        self.tail=self.head
        self.length=1

    def append(self, value):
        nn=NewNode(value)
        self.tail.next=nn
        self.tail=nn

    def display(self):
        data=self.head
        while data:
            print(data.value, end=" -> ")
            data=data.next
        print(None)

    def prepend(self, value):
        nn=NewNode(value)
        nn.next=self.head
        self.head=nn
        self.length+=1

    def insert(self, index, value):
        nn=NewNode(value)
        counter=0
        data=self.head
        while data:
            if counter==index-1:
                nn.next=data.next
                data.next=nn
                self.length+=1
            data=data.next
            counter+=1

    def remove(self, index):
        counter=0
        data=self.head
        while data:
            if counter==index-1:
                data.next=data.next.next
                self.length-=1
            data=data.next
            counter+=1

    def reverse(self):
        prev=None
        curr=self.head
        next=None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        curr=self.head
        while curr.next:
            curr=curr.next
        self.tail=curr

def reverseBetween(head, left=2, right=4):
    curr=head
    start=head
    counter=1
    while counter<left:
        start=curr
        curr=curr.next
        counter+=1

    prev=None
    tail=curr
    while counter>=left and counter <=right:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
        counter+=1

    start.next=prev
    tail.next=next
    if left>1:
        return head
    else:
        return prev

abc = LinLi(1)
abc.append(2)
abc.append(3)
abc.append(4)
abc.append(5)
#abc.prepend(3)
#abc.prepend(1)
#abc.insert(2, 17)
#abc.remove(3)
#print(abc.head.value)
#print(abc.tail.value)
#abc.display()
#abc.reverse()
abc.display()
print(reverseBetween(abc.head))
abc.display()
