# class Triangle():
#
#     def __init__(self, name, s1, s2, s3):
#         self.name = name
#         self.s1 = s1
#         self.s2 = s2
#         self.s3 = s3
#
#     def dosc(self):
#         print(f"i am a triangle, my sides are {self.s1}, {self.s2}, {self.s3}")
#
#
# class Pm(Triangle):
#
#     def peri(self):
#         self.perimeter = self.s1 + self.s2 + self.s3
#         return self.perimeter
#
# def main():
#     abc = Pm("t1", 10, 7, 3)
#     print(abc.peri())
#     print(type(abc))
#     abc.dosc()
#
# if __name__ == "__main__":
#     main()

class MyArray:
    def __init__(self):
        self.length=0
        self.data={}

    def get(self,index):
        return self.data.get(index)

    def push(self, item):
        self.data[self.length]=item
        self.length+=1
        return self.length

    def pop(self):
        ab=self.data[self.length-1]
        del self.data[self.length-1]
        self.length-+1
        return  ab

    def delete(self, index):
        item=self.data[index]
        self.shift_items(index)
        return item

    def shift_items(self,index):
        for i in range(index, self.length-1):
            self.data[i]=self.data[i+1]
        del self.data[self.length-1]
        self.length-=1


def main():
    abc = MyArray()
    abc.push("Ari")
    abc.push("Ari2")

    abc.pop()

    a=abc.get(0)

    print(a)


if __name__ == "__main__":
    main()