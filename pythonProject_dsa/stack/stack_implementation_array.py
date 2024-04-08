class StackA():
    def __init__(self):
        self.top=[]

    def peek(self):
        if len(self.top)==0:
            return None
        else:
            return self.top[len(self.top)-1]

    def popa(self):
        if len(self.top) == 0:
            return None
        self.top.pop()

    def push(self, value):
        self.top.append(value)


abc=StackA()
abc.push(1)
abc.push(2)
abc.push(3)
abc.push(4)
abc.push(5)
print(F"Top: {abc.top}")
# abc.display()
abc.popa()
# print("#################")
#abc.display()
abc.popa()
# print("#################")
# abc.display()
print(abc.peek())