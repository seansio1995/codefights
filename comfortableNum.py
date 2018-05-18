def feelComfortable(a,b):
    s=sum([int(i) for i in list(str(a))])
    left=a-s
    right=a+s
    return b>=left and b<=right
def comfortableNumbers(l, r):
    cnt=0
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            if feelComfortable(i,j) and feelComfortable(j,i):
                cnt+=1
    return cnt
