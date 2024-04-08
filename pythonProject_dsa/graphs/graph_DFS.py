def dfs_graph(adjlist, ans, vert, seen):
    ans.append(vert)
    seen[vert]=True
    for i in adjlist[vert]:
        if not seen[i]:
            dfs_graph(adjlist, ans, i, seen)
    return ans


adjlist=[[1,3],[0],[3,8],[0,2,4,5],[3,6],[3],[4,7],[6],[2]]
seen = [False] * len(adjlist)
print(dfs_graph(adjlist,[],0,seen))



