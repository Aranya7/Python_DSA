class HashMapp():
    def __init__(self, size):
        self.size=size
        self.data=[None]*size

    def hashh(self, key):
        hashv=0
        for i in range(0, len(key)):
            hashv=(hashv+ord(key[i])*i)%len(self.data) #instead of len(self.data), we can use self.size also here

        return hashv

    def sethm(self,key,value):
        a=self.hashh(key)
        #print(f"hash value={a}")
        if not self.data[a]:
            self.data[a]=[]
            self.data[a].append([key,value])
        else:
            self.data[a].append([key, value])
        # The above if-else block checks if the hashed address in array is empty. if yes, it initializes an array there and appends key value.
        # If no (hashed address in array is not empty), it appends to the existing data.
        return self.data[a]


    def gethm(self,key):
        a = self.hashh(key)
        #print(self.data)
        for i in self.data[a]:
            if i[0]==key:
                return i[1]
        return f"{key} Not found in HashTable"

    def keyshm(self):
        keys=[]
        for i in range(0, self.size):
            if self.data[i]:
                for a in self.data[i]:
                    keys.append(a[0])
        return keys




aabb=HashMapp(2)
aabb.sethm("grapes", 1000)
aabb.sethm("apples", 54)
print(aabb.gethm("grapes"))
print(aabb.gethm("apples"))
print(aabb.gethm("orange"))
print("####################################################")
print(aabb.keyshm())