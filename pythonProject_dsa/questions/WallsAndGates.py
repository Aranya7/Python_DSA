# def walls_and_gates(rooms):
#     # write your code here
#     def bfs(rooms, i, j):
#         count = 0
#         directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
#         queue = [[i, j]]
#         while queue:
#             count += 1
#             for _ in range(len(queue)):
#                 abc = queue.pop(0)
#                 row = abc[0]
#                 col = abc[1]
#                 for x in directions:
#                     rowx = row + x[0]
#                     coly = col + x[1]
#
#                     if rowx < 0 or rowx >= len(rooms) or coly < 0 or coly >= len(rooms[0]) or rooms[rowx][coly] == -1:
#                         continue
#                     if rooms[rowx][coly] == 0:
#                         rooms[i][j] = count
#                         return
#                     queue.append([rowx,coly])
#
#     for i in range(len(rooms)):
#         for j in range(len(rooms[0])):
#             if rooms[i][j] == -1 or rooms[i][j] == 0:
#                 continue
#             elif rooms[i][j] == 2147483647:
#                 bfs(rooms, i, j)
#
# rooms=[[2147483647, -1, 0, 2147483647],
#        [2147483647, 2147483647, 2147483647, -1],
#        [2147483647, -1, 2147483647, -1],
#        [0, -1, 2147483647, 2147483647]]
#
# rooms2=[[2147483647, -1, 0, 2147483647],
#        [-1, 2147483647, 2147483647, -1],
#        [2147483647, -1, 2147483647, -1],
#        [0, -1, 2147483647, 2147483647]]
# print(rooms2)
# walls_and_gates(rooms2)
# print(rooms2)

##0 to INF (BFS)
def walls_and_gates(rooms):
    # write your code here
    directions=[[-1,0],[0,1],[1,0],[0,-1]]
    queue=[]
    seen=[[False]*len(rooms[0]) for _ in range(len(rooms))]
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j]==0:
                queue.append([i,j])
            else:
                continue
    count=0
    while queue:
        count+=1
        for _ in range(len(queue)):
            abc=queue.pop(0)
            row=abc[0]
            col=abc[1]

            for i in directions:
                rowx=row+i[0]
                coly=col+i[1]

                if rowx<0 or rowx>=len(rooms) or coly<0 or coly>=len(rooms[0]) or rooms[rowx][coly]==-1 or rooms[rowx][coly]==0 or seen[rowx][coly]:
                    continue
                if count<rooms[rowx][coly]:
                    rooms[rowx][coly]=count
                seen[rowx][coly]=True
                queue.append([rowx,coly])


    return rooms



rooms=[[2147483647, -1, 0, 2147483647],
       [2147483647, 2147483647, 2147483647, -1],
       [2147483647, -1, 2147483647, -1],
       [0, -1, 2147483647, 2147483647]]

rooms2=[[2147483647, -1, 0, 2147483647],
       [-1, 2147483647, 2147483647, -1],
       [2147483647, -1, 2147483647, -1],
       [0, -1, 2147483647, 2147483647]]
print(rooms2)
walls_and_gates(rooms2)
print(rooms2)