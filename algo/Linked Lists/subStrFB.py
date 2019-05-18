def subStr(A,S):
    l = len(S)
    uniqueCounter = 0
    countMap = {}
    result = []
    t = 0
    for i in A:
        countMap[i] = 0

    for h in range(len(S)):
        char = S[h]
        if char not in countMap:
            continue

        if countMap[char] ==0:
            uniqueCounter +=1
        countMap[char] += 1
        while uniqueCounter == len(A):

            tempLength = h - t + 1

            if tempLength == len(A):
                return S[t:h+1]

            if not result or tempLength < len(result):
                result = S[t:h+1]

            tail = S[t]
            if tail in countMap:
                tailCount = countMap[tail] - 1
                if tailCount == 0:
                    uniqueCounter = uniqueCounter - 1
                countMap[tail] = tailCount
            t +=1
    return result

print(subStr(['a','c','b'],'aabbccba'))



