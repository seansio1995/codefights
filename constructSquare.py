from collections import Counter
def constructSquare(s):
    res=1
    found=False
    for i in range(100000):
        square=i**2
        a1=Counter(str(square))
        s1=Counter(s)
        if len(str(square))>len(s) and found:
            return res
        if sorted(a1.values())==sorted(s1.values()) and len(str(square))==len(s):
            found=True
            res=square

    return -1
"""
time limit exceed
"""


"""correct solution"""
from collections import Counter
from math import sqrt
def constructSquare(s):
    res=1
    found=False
    lower=int(sqrt(10**(len(s)-1)))+1
    upper=int(sqrt(10**len(s)))+1
    for i in range(upper-1,lower,-1):
        square=i**2
        a1=Counter(str(square))
        s1=Counter(s)
        # if len(str(square))>len(s) and found:
        #     return res
        if sorted(a1.values())==sorted(s1.values()):
            #found=True
            return square

    return -1
