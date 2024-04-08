# al=[[] for _ in range(20)]
preq=[[0,1],[3,1],[1,3],[3,2]]
#
#
#
# for i in preq:
#     al[i[1]].append(i[0])
#
# print(al)

numCourses=5

adjlist = [[] for _ in range(len(preq))]
indegree = [0 for x in range(numCourses)]

print(adjlist)
print(indegree)