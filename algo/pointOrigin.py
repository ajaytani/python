def pointDistance(inputArr,k):

    distArr = []
    for point in inputArr:
        distArr.append(distCalc(point))
    print(distArr)

    heapList = buildheap(distArr)
    result = []
    for i in range(k):
        result.append(delMin(heapList))

    return result


def distCalc(point):
    return pow((point[0]**2 + point[1]**2),0.5 )


def buildheap(inputArr):
    ptr = len(inputArr) // 2
    currentSize =  len(inputArr)
    heapList = [0] + inputArr
    while ptr > 0:
        percDown(ptr,heapList)
        ptr -= 1
    return heapList

def percDown(i,heapList):
    while i*2 <=len(heapList)-1:
        mc = minChild(i,heapList)
        if heapList[i] > heapList[mc]:
            heapList[i],heapList[mc] = heapList[mc],heapList[i]
        i = mc

def minChild(i,heapList):
    if i * 2 + 1 > len(heapList)-1:
        return i*2
    else:
        if heapList[i*2] < heapList[(i*2)+1]:
            return i*2
        else:
            return i*2 +1


def delMin(heapList):
    retVal = heapList[1]
    heapList[1] = heapList[-1]
    heapList.pop()
    percDown(1,heapList)
    return retVal



print(pointDistance([[1,1],[2,2],[2,4]],2))