# Enqueue:-
# S1 -> S2
# S1.push(value)
# S1 <- S2
# Deququq:-
# S1.pop()

class StackA():
    def __init__(self):
        self.top=[]
        self.length=len(self.top)

    def peek(self):
        if len(self.top)==0:
            return None
        else:
            return self.top[len(self.top)-1]

    def popa(self):
        if len(self.top) == 0:
            return None
        self.length = len(self.top) - 1
        return self.top.pop()

    def push(self, value):
        self.top.append(value)
        self.length = len(self.top)+1
class Queue():
    def __init__(self):
        self.s1=StackA()
        self.s2=StackA()

    def peek(self):
        return self.s1.peek()

    def enqueue(self, value):
        while self.s1.length!=0:
            self.s2.push(self.s1.popa())

        self.s1.push(value)

        while self.s2.length!=0:
            self.s1.push(self.s2.popa())

    def dequeue(self):
        return self.s1.popa()

abc=Queue()
abc.enqueue(1)
abc.enqueue(2)
abc.enqueue(3)
abc.enqueue(4)
abc.enqueue(5)
print(abc.s1.top)
#print(abc.)
abc.dequeue()
print(abc.s1.top)
#print(abc.s2)


# class Queue():
#     def __init__(self):
#         self.s1=[]
#         self.s2=[]
#
#     def peek(self):
#         return self.s1[len(self.s1)-1]
#
#     def enqueue(self, value):
#         while len(self.s1)!=0:
#             self.s2.append(self.s1.pop())
#
#         self.s1.append(value)
#
#         while len(self.s2)!=0:
#             self.s1.append(self.s2.pop())
#
#     def dequeue(self):
#         #self.first.pop(len(self.first)-1)
#         pass