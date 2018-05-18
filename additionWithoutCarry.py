def additionWithoutCarrying(param1, param2):
    s1=str(param1)
    s2=str(param2)

    if len(s1) >= len(s2):
        s1,s2=s1,s2
    else:
        s1,s2=s2,s1

    s2=(len(s1)-len(s2))*"0"+s2
    res=list()
    for i in range(len(s1)):
        num=(int(s1[i])+int(s2[i]))%10
        res.append(num)
    res=list(map(str,res))
    return int("".join(res))
        
