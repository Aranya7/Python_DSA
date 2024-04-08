class LiLi():
    debug=True
    def __init__(self, value):
        self.head = {"value": value, "next": None}
        self.length = 1
        self.tail=self.head


    def append(self, value):
        self.newNode={"value": value, "next": None}
        self.tail["next"]=self.newNode
        self.tail=self.newNode
        self.length+=1
        return

    def prepend(self, value):
        self.newNode={"value": value, "next":None}
        self.newNode["next"]=self.head
        self.head=self.newNode
        self.length+=1
        return self

    def display(self):
        currentNode=self.head
        while currentNode!=None:
            print(currentNode["value"], end=" -> ")
            currentNode=currentNode["next"]
        print("None")

    def insert(self, index, value): ## Zero based indexing - For one based indexing, make data_tracker 1
        if index==0:
            self.prepend(value)
        if index>self.length:
            self.append(value)
        self.newNode={"value": value, "next": None}
        data_tracker=0
        data=self.head
        while data:
            if data_tracker==index-1:
                self.newNode["next"]=data["next"]
                data["next"]=self.newNode
                self.length+=1
                break
            data=data["next"]
            data_tracker+=1

    def remove(self, index):
        counter=0
        data=self.head
        if index==0:
            self.head=self.head["next"]
            self.length-=1
        while data:
            if counter==index-1:
                data["next"]=data["next"]["next"]
                self.length-=1
                break
            data=data["next"]
            counter+=1

#newtail={"value": 10, "next":None}
#newhead={"value": 10, "next":None}

    def reverse(self):
        prev=None
        curr_data=self.head
        next=None
        while curr_data:
            next=curr_data["next"]
            curr_data["next"]=prev
            prev=curr_data
            curr_data=next
        self.head=prev
        #self.tail = self.head
        while self.tail["next"]:
            self.tail = self.tail["next"]
        return self.head


abc = LiLi(10)
abc.append(5)
abc.append(15)
#print(abc.length)
abc.prepend((1))
#print(abc.head)
abc.display()
abc.insert(2, 27)
abc.display()
abc.remove(0)
abc.display()
print(f"head={abc.head}")
print(f"tail={abc.tail}")
abc.reverse()
print("##########################")
print(f"Head after reversing: {abc.head}")
print(f"Tail after reversing: {abc.tail}")
#print(abc.tail)




#
# class LiLi():
#     def __init__(self, value):
#         self.head={"value":value, "next":None}
#         self.length=1
#         self.data=[]
#
#
#     def append(self, value):
#         if self.length==1:
#             self.tail={"value":value, "next":None}
#             self.head["next"]=value
#             self.length+=1
#
#         elif self.length>1:
#             self.data.append(self.tail)
#             self.data[len(self.data)-1]["next"]=value
#             self.tail={"value":value, "next":None}
#             self.length+=1
#
#
#
# abc=LiLi(10)
# abc.append(5)
# abc.append(16)
# abc.append(77)
# abc.append(171)
# print(abc.head)
# print(abc.data)
# print(abc.tail)
#
# # abc=[{"value": 10, "next":None}]
# # abc[0]["next"]=25
# # print(abc[0]["value"])