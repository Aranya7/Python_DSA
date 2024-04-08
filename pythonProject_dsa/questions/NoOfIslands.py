def numIslands_bfs(grid): # Array - BFS Implementatiom
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    def zeroland(grid, i, j):
        directions = [[-1, 0],
                      [0, 1],
                      [1, 0],
                      [0, -1]]
        queue = [[i, j]]
        while queue:
            abc = queue.pop(0)
            row = abc[0]
            col = abc[1]
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                continue
            grid[row][col] = "0"
            for i in directions:
                #zeroland(grid, row + i[0], col + i[1])
                queue.append([row+i[0],col+i[1]])

    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "0":
                continue
            if grid[i][j] == "1":
                counter += 1
                zeroland(grid, i, j)
    return counter

matrix_for_bfs=[["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","1"],
        ["0","0","0","1","1"]]

print(f"BFS Solution: {numIslands_bfs(matrix_for_bfs)}")


def numIslands_dfs(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    def dfs(grid, i, j):
        directions = [[-1, 0],
                      [0, 1],
                      [1, 0],
                      [0, -1]]
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        for k in directions:
            dfs(grid, i + k[0], j + k[1])

    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "0":
                continue
            if grid[i][j] == "1":
                counter += 1
                dfs(grid, i, j)
    return counter

matrix_for_dfs=[["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","1"],
        ["0","0","0","1","1"]]

print(f"DFS Solution: {numIslands_dfs(matrix_for_dfs)}")