def sudoku(grid):
    target=[i for i in range(1,10)]
    for i in range(9):
        if sorted(grid[i])!=target:
            return False
    for i in range(9):
        res=list()
        for line in grid:
            res.append(line[i])
        if sorted(res)!=target:
            return False

    for i in range(3):
        for j in range(3):
            x=i*3
            y=j*3
            res=0
            res=[grid[x+a][y+b] for a in range(3) for b in range(3)]
            if sorted(res)!=target:
                return False

    return True
