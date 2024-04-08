class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        indegree = [0 for x in range(numCourses)]
        for i in prerequisites:
            adjlist[i[1]].append(i[0])
            indegree[i[0]] += 1

        stack = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)

        count = 0
        while stack:
            abc = stack.pop()
            count += 1
            for i in range(len(adjlist[abc])):
                indegree[adjlist[abc][i]] -= 1

                if indegree[adjlist[abc][i]] == 0:
                    stack.append(adjlist[abc][i])

        return count == numCourses

[[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]


