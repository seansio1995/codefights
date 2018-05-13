def areSimilar(a, b):
    tmp1=list()
    tmp2=list()
    for i in range(len(a)):
        if a[i]!=b[i]:
            tmp1.append(a[i])
            tmp2.append(b[i])
    if len(tmp1)==0:
        return True
    elif len(tmp1)>2:
        return False
    else:
        print(tmp1)
        print(tmp2)
        return tmp1==list(reversed(tmp2))


if __name__=="__main__":
    a=[1, 2, 3]
    b=[2, 1, 3]
    print(areSimilar(a,b))
