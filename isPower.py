from math import sqrt
def isPower(n):
    if n==1:
        return True
    for i in range(2,int(sqrt(n))+1):
        for j in range(2,int(sqrt(n))+1):
            if i**j==n:
                return True
    return False
