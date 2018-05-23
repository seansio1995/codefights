from collections import Counter
def stringsConstruction(a, b):
    c1=[0]*26
    c2=[0]*26
    for ch in a:
        index=ord(ch)-ord("a")
        c1[index]+=1

    for ch in b:
        index=ord(ch)-ord("a")
        c2[index]+=1

    res=100000000

    for i in range(26):
        if c1[i]!=0:
            tmp=c2[i]//c1[i]
            if tmp<=res:
                res=tmp
    print(c1)
    print(c2)
    return res
