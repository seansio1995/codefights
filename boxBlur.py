def boxBlur(image):
    m=len(image)-2
    n=len(image[0])-2
    res=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j]=sum([image[i+a][j+b] for a in range(3) for b in range(3)])//9
    return res
