def candles(candlesNumber, makeNew):
    leftOver=0
    total=0
    leftOver+=candlesNumber
    total+=candlesNumber
    while leftOver>=makeNew:
        newCandle=leftOver//makeNew
        total+=newCandle
        leftOver-=(leftOver//makeNew)*makeNew
        leftOver+=newCandle
    return total
