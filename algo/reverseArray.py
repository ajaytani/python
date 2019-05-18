def reverseArr(arr):
    if not arr:
        return []
    return  reverseArr(arr[1:]) + [arr[0]]

print(reverseArr([1,2,3,4,5]))

def longestpalindromicSubstring(inputstr):
    end = len(inputstr)-1
    if len(inputstr)==1:
        return 1
    start = 0
    currLen = 1
    for i in range(len(inputstr)):
        for j in range(i+1, len(inputstr)):
            if checkPalindrome(inputstr[i:j]):
                currLen = j -i+1

def checkPalindrome(inputStr):
    ln = len(inputStr)
    start = 0
    end = ln-1
    if ln <= 1:
        return True
    if ln == 2:
        return inputStr[0]==inputStr[1]
    if ln > 2:
        while start < ln and end >= 0:
            if inputStr[start] == inputStr[end]:
                start +=1
                end -=1
            else:
                return False
    return True



