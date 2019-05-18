#xyipzyv  for xyz would be xyipz
def getShortestUniqueSubstring(arr,S1):
    t = 0
    result = None
    uniqueCounter = 0
    countMap = {}
    # initialize countMap:
    for i in range(0, len(arr)):
        countMap[arr[i]] = 0
    # scan str
    for h in range(0,len(S1)):
        # handle the new head get each char
        head = S1[h]
        #if head not in arr move on
        if head not in countMap:
            continue
        # get headcount of that char
        #if this is the first occurence add uniquecounter
        if countMap[head] == 0:
            uniqueCounter = uniqueCounter + 1
        #increment countMap to indicate this occurence
        countMap[head]  += 1
        # push tail forward
        #if uniqueCounter = len(arr) it means you received all the character once
        while uniqueCounter == len(arr):
            tempLength = h - t + 1
            #if len(arr) == length of substring identified it means this is the smallest possible
            if tempLength == len(arr):
                return S1[t:h+1]
            #if first length or smaller len till this point
            elif not(result) or tempLength < len(result):
                result = S1[t:h+1]
            tail = S1[t]
            if tail in countMap:
                tailCount = countMap[tail] - 1
                if tailCount == 0:
                    uniqueCounter = uniqueCounter - 1
                countMap[tail] = tailCount
            t = t + 1

    return result


def shortest_substring(alphabet,inp):
    start, end = 0, 1
    alphabet = set(alphabet)
    result = None
    while start < len(inp) and end < len(inp)+1:
        current = inp[start:end]
        if set(current).issuperset(alphabet):
            if result is None:
                result = current
            else:
                result = min([result, current], key=len)
            start += 1
        else:
            end += 1
    return result

print(shortest_substring(['x','y','z'],'ipoyxiz'))
print(getShortestUniqueSubstring(['x','y','z'],'ipoyxiz'))

# print(getShortestUniqueSubstring(['x','y','z'],'xyipzyv'))