matrix=[[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

directions=[[-1, 0], #up
            [0, 1], #right
            [1, 0], #down
            [0,-1]] #left

def traverseDFS(matrix):
    seen = [[False]*len(matrix[0]) for _ in range(len(matrix))]
    values=[]
    dfs(matrix, seen, 0,0,values)
    return values

def dfs(matrix, seen, row, col, values):
    if row<0 or row>=len(matrix) or col<0 or col>=len(matrix[0]) or seen[row][col]==True:
        return
    values.append(matrix[row][col])
    seen[row][col] = True
    for i in directions:
        dfs(matrix, seen, row+i[0], col+i[1], values)


print(traverseDFS(matrix))