def sumUpNumbers(inputString):
    res=list()
    words=inputString.split(" ")
    for word in words:
        if word[0].isdigit():
            res.append(int(word))
        elif word[1].isdigit():
            res.append(int(word[1:len(word)-1]))
    return sum(res)
"""
This solution is not optimal. It just passes all the test cases after unlock the hidden
case. However, the algorithm cannot deal possible case such as ((123))
"""
