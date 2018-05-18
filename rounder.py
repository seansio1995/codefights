def rounders(value):
    count=0
    while value >= 10:
        tail=value%10
        if tail < 5:
            value-=tail
        else:
            value+=(10-tail)
        count+=1
        value//=10
    return value*10**count
