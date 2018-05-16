def spiralNumbers(n):
    """
    1  2  3  4
    12 13 14 5
    11 16 15 6
    10 9  8  7
    """
    x,y=0,0
    dx,dy=0,1
    dirs=[(0,1),(1,0),(0,-1),(-1,0)]
    cnt=0
    res=[[None]*n for _ in range(n)]
    for i in range(1,n*n+1):
        res[x][y]=i
        nx,ny=x+dx,y+dy
        if 0<=nx<=n-1 and 0<=ny<=n-1 and res[nx][ny]==None:
            x,y=nx,ny
        else:
            cnt+=1
            index=cnt%4
            dx,dy=dirs[index]
            x,y=x+dx,y+dy
    return res
