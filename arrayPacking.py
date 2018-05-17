def arrayPacking(a):
    l=list()
    for num in a:
        binary=bin(num)[2:]
        l.append("0"*(8-len(binary))+binary)
    res="".join(list(reversed(l)))
    final=0
    for i in res:
        final*=2
        if i=="1":
            final+=1
    return final
