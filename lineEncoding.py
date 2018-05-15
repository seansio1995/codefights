def lineEncoding(s):
    cnt=1
    res=""
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            cnt+=1
        else:
            if cnt>1:
                res+=str(cnt)+s[i]
            else:
                res+=s[i]
            cnt=1
    if cnt>1:
        res+=str(cnt)+s[len(s)-1]
    else:
        res+=s[len(s)-1]
    return res
