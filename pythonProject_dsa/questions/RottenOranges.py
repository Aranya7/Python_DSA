class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return -1
        minutes = 0
        fresh = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                abc = queue.pop(0)
                row = abc[0]
                col = abc[1]
                directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                for x in directions:
                    rowx = row + x[0]
                    coly = col + x[1]

                    if rowx < 0 or rowx >= len(grid) or coly < 0 or coly >= len(grid[0]) or grid[rowx][coly] == 2 or \
                            grid[rowx][coly] == 0:
                        continue

                    fresh -= 1

                    grid[rowx][coly] = 2

                    queue.append([rowx, coly])

        return minutes if fresh == 0 else -1
