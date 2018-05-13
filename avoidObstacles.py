def avoidObstacles(inputArray):
    arr=sorted(inputArray)
    gap=1
    found=False

    while not found:
        found=True
        i=0
        while i<=arr[-1]:
            i+=gap
            if i in arr:
                found=False

        if found:
            return gap
        gap+=1
        
