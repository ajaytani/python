import sys
def countingSort(A):
    maxv = -sys.maxsize
    minv = sys.maxsize
    for i in A:
        maxv = max(i,maxv)
    for i in A:
        minv = min(i,minv)

    k = maxv - minv+1
    countMap = [0]*(k)

    for i in A:
        countMap[i-minv] += 1
    l = len(A)
    checkMedian = 0
    # medianAt
    for i in range(len(countMap)):
        if countMap[i] != 0:
            if countMap[i] + checkMedian < l//2:
                checkMedian +=1



countingSort([2,5,3,6,9,2])



