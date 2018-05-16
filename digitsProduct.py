def getProductDigits(digits):
    res=1
    for digit in list(str(digits)):
        res*=int(digit)
    return res
def digitsProduct(product):
    for i in range(1,100000):
        prod=getProductDigits(i)
        if prod==product:
            return i
    return -1
