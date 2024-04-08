ans=[[1]*i for i in range(1, 5+1)]
print(ans)
for i in range(2, len(ans)):
    for j in range(1, len(ans[i])-1):
        ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
print(ans)


class Solution:
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]

    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res, visited, [], nums)
        return res

    def backtracking(self, res, visited, subset, nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res, visited, subset + [nums[i]], nums)
                visited.remove(i)