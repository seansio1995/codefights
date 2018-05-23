from collections import Counter
def createAnagram(s, t):
    c1=Counter(s)
    c2=Counter(t)


    total=0
    for val in string.ascii_letters:
        total+=abs(c1[val]-c2[val])
    return total//2
