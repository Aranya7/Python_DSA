matrix=[[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]

directions=[[-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]]

def traverseBFS(matrix):
    seen=[[False]*len(matrix[0]) for _ in range(len(matrix))]
    values=[]
    queue=[[0,0]]
    while(queue):
        abc=queue.pop(0)
        row=abc[0]
        col=abc[1]
        if row<0 or row>=len(matrix) or col<0 or col>=len(matrix[0]) or seen[row][col]:
            continue
        seen[row][col] = True
        values.append(matrix[row][col])
        for i in directions:
            queue.append([row+i[0],col+i[1]])
    return values

print(traverseBFS(matrix))