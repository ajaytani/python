def merge(A1, A2):
    mergelist = []
    l1 = len(A1)
    l2 = len(A2)
    i = j = k = n = 0

    while i <len(A1) and j < len(A2):
        if  A1[i]< A2[j]:
            mergelist.append(A1[i])
            i += 1
            k += 1
        else:
            mergelist.append(A2[j])#+ mergelist
            j += 1
            n += 1
    print(mergelist)
    while k <len(A1):
        mergelist.append(A1[k]) #+ mergelist
        k += 1
    while n < len(A2):
        mergelist.append(A2[n]) #+ mergelist
        n += 1
    return mergelist

def mergeSort(A):
    if len(A) <= 1:
        return A
    else:
        return  merge(mergeSort(A[0:len(A)//2]),mergeSort(A[len(A)//2:]))


print(mergeSort([3,2,41,5,6,43,56,43,1,4,88,5,31,34,67,23,1,212,456,7,5,53,3,12,324,53,2,3242,346,752,2,4,343]))