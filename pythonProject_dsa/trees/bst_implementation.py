from collections import deque
class Node():
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class binsertree():
    def __init__(self):
        self.root=None

    def insert(self, value):
        nn = Node(value)

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
            elif value<data.value:
                if data.left:
                    data=data.left
                else:
                    data.left=nn
                    break

    def lookup(self,value):

        data=self.root
        while data:
            if value>data.value:
                data=data.right
            elif value<data.value:
                data=data.left
            elif value==data.value:
                return True
        return False

    def remove(self, value):
        parent = None
        current = self.root

        while current and current.value!=value:
            parent=current
            if value<current.value:
                current=current.left
            else:
                current=current.right

        #Current (Node to be deleted) has no child
        if not current.left and not current.right:
            if parent:
                if parent.left==current.value:
                    parent.left=None
                else:
                    parent.right=None
            else:
                self.root=None

        #Current has only one child
        elif not current.left or not current.right:
            if parent.left==current:
                if current.left:
                    parent.left=current.left
                else:
                    parent.left=current.right
            elif parent.right==current:
                if current.left:
                    parent.right = current.left
                else:
                    parent.right = current.right

        #Current has two children    # Parent, Curr.left, Curr.right, Secc.Parent
        else:
            successor_parent=current
            successor=current.right
            while successor.left:
                successor_parent=successor
                successor=successor.left

            current.value=successor.value #Doing this, current.left and current.right point accurately without any change, while the value gets updated to in-order successor.
            #Basically, doing above results in current (node to be removed) being replaced by successor. Now removed nodes left and right are now successor's left and right. And current/successor's parent also now points to successor.

            if successor_parent.left==successor:
                successor_parent.left=successor.right
            else:
                successor_parent.right=successor.right # Don't know what this last line is for. :')


    def bfs(self):
        current_level = [self.root]
        ans = []
        while current_level:
            next_level = []
            level_values = []
            for node in current_level:
                level_values.append(node.value)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            ans.append(level_values)
            current_level=next_level

        return ans

    def bfs_rec(self):
        return self.helper([self.root], [])
    def helper(self, current_level, ans):
        if len(current_level)==0:
            return ans
        while current_level:
            next_level=[]
            for node in current_level:
                ans.append(node.value)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level=next_level
        return self.helper(current_level, ans)

    def dfs_pre_order(self):

        stack=[self.root]
        ans=[]
        while stack:
            node=stack.pop()
            ans.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans

    def dfs_pre_order_rec(self, current, ans):
        if not current:
            return ans
        ans.append(current.value)
        self.dfs_pre_order_rec(current.left, ans)

        self.dfs_pre_order_rec(current.right, ans)

        return ans
    def dfs_in_order(self, current, ans):
        if not current:
            return ans
        self.dfs_in_order(current.left, ans)
        ans.append(current.value)
        self.dfs_in_order(current.right, ans)

        return ans

    def dfs_post_order(self, current, ans):
        if not current:
            return ans
        self.dfs_post_order(current.left, ans)
        self.dfs_post_order(current.right, ans)
        ans.append(current.value)
        return ans

    def print_bottom(self): #for Visa
        queue=[self.root]
        ans=[]
        while queue:
            next=[]
            for node in queue:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
                if not node.left and not node.right:
                    ans.append(node.value)
            queue=next
        return ans

#          9
#     4         20
#   1   6    15    170
#

abc=binsertree()
abc.insert(9)

abc.insert(4)
abc.insert(6)
abc.insert(20)
abc.insert(170)

abc.insert(15)
abc.insert(1)
print(abc.lookup(69))
#abc.remove(4)
print(f"BFS_Iterative: {abc.bfs()}")
print(f"BFS_Recursive: {abc.bfs_rec()}")
print(f"DFS - PreOrder: {abc.dfs_pre_order()}")
print(f"DFS - PreOrder_REC: {abc.dfs_pre_order_rec(abc.root, [])}")
print(f"DFS - InOrder: {abc.dfs_in_order(abc.root, [])}")
print(f"DFS - PostOrder: {abc.dfs_post_order(abc.root, [])}")
print(abc.print_bottom())

#print(abc.root.left.value)
