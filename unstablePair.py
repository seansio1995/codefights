def compare(file1,file2):
    maxLen=max(len(file1),len(file2))
    if len(file1)<maxLen:
        file1=file1+" "*(maxLen-len(file1))
    else:
        file2=file2+" "*(maxLen-len(file2))
    for i in range(maxLen):
        if file1[i]!=file2[i]:
            if file1[i] > file2[i]:
                return ">"
            else:
                return "<"
def isUnstablePair(filename1, filename2):
    if compare(filename1,filename2)==">":
        return compare(filename1.upper(),filename2.upper())=="<"
    elif compare(filename1,filename2)=="<":
        return compare(filename1.lower(),filename2.lower())==">"
    else:
        return False
