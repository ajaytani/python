def longestSubsequenceWithActualSolution(arr):
    T = []
    actualSolution = []
    for i in range(len(arr)):
        T.append(1)
        actualSolution.append(i)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                if T[j] + 1 > T[i]:
                    T[i] = T[j] + 1
# // set the actualSolution to point to guy before me
                    actualSolution[i] = j

# // find the index of max number in T
    maxIndex = 0
    for  i in range(len(T)):
        if T[i] > T[maxIndex]:
            maxIndex = i

    # // lets print the actual solution
    t = -1
    newT = maxIndex
    while (t != newT):
        t = newT
        print str(arr[t]) + " ",
        newT = actualSolution[t]

    return T[maxIndex]

longestSubsequenceWithActualSolution([3,4,-1,0,6,2,3])

