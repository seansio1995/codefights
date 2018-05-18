from math import sqrt
def getNumDiv(x):
    t=int(sqrt(x))
    cnt=0
    for i in range(1,t+1):
        if x%i==0:
            cnt+=1
    cnt*=2
    if t**2==x:
        cnt-=1
    return cnt


def getWeakness(x):
    cnt=0
    target=getNumDiv(x)
    for i in range(1,x):
        if getNumDiv(i)>target:
            cnt+=1
    return cnt


def weakNumbers(n):
    res=list()
    for i in range(1,n+1):
        res.append(getWeakness(i))
    minWeak=max(res)
    numWeak=res.count(minWeak)
    print(res)
    return [minWeak,numWeak]

print(weakNumbers(9))
