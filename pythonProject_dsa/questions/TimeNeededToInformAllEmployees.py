def numOfMinutes(n, headID, manager, informTime):
    adjlist = [[] for _ in range(len(manager))]

    for i in range(len(manager)):
        if manager[i] == -1:
            continue
        adjlist[manager[i]].append(i)

    def dfs(adjlist,informTime,currentvert):
        maxx=0
        if len(adjlist[currentvert])==0:
            return 0
        for i in adjlist[currentvert]:
            maxx=max(maxx, dfs(adjlist,informTime,i))
        return maxx+informTime[currentvert]

    return dfs(adjlist,informTime, headID)

n=8
headID=4
manager=[2,2,4,6,-1,4,4,5]
informTime=[0,0,4,0,7,3,6,0]

print(numOfMinutes(n,headID,manager,informTime))
