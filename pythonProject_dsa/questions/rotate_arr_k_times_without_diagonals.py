#https://www.geeksforgeeks.org/rotate-all-matrix-elements-except-the-diagonal-k-times-by-90-degrees-in-clockwise-direction/
def rorarr_k_wo_d(matrix, k):

    def swap(matrix, i, j):
        n=len(matrix)

        temp=matrix[i][j]
        matrix[i][j]=matrix[n-j-1][i]
        matrix[n-j-1][i]=matrix[n-i-1][n-j-1]
        matrix[n-i-1][n-j-1]=matrix[j][n-i-1]
        matrix[j][n-i-1]=temp

    def rotate(matrix, k):
        if k%4>0:
            for i in range(0, k%4):
                for i in range(0, len(matrix)):
                    for j in range(i, len(matrix)-i-1): #for rotating layers. for example, if 5x5 matrix, len(matrix)-i-1 -> 5-1-1=3 elements to be swapped in the outermost layer (all elements apart from first and last.)
                        if i!=j and i+j!=len(matrix)-1: #diagonals
                            swap(matrix, i, j)

    rotate(matrix, k)

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
rorarr_k_wo_d(matrix,1)
for i in range(0, len(matrix)):
    print(matrix[i])