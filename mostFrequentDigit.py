from collections import Counter
def mostFrequentDigitSum(n):
    res=list()
    while n!=0:
        a=sum(map(int,list(str(n))))
        n-=a
        res.append(a)
    res.append(0)
    print(res)
    c=Counter(res)
    mostCount=max(c.values())
    mostCountVal=list()
    for k,v in c.items():
        if v==mostCount:
            mostCountVal.append(k)
    return max(mostCountVal)
