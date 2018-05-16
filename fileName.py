def fileNaming(names):
    res=list()
    for name in names:
        if name in res:
            name=addPostifx(name,res)
        res.append(name)
    return res
def addPostifx(name,res):
    cnt=1
    newName=name+"("+str(cnt)+")"
    while newName in res:
        cnt+=1
        newName=name+"("+str(cnt)+")"
    return newName
