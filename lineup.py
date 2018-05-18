def lineUp(commands):
    pair=True
    res=0
    for c in commands:
        if c=="L" or c=="R":
            pair=not pair
            if pair:
                res+=1
        else:
            if pair:
                res+=1
    return res
        
