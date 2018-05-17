def countSumOfTwoRepresentations2(n, l, r):
    """
    2 8
    3  7
    4  6
    5 5


    2 7
    3 6
    4 5
    """
    while l<=r:
        if l+r > n:
            r-=1
        elif l+r<n:
            l+=1
        else:
            break
    mid=(l+r)//2
    return mid-l+1
