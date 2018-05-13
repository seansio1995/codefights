def isIPv4Address(inputString):

    a=inputString.split(".")
    if len(a)!=4:
        return False
    for i in a:
        if i=="" or not i.isdigit():
            return False
        if int(i)>255 or int(i)<0:
            return False
    return True
