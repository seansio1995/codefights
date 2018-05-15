def longestWord(text):
    maxLen=0
    word=""
    for i in range(len(text)):
        if not text[i].isalpha():
            if len(word)>maxLen:
                maxLen=len(word)
                longWord=word
            word=""
        else:
            word+=text[i]
    if len(word)>maxLen:
        longWord=word
    return longWord
