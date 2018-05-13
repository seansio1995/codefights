import sys
def arrayMaxConsecutiveSum(inputArray, k):
    maxRes=-float("inf")
    currSum=0
    for i in range(len(inputArray)):
        if i < k:
            currSum+=inputArray[i]
        else:
            currSum+=inputArray[i]-inputArray[i-k]
        if currSum>maxRes:
            maxRes=currSum
    return maxRes

        
