# Step 1: Transpose (Rows to columns)
# Step 2: Reverse each row.
def rot_mat(matrix):
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp
    for i in range(0, len(matrix)):
        matrix[i].reverse()

def rot_mat2(matrix):
    n=len(matrix)
    for i in range(0,n//2): #For how many layers to be iterated on. for matrix of 3x3, only one layer (outermost), for 5x5, outermost and another layer inside it.
        for j in range(i, n-1-i): #For number of elements to be swapped per layer. Eg, 3x3 matrix, in outermost layer, only 2 elements to be swapped (2 elements per top row/left col/right col/bot row)
            temp=matrix[i][j]
            matrix[i][j]=matrix[n-j-1][i] #Top left being swapped by bottom left
            matrix[n-j-1][i]=matrix[n-i-1][n-j-1] #bottom left being swapped by bottom right
            matrix[n-i-1][n-j-1]=matrix[j][n-i-1] # bottom right being swapped by top right ###VERY IMPORTANT (REMEMBER TOP RIGHT INDEXES)
            matrix[j][n-i-1]=temp  #top right being swapped by top left(temp)


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
rot_mat2(matrix)
for i in range(0, len(matrix)):
    print(matrix[i])