class Node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class bst():
    def __init__(self):
        self.root=None

    def insert(self,value):
        nn=Node(value)
        if not self.root:
            self.root=nn
            return
        data=self.root
        while data:
            if value>data.value:
                if data.right:
                    data=data.right
                else:
                    data.right=nn
                    break
            if value<data.value:
                if data.left:
                    data=data.left
                else:
                    data.left=nn
                    break

    def lookup(self,value):
        data=self.root
        while data:
            if value==data.value:
                return True
            if value<data.value:
                if data.left:
                    data=data.left
                else:
                    return False
            if value>data.value:
                if data.right:
                    data=data.right
                else:
                    return False

    def remove(self,value):
        curr=self.root
        parent=None
        while curr and curr.value!=value:
            if value>curr.value:
                parent=curr
                curr=curr.right
            else:
                parent=curr
                curr=curr.left

        if not curr.left and not curr.right:
            if parent.left==curr.value:
                parent.left=None
            elif parent.right==curr.value:
                parent.right=None

        elif not curr.left or not curr.right:
            if curr.left:
                if parent.left==curr.value:
                    parent.left=curr.left
                elif parent.right==curr.value:
                    parent.right=curr.left
            elif curr.right:
                if parent.left==curr.value:
                    parent.left=curr.right
                elif parent.right==curr.value:
                    parent.right=curr.right

        else:
            successor_parent=curr
            successor=curr.right
            while successor.left:
                successor_parent=successor
                successor=successor.left

            curr.value=successor.value

            if successor_parent.left==successor:
                successor_parent.left=successor.right
            else:
                successor_parent.right=successor.right

    def bfs(self):
        queue=[self.root]
        ans=[]

        while queue:
            currval=[]
            nextval=[]
            for node in queue:
                currval.append(node.value)
                if node.left:
                    nextval.append(node.left)
                if node.right:
                    nextval.append(node.right)
            ans.append(currval)
            queue=nextval
        return ans

    def dfs_pro_iter(self):
        queue=[self.root]
        ans=[]
        while queue:
            abc=queue.pop()
            if abc.right:
                queue.append(abc.right)
            if abc.left:
                queue.append(abc.left)
            ans.append(abc.value)
        return ans

    def dfs_pro_rec(self,curr,ans):
        if not curr:
            return ans
        ans.append(curr.value)
        self.dfs_pro_rec(curr.left,ans)
        self.dfs_pro_rec(curr.right,ans)

        return ans

    def dfs_io(self, curr, ans):
        if not curr:
            return ans
        self.dfs_io(curr.left, ans)
        ans.append(curr.value)
        self.dfs_io(curr.right,ans)

        return ans

    def dfs_posty(self,curr,ans):
        if not curr:
            return ans
        self.dfs_posty(curr.left, ans)
        self.dfs_posty(curr.right, ans)
        ans.append(curr.value)

        return ans

abc=bst()
abc.insert(9)

abc.insert(4)
abc.insert(6)
abc.insert(20)
abc.insert(170)

abc.insert(15)
abc.insert(1)
print(abc.bfs())
print(abc.lookup(170))
#abc.remove(4)
#print(abc.bfs())
print(abc.dfs_pro_iter())
print(abc.dfs_pro_rec(abc.root,[]))
print(abc.dfs_io(abc.root,[]))
print(abc.dfs_posty(abc.root, []))