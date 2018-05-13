def findMine(matrix,row,col):
    if row<0 or row>=len(matrix):
        return 0
    if col<0 or col>=len(matrix[0]):
        return 0
    if matrix[row][col] is True:
        return 1
    return 0

def minesweeper(matrix):
    m=len(matrix)
    n=len(matrix[0])
    res=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j]=sum([findMine(matrix,i+a,j+b) for a in [-1,0,1] for b in [-1,0,1]])-findMine(matrix,i,j)
    return res
