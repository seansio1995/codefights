def checkPalindrome(s1):
    return s1==s1[::-1]
def buildPalindrome(st):
    """
    abcdedc   cdedcba
    abcdedc   ba
    """
    if checkPalindrome(st):
        return st
    for i in range(1,len(st)+1):
        a=st+st[:i][::-1]
        if checkPalindrome(a):
            return a
