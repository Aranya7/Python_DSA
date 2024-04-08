def bfs_graph(adjlist):

    queue=[0]
    values=[]
    seen={}
    while queue:
        abc=queue.pop(0)
        values.append(abc)
        seen[abc]=True
        for i in adjlist[abc]:
            if i not in seen:
                queue.append(i)
                #seen[i]=True
    return values

adjlist=[[1,3],[0],[3,8],[0,2,4,5],[3,6],[3],[4,7],[6],[2]]
print(bfs_graph(adjlist))

#[0, 1, 3, 2, 4, 5, 8, 6, 7]

