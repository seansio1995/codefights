def arrayChange(inputArray):
    i=1
    cnt=0
    while i<len(inputArray):
        if inputArray[i]<=inputArray[i-1]:
            inputArray[i]+=1
            cnt+=1
        else:
            i+=1
    return cnt


"""
1 2 3 4 2 5
"""
def arrayChange2(inputArray):
    start=0
    for i in range(len(inputArray)-1):
        if inputArray[i]>=inputArray[i+1]:
            start=i
            break
    res=(inputArray[start]+inputArray[start]+len(inputArray)-start-1)*(len(inputArray)-start)//2-sum(inputArray[start:])
    return res if res>=0 else 0

"""
This solution is the only correct one
"""
def arrayChange3(inputArray):
    i=0
    cnt=0
    while i+1< len(inputArray):
        if inputArray[i]>=inputArray[i+1]:
            tmp=inputArray[i]-inputArray[i+1]+1
            inputArray[i+1]+=tmp
            cnt+=tmp
        i+=1
    return cnt


if __name__=="__main__":
    a=[-1000, 0, -2, 0]
    print(arrayChange2(a))
