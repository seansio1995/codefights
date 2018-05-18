def squareDigitsSequence(a0):
    record=list()
    record.append(a0)
    notFound=True
    prev=a0

    while notFound:
        newL=list(map(int,list(str(prev))))
        newNum=sum([x**2 for x in newL])
        if newNum in record:
            notFound=False
        record.append(newNum)
        prev=newNum


    return len(record)
