class Graph():
    def __init__(self):
        self.number_of_nodes=0
        self.adjlist={}

    def addVertex(self, node):
        self.adjlist[node]=[]
        self.number_of_nodes+=1

    def addEdge(self, node1, node2):
        if node1 in self.adjlist.keys() and node2 in self.adjlist.keys():
            self.adjlist[node1].append(node2)
            self.adjlist[node2].append(node1)

    def showGraph(self):
        for i in self.adjlist.keys():
            print(f"{i} -> {self.adjlist[i]}")

abc=Graph()
abc.addVertex(0)
abc.addVertex(1)
abc.addVertex(2)
abc.addVertex(3)
abc.addVertex(4)
abc.addVertex(5)
abc.addVertex(6)
abc.addEdge(0,1)
abc.addEdge(0,2)
abc.addEdge(1,2)
abc.addEdge(1,3)
abc.addEdge(2,4)
abc.addEdge(3,4)
abc.addEdge(4,5)
abc.addEdge(5,6)
abc.showGraph()