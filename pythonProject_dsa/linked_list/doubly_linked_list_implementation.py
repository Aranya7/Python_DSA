class DoLiLi():
    def __init__(self, value):
        self.head={"value": value, "next": None, "prev":None}
        self.length=1
        self.tail=self.head

    def append(self, value):
        self.newNode={"value": value, "next": None, "prev": None}
        self.tail["next"]=self.newNode
        self.newNode["prev"]=self.tail
        self.tail = self.newNode
        self.length+=1

    def display(self):
        data=self.head
        while data:
            print(data["value"], end=" <-> ")
            data=data["next"]
        print("None")

    def prepend(self,value):
        self.newNode={"value": value, "next": None, "prev": None}
        self.newNode["next"]=self.head
        self.head["prev"]=self.newNode
        self.head=self.newNode
        self.length+=1

    def insert(self,index,value):
        self.newNode={"value": value, "next": None, "prev": None}
        counter=0
        data=self.head
        while data:
            if counter==index-1:
                self.newNode["next"]=data["next"]
                self.newNode["prev"]=data
                data["next"]["prev"]=self.newNode
                data["next"] = self.newNode
                self.length+=1
                break
            counter+=1
            data=data["next"]

    def remove(self, index):
        counter=0
        data=self.head
        while data:
            if counter==index-1:
                data["next"]=data["next"]["next"]
                data["next"]["prev"]=data
                self.length-=1
            data=data["next"]
            counter+=1

abc=DoLiLi(10)
abc.append(5)
abc.append(15)
abc.prepend(1)
abc.insert(2, 27)
abc.remove(2)
#abc.append(77)
#abc.append(101)
abc.display()
print(f"Length: {abc.length}")
print(f"Head: {abc.head}")
print(f"Tail: {abc.tail}")

# 10 -> 5 -> 15 -> 17