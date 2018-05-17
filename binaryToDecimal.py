def binaryCal(res):
    final=0
    for i in res:
            final*=2
            if i=="1":
                final+=1
    return final

def arrayPacking(a):
    l=list()
    for num in a:
        binary=bin(num)[2:]
        l.append("0"*(8-len(binary))+binary)
    return "".join(l)

print(binaryCal("000110000101010100000000"))
print(arrayPacking([24, 85, 0]))
