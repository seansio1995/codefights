def messageFromBinaryCode(code):
    words=[code[i:i+8] for i in range(0,len(code),8)]
    converts=list()
    for word in words:
        res=0
        for c in word:
            res*=2
            if c=="1":
                res+=1

        converts.append(chr(res))
    return "".join(converts)
