from math import sqrt
def rectangleRotation(a, b):
    cnt=0
    for x in range(-(a+100),a+101):
        for y in range(-(b+100),b+101):
            x1=(y+x)/sqrt(2)
            y1=(y-x)/sqrt(2)
            if x1>=-a/2 and x1<=a/2 and y1<=b/2 and y1>=-b/2:
                cnt+=1
    return cnt
